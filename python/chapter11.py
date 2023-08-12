a = [581347508917684,823460198536809173509870897069472089,1,7]

def findmiddle(a):
    if len(a) != 3:
        return 'Invalid Array'
    if ((a[0] >= a[1]) and (a[1] >= a[2])) or ((a[0] <= a[1]) and (a[1] <= a[2])):
        return a[1]
    elif ((a[0] >= a[2]) and (a[2] >= a[1])) or ((a[0] <=a[2]) and (a[2] <= a[1])):
        return a[2]
    else:
        return a[0]
print(findmiddle(a))