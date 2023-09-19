movie: str = str(input("What movie would you like to see? "))
ageRating: int = int(input("What is the films age rating(as a number)? "))
age: int = int(input("What is your age(as an int)?"))

if ageRating > age:
    print(f"You need an adult too see {movie}")
else:
    print(f"You can go and see {movie} alone")
