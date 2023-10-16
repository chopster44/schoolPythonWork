ratings: list[int] = [0]

while True:
    rating: str = input("Input your rating 1-5 (Q to exit)? ")
    if rating == "Q":
        break
    else:
        ratings.append(int(rating))

average: int = 0

for i in ratings:
    average += i

average = int( average / len(ratings))

print(f"The average score was: {average} ")
