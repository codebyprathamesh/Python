## Compound Interest Calculator (Python)
This is a simple compound interest calculator written in Python. It allows the user to enter principal amount, rate of interest, duration (in days or years), and compounding frequency, and then shows the final amount and interest incurred.

## Features
Accepts principal amount in rupees.

Accepts rate of interest in percentage.

Lets the user choose duration:

in day(s) (converted to years by dividing by 365)

in year(s) directly

Accepts compounding frequency (n) so you can use yearly, half‑yearly, quarterly, monthly, etc.

Calculates:

total amount A using the compound interest formula

interest incurred A - P

Prints a friendly summary to the console.

Formula Used
The program uses the standard compound interest formula:

A=P*((1+(R/(100*n)))^(n*t))
 
Where:
P = principal amount (in rupees)
R = annual rate of interest (in percent)
n = number of times interest is compounded per year
t = time in years
A = final amount after time t including interest
The interest incurred is:


Interest=A−P
How the Program Works
Asks the user for:

principal amount P

rate of interest R

Asks the user how they want to enter duration:

1 → duration in days (internally converted to years as t = days / 365)

2 → duration in years (used directly as t)

Takes the compounding frequency n (for example):

1 → yearly

2 → half‑yearly

4 → quarterly

12 → monthly

Applies the compound interest formula to compute A.

Prints:

total amount A

interest incurred A - P

a closing Thank You! message.

## Example Usage
Run the script:

bash
python compound_interest.py
Example interaction:

text
Enter Principal Amt in Rs: 40000
Enter the rate of interest in % : 9
Enter the duration:
              1.In day(s).
              2.In year(s) 2
Enter the duration 1
Enter compounding frequency: 4
Total Amount :Rs.43723.33/-
The interest incurred : Rs.3723.33/-
Thank You !
(The exact numbers will depend on your duration and frequency values.)

## Requirements
Python 3.x

No external libraries are required. The script only uses basic Python functions like input(), float(), int(), and print().

Possible Improvements
Add input validation and clearer error messages instead of raising a raw ValueError.

Wrap the logic in functions for easier testing and reuse.

Build a simple web interface (Flask or HTML + PyScript) so users can access the calculator from a browser.