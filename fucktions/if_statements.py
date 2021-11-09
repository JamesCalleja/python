is_male = False
is_tall = True

if is_male:
    print("yep")
else:
    print("nope")

if is_male and is_tall: #and or
    print("both are true")
elif is_tall and not(is_male):
    print("you are a female")
else:
    print("this is the else")

def max_mum (num1, num2,num3):
    if num1 >= num2 and num1 >= mun3: # == != <=
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_mum(24,645453,325))

