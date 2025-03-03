import random
import os
import json

class Persona:
    def __init__(self, nombre, edad, genero, localizacion, habilidad=None):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero  # Puede ser "masculino", "femenino"
        self.habilidad = habilidad  # Solo puede tener una
        self.localizacion = localizacion  # 📌 Agregado

    def asignar_habilidad(self, nueva_habilidad, confirmacion=False):
        """ Asigna una habilidad, pero si ya tiene una, solicita confirmación para reemplazarla. """
        if self.habilidad and self.habilidad != nueva_habilidad:
            if not confirmacion:
                return "confirmar_cambio"
            habilidad_anterior = self.habilidad
            self.habilidad = nueva_habilidad
            return self.localizacion.get('skill_replaced', name=self.nombre, old_skill=habilidad_anterior, new_skill=nueva_habilidad)
        
        self.habilidad = nueva_habilidad
        return self.localizacion.get('skill_learned', name=self.nombre, skill=nueva_habilidad)

    def __str__(self):
        habilidad_str = self.habilidad if self.habilidad else "Ninguna"
        return f"{self.nombre} (Edad: {self.edad}) – Habilidad: {habilidad_str}"

class PoblacionManager:
    def __init__(self, localizacion):
        self.localizacion = localizacion
        self.poblacion = []
        self.nombres = self.cargar_nombres()
        self.inicializar_poblacion()
    
    def cargar_nombres(self):
        """ Carga los nombres de los Forjis desde el JSON. """
        ruta_json = os.path.join(os.path.dirname(__file__), "forjis_nombres.json")
        try:
            with open(ruta_json, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("nombres", [])
        except FileNotFoundError:
            print("❌ Error: No se encontró forjis_nombres.json")
            return ["Forji1", "Forji2", "Forji3"]  # Nombres por defecto en caso de error

    def inicializar_poblacion(self):
        cantidad = random.randint(2, 4)
        for _ in range(cantidad):
            self.añadir_persona()

    def añadir_persona(self):
        nombre = random.choice(self.nombres)
        edad = random.randint(10, 40)
        genero = random.choice(["masculino", "femenino"])
        persona = Persona(nombre, edad, genero, self.localizacion)
        self.poblacion.append(persona)

    def mostrar_poblacion(self):
        print(self.localizacion.get('population_overview'))
        for persona in self.poblacion:
            print(f"   - {persona}")

    def alguien_sabe(self, habilidad):
        """ Devuelve True si al menos una persona tiene la habilidad especificada. """
        return any(persona.habilidad == habilidad for persona in self.poblacion)

    def asignar_habilidad(self, habilidad, habilidades, nombre=None, confirmacion=False):
        """ Asigna una habilidad a una persona, pero solo si ha sido aprendida globalmente. """
        if not habilidades.esta_aprendida(habilidad):
            return self.localizacion.get('not_learned_general', skill=habilidad)

        if nombre:
            persona = self.encontrar_persona(nombre)
            if persona:
                resultado = persona.asignar_habilidad(habilidad, confirmacion)
                if resultado == "confirmar_cambio":
                    return self.localizacion.get('confirm_skill_change', name=nombre, old_skill=persona.habilidad, new_skill=habilidad)
                return resultado
            return self.localizacion.get('person_not_found', name=nombre)
        
        # Si no se especificó nombre, buscar una persona sin habilidad
        personas_sin_habilidad = [p for p in self.poblacion if not p.habilidad]
        if personas_sin_habilidad:
            persona = random.choice(personas_sin_habilidad)
            return persona.asignar_habilidad(habilidad)

        return self.localizacion.get('no_available_people')
    
    def encontrar_persona(self, nombre):
        """ Busca una persona por su nombre en la población. """
        for persona in self.poblacion:
            if persona.nombre.lower() == nombre.lower():
                return persona
        return None
