home:bool=bool(0)
while 1:
    if not home:
        awnty: str = str(input("Are we nearly there yet? ")).lower()
        if awnty == "yes":
            home=bool(1)
    else:
        cwghn: str = str(input("Can we go home now? ")).lower()
        if cwghn == "yes":
            break
