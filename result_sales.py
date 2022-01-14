# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = result_sales_model_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x

def from_float(x: Any) -> float:
    assert isinstance(x, float) and not isinstance(x, bool)
    return x

def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Bonus:
    id: int
    code: str
    name: str
    bonus: int
    spendable_bonus: int
    pending_bonus: int
    minimum_spend: int
    multiplier: int
    usage_limit: int
    receipt_limit: int
    receipt_item_limit: int
    monthly_discount_limit: int

    def __init__(self, id: int, code: str, name: str, bonus: int, spendable_bonus: int, pending_bonus: int, minimum_spend: int, multiplier: int, usage_limit: int, receipt_limit: int, receipt_item_limit: int, monthly_discount_limit: int) -> None:
        self.id = id
        self.code = code
        self.name = name
        self.bonus = bonus
        self.spendable_bonus = spendable_bonus
        self.pending_bonus = pending_bonus
        self.minimum_spend = minimum_spend
        self.multiplier = multiplier
        self.usage_limit = usage_limit
        self.receipt_limit = receipt_limit
        self.receipt_item_limit = receipt_item_limit
        self.monthly_discount_limit = monthly_discount_limit

    @staticmethod
    def from_dict(obj: Any) -> 'Bonus':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        code = from_str(obj.get("code"))
        name = from_str(obj.get("name"))
        bonus = from_int(obj.get("bonus"))
        spendable_bonus = from_int(obj.get("spendableBonus"))
        pending_bonus = from_int(obj.get("pendingBonus"))
        minimum_spend = from_int(obj.get("minimumSpend"))
        multiplier = from_int(obj.get("multiplier"))
        usage_limit = from_int(obj.get("usageLimit"))
        receipt_limit = from_int(obj.get("receiptLimit"))
        receipt_item_limit = from_int(obj.get("receiptItemLimit"))
        monthly_discount_limit = from_int(obj.get("monthlyDiscountLimit"))
        return Bonus(id, code, name, bonus, spendable_bonus, pending_bonus, minimum_spend, multiplier, usage_limit, receipt_limit, receipt_item_limit, monthly_discount_limit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["code"] = from_str(self.code)
        result["name"] = from_str(self.name)
        result["bonus"] = from_int(self.bonus)
        result["spendableBonus"] = from_int(self.spendable_bonus)
        result["pendingBonus"] = from_int(self.pending_bonus)
        result["minimumSpend"] = from_int(self.minimum_spend)
        result["multiplier"] = from_int(self.multiplier)
        result["usageLimit"] = from_int(self.usage_limit)
        result["receiptLimit"] = from_int(self.receipt_limit)
        result["receiptItemLimit"] = from_int(self.receipt_item_limit)
        result["monthlyDiscountLimit"] = from_int(self.monthly_discount_limit)
        return result


class SegmentList:
    id: int
    name: str

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(obj: Any) -> 'SegmentList':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        return SegmentList(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        return result


class CustomerData:
    is_e_invoice_customer: bool
    allow_gdpr_enum: int
    allow_gdpr: bool
    account_type: int
    source: int
    segments: List[int]
    segment_list: List[SegmentList]
    bonuses: List[Bonus]
    id: int
    code: str
    name: str
    card_number: str
    mobile_phone: str
    email: str
    date_of_birth: datetime
    date_of_marrige: datetime
    date_of_birth_wife: datetime
    address: str
    city_name: str
    district_name: str
    tax_office: str
    tax_number: str
    identity_number: str
    allow_promotion_email: bool
    allow_promotion_sms: bool
    segment_text: str
    passport_no: str
    nationality: str
    country: str

    def __init__(self, is_e_invoice_customer: bool, allow_gdpr_enum: int, allow_gdpr: bool, account_type: int, source: int, segments: List[int], segment_list: List[SegmentList], bonuses: List[Bonus], id: int, code: str, name: str, card_number: str, mobile_phone: str, email: str, date_of_birth: datetime, date_of_marrige: datetime, date_of_birth_wife: datetime, address: str, city_name: str, district_name: str, tax_office: str, tax_number: str, identity_number: str, allow_promotion_email: bool, allow_promotion_sms: bool, segment_text: str, passport_no: str, nationality: str, country: str) -> None:
        self.is_e_invoice_customer = is_e_invoice_customer
        self.allow_gdpr_enum = allow_gdpr_enum
        self.allow_gdpr = allow_gdpr
        self.account_type = account_type
        self.source = source
        self.segments = segments
        self.segment_list = segment_list
        self.bonuses = bonuses
        self.id = id
        self.code = code
        self.name = name
        self.card_number = card_number
        self.mobile_phone = mobile_phone
        self.email = email
        self.date_of_birth = date_of_birth
        self.date_of_marrige = date_of_marrige
        self.date_of_birth_wife = date_of_birth_wife
        self.address = address
        self.city_name = city_name
        self.district_name = district_name
        self.tax_office = tax_office
        self.tax_number = tax_number
        self.identity_number = identity_number
        self.allow_promotion_email = allow_promotion_email
        self.allow_promotion_sms = allow_promotion_sms
        self.segment_text = segment_text
        self.passport_no = passport_no
        self.nationality = nationality
        self.country = country

    @staticmethod
    def from_dict(obj: Any) -> 'CustomerData':
        if(obj == None):
            thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
            }
            return thisdict
        assert isinstance(obj, dict)
        is_e_invoice_customer = from_bool(obj.get("isEInvoiceCustomer"))
        allow_gdpr_enum = from_int(obj.get("allowGdprEnum"))
        allow_gdpr = from_bool(obj.get("allowGdpr"))
        account_type = from_int(obj.get("accountType"))
        source = from_int(obj.get("source"))
        segments = from_list(from_int, obj.get("segments"))
        segment_list = from_list(SegmentList.from_dict, obj.get("segmentList"))
        bonuses = from_list(Bonus.from_dict, obj.get("bonuses"))
        id = from_int(obj.get("id"))
        code = from_str(obj.get("code")) if obj.get("code") != None else ""
        name = from_str(obj.get("name"))
        card_number = from_str(obj.get("cardNumber")) if obj.get("cardNumber") != None else ""
        mobile_phone = obj.get("mobilePhone")
        email = obj.get("email")
        date_of_birth = obj.get("dateOfBirth")
        date_of_marrige = obj.get("dateOfMarrige")
        date_of_birth_wife = obj.get("dateOfBirthWife")
        address = obj.get("address")
        city_name = obj.get("cityName")
        district_name = obj.get("districtName")
        tax_office = obj.get("taxOffice")
        tax_number = obj.get("taxNumber")
        identity_number = obj.get("identityNumber")
        allow_promotion_email = from_bool(obj.get("allowPromotionEmail"))
        allow_promotion_sms = from_bool(obj.get("allowPromotionSms"))
        segment_text = obj.get("segmentText")
        passport_no = obj.get("passportNo")
        nationality =obj.get("nationality")
        country = obj.get("country")
        return CustomerData(is_e_invoice_customer, allow_gdpr_enum, allow_gdpr, account_type, source, segments, segment_list, bonuses, id, code, name, card_number, mobile_phone, email, date_of_birth, date_of_marrige, date_of_birth_wife, address, city_name, district_name, tax_office, tax_number, identity_number, allow_promotion_email, allow_promotion_sms, segment_text, passport_no, nationality, country)

    def to_dict(self) -> dict:
        result: dict = {}
        result["isEInvoiceCustomer"] = from_bool(self.is_e_invoice_customer)
        result["allowGdprEnum"] = from_int(self.allow_gdpr_enum)
        result["allowGdpr"] = from_bool(self.allow_gdpr)
        result["accountType"] = from_int(self.account_type)
        result["source"] = from_int(self.source)
        result["segments"] = from_list(from_int, self.segments)
        result["segmentList"] = from_list(lambda x: to_class(SegmentList, x), self.segment_list)
        result["bonuses"] = from_list(lambda x: to_class(Bonus, x), self.bonuses)
        result["id"] = from_int(self.id)
        result["code"] = from_str(self.code)
        result["name"] = from_str(self.name)
        result["cardNumber"] = from_str(self.card_number)
        result["mobilePhone"] = from_str(self.mobile_phone)
        result["email"] = from_str(self.email)
        result["dateOfBirth"] = self.date_of_birth.isoformat()
        result["dateOfMarrige"] = self.date_of_marrige.isoformat()
        result["dateOfBirthWife"] = self.date_of_birth_wife.isoformat()
        result["address"] = from_str(self.address)
        result["cityName"] = from_str(self.city_name)
        result["districtName"] = from_str(self.district_name)
        result["taxOffice"] = from_str(self.tax_office)
        result["taxNumber"] = from_str(self.tax_number)
        result["identityNumber"] = from_str(self.identity_number)
        result["allowPromotionEmail"] = from_bool(self.allow_promotion_email)
        result["allowPromotionSms"] = from_bool(self.allow_promotion_sms)
        result["segmentText"] = from_str(self.segment_text)
        result["passportNo"] = from_str(self.passport_no)
        result["nationality"] = from_str(self.nationality)
        result["country"] = from_str(self.country)
        return result


class LineCampaign:
    id: int
    campaign_id: int
    campaign_version: int
    campaign_erp_id: int
    campaign_name: str
    total_discount: int
    distributed_amount: int

    def __init__(self, id: int, campaign_id: int, campaign_version: int, campaign_erp_id: int, campaign_name: str, total_discount: int, distributed_amount: int) -> None:
        self.id = id
        self.campaign_id = campaign_id
        self.campaign_version = campaign_version
        self.campaign_erp_id = campaign_erp_id
        self.campaign_name = campaign_name
        self.total_discount = total_discount
        self.distributed_amount = distributed_amount

    @staticmethod
    def from_dict(obj: Any) -> 'LineCampaign':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        campaign_id = from_int(obj.get("campaignId"))
        campaign_version = from_int(obj.get("campaignVersion"))
        campaign_erp_id = from_int(obj.get("campaignErpId"))
        campaign_name = from_str(obj.get("campaignName"))
        total_discount = from_float(obj.get("totalDiscount"))
        distributed_amount = from_float(obj.get("distributedAmount"))
        return LineCampaign(id, campaign_id, campaign_version, campaign_erp_id, campaign_name, total_discount, distributed_amount)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["campaignId"] = from_int(self.campaign_id)
        result["campaignVersion"] = from_int(self.campaign_version)
        result["campaignErpId"] = from_int(self.campaign_erp_id)
        result["campaignName"] = from_str(self.campaign_name)
        result["totalDiscount"] = from_int(self.total_discount)
        result["distributedAmount"] = from_int(self.distributed_amount)
        return result


class Line:
    id: int
    sequence: int
    pos_document_id: int
    product_code: str
    product_name: str
    product_unit: str
    vat_percent: int
    amount: int
    total_price: int
    is_valid: bool
    vat_total: int
    barcode_no: str
    discount_total: int
    discount_total_direct: int
    discount_total_indirect: int
    discount_total_campaign: int
    salesman_id: int
    salesman_code: str
    description: str
    is_price_entered_by_user: bool
    line_campaigns: List[LineCampaign]

    def __init__(self, id: int, sequence: int, pos_document_id: int, product_code: str, product_name: str, product_unit: str, vat_percent: int, amount: int, total_price: int, is_valid: bool, vat_total: int, barcode_no: str, discount_total: int, discount_total_direct: int, discount_total_indirect: int, discount_total_campaign: int, salesman_id: int, salesman_code: str, description: str, is_price_entered_by_user: bool, line_campaigns: List[LineCampaign]) -> None:
        self.id = id
        self.sequence = sequence
        self.pos_document_id = pos_document_id
        self.product_code = product_code
        self.product_name = product_name
        self.product_unit = product_unit
        self.vat_percent = vat_percent
        self.amount = amount
        self.total_price = total_price
        self.is_valid = is_valid
        self.vat_total = vat_total
        self.barcode_no = barcode_no
        self.discount_total = discount_total
        self.discount_total_direct = discount_total_direct
        self.discount_total_indirect = discount_total_indirect
        self.discount_total_campaign = discount_total_campaign
        self.salesman_id = salesman_id
        self.salesman_code = salesman_code
        self.description = description
        self.is_price_entered_by_user = is_price_entered_by_user
        self.line_campaigns = line_campaigns

    @staticmethod
    def from_dict(obj: Any) -> 'Line':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        sequence = from_int(obj.get("sequence"))
        pos_document_id = from_int(obj.get("posDocumentId"))
        product_code = from_str(obj.get("productCode"))
        product_name = from_str(obj.get("productName"))
        product_unit = from_str(obj.get("productUnit"))
        vat_percent = from_int(obj.get("vatPercent"))
        amount = from_float(obj.get("amount"))
        total_price = from_float(obj.get("totalPrice"))
        is_valid = from_bool(obj.get("isValid"))
        vat_total = from_float(obj.get("vatTotal"))
        barcode_no = from_str(obj.get("barcodeNo"))
        discount_total = from_float(obj.get("discountTotal"))
        discount_total_direct = from_float(obj.get("discountTotalDirect"))
        discount_total_indirect = from_float(obj.get("discountTotalIndirect"))
        discount_total_campaign = from_float(obj.get("discountTotalCampaign"))
        salesman_id = from_int(obj.get("salesmanId"))
        salesman_code = from_str(obj.get("salesmanCode"))
        description = from_str(obj.get("description"))
        is_price_entered_by_user = from_bool(obj.get("isPriceEnteredByUser"))
        line_campaigns = from_list(LineCampaign.from_dict, obj.get("lineCampaigns"))
        return Line(id, sequence, pos_document_id, product_code, product_name, product_unit, vat_percent, amount, total_price, is_valid, vat_total, barcode_no, discount_total, discount_total_direct, discount_total_indirect, discount_total_campaign, salesman_id, salesman_code, description, is_price_entered_by_user, line_campaigns)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["sequence"] = from_int(self.sequence)
        result["posDocumentId"] = from_int(self.pos_document_id)
        result["productCode"] = from_str(self.product_code)
        result["productName"] = from_str(self.product_name)
        result["productUnit"] = from_str(self.product_unit)
        result["vatPercent"] = from_int(self.vat_percent)
        result["amount"] = from_int(self.amount)
        result["totalPrice"] = from_int(self.total_price)
        result["isValid"] = from_bool(self.is_valid)
        result["vatTotal"] = from_int(self.vat_total)
        result["barcodeNo"] = from_str(self.barcode_no)
        result["discountTotal"] = from_int(self.discount_total)
        result["discountTotalDirect"] = from_int(self.discount_total_direct)
        result["discountTotalIndirect"] = from_int(self.discount_total_indirect)
        result["discountTotalCampaign"] = from_int(self.discount_total_campaign)
        result["salesmanId"] = from_int(self.salesman_id)
        result["salesmanCode"] = from_str(self.salesman_code)
        result["description"] = from_str(self.description)
        result["isPriceEnteredByUser"] = from_bool(self.is_price_entered_by_user)
        result["lineCampaigns"] = from_list(lambda x: to_class(LineCampaign, x), self.line_campaigns)
        return result


class Payment:
    id: int
    pos_document_id: int
    payment_code: str
    payment_name: str
    amount: int
    is_change_amount: bool
    installment_count: str
    credit_card_batch_no: int
    credit_card_stan_no: int
    credit_card_terminal_id: str
    credit_card_no: str
    credit_card_acquirer_id: int
    currneys_type_code: str
    exchange_amount: int
    credit_card_authorization_code: str

    def __init__(self, id: int, pos_document_id: int, payment_code: str, payment_name: str, amount: int, is_change_amount: bool, installment_count: str, credit_card_batch_no: int, credit_card_stan_no: int, credit_card_terminal_id: str, credit_card_no: str, credit_card_acquirer_id: int, currneys_type_code: str, exchange_amount: int, credit_card_authorization_code: str) -> None:
        self.id = id
        self.pos_document_id = pos_document_id
        self.payment_code = payment_code
        self.payment_name = payment_name
        self.amount = amount
        self.is_change_amount = is_change_amount
        self.installment_count = installment_count
        self.credit_card_batch_no = credit_card_batch_no
        self.credit_card_stan_no = credit_card_stan_no
        self.credit_card_terminal_id = credit_card_terminal_id
        self.credit_card_no = credit_card_no
        self.credit_card_acquirer_id = credit_card_acquirer_id
        self.currneys_type_code = currneys_type_code
        self.exchange_amount = exchange_amount
        self.credit_card_authorization_code = credit_card_authorization_code

    @staticmethod
    def from_dict(obj: Any) -> 'Payment':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        pos_document_id = from_int(obj.get("posDocumentId"))
        payment_code = from_str(obj.get("paymentCode"))
        payment_name = from_str(obj.get("paymentName"))
        amount = from_float(obj.get("amount"))
        is_change_amount = from_bool(obj.get("isChangeAmount"))
        installment_count = from_str(obj.get("installmentCount"))
        credit_card_batch_no = from_int(obj.get("creditCardBatchNo"))
        credit_card_stan_no = from_int(obj.get("creditCardStanNo"))
        credit_card_terminal_id = from_str(obj.get("creditCardTerminalId"))
        credit_card_no = from_str(obj.get("creditCardNo"))
        credit_card_acquirer_id = from_int(obj.get("creditCardAcquirerId"))
        currneys_type_code = from_str(obj.get("currneysTypeCode"))
        exchange_amount = from_float(obj.get("exchangeAmount"))
        credit_card_authorization_code = from_str(obj.get("creditCardAuthorizationCode"))
        return Payment(id, pos_document_id, payment_code, payment_name, amount, is_change_amount, installment_count, credit_card_batch_no, credit_card_stan_no, credit_card_terminal_id, credit_card_no, credit_card_acquirer_id, currneys_type_code, exchange_amount, credit_card_authorization_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["posDocumentId"] = from_int(self.pos_document_id)
        result["paymentCode"] = from_str(self.payment_code)
        result["paymentName"] = from_str(self.payment_name)
        result["amount"] = from_int(self.amount)
        result["isChangeAmount"] = from_bool(self.is_change_amount)
        result["installmentCount"] = from_str(self.installment_count)
        result["creditCardBatchNo"] = from_int(self.credit_card_batch_no)
        result["creditCardStanNo"] = from_int(self.credit_card_stan_no)
        result["creditCardTerminalId"] = from_str(self.credit_card_terminal_id)
        result["creditCardNo"] = from_str(self.credit_card_no)
        result["creditCardAcquirerId"] = from_int(self.credit_card_acquirer_id)
        result["currneysTypeCode"] = from_str(self.currneys_type_code)
        result["exchangeAmount"] = from_int(self.exchange_amount)
        result["creditCardAuthorizationCode"] = from_str(self.credit_card_authorization_code)
        return result


class Data:
    id: int
    pos_document_id: int
    receipt_no: str
    document_type: int
    document_type_name: str
    document_no: str
    store_code: str
    pos_code: str
    user_code: str
    date: datetime
    start_date: datetime
    invoice_type: int
    sales_type: int
    refund_reason_id: int
    tax_number: str
    customer_id: int
    customer_card_no: str
    lines: List[Line]
    payments: List[Payment]
    closure_no: str
    linked_document_id: int
    linked_document_no: str
    customer_data: CustomerData
    price_id: int

    def __init__(self, id: int, pos_document_id: int, receipt_no: str, document_type: int, document_type_name: str, document_no: str, store_code: str, pos_code: str, user_code: str, date: datetime, start_date: datetime, invoice_type: int, sales_type: int, refund_reason_id: int, tax_number: str, customer_id: int, customer_card_no: str, lines: List[Line], payments: List[Payment], closure_no: str, linked_document_id: int, linked_document_no: str, customer_data: CustomerData, price_id: int) -> None:
        self.id = id
        self.pos_document_id = pos_document_id
        self.receipt_no = receipt_no
        self.document_type = document_type
        self.document_type_name = document_type_name
        self.document_no = document_no
        self.store_code = store_code
        self.pos_code = pos_code
        self.user_code = user_code
        self.date = date
        self.start_date = start_date
        self.invoice_type = invoice_type
        self.sales_type = sales_type
        self.refund_reason_id = refund_reason_id
        self.tax_number = tax_number
        self.customer_id = customer_id
        self.customer_card_no = customer_card_no
        self.lines = lines
        self.payments = payments
        self.closure_no = closure_no
        self.linked_document_id = linked_document_id
        self.linked_document_no = linked_document_no
        self.customer_data = customer_data
        self.price_id = price_id

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        pos_document_id = from_int(obj.get("posDocumentId"))
        receipt_no = from_str(obj.get("receiptNo"))
        document_type = from_int(obj.get("documentType"))
        document_type_name = from_str(obj.get("documentTypeName"))
        document_no = from_str(obj.get("documentNo"))
        store_code = from_str(obj.get("storeCode"))
        pos_code = from_str(obj.get("posCode"))
        user_code = from_str(obj.get("userCode"))
        date = from_datetime(obj.get("date"))
        start_date = from_datetime(obj.get("startDate"))
        invoice_type = from_int(obj.get("invoiceType"))
        sales_type = from_int(obj.get("salesType"))
        refund_reason_id = from_int(obj.get("refundReasonId"))
        tax_number = from_str(obj.get("taxNumber"))
        customer_id = from_int(obj.get("customerId"))
        customer_card_no = from_str(obj.get("customerCardNo"))
        lines = from_list(Line.from_dict, obj.get("lines"))
        payments = from_list(Payment.from_dict, obj.get("payments"))
        closure_no = from_str(obj.get("closureNo"))
        linked_document_id = from_int(obj.get("linkedDocumentId"))
        linked_document_no = from_str(obj.get("linkedDocumentNo"))
        customer_data = CustomerData.from_dict(obj.get("customerData"))
        price_id = from_int(obj.get("priceId"))
        return Data(id, pos_document_id, receipt_no, document_type, document_type_name, document_no, store_code, pos_code, user_code, date, start_date, invoice_type, sales_type, refund_reason_id, tax_number, customer_id, customer_card_no, lines, payments, closure_no, linked_document_id, linked_document_no, customer_data, price_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["posDocumentId"] = from_int(self.pos_document_id)
        result["receiptNo"] = from_str(self.receipt_no)
        result["documentType"] = from_int(self.document_type)
        result["documentTypeName"] = from_str(self.document_type_name)
        result["documentNo"] = from_str(self.document_no)
        result["storeCode"] = from_str(self.store_code)
        result["posCode"] = from_str(self.pos_code)
        result["userCode"] = from_str(self.user_code)
        result["date"] = self.date.isoformat()
        result["startDate"] = self.start_date.isoformat()
        result["invoiceType"] = from_int(self.invoice_type)
        result["salesType"] = from_int(self.sales_type)
        result["refundReasonId"] = from_int(self.refund_reason_id)
        result["taxNumber"] = from_str(self.tax_number)
        result["customerId"] = from_int(self.customer_id)
        result["customerCardNo"] = from_str(self.customer_card_no)
        result["lines"] = from_list(lambda x: to_class(Line, x), self.lines)
        result["payments"] = from_list(lambda x: to_class(Payment, x), self.payments)
        result["closureNo"] = from_str(self.closure_no)
        result["linkedDocumentId"] = from_int(self.linked_document_id)
        result["linkedDocumentNo"] = from_str(self.linked_document_no)
        result["customerData"] = to_class(CustomerData, self.customer_data)
        result["priceId"] = from_int(self.price_id)
        return result


class ResultSalesModel:
    success: bool
    id: int
    message: str
    error_message: str
    faulty_parameters: List[str]
    status_code: int
    status_code_message: str
    datas: List[Data]

    def __init__(self, success: bool, id: int, message: str, error_message: str, faulty_parameters: List[str], status_code: int, status_code_message: str, datas: List[Data]) -> None:
        self.success = success
        self.id = id
        self.message = message
        self.error_message = error_message
        self.faulty_parameters = faulty_parameters
        self.status_code = status_code
        self.status_code_message = status_code_message
        self.datas = datas

    @staticmethod
    def from_dict(obj: Any) -> 'ResultSalesModel':
        assert isinstance(obj, dict)
        success = from_bool(obj.get("success"))
        id = from_int(obj.get("id"))
        message = from_str(obj.get("message"))
        error_message = from_str(obj.get("errorMessage"))
        faulty_parameters = from_list(from_str, obj.get("faultyParameters"))
        status_code = from_int(obj.get("statusCode"))
        status_code_message = from_str(obj.get("statusCodeMessage"))
        datas = from_list(Data.from_dict, obj.get("datas"))
        return ResultSalesModel(success, id, message, error_message, faulty_parameters, status_code, status_code_message, datas)

    def to_dict(self) -> dict:
        result: dict = {}
        result["success"] = from_bool(self.success)
        result["id"] = from_int(self.id)
        result["message"] = from_str(self.message)
        result["errorMessage"] = from_str(self.error_message)
        result["faultyParameters"] = from_list(from_str, self.faulty_parameters)
        result["statusCode"] = from_int(self.status_code)
        result["statusCodeMessage"] = from_str(self.status_code_message)
        result["datas"] = from_list(lambda x: to_class(Data, x), self.datas)
        return result


def result_sales_model_from_dict(s: Any) -> ResultSalesModel:
    return ResultSalesModel.from_dict(s)


def result_sales_model_to_dict(x: ResultSalesModel) -> Any:
    return to_class(ResultSalesModel, x)
