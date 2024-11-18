# function for choices
def menu():
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice = int(input("Enter your choice: "))
    
    if(choice>0 and choice<6):
        if(choice==5):
            print("Thank you!!")
            exit()

        a = eval(input("Enter first number: "))
        b = eval(input("Enter second number: "))
        match(choice):
            case 1:
                print("Result is : ",addition(a,b))
            case 2:
                print("Result is : ",subtraction(a,b))
            case 3:
                print("Result is : ",multiply(a,b))
            case 4:
                res = divide(a,b)
                if res:
                    if res.is_integer():
                        # print interger result
                        print("Result is : ",int(res))
                    else:
                        # round off float result to two places
                        print("Result is : ",round(res,2))
            case _:
                print("Invalid choice!!")
    else:
        print("Invalid choice!!")
        
        

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    # handling exception if use enters second number as zero
    except ZeroDivisionError:
        print("Second number must be non-zero")
        return


if __name__=="__main__":
    while(True):
        menu()