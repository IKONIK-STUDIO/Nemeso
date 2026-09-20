# importing libraries
import subprocess

# importing tools
from core import modelManagerMain
from tools import clearTerminal
from config import MODEL


# start nemeso
ollamaTerminal = subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) # opening terminal and sending "ollama serve" command --> starting ollama


# main
while True:
    clearTerminal()
    print("---NEMESO MAIN MENU---\n\t1 - Model Manager\n\t2 - Continue to chat\n")

    action = input("Choose an action you want to do (Type 'exit' if you want to close Nemeso): ")
    if action == "1":
        modelManagerMain()
    elif action == "2":
        pass # adding this feature later
    elif action == "exit":
        print("\n\nExiting Nemeso...")
        break


# shutdown nemeso
ollamaTerminal.terminate() # stopping ollama