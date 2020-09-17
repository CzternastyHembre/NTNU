start = int(input('start: '))
stopp = int(input('stopp: '))
hopp = int(input('hopp: '))
for i in range(start,stopp,hopp):
    for k in range(start,stopp,hopp):
            print('i, k:', i, k)

# i = int(input('Tall: '))
# x = i
# y = 2
# if not i % y == 0:
#     i = i - i%y
# while i >= 0:
#     print(i)
#     i-= y
# i = x
# while i >= 0:
#     if i % y == 0:
#         print(i)
#     i-= 1

# i = 0
# while True:
#     i += 1
#     if i == 100:
#         print(i)
#         break

# sum = 0
# antall = 0
# for i in range(100):
#     for j in range(100):
#         antall += 1
#         if i+j == 50:
#             # print(i,"+",j,"=",i+j)
#             sum += 1
# print('antall sum == 50 uten break:',sum)
# print('antall iterasjoner uten break:',antall)
#
# print("\n")
#
# sum = 0
# antall = 0
# for i in range(100):
#     for j in range(100):
#         antall += 1
#         if i+j == 50:
#             # print(i,"+",j,"=",i+j)
#             sum += 1
#             break
# print('antall sum == 50 med break:',sum)
# print('antall iterasjoner med break:',antall)
#
# print("\n")
#
# sans = 1-(99/100)**10
# print(sans)




input('Enter to exit ')
