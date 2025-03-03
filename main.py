from juego import JuegoSupervivencia
import traceback

if __name__ == "__main__":
    try:
        juego = JuegoSupervivencia()
        juego.jugar()
    except Exception as e:
        print("\n❌ ERROR DETECTADO: El juego ha fallado con el siguiente error:\n")
        traceback.print_exc()  # Muestra detalles del error
        input("\nPresiona Enter para salir...")
