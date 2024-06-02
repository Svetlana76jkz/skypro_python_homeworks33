from turtle import *

t = Turtle() # Чтобы начать работу с модулем, нужно ввести объект Turtle()
t.screen.setup(800, 800) # ввести окно для графических объектов,где x и y – ширина и высота
t.screen.bgcolor("orange")
t.shape("turtle")
t.color("blue")
t.stamp()
t.color("black")
t.up()
t.fd(50)
t.down()
t.circle(200, 70)
t.screen.exitonclick() #Чтобы программа с модулем turtle на Python работала корректно, в самом конце программы всегда нужно прописывать две команды.
t.screen.mainloop() #  t.screen.exitonclick()- реагирует на нажатие кнопки мыши.  t.screen.mainloop() останавливает выполнение программы.