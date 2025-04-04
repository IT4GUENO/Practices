import os

commandPygame1 = "python -m pip uninstall pygame"
commandPygame2 = "python -m pip install pygame"
versions = "python -m pip list"
while True:
    print("1. Pygame")
    opcion = input("Install Pygame? ")

if opcion == "1":
    os.system(commandPygame1)
    os.system(commandPygame2)
    print(os.system(versions))