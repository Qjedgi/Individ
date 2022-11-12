# Задание 8 В файле записана последовательность натуральных чисел.
# Гарантируется, что все числа различны. Из этой последовательности нужно
# выбрать четыре числа, чтобы их сумма делилась на 9 и была наименьшей.
# Какую наименьшую сумму можно при этом получить?
f=list(open("8a.txt",'r'))
p=[]
for line in f[1::1]:
    p.append(line)
p = [int(x) for x in p]
print('Изначальный список',p)
summa=[]
step=1
#заполнение суммы
while step!=5:
    #от 0 до p-4 с шагом step
    for i in range(len(p)-4):
        summa.append(p[i]+p[i+step]+p[i+step]+p[i+step])
    step += 1
print('Суммы изначального списка',summa)
summa=list(set(summa))
summa.sort()
u=[]
for j in summa:
    if (j%9==0):
        u.append(j)
print('Делящиеся на 9', u)
