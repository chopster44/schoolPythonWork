class Performer:
    name: str = ""
    performanceType: str = ""

class Show:
    performers: list[Performer] = []
    time: list[int] = []
    date: list[int] = []