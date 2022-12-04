# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst=list(map(int,input().split()))
ind_start=0
ind_end=len(lst)-1
lst_mult=[]
mult=0
while ind_start<=ind_end:    
    mult= lst[ind_start]*lst[ind_end]
    lst_mult.append(mult) 
    ind_start+=1     
    ind_end-=1
print(lst_mult)