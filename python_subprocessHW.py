import numbers
from re import sub
import subprocess




def printHello():
    print("Hello World!")

def sum_digits_string(str1):
    sum_digit = 0
    for char in str1:
        if char.isdigit() or (char.strip().lstrip('-').isdigit()):
            digit = int(char)
            sum_digit += digit
    return sum_digit

if __name__ == "__main__":


    print(f"first run num=100 XX=90")
    subprocess.run(["python", "firstpy.py", "--num", "100", "--XX", "90"])
    print(f"------------------------------------------------------\n")
    print(f"second run num=-10 XX=-90")
    subprocess.run(["python", "firstpy.py", "--num", "-10", "--XX", "-90"])
    print(f"------------------------------------------------------\n")
    print(f"third run num=0")
    subprocess.run(["python", "firstpy.py", "--num", "0"])
    print(f"------------------------------------------------------\n")

#use output from other program
    process_output = subprocess.Popen(["python", "fristpy.py", "--num", "0"],
                                      stdout = subprocess.PIPE,
                                      stderr = subprocess.PIPE)
   
    out, err = process_output.communicate()
    print(out.decode('utf-8'))
    print(len(out.decode('utf-8')))

#############HW##########################

    sum1 = sum_digits_string(["python", "firstpy.py", "--num", "100", "--XX", "90"])
    print(sum1) 

    sum2 = sum_digits_string(["python", "firstpy.py", "--num", "-10", "--XX", "-90"])
    print(sum2) 

    sum3 = sum_digits_string(["python", "firstpy.py", "--num", "0"])
    print(sum3) 

    total_sum = sum([sum1, sum2, sum3])
    print(f"Total sum is: {sum1} + {sum2} + {sum3} = {total_sum}")
    printHello()