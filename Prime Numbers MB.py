#Written by Matthew Bamford for Raytheon interview

def soloution1():
    lower = 1
    upper = 100
    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
       if num >= 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
               else:
                   print(num)

def soloution2():
    print("2")
    print("3")
    print("5")
    print("7")
    print("11")
    print("13")
    print("17")
    print("19")
    print("23")
    print("29")
    print("31")
    print("37")
    print("41")
    print("43")
    print("47")
    print("53")
    print("59")
    print("61")
    print("67")
    print("71")
    print("73")
    print("79")
    print("83")
    print("89")
    print("97")

def soloution3():
    valid = False
    lower = 0
    upper = 0
    while(valid == False):  
        lower = int(input("Enter the lower number (Must be positive) "))
        upper = int(input("Enter the higher number (Must also be potitive and more than lower) "))
        if(check(lower, upper) == True):
            valid = True
        else:
            print("Please enter 2 valid numbers")
    for num in range(lower, upper + 1):
       if num >= 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
               else:
                   print(num)

def check(lower, upper):
    if(lower > 0):
        if(lower < upper):
            return True
        else:
            return False
    else:
        return False
    

valid = False
while(valid == False):
    answer = int(input("Soloution 1, 2 or 3? "))
    if(answer == 1):
        valid = True
        soloution1()
    elif(answer == 2):
        valid = True
        soloution2()
    elif(answer == 3):
        valid = True
        soloution3()
    else:
        print("Please enter number 1, 2 or 3")
    
