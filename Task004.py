# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num=int(input("Введите число: "))
num_2=0
lst_double=[]
while num>=1:
    lst_double.insert(0, num%2)
    num=int(num/2)
    

print("Введенное число в двоичное системе ", lst_double)
