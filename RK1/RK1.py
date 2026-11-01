# Федяев А.С. ИУ5-33Б Вариант 16 В
from operator import itemgetter

class Book:
    def __init__(self, id, title, price, shop_id):
        self.id = id
        self.title = title
        self.price = price
        self.shop_id = shop_id


class Shop:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ShopBook:
    def __init__(self, shop_id, book_id):
        self.shop_id = shop_id
        self.book_id = book_id

shops = [
    Shop(1, 'Читай-город'),
    Shop(2, 'Библио-Глобус'),
    Shop(3, 'Московский Дом Книги'),
    Shop(11, 'Республика'),
    Shop(22, 'Лабиринт'),
    Shop(33, 'Буквоед'),
]

books = [
    Book(1, 'Алгоритмы: построение и анализ', 2400, 1),
    Book(2, 'Архитектура компьютера', 1950, 2),
    Book(3, 'Изучаем Python', 1800, 2),
    Book(4, 'Анализ данных в Python', 1450, 3),
    Book(5, 'Чистый код', 1200, 3),
    Book(6, 'Совершенный код', 2100, 3),
]

shops_books = [
    ShopBook(1, 1),
    ShopBook(2, 2),
    ShopBook(2, 3),
    ShopBook(3, 4),
    ShopBook(3, 5),
    ShopBook(3, 6),
    ShopBook(11, 1),
    ShopBook(11, 4),
    ShopBook(22, 2),
    ShopBook(22, 5),
    ShopBook(33, 3),
    ShopBook(33, 6),
]


def main():
    one_to_many = [
        (b.title, b.price, s.name)
        for s in shops
        for b in books
        if b.shop_id == s.id
    ]

    many_to_many_temp = [
        (s.name, sb.shop_id, sb.book_id)
        for s in shops
        for sb in shops_books
        if s.id == sb.shop_id
    ]

    many_to_many = [
        (b.title, b.price, shop_name)
        for shop_name, shop_id, book_id in many_to_many_temp
        for b in books
        if b.id == book_id
    ]

    print('Задание В1')
    res_1 = [
        (title, shop_name)
        for title, _, shop_name in one_to_many
        if title.startswith('А')
    ]
    print(res_1)

    print('\nЗадание В2')
    res_2_unsorted = []
    for s in shops:
        s_books = list(filter(lambda i: i[2] == s.name, one_to_many))
        if len(s_books) > 0:
            s_prices = [price for _, price, _ in s_books]
            s_price_min = min(s_prices)
            res_2_unsorted.append((s.name, s_price_min))

    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    print(res_2)

    print('\nЗадание В3')
    res_3 = sorted(many_to_many, key=itemgetter(0))
    print(res_3)


if __name__ == '__main__':
    main()