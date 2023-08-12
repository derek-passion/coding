#for i in range (10,1,-3):
    #print(i)
# a = int(input('Enter a number:'))
# for e in range(a):
#     print(e)
# for e in range(2, 7, 3):
#     print(e)
import random
n = int(input('Enter a number: '))
a = random.randint(1,10)
while n != a:
    n = int(input('Try a different number: '))
if n == a:
    print('Success!')