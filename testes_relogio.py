from relogio import Relogio


#r.segundos + 1 < 60, r.minutos + 1 < 60, r.horas + 1 < 24
def test_incrementa_1():
    r = Relogio(20, 30, 5)
    r.incrementar()
    assert str(r) == "20:30:06"

#r.segundos + 1 < 60, r.minutos + 1 < 60, r.horas + 1 = 24
def test_incrementa_2():
    r = Relogio(23, 15, 15)
    r.incrementar()
    assert str(r) == "23:15:16"

#r.segundos + 1 < 60, r.minutos + 1 = 60, r.horas + 1 < 24
def test_incrementa_3():
    r = Relogio(10, 59, 0)
    r.incrementar()
    assert str(r) == "10:59:01"

#r.segundos + 1 < 60, r.minutos + 1 = 60, r.horas + 1 = 24
def test_incrementa_4():
    r = Relogio(23, 59, 58)
    r.incrementar()
    assert str(r) == "23:59:59"

#r.segundos + 1 = 60, r.minutos + 1 < 60, r.horas + 1 < 24
def test_incrementa_5():
    r = Relogio(20, 20, 59)
    r.incrementar()
    assert str(r) == "20:21:00"

#r.segundos + 1 = 60, r.minutos + 1 < 60, r.horas + 1 = 24
def test_incrementa_6():
    r = Relogio(23, 20, 59)
    r.incrementar()
    assert str(r) == "23:21:00"

#r.segundos + 1 = 60, r.minutos + 1 = 60, r.horas + 1 < 24
def test_incrementa_7():
    r = Relogio(1, 59, 59)
    r.incrementar()
    assert str(r) == "02:00:00"

#r.segundos + 1 = 60, r.minutos + 1 = 60, r.horas + 1 = 24
def test_incrementa_8():
    r = Relogio(23, 59, 59)
    r.incrementar()
    assert str(r) == "00:00:00"


# r1.horas > r2.horas
def test_comparacao_1():
    r1 = Relogio(12, 30, 30)
    r2 = Relogio(11, 45, 50)
    assert r1 > r2

# r1.horas < r2.horas
def test_comparacao_2():
    r1 = Relogio(0, 20, 20)
    r2 = Relogio(15, 30, 20)
    assert r1 < r2

# r1.horas = r2.horas, r1.minutos > r2.minutos
def test_comparacao_3():
    r1 = Relogio(8, 30, 21)
    r2 = Relogio(8, 10, 30)
    assert r1 > r2

# r1.horas = r2.horas, r1.minutos < r2.minutos
def test_comparacao_4():
    r1 = Relogio(15, 20, 0)
    r2 = Relogio(15, 30, 0)
    assert r1 < r2

# r1.horas = r2.horas, r1.minutos = r2.minutos, r1.segundos < r2.segundos
def test_comparacao_5():
    r1 = Relogio(22, 10, 53)
    r2 = Relogio(22, 10, 55)
    assert r1 < r2

# r1.horas = r2.horas, r1.minutos = r2.minutos, r1.segundos > r2.segundos
def test_comparacao_6():
    r1 = Relogio(12, 15, 55)
    r2 = Relogio(12, 15, 40)
    assert r1 > r2

# r1.horas = r2.horas, r1.minutos = r2.minutos, r1.segundos = r2.segundos
def test_comparacao_7():
    r1 = Relogio(20, 0, 0)
    r2 = Relogio(20, 0, 0)
    assert r1 == r2


# (r1.segundos + r2.segundos) < 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) < 24
def test_adicao_1():
    r1 = Relogio(20, 15, 30)
    r2 = Relogio(2, 40, 21)

    assert str(r1+r2) == "22:55:51"


# (r1.segundos + r2.segundos) < 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) ≥ 24
def test_adicao_2():
    r1 = Relogio(20, 15, 30)
    r2 = Relogio(20, 40, 21)

    assert str(r1+r2) == "16:55:51"

# (r1.segundos + r2.segundos) < 60, (r1.minutos + r2.minutos) ≥ 60, (r1.horas + r2.horas) < 24
def test_adicao_3():
    r1 = Relogio(20, 50, 30)
    r2 = Relogio(1, 31, 15)

    assert str(r1+r2) == "22:21:45"

# (r1.segundos + r2.segundos) < 60, (r1.minutos + r2.minutos) ≥ 60, (r1.horas + r2.horas) < 24
# r1.horas + r2.horas = 23
def test_adicao_3_limite():
    r1 = Relogio(20, 50, 30)
    r2 = Relogio(3, 31, 15)

    assert str(r1+r2) == "00:21:45"

