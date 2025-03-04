import json

class Localization:
    def __init__(self, language="es"):
        self.language = language
        self.strings = self.load_strings()

    def load_strings(self):
        try:
            with open("strings.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get(self.language, {})
        except FileNotFoundError:
            return {}

    def get(self, key, **kwargs):
        """ Obtiene un string traducido con soporte para reemplazar valores dinámicos """
        text = self.strings.get(key, f"String for {key} not found")
        return text.format(**kwargs)

    def set_language(self, language):
        """ Cambia el idioma y recarga los textos """
        self.language = language
        self.strings = self.load_strings()
