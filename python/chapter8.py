filename = input("Enter the name of the data file: ")
infile = open(filename, 'r')
a = 0
b = 0
#Read lines from File
datalist = []
for line in infile:
#get data from line
    date, h, l, r = (line.split(','))
    lowtemp = int(l)
    hightemp = int(h)
    rainfall = float(r)
    m, d, y = date.split('/')
    month = int(m)
    day = int(d)
    year = int(y)
#Put data into list
    datalist.append([day, month, year, lowtemp, hightemp, rainfall])
    b = b + 1
    if rainfall > 0:
        a = a + 1
infile.close()
########## Analyze Data ##########
#Get date of interest
month = int(input("For the date you care about, enter themonth: "))
day = int(input("For the date you care about, enter theday: "))
#Find historical data for date
gooddata = []
for singleday in datalist:
    if (singleday[0] == day) and (singleday[1] == month):
        gooddata.append([singleday[2], singleday[3],singleday[4], singleday[5]])
minsofar = 120
maxsofar = -100
numgooddates = 0
sumofmin=0
sumofmax=0
for singleday in gooddata:
    numgooddates += 1
    sumofmin += singleday[1]
    sumofmax += singleday[2]
    if singleday[1] < minsofar:
        print(minsofar, singleday[1])
        minsofar = singleday[1]
    if singleday[2] > maxsofar:
         maxsofar = singleday[2]
avglow = sumofmin / numgooddates
avghigh = sumofmax / numgooddates
print("There were",numgooddates,"days")
print("The lowest temperature on record was", minsofar)
print("The highest temperature on record was", maxsofar)
print("The average low has been", avglow)
print("The average high has been", avghigh)
print('The average chance of rain has been', a / b)