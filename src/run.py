from buildings import ResidentialBuilding


a = ResidentialBuilding("Дом Осадчих",40,100,6,"Белый")
b = a.copy()
b.name = "Дом Боляковых"
b.size_x = 100
b.size_y = 100
b.room = 10
b.color = "Розовый"

print(a)
print()
print(b)
print()
c = a.copy()

c.name = "Дом Павловых"
c.size_x = 30
c.size_y = 50
c.room = 3
c.color = "Черный"
print(c)