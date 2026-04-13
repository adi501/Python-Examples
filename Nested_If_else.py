#Nested If Else
marks = int(input("Enter Your Marks? "))

if marks >= 50:
    if marks >= 90:
        print("Grade A+")
    elif marks >= 75:
        print("Grade A")
    else:
        print("Grade B")
else:
    print("Fail")