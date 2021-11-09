try:
    #value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as error:
    print("zero division error")
except:
    print("Something went wrong")
