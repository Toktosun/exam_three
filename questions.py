# Как вы понимаете что такое фреймворк? Для чего используется?
# Что такое SQL? И приведите пример SQL кода.
# Что такое ORM? Где вы с ним сталкивались?
# Какие принципы ООП вы знаете? И опишите вкратце каждый.
# Приведите пример ассоциации и агрегации между классами?


# 1. framework – это каркас, который состоит из множества различных библиотек,
# которые облегчают разработку программного продукта или сайта.
# Это программные продукты,которые упрощают создание и поддержку технически сложных
# или нагруженных проектов.

# 2. SQL — это язык программирования структурированных запросов,
# который используется в качестве эффективного способа сохранения данных
# INSERT INTO table (user_id, phone_number) VALUE ('2','200');

# 3. ORM - технология программирования, суть которой заключается в создании виртуальной базы данных.
# Мы сталкивались с orm в django.

# 4. ООП имеет несколько принципов, такие как:
# Данные структурируются в виде объектов, каждый из которых имеет определенный тип.
# Классы – результат формализации решаемой задачи.
# Внутри объекта инкапсулируется логика работы с относящейся к нему информацией.
# Объекты в программе взаимодействуют друг с другом, обмениваются запросами и ответами.
# При этом объекты одного типа сходным образом отвечают на одни и те же запросы.
# Объекты могут организовываться в более сложные структуры, например, включать другие объекты или наследовать от одного или нескольких объектов.

# 5. ассоциация - это связь между классами, а агрегация это вложенность одного класса в другой,
# но при этом класс обертка не управляет сроком жизни вложенного объекта

# Aссоциация
# class A(object):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def addNums():
#         self.b + self.c

# class B(object):
#     def __init__(self, d, e):
#         self.d = d
#         self.e = e

#     def addAllNums(self, Ab, Ac):
#         x = self.d + self.e + Ab + Ac
#         return x

# ting = A("privet", 2, 6)
# ling = B(5, 9)

# print ling.addAllNums(ting.b, ting.c)

# Агрегация
# class A(object):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def addNums():
#         self.b + self.c

# class B(object):
#     def __init__(self, d, e, A):
#         self.d = d
#         self.e = e
#         self.A = A

#     def addAllNums(self):
#         x = self.d + self.e + self.A.b + self.A.c
#         return x

# ting = A("yo", 2, 6)
# ling = B(5, 9, ting)

# print ling.addAllNums()