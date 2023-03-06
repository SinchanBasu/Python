P=int(input("Enter a principal amount : "))
T=int(input("Enter the Time Period : "))
R=float(input("Enter the Interest Rate : "))
A=P*(pow((1+R/100),T))
Compound_Interest=A-P
print("The amount after compound interest is : ",Compound_Interest)