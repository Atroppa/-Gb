# # Первая задача
# print('Введите трехзначное число: ')#пользователь вводит число
# a = input()
# b = int(a[0])
# c = int(a[1])
# d = int(a[2])
# print(b+c+d)

# # Вторая задача
# print('Сколько всего сделали журавликов?')
# s = int(input())
# a = s//4#по 2 доли Пети и Сережи,  2 доли Кати
# b = a*2 #Сделала Катя
# d = a #сделал каждый из мальчиков
# print('Катя сделал '+ str(b) + ' Петя и Сережа сделали по ' + str(d))

# #Третья задача
# print('Введите номер билета:')
# a = input()
# b = int(a[0])
# c = int(a[1])
# d = int(a[2])
# e = int(a[3])
# f = int(a[4])
# g = int(a[5])
# if b+c+d == e+f+g:
#     print('У вас счастливый билет!')
# else:
#     print('Билет не счастливый')\
    
#Четвертая задача

print('Введите сторону n:')
n = int(input())
print ('Введите сторону m:')
m = int(input())
print ('Введите количество долек k:')
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
    
    


