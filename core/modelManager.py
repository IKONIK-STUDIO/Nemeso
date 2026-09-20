# importing libraries
import ollama
import time

# importing tools
from config import MODEL
from tools import clearTerminal, printDownloadedModels

# definitions
def modelManagerMain():
    clearTerminal()

    action = input(f"---NEMESO MODEL MANAGER---\n\t1 - Download a model\n\t2 - Delete a model\n\t3 - Select a model (Currently selected model: {MODEL})\n\nPlease select an action you would like to do. (Type 'exit' if you want to get back to Main Menu): ")

    if action == "exit":
        print("Exiting Nemeso...")
        return
    elif int(action) == 1:
        downloadModel()
    elif int(action) == 2:
        deleteModel()
    elif int(action) == 3:
        selectModel()

def downloadModel():
    clearTerminal()

    modelToDownload = input("---NEMESO MODEL DOWNLOADER---\n\nPlease type in the model name you want to download (Type 'exit' if you want to get back to Main Menu): ")

    if modelToDownload == "exit":
        return
    else:
        print(f"\nDownloading {modelToDownload}...")
        ollama.pull(modelToDownload) # downloads the selected model

        print(f"Succesfully downloaded {modelToDownload}. Continuing back to Main Menu in 3 seconds.")
        time.sleep(3)

def deleteModel():
    clearTerminal()

    print(f"---NEMESO MODEL DELETER---\n\nCurrently downloaded models:")
    printDownloadedModels()

    modelToDelete = input("\n\nPlease type the name of the model you want to delete (Type 'exit' if you want to get back to Main Menu): ")
    if modelToDelete == "exit":
        return
    else:
        ollama.delete(modelToDelete) # deletes the selected model

        print(f"Succesfully deleted {modelToDelete}. Continuing back to Main Menu in 3 seconds.")
        time.sleep(3)

def selectModel():
    clearTerminal()

    print(f"---NEMESO MODEL SELECTOR---\n\nCurrently available models:")
    printDownloadedModels()

    modelToSelect = input("\n\nPlease type the name of the model you want to select (Type 'exit' if you want to get back to Main Menu): ")
    if modelToSelect == "exit":
        return
    else:
        MODEL = modelToSelect

        print(f"Succesfully selected {modelToSelect}. Continuing back to Main Menu in 3 seconds.")
        time.sleep(3)