P=float(input("Enter Principal Amt in Rs: "))
R=float(input("Enter the rate of interest in % :"))
d=int(input('''Enter the duration:
              1.In day(s).
              2.In year(s)'''))
if(d==1):
    t=d/365
elif(d==2):
    t=d


else:
    raise ValueError
t=float(input("Enter the duration"))
    
n=float(input("Enter compounding frequency:"))
A=P*((1+(R/(100*n)))**(n*t)) 
print(f"Total Amount :Rs.{A}/- ")
print(f"The interest incurred : Rs.{A-P}/- ")
print(f"Thank You !")