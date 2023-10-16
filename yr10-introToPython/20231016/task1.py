prices: dict[str, int] = {
    "adult":100, 
    "child":50,
    "senior":75}

subtotal: int = 0

def print_options():
    print("Purchase tickets:")
    print(f"1) Adult: £{prices['adult']}")
    print(f"2) Child: £{prices['child']}")
    print(f"3) Senior: £{prices['senior']}")
    print("Q) Finish")

while True:
    print_options()
    inputChoice: str = str(input("?"))
    if inputChoice == "1":
        subtotal += prices["adult"]
    elif inputChoice == "2":
        subtotal += prices["child"]
    elif inputChoice == "3":
        subtotal += prices["senior"]
    elif inputChoice == "Q":
        break

print(f"Subtotal: {subtotal}")
