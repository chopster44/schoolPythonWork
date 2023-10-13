import time
cat_times1: list[list[int]] = [[10, 32]]
cat_times2: list[list[int]] = [[14, 20]]
cat_times3: list[list[int]] = [[23, 44]]

for i in range(24):
    for j in range(60):
        print(f"It is {f'0{i}' if i < 10 else i}:{f'0{j}' if j < 10 else j}")
        if [i,j] in cat_times1:
            print("Cat 1 is eating")
        elif [i,j] in cat_times2:
            print("Cat 2 is eating")
        elif [i,j] in cat_times3:
            print("Cat 3 is eating")
        time.sleep(0.05)