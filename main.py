# 📌Создайте класс Моя Строка, где: 📌будут доступны все возможности str 📌дополнительно хранятся имя автора строки и время создания (time.time)
# class NamedInt(int):
#     def __new__(cls, value, name):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         print(f'Создал класс {cls}')
#         return instance
#
# '''
# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
# Добавьте  строки документации для классов.
# '''
# import datetime
#
#
# class MyStr(str):
#     """
#     My class  comment
#     """
#     d = 5
#
#     def __new__(cls, value, author_name):
#         """
#         Создает экземпляр
#         :param value:
#         :param author_name:
#         creation_time = datetime.datetime.now()
#         """
#         instance = super().__new__(cls, value)
#         instance.author_name = author_name
#         instance.creation_time = datetime.datetime.now()
#         return instance
#
#
# if __name__ == '__main__':
#
#     s = MyStr("Строка", 'Илюша')            # к этому классу теперь все методы str применимы
#     print(s, s.author_name, s.creation_time)
#     print(s.upper())
#     #print(s.upper().author_name)
#
#     print(MyStr.__doc__)
#     print(MyStr.__new__.__doc__)
#     print(help(MyStr))
    #
    # 📌Создайте класс Архив, который хранит пару свойств.Например, число и строку. 📌При нового экземпляра  класса, старые данные из ранее созданных  экземпляров  сохраняются в пару  списковархивов 📌list - архивы также являются свойствами экземпляра
# class Archive:
#
#     numbers_archive = []
#     some_strs_archive = []
#     last_number = None
#     last_str = None
#
#
#     def __init__(self, number, some_str):
#         self.number = number
#         self.some_str = some_str
#
#         if Archive.last_number is not None:
#             Archive.numbers_archive.append(Archive.last_number)
#             Archive.some_strs_archive.append(Archive.last_str)
#         Archive.last_number = number
#         Archive.last_str = some_str
#
#     def __str__(self):
#         return f'Number: {self.number}, string: {self.some_str}, archive: {list(zip(Archive.numbers_archive,Archive.some_strs_archive))} '
#
#
# if __name__ == '__main__':
#     arc1 = Archive(1, "str1")
#     print(arc1)
#     # print(arc1.number, arc1.numbers_archive, Archive.numbers_archive)
#     arc2 = Archive(2, "str2")
#     print(arc2)
#     # print(arc2.number, arc2.numbers_archive, Archive.numbers_archive)
#     arc3 = Archive(3, "str3")
#     print(arc3)
#     # print(arc3.number, arc3.numbers_archive, Archive.numbers_archive)
#
# class Archive:
#     _instance = None
#     _archive = []
#
#     def __new__(cls, name: str, age: int):
#         instance = super().__new__(cls)
#         if cls._instance:
#             cls._archive.append(cls._instance)
#         cls._instance = instance
#         instance.archive = cls._archive
#         return cls._instance
#
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f'{self.name} {self.age}'




# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра
#
# Добавьте  строки документации для классов.

'''

class Archive:
    """
    Архив, который хранит пару свойств. При нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списковархивов  list-архивы также являются свойствами экземпляра
    добавить repr
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        СИНГЛТОН ПАТТЕРН
        :param args:
        :param kwargs:
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.numbers_archive = []
            cls.some_strs_archive = []
        else:
            cls._instance.numbers_archive.append(cls._instance.number)
            cls._instance.some_strs_archive.append(cls._instance.some_str)
        return cls._instance

    def __init__(self, number, some_str):
        """
        init
        :param number:
        :param some_str:
        """
        self.number = number
        self.some_str = some_str

    def __str__(self):
        """
        Human-readable representation
        :return:
        """
        return f'Number: {self.number}, string: {self.some_str}, archive: {list(zip(self.numbers_archive,self.some_strs_archive))} '

    def __repr__(self):
        return f'Archive({self.number},{self.some_str})'


if __name__ == '__main__':
    arc1 = Archive(1, "str1")
    print(arc1)
    # print(arc1.number, arc1.numbers_archive, Archive.numbers_archive)
    arc2 = Archive(2, "str2")
    print(arc2)
    # print(arc2.number, arc2.numbers_archive, Archive.numbers_archive)
    arc3 = Archive(3, "str3")
    print(arc3)
    # print(arc3.number, arc3.numbers_archive, Archive.numbers_archive)

    print(Archive.__doc__)
    print(Archive.__new__.__doc__)
    # print(help(Archive))

    print(arc1.__repr__())
    print(arc2.__repr__())
    print(arc3.__repr__())