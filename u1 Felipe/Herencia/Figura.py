class Figura:
    def __init__(self, ancho, lado) -> None:
        self._ancho = ancho
        self._lado = lado

    def __str__(self) -> str:
        return f"Ancho: {self._ancho} Largo: {self._lado}"