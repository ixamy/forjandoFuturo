from epoca import EpocaManager
from eventos import EventoManager
from recursos import RecursoManager
from poblacion import PoblacionManager
from habilidades import HabilidadManager
from decisiones import DecisionManager
from localization import Localization
from utils import limpiar_pantalla

class JuegoSupervivencia:
    def __init__(self, idioma="es"):
        self.localizacion = Localization(idioma)
        self.eventos = EventoManager(self.localizacion)
        self.recursos = RecursoManager(self.localizacion)
        self.poblacion = PoblacionManager(self.localizacion)
        self.habilidades = HabilidadManager(self.localizacion)
        
        # 📌 Corregido: ahora pasamos `self.poblacion` también
        self.epoca = EpocaManager(self.recursos, self.poblacion, self.habilidades, self.eventos, self.localizacion)
        
        self.decision_manager = DecisionManager(self.recursos, self.poblacion, self.habilidades, self.eventos, self.localizacion)

    def mostrar_estado(self):
        limpiar_pantalla()
        
        estrella = "⭐" if self.epoca.ha_cambiado_epoca() else ""
        print(self.localizacion.get("epoch_current", epoch=self.epoca.obtener_epoca()) + f" {estrella}\n")
        
        self.poblacion.mostrar_poblacion()
        print()
        
        self.recursos.mostrar()
        print()
        
        self.habilidades.mostrar()
        print()
        
        self.eventos.mostrar()
        print("\n")

        self.epoca.nueva_epoca = False  

    def jugar(self):
        print(self.localizacion.get("welcome"))
        while not self.epoca.ha_alcanzado_final():
            self.mostrar_estado()
            decision = input(f"{self.localizacion.get("prompt")} ").lower()
            if decision == "salir":
                print(self.localizacion.get("goodbye"))
                break
            elif decision == "avanzar":
                self.epoca.avanzar()
            else:
                self.decision_manager.procesar(decision)

        if self.epoca.ha_alcanzado_final():
            print(self.localizacion.get("win"))
