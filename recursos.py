import random
from utils import esperar

class RecursoManager:
    def __init__(self, localizacion):
        umbral_inicial = (2, 23, 3)  

        self.recursos = {
            "comida": random.randrange(*umbral_inicial),
            "madera": random.randrange(*umbral_inicial),
            "piedra": random.randrange(*umbral_inicial),
            "flores": random.randrange(*umbral_inicial)
        }
        self.emojis = {
            "comida": "🍖",
            "madera": "🪵",
            "piedra": "🪨",
            "flores": "🌷"
        }
        self.decision_a_recurso = {
            "cazar": ["comida"],
            "talar": ["madera"],
            "minar": ["piedra"],
            "recolectar": ["flores"]
        }
        self.incrementos = {
            "comida": 15,
            "madera": 10,
            "piedra": 7,
            "flores": 5
        }
        self.localizacion = localizacion

    def mostrar(self):
        print(f"{self.localizacion.get('resources')}:")
        for k, v in self.recursos.items():
            print(f"   - {self.obtener_nombre_mostrable(k)}: {v}")

    def obtener(self, recurso):
        return self.recursos.get(recurso, 0)

    def actualizar(self, recurso, cantidad, mensaje, evento_manager):
        if recurso not in self.recursos:
            mensaje_error = self.localizacion.get('invalid_resource', resource=recurso)
            evento_manager.registrar({mensaje_error})
            return

        cantidad_real = self.incrementos.get(recurso, 10)
        self.recursos[recurso] += cantidad_real
        
        self.recursos[recurso] += cantidad
        evento_manager.registrar(f"{mensaje} ({self.obtener_nombre_mostrable(recurso)}: +{cantidad_real})")
        esperar(1)

    def obtener_nombre_mostrable(self, recurso):
        return f"{self.emojis.get(recurso, '')} {self.localizacion.get(recurso)}"

    def obtener_recurso_por_decision(self, decision):
        """
        Devuelve una lista de recursos asociados a la decisión.
        Si la decisión no tiene recursos, devuelve una lista vacía.
        """
        return self.decision_a_recurso.get(decision, [])
