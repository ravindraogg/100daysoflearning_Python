#Question 1. {Age=30 Gender=M}

Age = int(input("Enter age: "))
Gender = input("Enter Gender M/F: ")

if (20 <= Age <= 60) and (Gender == "M"):
    print("Fee is 100")
elif (20 <= Age <= 60) and (Gender == "F"):
    print("Fee is 200")
else:
    print("Not Applicable")
