class City:
    def __init__(self, name):
        self.name = name

    def move_to_old_column(self, old_column, new_column):
        if self.name in new_column:
            new_column.remove(self.name)
            old_column.append(self.name)

cities = [City("New York"), City("London"), City("Paris")]

new_column = [city.name for city in cities]
old_column = []

print("New\tOld")
for i in range(len(new_column)):
    print(f"{new_column[i]}\t{old_column[i] if i < len(old_column) else ''}")

cities[1].move_to_old_column(old_column, new_column)

print("\nAfter moving London to old column:")
print("New\tOld")
for i in range(len(new_column)):
    print(f"{new_column[i]}\t{old_column[i] if i < len(old_column) else ''}")


# А