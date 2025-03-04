from juego import JuegoSupervivencia
import traceback

if __name__ == "__main__":
    try:
        juego = JuegoSupervivencia()
        juego.jugar()
    except Exception as e:
        traceback.print_exc()
        input("\n...")
