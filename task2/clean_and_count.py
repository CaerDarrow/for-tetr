import csv


def read_csv():
    data = []
    with open('durty_list.csv', 'r') as f_input:
        for row in csv.reader(f_input):
            data.extend(row)
    return data


def clean_and_count(durty_list):
    clean_list = durty_list[:durty_list.index('Acalolepta')] 
    ALFA = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    first_words_list = []
    counted_list = []
    for i in range(len(clean_list)):
        first_words_list.append(clean_list[i][0])
    for k in range(len(ALFA)):
        counter = 0 
        for j in range(len(first_words_list)):
            if first_words_list[j] == ALFA[k]:
                counter += 1
        result = ALFA[k] + ':' + str(counter)
        counted_list.append(result)
    print(*counted_list, sep = '\n')
    return counted_list

clean_and_count(read_csv())