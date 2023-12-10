import os
import sys

type = int(input("""It's a:
1. Actionbar
2. Title
3. Tellraw
"""))

deleteText = input("(y/n) it will delete the text? ")

tick = int(input("\nTick speed per letter: "))
name = input("Dialogue Name: ")
text = input("Dialogue Text: ")

if deleteText == "y":
    tickWait = int(input("\nTick for the letter deletion: "))
    tickDelete = int(input("\nTick speed per letter delete: "))

beforeText = ""
fileAllText = f"""## Made By Flocos! <3
# Text: "{text}"
# Tick Speed: {tick}
\n"""
counter = 0
counterDelete = 1

if type == 1:
    file = open(os.path.join(sys.path[0],f"action_{name}.mcfunction"), "w")
    fileAllText += f"execute if score action.{name} dialogue matches 0.. run scoreboard players set action.isActive dialogue 1\n"
    fileAllText += f"execute if score action.{name} dialogue matches 0.. run scoreboard players add action.{name} dialogue 1\n"

    for x in text:
        if counter + 1 != len(text) or deleteText == "n":
            fileAllText += f'execute if score action.{name} dialogue matches {counter * tick} run title @a actionbar "{beforeText + x}"\n'
        elif deleteText == "y":
            fileAllText += f'execute if score action.{name} dialogue matches {counter * tick}..{counter * tick + tickWait} run title @a actionbar "{beforeText + x}"\n'
            for y in range(len(text) - 1):
                fileAllText += f'execute if score action.{name} dialogue matches {counter * tick + tickWait + (counterDelete * tickDelete)} run title @a actionbar "{text[:-counterDelete]}"\n'
                counterDelete += 1
            fileAllText += f'execute if score action.{name} dialogue matches {counter * tick + tickWait + (counterDelete * tickDelete)} run title @a actionbar ""\n'
        beforeText += x
        counter += 1
    
    if deleteText == "y":
        fileAllText += f'execute if score action.{name} dialogue matches {counter * tick + tickWait + ((counterDelete - 1) * tickDelete)} run scoreboard players set action.isActive dialogue 0\n'
        fileAllText += f'execute if score action.{name} dialogue matches {counter * tick + tickWait + ((counterDelete - 1) * tickDelete)} run scoreboard players reset action.{name} dialogue\n'
    else:
        fileAllText += f'execute if score action.{name} dialogue matches {counter * tick} run scoreboard players set action.isActive dialogue 0\n'
        fileAllText += f'execute if score action.{name} dialogue matches {counter * tick} run scoreboard players reset action.{name} dialogue\n'

if type == 2:
    file = open(os.path.join(sys.path[0],f"title_{name}.mcfunction"), "w")
    fileAllText += f"execute if score title.{name} dialogue matches 0.. run scoreboard players set title.isActive dialogue 1\n"
    fileAllText += f"execute if score title.{name} dialogue matches 0.. run scoreboard players add title.{name} dialogue 1\n"
    fileAllText += f"execute if score title.{name} dialogue matches 0..1 run title @a times 0 30 5\n"

    for x in text:
        if counter + 1 != len(text) or deleteText == "n":
            fileAllText += f'execute if score title.{name} dialogue matches {counter * tick} run title @a title "{beforeText + x}"\n'
        elif deleteText == "y":
            fileAllText += f'execute if score title.{name} dialogue matches {counter * tick}..{counter * tick + tickWait} run title @a title "{beforeText + x}"\n'
            for y in range(len(text) - 1):
                fileAllText += f'execute if score title.{name} dialogue matches {counter * tick + tickWait + (counterDelete * tickDelete)} run title @a title "{text[:-counterDelete]}"\n'
                counterDelete += 1
            fileAllText += f'execute if score title.{name} dialogue matches {counter * tick + tickWait + (counterDelete * tickDelete)} run title @a title ""\n'
        beforeText += x
        counter += 1
    
    if deleteText == "y":
        fileAllText += f'execute if score title.{name} dialogue matches {counter * tick + tickWait + ((counterDelete - 1) * tickDelete)} run scoreboard players set title.isActive dialogue 0\n'
        fileAllText += f'execute if score title.{name} dialogue matches {counter * tick + tickWait + ((counterDelete - 1) * tickDelete)} run scoreboard players reset * dialogue\n'
    else:
        fileAllText += f'execute if score title.{name} dialogue matches {counter * tick} run scoreboard players set title.isActive dialogue 0\n'
        fileAllText += f'execute if score title.{name} dialogue matches {counter * tick} run scoreboard players reset * dialogue\n'

if type == 3:
    file = open(os.path.join(sys.path[0],f"tellraw_{name}.mcfunction"), "w")
    fileAllText += f"execute if score tellraw.{name} dialogue matches 0.. run scoreboard players set tellraw.isActive dialogue 1\n"
    fileAllText += f"execute if score tellraw.{name} dialogue matches 0.. run scoreboard players add tellraw.{name} dialogue 1\n"

    for x in text:
        if counter + 1 != len(text) or deleteText == "y":
            fileAllText += rf'execute if score tellraw.{name} dialogue matches {counter * tick} run tellraw @a ["\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"]' + '\n'
            fileAllText += f'execute if score tellraw.{name} dialogue matches {counter * tick} run tellraw @a "{beforeText + x}"\n'
        elif deleteText == "y":
            fileAllText += rf'execute if score tellraw.{name} dialogue matches {counter * tick} run tellraw @a ["\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"]' + '\n'
            fileAllText += f'execute if score tellraw.{name} dialogue matches {counter * tick}..{counter * tick + tickWait} run tellraw @a "{beforeText + x}"\n'
            for y in range(len(text) - 1):
                fileAllText += rf'execute if score tellraw.{name} dialogue matches {counter * tick} run tellraw @a ["\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"]' + '\n'
                fileAllText += f'execute if score tellraw.{name} dialogue matches {counter * tick + tickWait + (counterDelete * tickDelete)} run tellraw @a "{text[:-counterDelete]}"\n'
                counterDelete += 1
            fileAllText += rf'execute if score tellraw.{name} dialogue matches {counter * tick} run tellraw @a ["\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"]' + '\n'
            fileAllText += f'execute if score tellraw.{name} dialogue matches {counter * tick + tickWait + (counterDelete * tickDelete)} run tellraw @a ""\n'
        beforeText += x
        counter += 1
    
    if deleteText == "y":
        fileAllText += f'execute if score tellraw.{name} dialogue matches {counter * tick + tickWait + ((counterDelete - 1) * tickDelete)} run scoreboard players set tellraw.isActive dialogue 0\n'
        fileAllText += f'execute if score tellraw.{name} dialogue matches {counter * tick + tickWait + ((counterDelete - 1) * tickDelete)} run scoreboard players reset * dialogue\n'
    else:
        fileAllText += f'execute if score tellraw.{name} dialogue matches {counter * tick} run scoreboard players set tellraw.isActive dialogue 0\n'
        fileAllText += f'execute if score tellraw.{name} dialogue matches {counter * tick} run scoreboard players reset * dialogue\n'

file.write(fileAllText)
file.close()