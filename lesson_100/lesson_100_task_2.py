from smartphone1 import Smartphone1

catalog1 = []

catalog1.append(Smartphone1("Apple","iPhone 12", +78945612312))
catalog1.append(Smartphone1("Galaxy S21", "Samsung", +789456123360))
catalog1.append(Smartphone1("OnePlus 9", "OnePlus", +78945612345))
catalog1.append(Smartphone1("Mi 11", "Xiaomi", +78945612385))
catalog1.append(Smartphone1("Pixel 5", "Google", +78945612343))


for phone1 in catalog1:
    print(f"{phone1.brand}, {phone1.model},{phone1.number_phone}")