#(r1.segundos + r2.segundos) < 60, (r1.minutos + r2.minutos) ≥ 60, (r1.horas + r2.horas) ≥ 24
def teste_adicao_4():
    r1 = Relogio(18, 49, 1)
    r2 = Relogio(14, 37, 0)

    assert str(r1+r2) == "09:26:01"

# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) < 24
def test_adicao_5():
    r1 = Relogio(20, 15, 59)
    r2 = Relogio(2, 31, 58)

    assert str(r1+r2) == "22:47:57"


# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) < 24
# r1.minutos + r2.minutos = 59
def test_adicao_5_limiteA():
    r1 = Relogio(20, 28, 59)
    r2 = Relogio(2, 31, 2)

    assert str(r1+r2) == "23:00:01"

# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) < 24
# r1.horas + r2.horas = 23 e r1.minutos + r2.minutos = 59
def test_adicao_5_limiteB():
    r1 = Relogio(20, 28, 59)
    r2 = Relogio(3, 31, 15)

    assert str(r1+r2) == "00:00:14"

# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) ≥ 24
def teste_adicao_6():
    r1 = Relogio(20, 1, 31)
    r2 = Relogio(4, 2, 57)

    assert str(r1+r2) == "00:04:28"

# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) ≥ 24
# r1.minutos + r2.minutos = 59
def teste_adicao_6_limite():
    r1 = Relogio(20, 58, 31)
    r2 = Relogio(4, 1, 57)

    assert str(r1+r2) == "01:00:28"


# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) ≥ 60, (r1.horas + r2.horas) < 24
def teste_adicao_7():
    r1 = Relogio(20, 30, 25)
    r2 = Relogio(1, 35, 48)

    assert str(r1+r2) == "22:06:13"


# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) ≥ 60, (r1.horas + r2.horas) < 24
# r1.horas + r2.horas = 23
def teste_adicao_7_limite():
    r1 = Relogio(20, 30, 25)
    r2 = Relogio(3, 35, 48)

    assert str(r1+r2) == "00:06:13"

# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) ≥ 60, (r1.horas + r2.horas) ≥ 24
def teste_adicao_8():
    r1 = Relogio(23, 38, 25)
    r2 = Relogio(20, 35, 48)

    assert str(r1+r2) == "20:14:13"

# (r1.segundos - r2.segundos) ≥ 0, (r1.minutos - r2.minutos) ≥ 0, (r1.horas - r2.horas) ≥ 0
def test_subtracao_1():
    r1 = Relogio(15, 30, 45)
    r2 = Relogio(10, 20, 15)
    assert str(r1 - r2) == "05:10:30"

# (r1.segundos - r2.segundos) ≥ 0, (r1.minutos - r2.minutos) ≥ 0, (r1.horas + r2.horas) < 0
def test_subtracao_2():
    r1 = Relogio(10, 45, 20)
    r2 = Relogio(5, 25, 30)
    assert str(r1 - r2) == "05:19:50"

# (r1.segundos - r2.segundos) ≥ 0, (r1.minutos - r2.minutos) < 0, (r1.horas - r2.horas) ≥ 0
def test_subtracao_3():
    r1 = Relogio(18, 30, 40)
    r2 = Relogio(5, 40, 50)
    assert str(r1 - r2) == "12:49:50"

# (r1.segundos - r2.segundos) ≥ 0, (r1.minutos - r2.minutos) < 0, (r1.horas - r2.horas) < 0
def test_subtracao_4():
    r1 = Relogio(8, 15, 20)
    r2 = Relogio(3, 35, 30)
    assert str(r1 - r2) == "04:39:50"

# (r1.segundos - r2.segundos) < 0, (r1.minutos - r2.minutos) ≥ 0, (r1.horas - r2.horas) ≥ 0
def test_subtracao_5():
    r1 = Relogio(14, 50, 30)
    r2 = Relogio(6, 25, 20)
    assert str(r1 - r2) == "08:25:10"

# (r1.segundos - r2.segundos) < 0, (r1.minutos - r2.minutos) ≥ 0, (r1.horas - r2.horas) < 0
def test_subtracao_6():
    r1 = Relogio(5, 40, 15)
    r2 = Relogio(2, 35, 25)
    assert str(r1 - r2) == "03:04:50"

# (r1.segundos - r2.segundos) < 0, (r1.minutos - r2.minutos) < 0, (r1.horas - r2.horas) ≥ 0
def test_subtracao_7():
    r1 = Relogio(16, 25, 40)
    r2 = Relogio(9, 40, 50)
    assert str(r1 - r2) == "06:44:50"

# (r1.segundos - r2.segundos) < 0, (r1.minutos - r2.minutos) < 0, (r1.horas - r2.horas) < 0
def test_subtracao_8():
    r1 = Relogio(2, 15, 30)
    r2 = Relogio(5, 35, 45)
    assert str(r1 - r2) == "20:39:45"
