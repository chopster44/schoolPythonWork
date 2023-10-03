table:int=int(input("What time table are you using? "))

for i in range(1,13):
    print(f"{table} x {i} = {table*i}")