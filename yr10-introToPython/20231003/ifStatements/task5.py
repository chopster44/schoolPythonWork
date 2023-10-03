import sympy
number:int= int(input("What is your number? "))
print(f"Your number {'is' if sympy.isprime(number) else 'is not'} prime")