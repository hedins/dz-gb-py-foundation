TEXT_DIGITS = {
    'а': ('Анна', 'Август'),
    'б': ('Барбара', 'Борис'),
    'в': ('Варвара', 'Василий'),
    'г': ('Галина', 'Григорий'),
    'д': ('Доброгнева', 'Денис'),
    'е': ('Ева', 'Евгений'),
    'ж': ('Жанна', 'Жан'),
    'з': ('Зинаида', 'Захар'),
    'и': ('Изольда', 'Иван'),
    'к': ('Клара', 'Константин'),
    'л': ('Лея', 'Лазарь'),
    'м': ('Мариана', 'Михаил'),
    'н': ('Нина', 'Николай'),
    'о': ('Олимпия', 'Олег'),
    'п': ('Пелагея', 'Пертурабо'),
    'р': ('Рената', 'Роман'),
    'с': ('Светлана', 'Сангвний'),
    'т': ('Тамара', 'Тимфей'),
    'у': ('Ульяна', 'Уильям'),
    'ф': ('Фаина', 'Федор'),
    'х': ('Хильда', 'Хуан'),
    'ц': ('Целестина', 'Цэрэндорж'),
    'ч': ('Чулпан', 'Чеслав'),
    'ш': ('Шарлотта', 'Шалом'),
    'э': ('Эльза', 'Эраст'),
    'ю': ('Юнона', 'Юрий'),
    'я': ('Ядвига', 'Яков'),
}


def thesaurus(*names, sort=False):
    """Возращает список имен по первой букве
    :param names: список имен
    :param sort: отсортировать список
    """
    result = {}
    for name in names:
        key = name[0]
        result[key.upper()] = TEXT_DIGITS[key.lower()]
    if sort:
        result = dict(sorted(result.items(), key=lambda x: x[0]))
    return result


print(thesaurus('е', 'б', sort=True))
