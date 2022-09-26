#What is the score?
score = int(input("What is your test score?"))
#Determine Grade
if score >+ 90:
    print("your grade is an A")
else:
    if score >= 80:
        print("your grade is a B")
    else:
        if score >= 70:
            print("your grade is a C")
        else:
            if score >= 60:
                print("Your Grade is a D")
            else:
                print("Your grade is an F.")
