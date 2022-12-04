# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#num=int(input("Введите количество чисел последовательности Фибоначчи: "))
num=5
num_fib=0
fib=[0, 1]

for i in range (2, num+1):
    num_fib=fib[i-1]+fib[i-2]
    fib.append(num_fib)

fib_min=[]
for i in range(2, num+1):    
    num_fib=fib[i-1]+fib[i-2]
    if i%2==0:
        num_fib*=-1   
    fib_min.append(num_fib)

for i in range (0, len(fib_min)):
    fib.insert(0, fib_min[i])

print(fib)