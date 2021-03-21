from datetime import datetime


def get_time(func): #небольшой декоратор для подсчета таймстэпмов
    def wrapper(array):
        print('Start:', datetime.now().microsecond)
        result = func(array)
        print('Finish:', datetime.now().microsecond)
        return print(result)

    return wrapper


@get_time
def task(array): 
    for i in range(len(array)):
        if array[i] == '0':
            return i + 1

task("11111110000111")

#IN: 11111110000111
#Start: 951298
#Finish: 952316 
#OUT: 8

#IN: 1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110000111
#Start: 189436
#Finish: 190409
#OUT: 97

'''В данном случае оценку сложности алгоритма по времени можно обозначить как 
"линейная зависимость", ввиду того, что количество операций будет возрастать с увеличением массива входных данных'''