def city_country(city, country):
    dict_city = {city.title(): country.title()}
    return dict_city




#
# def make_album(singer_name,album_name, num=''):
#     if num == '':
#         dict_album = {'singer_name': singer_name, 'album_name': album_name}
#     else:
#         dict_album = {'singer_name': singer_name, 'album_name': album_name, 'album_num': num}
#     return dict_album
#
#
# while True:
#     singer_name = input("singer_name:")
#     if singer_name =='q':
#          break
#     album_name = input("album_name:")
#     if album_name == 'q':
#         break
#     print(make_album(singer_name,album_name,1))

# def greet_users(names):
#     for name in names:
#         msg = 'Hello, {}!'.format(name.title())
#         print(msg)
#
#
# usernames = ['nes','ty','mary']
# greet_users(usernames)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表completed_models中
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     #模拟根据设计制作3D打印模型的过程
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)
#     # 显示打印好的所有模型
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
#
#
# def make_print(designs):
#     completed_designs = []
#     for i in range(len(designs)):
#         completed_design = designs[i - 1]
#         completed_designs.append(completed_design)
#         print('Printing model:' + completed_design)
#         print('he following models have been printed:{}'.format(','.join(completed_designs)))
#
#
# make_print(unprinted_designs)
#
# list_name = ['alex', 'bobo', 'lucy', 'lily']
#
#
# def make_great(names):
#     great_names = []
#     for name in names:
#         great_name = 'The Great {}'.format(name.title())
#         great_names.append(great_name)
#     return great_names
#
#
# def show_magicians(names):
#     for i in range(len(names)):
#         print(names[i - 1])
#
#
# show_magicians(make_great(list_name))


#
# def print_models(unprinted_designs, completed_models):
#     """ 模拟打印每个设计，直到没有未打印的设计为止 打印每个设计后，都将其移到列表completed_models中 """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# print(unprinted_designs)
#
# show_completed_models(completed_models)
#
#
# print_models(unprinted_designs[:],completed_models)
# print(unprinted_designs)
# show_completed_models(completed_models)

def car_info(manufacturer,model,**info):
    profile = {'manufacturer': manufacturer, 'model': model}
    for key,value in info.items():
        profile[key] = value
    return profile

