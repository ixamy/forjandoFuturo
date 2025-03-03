import random
from utils import esperar

class RecursoManager:
    def __init__(self, localizacion):
        umbral_inicial = (5, 15, 5)  
        
        self.recursos = {
            "comida": random.randrange(*umbral_inicial),
            "madera": random.randrange(*umbral_inicial),
        }
        self.emojis = {
            "comida": "🍖",
            "madera": "🪵"
        }
        self.localizacion = localizacion

    def mostrar(self):
        print(f"{self.localizacion.get('resources')}:")
        for k, v in self.recursos.items():
            print(f"   - {self.obtener_nombre_mostrable(k)}: {v}")

    def obtener(self, recurso):
        return self.recursos.get(recurso, 0)

    def actualizar(self, recurso, cantidad, mensaje, evento_manager):
        self.recursos[recurso] += cantidad
        evento_manager.registrar(f"{mensaje} ({self.obtener_nombre_mostrable(recurso)}: {'+' if cantidad > 0 else ''}{cantidad})")
        esperar(1)

    def obtener_nombre_mostrable(self, recurso):
        return f"{self.emojis.get(recurso, '')} {self.localizacion.get(recurso)}"
