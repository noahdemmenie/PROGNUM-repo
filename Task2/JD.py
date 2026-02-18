# Input variables for the Gregorian date

M = int(input("Enter month:"))
D = float(input("Enter day:"))
Y = int(input("Enter year:"))

# Compute JD for the Gregorian date

JD = 367*Y -7*int((Y+int((M+9)/12))/4) - 3*int((int((Y+int((M-9)/7))/100) + 1)/4) + int((275*M)/9) + D + 1721029-0.5
print(f"JD = {JD}")