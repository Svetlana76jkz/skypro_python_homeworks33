

rate_as_str=input("Оцените работу оператора от 1 до 5:") #str
rate=int(rate_as_str) #int



if (rate< 1 ):
    rate=1

if (rate > 5 ):
    rate=5




feedback=""

if rate ==1:
    feedback=input("Расскажите, что нам улучшить:")

elif rate ==2:
    feedback=input("Расскажите, что вас смутило:")

elif rate ==3:
    feedback=input("Расскажите, как нам стать лучше:")
                         
elif rate ==4:
    feedback=input("Расскажите, почему не 5:")

else:
    feedback=input("Расскажите, за что похвалить сотрудника: ")

print(feedback)




