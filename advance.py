import math 
a=5
b=10
c =7

a += 3 
b *= 2
c %= 4
print (a ,b ,c)

#variables
square = a ** 2 + b ** 2 + c ** 2

#variable
square_root = math.sqrt(square)
rounded = round (square_root, 2)

print(rounded)

#integers
x = 10
y = 0
z = 14

is_even = x % 2 == 0
is_positive = y > 0
is_range = z >= 10 and z <= 50
final_condition = is_even and is_positive and is_range
print(final_condition)

base_score = float(input("Type in the score:"))
bouns_points = (+5)
late_penalty = (-10)
if base_score >= 90 and base_score < 100:
    print("grade A")
elif base_score >= 80 and base_score < 90:
    print("grade B")
elif base_score >= 70 and base_score < 80:
    print("grade C")
elif base_score >= 60 and base_score < 70:
    print("grade D")
else:
    print("fail")

# advanced calculater
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /, % ,**):")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2

print(result)