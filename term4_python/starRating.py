starRating = int(input("Enter a rating 0-5 "))
while not starRating in range(0,6):
    print("Invalid int, try again:")
    starRating = int(input("Enter a rating 0-5 "))
print("Thankyou")