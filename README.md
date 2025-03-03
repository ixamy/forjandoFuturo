# 🏕️ Juego de Supervivencia y Evolución

Bienvenido a **Juego de Supervivencia y Evolución**, un juego basado en la administración de recursos, población y habilidades a través de distintas épocas de la historia.

---

## 📜 Descripción
En este juego, debes gestionar tu población, recolectar recursos, aprender nuevas habilidades y tomar decisiones estratégicas para avanzar en la historia de la humanidad.

- 📌 Empiezas en la **Prehistoria** y puedes evolucionar hasta la **Edad Media**.
- 🎯 Administra **recursos** como comida y madera.
- 🛠️ Desbloquea y asigna **habilidades** a los miembros de tu población.
- 🔄 Toma decisiones que afectarán el curso del juego.

---

## 🚀 Instalación y Ejecución

### 1️⃣ **Clonar el repositorio**
Si aún no has clonado el repositorio, usa:

```sh
 git clone https://github.com/oscaralfonso93/mi-juego-python.git
 cd mi-juego-python
```

### 2️⃣ **Ejecutar el juego**

Ejecuta el archivo principal:

```sh
python main.py
```

Si necesitas instalar dependencias adicionales, agrégalas en `requirements.txt` y ejecuta:

```sh
pip install -r requirements.txt
```

---

## 🎮 Cómo jugar

- **`avanzar`** → Avanza en la historia si cumples los requisitos.
- **`aprender [habilidad]`** → Aprende una nueva habilidad.
- **`asignar [habilidad]`** → Asigna una habilidad a un personaje.
- **`cazar`** → Recolecta comida.
- **`talar`** → Recolecta madera.
- **`poblacion`** → Muestra la población actual.
- **`salir`** → Cierra el juego.

---

## 🛠️ Tecnologías utilizadas
- **Python 3**
- **Gestor de versiones Git**
- **Sistema de localización con JSON**

---

## 📌 Estructura del proyecto
```
mi-juego-python/
├── decisiones.py    # Maneja la toma de decisiones
├── epoca.py         # Controla las diferentes épocas del juego
├── eventos.py       # Registra los eventos ocurridos en el juego
├── habilidades.py   # Administra las habilidades disponibles
├── juego.py         # Motor principal del juego
├── localization.py  # Sistema de localización en varios idiomas
├── main.py          # Punto de entrada del juego
├── poblacion.py     # Manejo de la población y sus habilidades
├── recursos.py      # Administración de los recursos
├── strings.json     # Textos y mensajes en distintos idiomas
├── utils.py         # Utilidades varias
└── README.md        # Documentación del proyecto
```

---

## 🤝 Contribuciones
Si quieres contribuir, sigue estos pasos:
1. **Fork** el repositorio
2. Crea una rama nueva: `git checkout -b mi-nueva-feature`
3. Haz tus cambios y **haz un commit**: `git commit -m "Agregado X feature"`
4. **Sube los cambios**: `git push origin mi-nueva-feature`
5. Abre un **Pull Request** 🚀

---

## 📜 Licencia
Este proyecto está bajo la [MIT License](https://opensource.org/licenses/MIT).

