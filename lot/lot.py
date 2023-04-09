class Lot:
    def __init__(self, lot_number, trade_type, e_platform, property_location, start_date,
                 closing_date, date_of_bidding, subject_of_bidding, lot_description, subject_property_location,
                 object_category):

        self.lot_number = lot_number # Номер лота
        self.trade_type = trade_type # Вид торгов
        self.e_platform = e_platform  # Электроннаяплощадка
        self.subject_property_location = subject_property_location  # Субъект местонахождения имущества
        self.start_date = start_date  # Дата и время начала подачи заявок
        self.closing_date = closing_date  # Дата и время окончания подачи заявок
        self.date_of_bidding = date_of_bidding  # Дата проведения торгов
        self.subject_of_bidding = subject_of_bidding  # Предмет торгов
        self.lot_description = lot_description  # Описание лота
        self.property_location = property_location  # Местонахождение имущества
        self.object_category = object_category  # Категория объекта
        self.form_of_ownership
