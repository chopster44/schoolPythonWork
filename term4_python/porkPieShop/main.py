price = {
    "eggs": 0.45,
    "pies": 0.85,
    "quiche": 1.49
} 

print("--- Welcome to Pete Porker's Pork Pie Emporium ---")
print("Scotch eggs are 45p, pork pies are 85p and quiche tarts are £1.49.")

while True:
    eggs: int = int(input("How many Scotch eggs do you want to buy: "))
    if eggs < 1 or eggs > 20:
        print("You can only buy between 1 and 20 scotch eggs.")
        continue
    pies: int = int(input("How many pork pies do you want to buy: "))
    if pies < 1 or pies > 20:
        print("You can only buy between 1 and 20 pork pies.")
        continue
    quiche: int = int(input("How many quiche tarts do you want to buy: "))
    if quiche < 1 or quiche > 20:
        print("You can only buy between 1 and 20 quiche tarts.")
        continue
    print(f"You selected {eggs} scotch eggs, {pies} pork pies and {quiche} quiche tarts.")

    confirm: str = str(input("Are you happy with your choices [y/N]: ")).lower()
    if confirm == "y":
        break
    continue

print("Here is your recipt:")
print(f"{eggs} scotch eggs = {eggs * price['eggs']}")
print(f"{pies} pork pies = {pies * price['pies']}")
print(f"{quiche} quiche tarts = {quiche * price['quiche']}")
print(f"Total: {eggs * price['eggs'] + pies * price['pies'] + quiche * price['quiche']}")

