from address1 import Address1
from mailing1 import Mailing1

to_address = Address1('123000','г.Москва', 'ул.Неизвестная', 'д.1б', 'кв.20')
from_address = Address1('420000', 'г.Казань', 'ул.Известная', 'д.16', 'кв.69')
mailing1= Mailing1('to_address','from_address', '125', 'fghfg1566')

print(f"Отправление {mailing1.track} из {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house}, {to_address.apartment} в {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house}, {from_address.apartment}. Стоимость {mailing1.cost} рублей.")