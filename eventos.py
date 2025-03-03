class EventoManager:
    def __init__(self, localizacion):
        self.eventos = []
        self.localizacion = localizacion

    def registrar(self, mensaje):
        self.eventos.append(mensaje)
        if len(self.eventos) > 10:
            self.eventos.pop(0)

    def mostrar(self):
        print(f"{self.localizacion.get('events')}:")
        for evento in self.eventos[-10:]:
            print(f"   - {evento}")
