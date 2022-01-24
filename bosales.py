from datetime import datetime
import sys
import json
import requests
from time import gmtime, strftime
import datetime
import logging
import pyodbc as dbc
import http.client
from types import SimpleNamespace
import result_sales

conn = None
cursor = None
failedCount = 0
BASE_URL = "http://172.23.21.86:9996"
firstTime = True
token = ""

storesCode = []
#logging HTTP Requests
"""http.client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True"""
# substract time from now
def getDate(time):
    now = datetime.datetime.now()
    d = now- datetime.timedelta(hours=0, minutes=time)
    today = d.strftime('%Y-%m-%dT%H:%M:%SZ')
    return today

#Getting StoreId and saving list
def getStores():
    print("Güncel mağaza listesi alınıyor...")
    global storesCode
    token = getToken()
    url = BASE_URL+"/api/Store/stores"
    headers = {'Content-type': 'application/json',"Authorization": "Bearer "+ token}
    try:
        response =  requests.get(url,headers=headers)
        result =json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
    except:
        print("Mağaza listesi Alıamadı !")
    for item in result.datas:
        if(item == 1):
            continue
        url2 = BASE_URL+"/api/Store/store-byId/"+str(item)
        headers2 = {'Content-type': 'application/json',"Authorization": "Bearer "+ token}
        try:
            response2 =  requests.get(url2,headers=headers2)
        except:
            print("Mağaza bilgileri alınırken bir hata oluştu")
        try:
            result2 =json.loads(response2.text, object_hook=lambda d: SimpleNamespace(**d))
        except:
            print("Mağaza bilgileri dönüştürlülemedi.")
        storesCode.append(result2.datas.code)
    
#Getting token for request API
def getToken():
    global firstTime,token
    #Checking  is token avaliable
    if(firstTime):
        url = BASE_URL+"/token"
        headers = {'Content-type': 'application/json'}
        data={ 'grant_type': 'password','username': 'kasa','password': '81dc9bdb52d04dc20036dbd8313ed055'}
        data = json.dumps(data)
        try:
            response =  requests.post(url,data=data,headers=headers)
            firstTime = False
            token = response.text.replace('"', "")
            return token
        except:
            print("Token Alınamadı !")
    else:
        return token
   
# Getting sales from API
def getSales(time =35):
    print("Satışlar  işleniyor...")
    for item in storesCode:
        url = BASE_URL+"/api/Reports/sales"
        myObj = {'posCode': '','storeCode': item,'date': getDate(time),'salesType': 0}
        myObj = json.dumps(myObj)
        token = getToken()
        headers = {'Content-type': 'application/json',"Authorization": "Bearer "+ token}
        x = requests.post(url, data = myObj,headers=headers)
        try:
            #result = json.loads(x.text, object_hook=lambda d: SimpleNamespace(**d))
            result = result_sales.result_sales_model_from_dict(json.loads(x.text))
            writeData(result)
        except:
            print("Satışlar dönüştürülürken bir hata oluştu !")
        
# Connect MSSQL DB
def connectDB():
    global conn, cursor
    dsn="DRIVER={SQL SERVER};server=172.23.21.28;database=ENTEGRASYON;uid=encore;pwd=29K4y1rZ7wOVShX1y"
    conn = dbc.connect(dsn)
    cursor = conn.cursor()
    
# Show all Data from ENCORE_SALES
def showData():
    global conn
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ENCORE_SALES')
    for i in cursor:
        print(i)
# Delete all records
def deleteTable():
    global conn
    cursor = conn.cursor()
    cursor.execute('DELETE FROM ENCORE_SALES')
    conn.commit()
# Insert data from api
def insertData(werks,posId,recieptNo,productCode,amount,total_price,vat,sequence,date):
    global failedCount
    global cursor,conn
    try:
        cursor.execute("insert into ENCORE_SALES(WERKS, POS,INVOICE,MATERIAL,AMOUNT,TOTAL_PRICE,VAT,SEQUENCE,DATE) values (?, ?, ?, ?, ?, ?, ?, ?, ?)", werks, posId,recieptNo, productCode,amount, total_price,vat,sequence,date)
        conn.commit()
    except:
        failedCount = failedCount+1
        # print("Veri DB eklenemedi werks: "+werks+" invoice : "+ recieptNo+" product: "+ productCode)
# Getting Pos ID
def getPosId(posCode):
    token = getToken()
    url = BASE_URL+"/api/Store/pos-byCode/"+posCode
    headers = {'Content-type': 'application/json',"Authorization": "Bearer "+ token}
    response =  requests.get(url,headers=headers)
    try:
        result =json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
    except:
        print("DeCode edilirken oluşan hata (POSID)")
    return result.datas.id
#Writing data to DB
def writeData(result):
    global failedCount
    storeCode = ""
    for datas in result.datas:
        if(datas != None):
            storeCode = datas.store_code
            posCode = getPosId(datas.pos_code)
            invoice = datas.receipt_no
            date = datas.date
            if(datas.lines != None and len(datas.lines) > 0):
                for lines in datas.lines:
                    if(lines.is_valid):
                        total_price = lines.total_price - lines.vat_total
                        insertData(storeCode,posCode,invoice,lines.product_code,lines.amount,total_price,lines.vat_total,lines.sequence,date)
    if(storeCode != ""):
        print(storeCode+" Mağazası aktarılıdı. "+"Başarısız kayıt sayısı:"+ str(failedCount))
    failedCount = 0
    
    

if __name__ == "__main__":
    #Deleting database
    # connectDB()
    # deleteTable()
    try:
        print("Veri tabanına bağlanıyor...")
        connectDB()
    except:
        print("Veri tabanına bağlanılamadı.")
    getStores()
    if len(sys.argv) == 1:
        getSales()
    else:
        time = int(sys.argv[1])
        getSales(time)
    print("İşlem Tamamlandı.")
  

