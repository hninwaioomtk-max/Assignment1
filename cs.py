a= int (input("Give me your first number:"))
b= int (input("Give me your second number:"))

print("Anaswer of Addition:",a + b)
print("Anaswer of Multiplication:",a * b)

if (a > b) :
    print("Anaswer of Subtraction:",a - b)
    print("Anaswer of Division:",a / b)

elif (a < b):
    print("Anaswer of Subtraction:",b - a)
    print("Anaswer of Division:",b / a)
    
    all_a= id(a)
    all_b= id(b)
    print("Allocation of first number:",all_a)
    print("Allocation of second number:",all_b)
    
    hex_a=hex(a)
    hex_b=hex(b)
    print("Hex value of first number:",hex_a)
    print("Hex value of second number:",hex_b)