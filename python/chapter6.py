with open('askj.txt', 'r') as f:
     contents = f.read()
arr = contents.split('\n')
a = 0
for e in arr:
    if e != '':
        a = a + int(e)
print(a / len(arr))



# fname = input('Enter file name: ')
# file = open(fname + '.txt', 'w')
# for e in range(1,11):
#     file.write(str(e) + '\n')
# file.close()

