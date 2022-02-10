class Lemonade:

    def __init__(self, additives):
        self.additives = additives

    def drink_info(self):
        print(f'Лимонад с добавкой: {self.additives}\n')

    def lim(self):
        print(f'Обычная газировка: {self.additives}\n')


first_lemonade = Lemonade('Сироп')
print(first_lemonade.drink_info())
