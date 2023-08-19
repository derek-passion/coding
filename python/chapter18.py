import pickle
a = 1
b = 0
while b != 1:
    b = int(input('Enter a number: '))
    a = a + b
print(a)
with open('game.dat','wb') as f:
    pickle.dump(a, f)
with open('game.dat','rb') as f:
    a = pickle.load(f)