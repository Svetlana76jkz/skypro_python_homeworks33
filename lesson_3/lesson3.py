from user import User
from card import Card

alex = User("Alex")

alex.sayName()
alex.setAge(33)
alex.sayAge()



card = Card("4235 9857 1597 6245", "01/99", "Alex F")

alex.addCard(card)
alex.getCard().pay(1000)

