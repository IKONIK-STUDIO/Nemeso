import ollama
import sys
from config import MODEL

def modelManager():
    action = input(f"WELCOME TO NEMESO MODEL MANAGER\n\t1 - Download a model\n\t2 - Delete a model\n\t3 - Select a model\nPlease select an action you would like to do. Type 'exit' if you want leave Nemeso.\nCurrently selected model: {MODEL}")

    if action == "exit":
        print("Exiting Nemeso...")
        sys.exit()
    elif int(action) == 1:
        downloadModel()
    elif int(action) == 2:
        deleteModel()
    elif int(action) == 3:
        selectModel()

def downloadModel():
    modelToDownload = input("Please type in the model name you want to download (Type 'exit' if you want to get back to Nemeso Model Manager):\n")

    if modelToDownload == "exit":
        sys.exit()
    else:
        print(f"Downloading {modelToDownload}")
        ollama.pull(modelToDownload)

def deleteModel():
    print(f"Currently downloaded models:")

    listDownloadedModels()

    modelToDelete = input("Please type the name of the model you want to delete (Type 'exit' if you want to get back to Nemeso Model Manager):\n")
    if modelToDelete == "exit":
        sys.exit()
    else:
        ollama.delete(modelToDelete)

def selectModel():
    print(f"Currently available models:")

    listDownloadedModels()

    modelToSelect = input("Please type the name of the model you want to select (Type 'exit' if you want to get back to Nemeso Model Manager):\n")
    if modelToSelect == "exit":
        sys.exit()
    else:
        MODEL = modelToSelect
    print(f"You've selected: {MODEL}")

def listDownloadedModels():
    modelList = ollama.list()
    for i in modelList["models"]:
        print(f"\t{i['model']}")