#simple Calculator

a = eval(input('Enter first value: '))
operator = input('Operator(+,-,*,/): ')
b = eval(input('Enter second value: '))
try:
    if operator == '+':
        res = a + b 
        print('Addition: ',res)
    
    elif operator == '-':
        res = a-b
        print('Subtraction: ', res)

    elif operator == '*':
        res = a*b
        print('Multiplication: ',round(res,3))

    elif operator == '/':
        res = a/b
        print('Division: ',round(res,3))
        
    else:
        print('invalid')
        
finally:
    print('Finished!')
