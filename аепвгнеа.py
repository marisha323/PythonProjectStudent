import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 5
        self.progress = 0
        self.alive = True

    def to_eat(self):
        print("Васе пора кушать")
        self.progress += 1
        self.gladness -= 2

    def to_sleep(self):
        print("Васе пора спать")
        self.gladness += 2
        self.progress += 1

    def to_chill(self):
        print("Васе пора отдыхать")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
                print("Вася не хочет развиваться")
                self.alive = False
        elif self.gladness <= 0:
                print("У Васи депрессия")
                self.alive = False
        elif self.progress > 190:
                print("Вася гений")
                self.alive = False

    def end_of_day(self):
        print(f"Радость Васи = {self.gladness}")
        print(f"Развитие Васи = {round(self.progress, 2)}")

    def live(self, day):
        day = "День" + str(day) + "жизни" + self.name
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
nick = Cat(name="Васи")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)