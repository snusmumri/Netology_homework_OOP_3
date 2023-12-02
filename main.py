import os.path
import os

ls = [i for i in os.listdir() if i.endswith('.txt')]
ls.sort()

list_rows = []
spisok_slovar = {}
for i in ls:
    file_putch = os.path.join(os.getcwd(), i)
    f = open(file_putch, encoding='utf-8')
    dat = f.read()
    list_rows.append(dat)

    with open(file_putch, encoding='utf-8') as f:
        lines = f.readlines()
        slovar = {len(lines): i}
        spisok_slovar.update(slovar)

sort_spisok_slovar = dict(sorted(spisok_slovar.items()))
list_rows.sort(key = len)

my_file = open('rezult.txt', 'w')
my_file.close()
my_file = open('rezult.txt', 'a')
for ex, i in enumerate(sort_spisok_slovar):
    my_file.write(f'{sort_spisok_slovar[i]}\n')
    my_file.write(f'{i}\n')
    my_file.write(f'{list_rows[ex]}\n')

my_file.close()
my_file = open('rezult.txt')
y = my_file.read()

print(y)
