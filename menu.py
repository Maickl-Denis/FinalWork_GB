import os
# def menu() -> int:
#     while True:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         numbers = num()
#         if numbers == 0:
#             break
#         elif numbers == 1:
#             os.system('cls' if os.name == 'nt' else 'clear')
#             akt = action(numbers)
#             if akt == 0:
#                 continue
#             elif 0 < akt < 9:
#                 Rational.original(akt)
#             else:
#                 print("Такого пункта меню нет")
#         elif numbers == 2:
#             os.system('cls' if os.name == 'nt' else 'clear')
#             akt = action(numbers)
#             if akt == 0:
#                 continue
#             elif 0 < akt < 8:
#                 komplex.original(akt)
#             else:
#                 print("Такого пункта меню нет")
#         else:
#             print("Такого пункта меню нет")
#
#
# def num():
#     try:
#         che = int(input("Выберите пункт меню: \n"
#                         "1. Список животных\n"
#                         "2. Комплексные\n"
#                         "0. Выход\n"))