def main():
    choice = 1
    while choice != '0':
        num1 = int(input('Enter the Num1 : '))
        num2 = int(input('Enter the Num2 : '))

        operation = input('''
Choose your Operation:
    + for Addition
    - for Substraction
    * for Multiplication
    / for Division
    0 for Exit                  
''')    
        if operation == '+':
            print(f'Result : {Add(num1, num2)}')
        elif  operation == '-':
            print(f'Result : {Sub(num1, num2)}')
        elif operation == '*':
            print(f'Result : {Mul(num1, num2)}')
        elif operation == '/':
            print(f'Result : {Div(num1, num2)}')
        else:
            print('Choose a Valid Operation Type!!')
        print('')

        choice = input('To Exit Press 0 \nElse, Enter : ')
        print()

def Add(a, b):
    return a+b

def Sub(a, b):
    return a-b

def Mul(a, b):
    return a*b

def Div(a, b):
    return format(a/b,'.2f')

if __name__ == '__main__':
    main()