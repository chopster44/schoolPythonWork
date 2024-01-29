import rich

menuItem = 0

def get_music():
    file = open("music.txt", "r")
    content = file.read().split("\n")
    return content

def show_menu(item):
    menu = ["Show Songs","Random Song", "Add song", "Remove song", "Count songs", "Shuffle playlist", "Create new playlist", "Quit"]
    for i in range(0, len(menu)):
        if i == item:
            rich.print(f"[red bold]{menu[i]}[/red bold]")
            continue
        rich.print(menu[i])

def waitForInput():
    inputStr = input()
