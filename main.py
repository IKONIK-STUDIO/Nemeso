import ollama
import sys
from tools import modelManager
import subprocess

ollamaTerminal = subprocess.Popen(["ollama", "serve"])

modelManager.modelManager()

ollamaTerminal.terminate()