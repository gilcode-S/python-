import random as ran

# print("\u25CF \u250C \u2510 \u2500 \u2502 \u2518 \u2514")
# ● ┌ ┐ ─ │ ┘ └

"┌ ─ ─ ─ ─ ┐"
"│         │"
"│         │"
"│         │"
"└ ─ ─ ─ ─ ┘"


# dice dictionary

dice_art = {
    1: ("┌ ─ ─ ─ ─ ┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└ ─ ─ ─ ─ ┘"),
    2: ("┌ ─ ─ ─ ─ ┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└ ─ ─ ─ ─ ┘"),
    3: ("┌ ─ ─ ─ ─ ┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└ ─ ─ ─ ─ ┘"),
    4: ("┌ ─ ─ ─ ─ ┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└ ─ ─ ─ ─ ┘"),
    5: ("┌ ─ ─ ─ ─ ┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└ ─ ─ ─ ─ ┘"),
    4: ("┌ ─ ─ ─ ─ ┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└ ─ ─ ─ ─ ┘"),

}


dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(ran.randint(1, 6))

#display art

for die in range(num_of_dice):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total += die

print(f"total: {total}")
