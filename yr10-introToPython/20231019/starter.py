width: int = 16
length: int = 16
height: int = 10

radius: int = 6371000000

print(f"The Earth's radius is {radius}mm")

planetEarth: int = int(4*3.14*(radius^3)/3)

print(f"The Earth's volume is {planetEarth} mm^3")

legoBrick: int = width * length * height

print(f"The volume of a lego brick is {legoBrick} mm^3")

numberOfBricks: int = int(planetEarth / legoBrick)

print(f"You need {numberOfBricks} to build planet earth")
