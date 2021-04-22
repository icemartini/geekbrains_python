# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость 60!')
        else:
            print(f'Вы движетесь со скоростью {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость 40!')
        else:
            print(f'Вы движетесь со скоростью {self.speed}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.__init__(self, speed, color, name, is_police)

town = TownCar(200, 'black', 'hyunday')
sport = SportCar(300, 'red', 'ferrari')
work = WorkCar(30, 'white', 'nissan')
police = PoliceCar(180, 'grey', 'kia')

print(town.speed, town.color, town.name, town.is_police)
town.go()
town.show_speed()
sport.show_speed()
sport.stop()
work.show_speed()
police.show_speed()
police.turn('налево')
