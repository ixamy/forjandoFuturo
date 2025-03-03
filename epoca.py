class EpocaManager:
    def __init__(self, recursos, poblacion, habilidades, eventos, localizacion):
        self.epocas = ["Prehistoria", "Edad de Piedra", "Edad de los Metales", "Edad Media"]
        self.indice_epoca = 0
        self.recursos = recursos
        self.poblacion = poblacion
        self.habilidades = habilidades
        self.eventos = eventos
        self.localizacion = localizacion
        self.nueva_epoca = False  

    def obtener_epoca(self):
        return self.epocas[self.indice_epoca]

    def ha_alcanzado_final(self):
        return self.obtener_epoca() == "Edad Media"

    def ha_cambiado_epoca(self):
        return self.nueva_epoca  

    def avanzar(self):
        """ Verifica si se cumplen los requisitos y avanza de época si es posible. """
        requisitos = [
            {"habilidad": "cazar", "comida": 20, "poblacion": 2},  # Edad de Piedra
            {"habilidad": "talar", "comida": 50, "poblacion": 6},  # Edad de los Metales
            {"habilidad": "cazar", "comida": 80, "poblacion": 10}  # Edad Media
        ]

        if self.indice_epoca >= len(requisitos):
            self.eventos.registrar(self.localizacion.get("already_in_final_epoch"))
            return

        req = requisitos[self.indice_epoca]

        if (
            self.recursos.obtener("comida") >= req["comida"] and
            self.poblacion.alguien_sabe(req["habilidad"]) and
            len(self.poblacion.poblacion) >= req["poblacion"]
        ):
            self.indice_epoca += 1
            self.nueva_epoca = True
            self.eventos.registrar(self.localizacion.get("epoch_advance", epoch=self.obtener_epoca()))
        else:
            self.eventos.registrar(self.localizacion.get("cant_advance"))
