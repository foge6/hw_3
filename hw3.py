# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

# length = int(input("write length massive "))
# massive = []
# count=0
# for i in range(0,length):
#     number = int(input('write number of massive '))
#     massive.append(number)
# find = int(input("write element, which should find "))
# for i in range(0,length):
#     if massive[i]==find:
#         count+=1
# print(count)
    

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:* 
# 5
#     1 2 3 4 5
#     6
#     -> 5

# length = int(input("write length massive "))
# massive = []
# for i in range(0,length):
#     number = int(input('write number of massive '))
#     massive.append(number)

# x = int(input('write number '))

# difference = x - massive[0]
# numb_of_diff=0
# if difference < 0:
#     difference*= -1
# for i in range(1,len(massive)):
#     if x > massive[i]:
#         if x-massive[i] < difference:
#             difference = x-massive[i]
#             numb_of_diff = i
#     elif x < massive[i]:
#         if massive[i]-x < difference:
#             difference = massive[i] - x
#             numb_of_diff = i
#     else:
#         difference=0
#         numb_of_diff=i
#         break
# print(massive[numb_of_diff])

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12

# word = input("write word ")
# sum = 0
# if word[0] in ["a","e","i","o","u","l","n","s","t","r","d","g","b","c","m","p","f","h","v","w","y","k","j","x","q","z"]:
#     for i in range(len(word)):
#         if word[i] in ["a","e","i","o","u","l","n","s","t","r"] :
#             sum+=1
#         elif word[i] in ["d","g"] :
#             sum+=2
#         elif word[i] in ["b","c","m","p"]:
#             sum+=3
#         elif word[i] in ["f","h","v","w","y"]:
#             sum+=4
#         elif word[i] in ["k"]:
#             sum+=5
#         elif word[i]in["j","x"]:
#             sum+=8
#         elif word[i]in["q","z"]:
#             sum+=10
# else:
#     for i in range(len(word)):
#         if word[i] in ["а","в","е","и","н","о","р","с","т"] :
#             sum+=1
#         elif word[i] in ["д","к","л","м","п","у"] :
#             sum+=2
#         elif word[i] in ["б","г","ё","ь","я"]:
#             sum+=3
#         elif word[i] in ["й","ы"]:
#             sum+=4
#         elif word[i] in ["ж","з","х","ц","ч"]:
#             sum+=5
#         elif word[i]in["ш","э","ю"]:
#             sum+=8
#         elif word[i]in["ф","щ","ъ"]:
#             sum+=10
    
# print(f' итоговый сумм {sum} ')

    