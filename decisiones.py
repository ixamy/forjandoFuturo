class DecisionManager:
    def __init__(self, recursos, poblacion, habilidades, eventos, localizacion):
        self.recursos = recursos
        self.poblacion = poblacion
        self.habilidades = habilidades
        self.eventos = eventos
        self.localizacion = localizacion

    def procesar(self, decision):
        partes = decision.split()

        if len(partes) == 2 and partes[0] == "aprender":
            _, habilidad = partes
            self.habilidades.aprender(habilidad, self.eventos)

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

        elif decision in self.habilidades.habilidades_aprendidas:
            if not self.poblacion.alguien_sabe(decision):
                self.eventos.registrar(self.localizacion.get('not_assigned', skill=decision))
                return

            for forji in self.poblacion.poblacion:
                if forji.habilidad == decision:
                    conocimiento_anterior = forji.conocimientos.get(decision, 0)
                    forji.incrementar_conocimiento(decision, 10)
                    incremento = forji.conocimientos[decision] - conocimiento_anterior

                    recursos = self.recursos.obtener_recurso_por_decision(decision)

                    if not recursos:
                        mensaje_error = self.localizacion.get('invalid_resource_action', action=decision)
                        self.eventos.registrar({mensaje_error})
                        return
                    
                    mensaje = self.localizacion.get('action_success', action=decision)
                    self.eventos.registrar(
                        self.localizacion.get('knowledge_gain_success', name=forji.nombre, percentage=incremento, skill=decision)
                    )

                    for recurso in recursos:  
                        if recurso not in self.recursos.recursos:
                            mensaje_error = self.localizacion.get('invalid_resource', resource=recurso)
                            self.eventos.registrar({mensaje_error})
                        else:
                            self.recursos.actualizar(recurso, 0, mensaje, self.eventos)

        elif decision == "poblacion":
            self.poblacion.mostrar_poblacion()
            input("...")

        else:
            self.eventos.registrar(self.localizacion.get('invalid_action'))
