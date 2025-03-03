import os
import time

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar(segundos):
    time.sleep(segundos)
