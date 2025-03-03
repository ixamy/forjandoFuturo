class DecisionManager:
    def __init__(self, recursos, poblacion, habilidades, eventos, localizacion):
        self.recursos = recursos
        self.poblacion = poblacion
        self.habilidades = habilidades
        self.eventos = eventos
        self.localizacion = localizacion

    def procesar(self, decision):
        partes = decision.split()

        # 📌 Aprender una habilidad globalmente
        if len(partes) == 2 and partes[0] == "aprender":
            _, habilidad = partes
            self.habilidades.aprender(habilidad, self.eventos)

        # 📌 Asignar una habilidad a un forji
        elif decision.startswith("asignar"):
            if len(partes) == 2:
                _, habilidad = partes
                mensaje = self.poblacion.asignar_habilidad(habilidad, self.habilidades)
            elif len(partes) == 3:
                _, nombre, habilidad = partes
                mensaje = self.poblacion.asignar_habilidad(habilidad, self.habilidades, nombre)
            else:
                mensaje = self.localizacion.get('assign_error')

            self.eventos.registrar(mensaje)

        # 📌 Usar habilidades como "cazar" y "talar"
        elif decision in ["cazar", "talar"]:
            if not self.habilidades.esta_aprendida(decision):
                self.eventos.registrar(self.localizacion.get('not_learned_general', skill=decision))
            elif not self.poblacion.alguien_sabe(decision):
                self.eventos.registrar(self.localizacion.get('not_assigned', skill=decision))
            else:
                recurso = "comida" if decision == "cazar" else "madera"
                mensaje = self.localizacion.get('action_success', action=decision)
                self.recursos.actualizar(recurso, 10, mensaje, self.eventos)

        # 📌 Ver la población
        elif decision == "poblacion":
            self.poblacion.mostrar_poblacion()
            input("...")

        # 📌 Acción no válida
        else:
            self.eventos.registrar(self.localizacion.get('invalid_action'))
