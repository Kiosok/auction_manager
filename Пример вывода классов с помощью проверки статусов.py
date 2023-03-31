class MyClass:
    def __init__(self, status):
        self.status = status

    def show(self):
        print("Class with status", self.status)


# Создание списка классов
classes = [MyClass("новый"), MyClass("старый"), MyClass("старый"), MyClass("новый")]
# Вывод классов в соответствующие окна
for c in classes:
    if c.status == "новый":
        print("Окно новых классов:")
        c.show()
    elif c.status == "старый":
        print("Окно старых классов:")
        c.show()