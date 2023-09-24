import random

class Cipher:

    def __init__(self, number):

        self.number = number

    def __encapsulate (self) :
        operation = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 10)

        if operation == '+':
            self.number += operand

        if operation == '-':

            self.number -= operand

        if operation == '*':

            self.number *= operand

        if operation == '/':

             self.number /= operand

    def get_result(self):

      self.encapsulate()
      return self.number

# Використання об'єкта-шифратора

number = int(input("Введіть число: "))

cipher = Cipher(number)

result = cipher.get_result()

print("Результат: ", result)








