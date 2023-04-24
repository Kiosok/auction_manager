from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Lot(Base):
    __tablename__ = 'lots'
    # id = Column(Integer)
    lot_number = Column(String, primary_key=True)
    trade_type = Column(String)
    e_platform = Column(String)
    subject_property_location = Column(String)
    start_date = Column(String)
    closing_date = Column(String)
    date_of_bidding = Column(String)
    subject_of_bidding = Column(String)
    lot_description = Column(String)
    property_location = Column(String)
    object_category = Column(String)
    form_of_ownership = Column(String)
    term_of_agreement = Column(String)
    type_of_contract = Column(String)
    lease_term = Column(String)
    initial_price = Column(String)
    auction_step = Column(String)
    deposit_amount = Column(String)
    recipient = Column(String)
    purpose_of_payment = Column(String)
    cadastral_number = Column(String)
    land_area = Column(String)
    type_of_use = Column(String)
    application_form = Column(String)

    status = Column(String)
    link_lot = Column(String)

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
        self.link_lot = dict_lot.get('link_lot', None)

    def moving(self):
        print('В работу')
        # moving to archive
        # moving to status in work
        # Move to approval status
        #
        pass

#
# gov = Lot({'Извещение, лот': '№21000000010000000069, лот №1', 'Вид торгов': 'Аренда и продажа земельных участков',
#            'Субъект местонахождения имущества': 'Кемеровская область',
#            'Дата и время начала подачи заявок': '21.03.2023 09:00 (МСК+4)',
#            'Дата и время окончания подачи заявок': '24.04.2023 15:00 (МСК+4)',
#            'Дата проведения торгов': '28.04.2023 11:00 (МСК+4)',
#            'Предмет торгов (наименование лота)': 'Земельный участок, пл.508 515 кв.м, кадастровый №42:02:0105005:172, разрешенное использование: для сельскохозяйственного производства, по адресу: Кемеровская обл, Гурьевский муниципальный район.',
#            'Описание лота': 'Земельный участок, пл.508 515 кв.м, кадастровый №42:02:0105005:172, разрешенное использование: для сельскохозяйственного производства, по адресу: Кемеровская обл, Гурьевский муниципальный район.',
#            'Местонахождение имущества': 'Кемеровская обл, Гурьевский муниципальный район',
#            'Категория объекта': 'Земли сельскохозяйственного назначения',
#            'Форма собственности': 'Собственность субъектов РФ',
#            'Сведения о решении о проведении аукциона': 'от 06.12.2022 №4-2/2530',
#            'Дата принятия решения о проведении аукциона': '06.12.2022',
#            'Срок заключения договора': 'Не допускается заключение договора ранее чем через десять дней со дня размещения информации о результатах аукциона на официальном сайте торгов Российской Федерации в сети "Интернет"',
#            'Вид договора': 'Договор купли-продажи', '': '', 'Начальная цена': '41\xa0220\xa0226,00\xa0₽',
#            'Шаг аукциона': '1\xa0236\xa0606,78\xa0₽', 'Размер задатка': '41\xa0220\xa0226,00\xa0₽',
#            'Получатель': 'ГОСУДАРСТВЕННОЕ ПРЕДПРИЯТИЕ "ФОНД ИМУЩЕСТВА КУЗБАССА"', 'ИНН': '4205231091',
#            'КПП': '420501001', 'Наименование банка получателя': 'ФИЛИАЛ «НОВОСИБИРСКИЙ» АО «АЛЬФА-БАНК»',
#            'Расчетный счет (казначейский счет)': '40602810123060000001', 'Лицевой счет': '—', 'БИК': '045004774',
#            'Корреспондентский счет (ЕКС)': '30101810600000000774',
#            'Назначение платежа': 'Назначение платежа: “Задаток  (наименование лота, № лота, дата торгов)”. Получатель - Кузбассфонд ИНН/КПП 4205231091/420501001 р/с 40602810123060000001 в ФИЛИАЛЕ «НОВОСИБИРСКИЙ» АО «АЛЬФАБАНК» к/с 30101810600000000774 БИК 045004774  (комиссия за перечисление денежных средств взимается за счет претендента)',
#            'Срок и порядок внесения задатка': 'указано в извещении', 'Порядок возврата задатка': 'указано в извещении',
#            'Кадастровый номер земельного участка': '42:02:0105005:172', 'Площадь земельного участка': '508\xa0515 м2',
#            'Вид разрешённого использования земельного участка': 'Обеспечение сельскохозяйственного производства',
#            'Форма заявки': 'Аукцион', 'Статус': 'Определение победителя',
#            'link_lot': 'https://torgi.gov.ru/new/public/lots/lot/21000000010000000069_1/(lotInfo:info)?fromRec=false'}
#           )
#
#
#
# engine = create_engine('sqlite:///lots.db')
# Session = sessionmaker(bind=engine)
# Base.metadata.create_all(engine)  # create tables
# session = Session()
# session.merge(gov)
# session.commit()