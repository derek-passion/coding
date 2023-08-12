#Get information from user
balance = float(input("Enter how much you want to save: "))
interval = input("Enter how often you want to save: ")
if (balance<0):
    print("Looks like you already saved enough!")
    balance = 0
payment = float(input("Enter how much you will save each period:"))
if (payment <= 0):
    payment = float(input("Savings must be positive. Please entera positive value:"))
#Calculate number of payments that will be needed
num_remaining_payments = balance/payment
#Present information to user
print("You must make", num_remaining_payments, "more payments. This will take " + str(num_remaining_payments) + ' ' + str(interval + '.'))