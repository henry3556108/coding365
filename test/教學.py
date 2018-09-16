import math
def Difference(num1,num2):
    difference = num1 - num2
    return difference

def Sum(num1,num2):
    sum = num1 + num2
    return sum

def Quotient(num1,num2):
    quotient = num1 / num2
    return quotient

def Product(num1,num2):
    product = num1 * num2
    return product

def main():
    num1 = float(input())
    num2 = float(input())
    difference = Difference(num1,num2)
    sm = Sum(num1,num2)
    quotient = Quotient(num1,num2)
    product = Product(num1,num2)
    print('Difference:%.2f' %(math.floor(difference*100)/100))
    print('Sum:%.2f' %(math.floor(sm*100)/100))
    print('Quotient:%.2f' %(math.floor(quotient*100)/100))
    print('Product:%.2f' %(math.floor(product)/100))

main()