# importing libraries
import os
import ollama

# definitions
def clearTerminal():
    os.system("cls")

def printDownloadedModels():
    modelList = ollama.list()
    for i in modelList["models"]:
        print(f"\t{i['model']}")