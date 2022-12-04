# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
lst=list(map(float, input().split()))

lst_fract=[]
fract=0
for i in range (len(lst)):
    fract=lst[i]%1
    lst_fract.append(fract)
res=round(max(lst_fract)-min(lst_fract),2)
print("Разница между максимальным и минимальным значением дробной части равна:  ", res)