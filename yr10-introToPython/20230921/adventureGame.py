import os
from random import randint

screen_height = os.get_terminal_size()[0]
screen_width = os.get_terminal_size()[1]

player_pos: list[int] = [1, 1]
player: str = "@"


def room_generator(size: int) -> list[list[str]]:
    size = size * 2 + 1
    generated_room: list[list[str]] = [[]]
    for i in range(0, size):
        if i < (size - 1):
            generated_room.append([])
        for j in range(0, size):
            generated_room[i].append(" ")
    for i in range(0, size):
        for j in range(0, size):
            if i == 0 or i == (size - 1):
                generated_room[i][j] = "-"
            elif j == 0 or j == (size - 1):
                generated_room[i][j] = "|"
            else:
                generated_room[i][j] = " "
    return generated_room


def draw_player(pos: list[int], icon: str):
    pass


def print_game(game: list[list[str]]):
    os.system("clear")
    print("\n" * (screen_height - len(game)))
    line: str = "\n"
    for i in game:
        line = ""
        for j in game[game.index(i)]:
            line += j
        print(line)

    print("\n\nControls:")
    print("Up: w     Down: s     Left: a     Right: d     Attack: (dir)+(spc)\n")


room: list[list[str]] = room_generator(4)

print_game(room)

input()