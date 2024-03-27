import csv
def promo(n):
    return n[1][:2:]+n[2][:2:]+n[1][-2:]+(n[2][3:5][::-1])##получаем нужный промокод


f=open('products (1).csv') ##открываем файл
a=[]##создаем массив, в котором будут находится элементы из таблицы
for i in f:
    a.append(i.split(';'))##проходимся по таблице, добавляя в массив каждую строчку
a[0][4]=a[0][4][:-1]
a[0].append('promocode')##добавляем еще один стоолбец в шапку таблицы
for i in range(1, len(a)):
    a[i][4] = a[i][4][:-1]  ##добавляем полученное значение
    a[i].append(promo(a[i]))

f1=open('product_promo.csv', 'w')##новый файл
writer=csv.writer(f1)
w=writer.writerows(a)##записываем полученные результаты в новый файд
f.close()
f1.close()