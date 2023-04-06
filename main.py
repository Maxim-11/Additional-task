import math
import itertools
map = []
f = input("Введите первую координату:\n").split()
map.append(f)
f = input("Введите вторую координату:\n").split()
map.append(f)
print(f'Координаты {map}')
toch = []
i = 0
n = 0
def main():
    enter = int(input("Выберите функцию: \n"
            "1 - Добавление\n"
            "2 - Просмотр добавленных точек\n"
            "3 - Удаление точек\n"
            "4 - Изменение точек\n"
            "5 - Удаление точек в области\n"
            "6 - Выход\n"))
    if (enter > 0 and enter <= 6):
            match enter:
                case 1:
                        try:
                            f = (input("Введите точки:\n").split()) 
                        except ValueError:
                               print("Ошибка!")
                        toch.append(f)
                        print(f'Точки {toch}')
                        main()
                case 2:
                        print(f'Точки {toch}')
                        main()
                case 3:
                        a = input("Введите координату:\n").split()
                        while i < len(toch):
                            if (a in toch):
                                toch.remove(a)
                                main()
                            else:
                                i+1
                case 4:
                        a = input("Введите координату:\n").split()
                        while n < len(toch):
                            if (a in toch):
                                h = toch.index(a)
                                toch.remove(a)
                                j = (input("Введите точки:\n").split()) 
                                toch.insert(h,j)
                                main()
                            else:
                                n+1
                        main()
                case 5:
                        r = 0
                        while r < len(toch):
                                if(int(toch[r][0]) >= int(map[0][0])) and (int(toch[r][0]) <= int(map[1][0])) and (int(toch[r][1]) >= int(map[0][1])) and (int(toch[r][1]) <= int(map[1][1])):
                                        toch.pop(r)
                                else:
                                        r+=1

                        main()
                case 6:
                        exit()
main()
