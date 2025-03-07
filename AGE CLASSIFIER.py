print("Hello! how are you? Can I know your name?")

name = input("Enter your name:")
print("Hello,"+name,"Are you a child, teen, adult, or senior?")


while True:
    try:
        age_classifier = float(input("How old are you?:"))
        if age_classifier<=0:
            print("You're not born yet")
        elif age_classifier<12:
            print("You're a child")
        elif age_classifier<=19:
            print("You're a teen")
        elif age_classifier<=64:
            print("You're an adult")
        elif age_classifier>=65:
            print("You're a senior")
        else:
            print("put your age in numbers, please:")
            break
    except: 
        print("put your age in numbers, please:")
