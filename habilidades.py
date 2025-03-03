class HabilidadManager:
    def __init__(self, localizacion):
        self.habilidades_aprendidas = []  # Lista de habilidades desbloqueadas
        self.localizacion = localizacion

    def mostrar(self):
        """ Muestra las habilidades aprendidas globalmente. """
        if self.habilidades_aprendidas:
            habilidades_str = ", ".join(self.habilidades_aprendidas)
        else:
            habilidades_str = self.localizacion.get('no_skills')
        print(f"{self.localizacion.get('skills')}: {habilidades_str}")

    def aprender(self, habilidad, evento_manager):
        """ Desbloquea una habilidad globalmente. """
        if habilidad in self.habilidades_aprendidas:
            evento_manager.registrar(self.localizacion.get('already_learned', skill=habilidad))
        else:
            self.habilidades_aprendidas.append(habilidad)
            evento_manager.registrar(self.localizacion.get('learned_general', skill=habilidad))

    def esta_aprendida(self, habilidad):
        """ Verifica si una habilidad ha sido aprendida globalmente. """
        return habilidad in self.habilidades_aprendidas
