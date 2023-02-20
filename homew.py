#Первая задача
list = [1, 0, 0 ,1, 0, 1, 1, 1]
a = list.count(1)
b = len(list)
c = a - b

if c < a:
    print ('Нужно перевернуть ' + str(c) + ' разa')
print ('Нужно перевернуть ' + str(a) + ' разa')
    
    
    

S = int(input('Введите сумму: '))
P = int(input('Введите произведение: '))

a = 1
while a*(S-a) != P:
    a +=1
print(a, S-a)



print('Введите сумму')
n = int(input())
two = 2
power = 1
while two <= n:
    two *= 2
    power += 1
print(power - 1, two// 2)


    

    

    





    


    
    
    
    
    


