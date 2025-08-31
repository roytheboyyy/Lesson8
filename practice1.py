#basic
num1 = int(input("enter number 1"))
num2 = int(input("enter number 2"))
num3 = int(input("enter number 3"))
print(num3 , num2 , num1)
#advanced
num = int(input("enter number 3 digit to be swapped"))
num = (num % 10) * 100 + (num // 10 % 10) * 10 + (num // 100)
print("After swap:", num)