print("welvome to my calculator")
import math 

print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : div")
print("sqrt")
print("sin")
print("cos")
print("ton")
print("cot")
print("factorial")

print("please enter your choice: ")
op = input()

if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    
    if op == "+":
        result = a + b 
    
    elif  op == "-": 
        result = a - b 
        
    elif  op == "*":
        result = a * b
        
    elif op == "/":
        if b == 0:
            result ="cannot divide by zero"
        else:
            result = a / b       
    
else:
    a = float(input("please enter first number: ")) 
        
    if op == "sqer":
        result = (math.sqrt(a))
        
    elif op == "sin":
        result = (math.sin(a))
        
    elif op == "cos":
        result = (math.cos(a))
            
    elif op == "ton": 
        result = (math.tan(a))
            
    elif op == "cot":
        result = (math.cot(a))
            
    elif op == "factorial":
        result = (math.factorial(a))
        
    print(result)
        