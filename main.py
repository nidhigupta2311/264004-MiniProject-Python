

def find_Summation(value1, value2):
    return (value1 + value2)



def find_Difference(value1, value2):
    return (value1 - value2)



def find_Float_Div(value1, value2):
    return (value1 / value2)



def find_Integer_Div(value1, value2):
    return (value1 // value2)



def find_Modulous(value1, value2):
    return (value1 % value2)


def find_Product(value1, value2):
    return (value1 * value2)


def show_Last_Result():
    with open("Output.txt", "r") as file:
        lastResult = int(file.read())
        print(lastResult)









def Find_Power(base, exponent):
    return (base ** exponent)


def printResult(result):
    print("The result of the operation is:",result)
    return


def perform():
    print("\n\n")

    print("********************************************************")
    print("********************************************************")
    print("**********************CALCULATOR************************")
    print("********************************************************")
    print("********************************************************")

    print("---------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------")

    print('\n-- Enter "1" to add the values')
    print('-- Enter "2" to substract the values')
    print('-- Enter "3" to find float division')
    print('-- Enter "4" to find integer division')
    print('-- Enter "5" to find modulus')
    print('-- Enter "6" to find product of the values')
    print('-- Enter "7" to find power of value')
    print("\n")
    print('-- Enter "8" to see previous result')
    print('-- Enter "0" to exit')
    print("\n")


    operator =  input("-- Enter your choice ")
    print("\n")
    if operator == "1":
        print("Enter the values to find Addition (Please enter the values separated by Space)")
       

        value1, value2 = [int(x) for x in input().split()]
        result = find_Summation(value1, value2)
    elif operator == "2":
        print("Enter the values to find difference (Please enter the values separated by Space)")
        value1, value2 = [int(x) for x in input().split()]
        result = find_Difference(value1, value2)
    elif operator == '3':
        print("Enter the values to perform float division (Please enter the values separated by Space)")
        value1, value2 = [int(x) for x in input().split()]
        result = find_Float_Div(value1, value2)
    elif operator == '4':
        print("Enter the values to perform integer division (Please enter the values separated by Space)")
        value1, value2 = [int(x) for x in input().split()]
        result = find_Integer_Div(value1, value2)
    elif operator == "5":
        print(
            "Enter the value to find modulus (Please enter the values separated by Space)")
        value1, value2 = [int(x) for x in input().split()]
        result = find_Modulous(value1, value2)
    elif operator == "6":
        print("Enter the values to perform multiplication (Please enter the values separated by Space)")
        value1, value2 = [int(x) for x in input().split()]
        result = find_Product(value1, value2)
    elif operator == "7":
        print("Enter the base and exponent for the power operation (Please enter the values separated by Space)")
        base, exponent = [int(x) for x in input().split()]
        result = Find_Power(base, exponent)
    elif operator == "8":
        print("Previous Result is : ", end = " ")
        show_Last_Result()
    elif operator == "0":
        exit()
    if operator != "8":
        
        printResult(result)
        with open("Output.txt","w") as file:
            file.write(str(result))
    return



def main():
    while(True):
        perform()

if __name__ == '__main__':
    main()
    
