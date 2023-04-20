class Lot:
    def __init__(self, dict_lot):

        self.lot_number = dict_lot.get('Извещение, лот', None)
        self.trade_type = dict_lot.get('Вид торгов', None)
        self.e_platform = dict_lot.get('Электроннаяплощадка', None)
        self.subject_property_location = dict_lot.get('Субъект местонахождения имущества', None)
        self.start_date = dict_lot.get('Дата и время начала подачи заявок', None)
        self.closing_date = dict_lot.get('Дата и время окончания подачи заявок', None)
        self.date_of_bidding = dict_lot.get('Дата проведения торгов', None)
        self.subject_of_bidding = dict_lot.get('Предмет торгов (наименование лота)', None)
        self.lot_description = dict_lot.get('Описание лота', None)
        self.property_location = dict_lot.get('Местонахождение имущества', None)
        self.object_category = dict_lot.get('Категория объекта', None)
        self.form_of_ownership = dict_lot.get('Форма собственности', None)
        self.term_of_agreement = dict_lot.get('Срок заключения договора', None)
        self.type_of_contract = dict_lot.get('Вид договора', None)
        self.lease_term = dict_lot.get('Срок аренды', None)
        self.initial_price = dict_lot.get('Начальная цена', None)
        self.auction_step = dict_lot.get('Шаг аукциона', None)
        self.deposit_amount = dict_lot.get('Размер задатка', None)
        self.recipient = dict_lot.get('Получатель', None)
        self.purpose_of_payment = dict_lot.get('Назначение платежа', None)
        self.cadastral_number = dict_lot.get('Кадастровый номер земельного участка', None)
        self.land_area = dict_lot.get('Площадь земельного участка', None)
        self.type_of_use = dict_lot.get('Вид разрешённого использования земельного участка', None)
        self.application_form = dict_lot.get('Форма заявки', None)
        self.status = dict_lot.get('Статус', None)

        self.link_doc = dict_lot.get('link_doc', None)
        self.link_lot = dict_lot.get('link_lot', None)


    def moving(self):
        print('В работу')
        pass