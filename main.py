class Student:
    age = 0
    name = ''
    money = 0

    def __init__(self, age, name, money):
        self.name = name
        self.age = age
        self.money = money

    def earn_money(self):
        self.money += 1000

    def spend_money(self, amount):
        self.money -= amount

    def __str__(self):
        return f'Student {self.name}'


student1 = Student(15, 'Bob', 1000)
student2 = Student(18, 'Ann', 2500)

student1.name = 'Bob'
print(student1.money)
student1.earn_money()
print(student1.money)
student1.spend_money(500)
print(student1.money)


class Sims:
    def __init__(self, experience, years, age, name, money, hungry, health):
        self.name = name
        self.age = age
        self.money = money
        self.hungry = hungry
        self.health = health
        self.years = years
        self.experience = experience
        self.job = None
        self.house = None
        self.family = None

    def buy_home(self, home):
        if home.price <= self.money:
            print('Congrats! You bought this house!')
            self.house = home
            home.humans.append(self)
            self.money -= home.price
        else:
            print('Looks like you do not have enough money')

    def buy_car(self, car):
        if car.price <= self.money:
            print(f"Congratulations! You bought a {car.brand} car!")
            self.money -= car.price
            car.humans.append(self)
            print(f"Your money after buying {car.brand}: {self.money}")
        else:
            print("Sorry, you don't have enough money to buy this car.")


class Home:
    def __init__(self, price):
        self.furniture = []
        self.humans = []
        self.price = price

    def __str__(self):
        return f'home for {self.price}'


class Job:
    def __init__(self, salary, name, experience, years):
        self.salary = salary
        self.name = name
        self.experience = experience
        self.years = years
        self.job = None

    def get_work(self, person):
        if self.experience >= self.years:
            person.job = self
            print('Congrats! You got a good job')
        else:
            print('Sorry! You are not suitable for this job')

    def work(self, person):
        person.money += self.salary

    def eat(self, person):
        person.hungry += 20


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sleep = 0

    def do_sleep(self):
        self.sleep += 10


class Student(Human):
    def study(self):
        self.sleep -= 10


student = Student('Bob', 12)
student.do_sleep()
student.study()
bob = Sims(10, 30,30,'Bob', 20000, 100, 100)
villa = Home(15000)
print(bob.house, villa.humans)
bob.buy_home(villa)
print(bob.house, villa.humans, bob.money)


class Restaurant(Home):
    def work(self):
        if len(self.humans) != 0:
            self.humans[0].money += 1000
class Car:
    def __init__(self, brand, price, comfort):
        self.brand = brand
        self.price = price
        self.comfort = comfort
        self.humans = []
car1 = Car("Tesla", 50000, 30)
car2 = Car("Toyota", 20000, 20)
print(car1)
print(car2)
sim = Sims(10, 30, 30, 'Bob', 20000, 100, 100)
sim2 = Sims(12, 25, 25, 'Alice', 30000, 90, 90)
sim.buy_car(car1)
sim2.buy_car(car2)