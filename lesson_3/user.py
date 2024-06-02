class User:
    age = 0;

    def __init__(self, name):
        print("я создался")
        self.username = name

    def sayName(self):
        print("Меня зовут ", self.username )

    def sayAge(self):
        print(self.age)

    def setAge(self, newAge):
        self.age = newAge

mark = User("Mark")
alex = User("Alex")
marta = User("Marta")
svetlana = User("Svetlana")
igor = User("Igor")

alex.sayName()
alex.sayAge()
alex.setAge(33)
alex.sayAge()
mark.sayName()
igor.sayName()
svetlana.sayName()
marta.sayName()