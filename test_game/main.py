class Lot:
    def __init__(self, name, link, path=''):
        self.name = name
        self.link = link
        self.path = path

    def show_all(self):
        print(f'{self.name}{self.link}{self.path}')


class Download:
    def __init__(self, lot):
        self.name = lot.name
        self.link = lot.link
        self.lot = lot

    def downloading_files(self):
        print(f'Перешёл на страницу - {self.link}')
        print(f'Файлы скачены в папку - /path/{self.name}')
        self.lot.path = f'/path/{self.name}'


lot_55587 = Lot('55587', 'http/:good')
lot_55587.show_all()

dow_lot = Download(lot_55587)
dow_lot.downloading_files()

print(lot_55587.path)






