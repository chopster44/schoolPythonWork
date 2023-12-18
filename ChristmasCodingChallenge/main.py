def get_advent_calendar_content() -> list[str]:
    file = open("adventCalendar.txt", "r", encoding="UTF-8")
    return file.read().split("\n")

def main():
    day: int = int(input("What day is it? "))
    adventCalendarContent: list[str] = get_advent_calendar_content()
    print(adventCalendarContent[day])

main()
