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
