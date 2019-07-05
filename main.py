def file_data_open():
    with open('recipes.txt', encoding='utf-8') as f:
        counter = 0
        ingridient_s = list()
        cook_book = dict()
        dish = ''
        for line in f:  # Проходимся по строке в файле
            line = line.rstrip()
            counter += 1
            if counter == 1:  # Первая строка всегда название блюда
                dish = line
            elif counter == 2:  # Вторая указывает на количество ингредиентов
                pass
            elif line == '':  # Пустая строка значит переход к следующему блюду
                counter = 0
                dish_list = {dish: ingridient_s}
                cook_book.update(dish_list)
                # print(cook_book)                     # ЧТОБЫ ПОСМОТРЕТЬ ВЫВОД!
                ingridient_s = []
            else:  # Все остальные строки непосредственно сами составляющие блюда
                name = ''
                weight = ''
                system = ''
                num_word_in_str = 1
                for symbol in line:  # Проходимся по каждой строке
                    if (symbol == '|'):
                        num_word_in_str += 1
                    elif num_word_in_str == 1:
                        name += symbol
                    elif num_word_in_str == 2:
                        weight += symbol
                    elif num_word_in_str == 3:
                        system += symbol
                ing = {'ingridient_name': name.strip(), 'quantity': weight.strip(), 'measure': system.strip()}
                ingridient_s.append(ing)
        return cook_book


def input_dish():
    dish_list = list()
    while True:
        try:
            dish = input('Какое блюдо готовим? ')
            for dish_l in file_data_open():
                if dish_l == dish:
                    dish_list.append(dish)
                    exist_in_menu = True
                    break
                else:
                    exist_in_menu = False
            if exist_in_menu == False:
                raise NameError
            if input('Ещё что-нибудь? (y/n) ') == 'y':
                pass
            else:
                break
        except NameError:
            print('Блюда нет в менню')
    return dish_list


def input_persone():
    while True:
        try:
            persone = int(input('На сколько человек готовим? '))
            return persone
        except:
            print('Введите число')
    return


def get_shop_list_by_dishes(dish_list, persone):
    menu = file_data_open()
    answer_list = []
    unik_list = []
    # dish_list = set(dish_list)
    # a = dish_list.intersection(menu)
    # print(a)

    for dish_in in dish_list: # для первого блюда из введённого
      for dish_l in menu:     # проходясь по меню сверяем
        if dish_in == dish_l:
          ingr_list = menu.get(dish_in) # заходим в список ингредиентов [{},{},{}]
          for ingr in ingr_list:
            ingr_unik = {ingr.get('ingridient_name'): {'measure': ingr.get('measure'),
                                                                'quantity': int(ingr.get('quantity')) * persone}}
            try:
                assert ingr_unik.keys() in answer_list,''
                a = (ingr_unik.get(ingr.get('ingridient_name'))).get('quantity')# Нужно зайти внутрь словаря и увеличить колличество
                for i in unik_list:
                    if i.keys() == ingr_unik.keys():
                        new = {ingr.get('ingridient_name'): {'measure': ingr.get('measure'),
                                                                'quantity': (int(ingr.get('quantity')) * persone) + a}}
                        i.update(new)
            except AssertionError:
                unik_list.append(ingr_unik)
                answer_list.append(ingr_unik.keys())
                # print(unik_list, '\n')
                # print(answer_list, '\n')

    print(unik_list)
    # for i in answer_list:
    #     if (set(i)).intersection(set(unik_list)) != set(None):
    #
    #         print(set(i).intersection(set(unik_list)))




    # Нужный нам выод:
    # {
    #   'Картофель': {'measure': 'кг', 'quantity': 2},
    #   'Молоко': {'measure': 'мл', 'quantity': 200},
    #   'Помидор': {'measure': 'шт', 'quantity': 4},
    #   'Сыр гауда': {'measure': 'г', 'quantity': 200},
    #   'Яйцо': {'measure': 'шт', 'quantity': 4},
    #   'Чеснок': {'measure': 'зубч', 'quantity': 6}
    # }


get_shop_list_by_dishes(input_dish(), input_persone())

# Я Что-то невероятно туплю. Неполучается сформировать файл в нужный вид. Ощущение, что всё на костылях строится.