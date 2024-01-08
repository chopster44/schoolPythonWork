import random
resolutions: list[str] = ["Excercise more", "Read more", "Get Organised", "Eat Healthier"]
print("Your new years resolution is to", resolutions[random.randint(0, len(resolutions))] )
