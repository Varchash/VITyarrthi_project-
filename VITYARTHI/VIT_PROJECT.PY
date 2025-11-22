import math
import time


def resistance_cal():
    print("resistance calculator ")    
    print(" 1 Series (R = R1 + R2)")  
    print(" 2  Parallel (1/R = 1/R1 + 1/R2)")
    type = input("what type of connection (1-2): ")
    r_1 = int(input("resistor 1 (Ohms):"))
    r_2 = int(input("resistor 2 (Ohms):"))
    if type == 1:
        r_total = r_1+r_2
        print("Total Series Resistance: " , r_total ," Ohms , in series")  
    elif type == 2:
        if r_1 == 0 or r_2 == 0:
            print("Resistance cannot be zero in parallel calculation.")
        else: 
            r_total = (r_1*r_2)/(r_1+r_2)  
            print("Total Parallel Resistance: " , r_total ," Ohms , in parallel")

def resistance_color_code(): 
    print("resistance from color code")
    color = {
        'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
        'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
    }
    
    multiples = {   
        'black': 1, 'brown': 10, 'red': 100, 'orange': 1000, 'yellow': 10000,
        'green': 100000, 'blue': 1000000, 'gold': 0.1, 'silver': 0.01
    }
    line_1 = input("Enter color of Band 1: ").lower().strip()
    line_2 = input("Enter color of Band 2: ").lower().strip()
    multiplier = input("Enter color of Multiplier Band: ").lower().strip()
    if line_1 in color and line_2 in color and multiplier in multiples:
        digit_1 = color[line_1]
        digit_2 = color[line_2]
        multiplier_value = multiples[multiplier]
        resistance_value = (digit_1*10 + digit_2)*multiplier_value
        print("The resistance value is:" , resistance_value , "Ohms")
    else:
        print("Invalid color input")

def gcd_cal():
    print("greatest common divisor")
    num1 = int(input("Enter first num:"))
    num2 = int(input("Enter second num:"))  
    gcd_result = math.gcd(num1, num2) 
    print("The GCD of", num1, "and", num2, "is:", gcd_result)

def roots_cal():
    print("square and cube roots")
    number = float(input("Enter the number: "))
    sqrt = math.sqrt(number)
    print("The square root of", number, "is:", sqrt)
    print("cube roots")
    number = float(input("Enter the number: "))
    cbrt = number ** (1/3)
    print("The cube root of", number, "is:", cbrt )

def ap_cal():
    print("arithmetic progression ")
    a = float(input("first term (a1): "))
    d = float(input("common  difference (d): "))
    n = int(input("number of terms (n): "))
    a_n = a + (n - 1) * d 
    sum_nth = n / 2 * (a +  a_n)
    print("The", n, "th term  (an) is:", a_n)
    print("The sum of the first", n, "terms (Sn) is:", sum_nth)

print("===== CALCULATION TOOLKIT =======")
time.sleep(.3)
print(" 1 Resistance Calculator")
print(" 2   Resistance from Color Code ")
print(" 3 GCD Calculator")
print(" 4 Root Calculotor")
print(" 5 Arithmetic Progression Calculator")
input_15 = input("Select an option (1-5): ")
if input_15 == '1':
    time.sleep(1)
    resistance_cal()
elif input_15 == '2':
    time.sleep(1)
    resistance_color_code()
elif input_15 == '3':
    time.sleep(1)
    gcd_cal()
elif input_15 == '4':
    time.sleep(1)
    roots_cal()
elif input_15 == '5':
    time.sleep(1)
    ap_cal()
else:
    print("wrong choice")

