import csv
f=open('products (1).csv') ##открываем файл
a=[]##создаем массив, в котором будут находится элементы из таблицы
for i in f:
    a.append(i.split(';'))##проходимся по таблице, добавляя в массив кфждую строчку
for i in range(1, len(a)-1):
    for j in range(len(a)-2, i-1, -1):
        if a[j][0]>a[j+1][0]:
            a[j],a[j+1]=a[j+1],a[j]##сортировка пузырьком всех строчек таблицы в алфавитном порядке по категории
price=int(a[1][3][:-2])##цена первого товара отсортированного списка
name=''##
categ=a[1][0]##
for i in range(1, len(a)):
    for j in range(i+1, len(a)):
        if a[i][0]==a[j][0]:##если они одной категории
            if price<int(a[j][3][:-2]):##если цена нового товара больше, то выполняем действия:
                price=int(a[j][3][:-2])## обновляем цену товара
                name=a[j][1]##переписываем название товара
    break##заканчиваем перебор, поскольку нужна максимальная цена только первой категории
print(f'В категории: {categ} самый дорогой товар: {name} его цена составляет {price}')
f.close()
