from dataclasses import dataclass

@dataclass
class Relogio:
    segundos : int
    minutos : int
    horas : int

    def __init__(self, horas : int, minutos : int, segundos : int):
        if not 0 <= horas < 24:
            raise ValueError("Horas devem estar no intervalo [0,24)")
        self.horas = horas
        if not 0 <= minutos < 60:
            raise ValueError("Minutos devem estar no intervalo [0,60)")
        self.minutos = minutos
        if not 0 <= segundos < 60:
            raise ValueError("Segundos devem estar no intervalo [0,60)")
        self.segundos = segundos

    def incrementar(self):
        self.segundos += 1

        if self.segundos == 60:
            self.segundos = 0
            self.minutos += 1

        if self.minutos == 60:
            self.minutos = 0
            self.horas += 1

        if self.horas == 24:
            self.horas = 0

    def __str__(self):
        return f'{str(self.horas).zfill(2)}:{str(self.minutos).zfill(2)}:{str(self.segundos).zfill(2)}'

    def __eq__(self, other):
        return self.horas == other.horas and \
                self.minutos == other.minutos and \
                self.segundos == other.segundos

    def __lt__(self, other):
        if self.horas != other.horas:
            return self.horas < other.horas
        if self.minutos != other.minutos:
            return self.minutos < other.minutos
        if self.segundos != other.segundos:
            return self.segundos < other.segundos
        else:
            return False # horário iguais

    def __add__(self, other):
        novo_segundos = self.segundos + other.segundos;
        novo_minutos = self.minutos + other.minutos
        novo_horas = self.horas + other.horas

        if not 0 <= novo_segundos <= 60:
            novo_minutos += 1 
            novo_segundos %= 60

        if not 0 <= novo_minutos <= 60:
            novo_horas += 1 
            novo_minutos %= 60

        novo_horas %= 24

        return Relogio(novo_horas, novo_minutos, novo_segundos)

    def __sub__(self, other):
        novo_segundos = self.segundos - other.segundos;
        novo_minutos = self.minutos - other.minutos
        novo_horas = self.horas - other.horas

        if not 0 <= novo_segundos <= 60:
            novo_minutos -= 1 
            novo_segundos %= 60

        if not 0 <= novo_minutos <= 60:
            novo_horas -= 1 
            novo_minutos %= 60

        novo_horas %= 24

        return Relogio(novo_horas, novo_minutos, novo_segundos)
