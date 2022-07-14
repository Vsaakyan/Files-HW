# TASK 1
from pprint import pprint
import os


def open_dict_txt():

    """
    This function makes a dictionary
    from files .txt similar in structure like this
    """

    with open('file.txt', encoding='utf-8') as file_obj:
        cook_book = {}
        keys_list = ['ingredient_name', 'quantity', 'measure']
        for line in file_obj:
            list_ = []
            data_l = line
            quantity = int(file_obj.readline())

            for ingredients in range(quantity):
                parse_str = str(file_obj.readline().strip()).split('|')
                ingredient_dict = {keys_list[i]: parse_str[i] for i in range(len(keys_list))}
                list_.append(ingredient_dict)
            file_obj.readline()
            cook_book[data_l.strip()] = list_
    return cook_book


#pprint(open_dict_txt())


# TASK 2
cook_book = {'Запеченный картофель': [{'ingredient_name': 'Картофель ',
                           'measure': ' кг',
                           'quantity': ' 1 '},
                          {'ingredient_name': 'Чеснок ',
                           'measure': ' зубч',
                           'quantity': ' 3 '},
                          {'ingredient_name': 'Сыр гауда ',
                           'measure': ' г',
                           'quantity': ' 100 '}],
 'Омлет': [{'ingredient_name': 'Яйцо ', 'measure': ' шт', 'quantity': ' 2 '},
           {'ingredient_name': 'Молоко ',
            'measure': ' мл',
            'quantity': ' 100 '},
           {'ingredient_name': 'Помидор ',
            'measure': ' шт',
            'quantity': ' 2 '}],
 'Утка по-пекински': [{'ingredient_name': 'Утка ',
                       'measure': ' шт',
                       'quantity': ' 1 '},
                      {'ingredient_name': 'Вода ',
                       'measure': ' л',
                       'quantity': ' 2 '},
                      {'ingredient_name': 'Мед ',
                       'measure': ' ст.л',
                       'quantity': ' 3 '},
                      {'ingredient_name': 'Соевый соус ',
                       'measure': ' мл',
                       'quantity': ' 60 '}],
 'Фахитос': [{'ingredient_name': 'Говядина ',
              'measure': ' г',
              'quantity': ' 500 '},
             {'ingredient_name': 'Перец сладкий ',
              'measure': ' шт',
              'quantity': ' 1 '},
             {'ingredient_name': 'Лаваш ', 'measure': ' шт', 'quantity': ' 2 '},
             {'ingredient_name': 'Винный уксус ',
              'measure': ' ст.л',
              'quantity': ' 1 '},
             {'ingredient_name': 'Помидор ',
              'measure': ' шт',
              'quantity': ' 2 '}]}


def get_shop_list_by_dishes(dishes, person_count):

    """
    This function gives a dictionary of ingredients of dishes that you want
    to cook and also takes into account amount of person.
    """

    ingred_dict = {}
    for dish_name in dishes:
        if dish_name in cook_book.keys():
            for ingred in cook_book[dish_name]:
                ingredient = ingred['ingredient_name']
                quantity = int(ingred['quantity']) * person_count
                measure = ingred['measure']
                if ingredient not in ingred_dict.keys():
                    ingred_dict[ingredient] = {'quantity': quantity, 'measure': measure}
                else:
                    ingred_dict[ingredient]['quantity'] += quantity
        else:
            print(f'Блюдо {dish_name} не найдено')
    return ingred_dict


#pprint(get_shop_list_by_dishes(['Омлет'], 2))


#TASK 3
def merging_files():
    all_files_name = ['file' + str(num_file) + '.txt' for num_file in range(1, 4)]
    result_file = 'result.txt'
    file_len_dict = {}

    for file in all_files_name:
        with open(os.path.join(os.getcwd(), file)) as reading_file:
            keys_in_dict = len(reading_file.readlines())
            if keys_in_dict not in file_len_dict.keys():
                file_len_dict[keys_in_dict] = list(file.split())
            else:
                file_len_dict.get(keys_in_dict).append(file)
            sort_keys = sorted(file_len_dict.keys())
            sort_dict = {i: file_len_dict[i] for i in sort_keys}

    with open(os.path.join(os.getcwd(), result_file), 'w') as result:
        for strings, name_file in sort_dict.items():
            for i in range(len(name_file)):
                result.write(str(name_file[i]) + '\n')
                result.write(str(strings) + '\n')
                with open(os.path.join(os.getcwd(), name_file[i])) as reading_file:
                    for rw_string in reading_file:
                        result.write(rw_string + reading_file.readline())
                result.write('\n\n')
            return file_len_dict


print(merging_files())


