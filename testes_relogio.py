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
    assert str(r) == "22:20:59"

#r.segundos + 1 = 60, r.minutos + 1 < 60, r.horas + 1 = 24
def test_incrementa_6():
    r = Relogio(23, 20, 59)
    r.incrementar()
    assert str(r) == "22:20:59"

#r.segundos + 1 = 60, r.minutos + 1 = 60, r.horas + 1 < 24
def test_incrementa_7():
    r = Relogio(1, 59, 59)
    r.incrementar()
    assert str(r) == "22:20:59"

#r.segundos + 1 = 60, r.minutos + 1 = 60, r.horas + 1 = 24
def test_incrementa_8():
    r = Relogio(23, 59, 59)
    r.incrementar()
    assert str(r) == "00:00:00"

# r1.horas ≤ r2.horas, r1.minutos ≤ r2.minutos, r1.segundos ≤ r2.segundos
def test_comparacao_1():
    r1 = Relogio(10, 30, 45)
    r2 = Relogio(11, 45, 50)
    assert r1 < r2

# r1.horas ≤ r2.horas, r1.minutos ≤ r2.minutos, r1.segundos ≥ r2.segundos
def test_comparacao_2():
    r1 = Relogio(15, 20, 35)
    r2 = Relogio(15, 10, 30)
    assert r1 > r2

# r1.horas ≤ r2.horas, r1.minutos ≥ r2.minutos, r1.segundos ≤ r2.segundos
def test_comparacao_3():
    r1 = Relogio(8, 45, 15)
    r2 = Relogio(8, 30, 20)
    assert r1 > r2

# r1.horas ≤ r2.horas, r1.minutos ≥ r2.minutos, r1.segundos ≥ r2.segundos
def test_comparacao_4():
    r1 = Relogio(18, 40, 50)
    r2 = Relogio(18, 35, 55)
    assert r1 > r2

# r1.horas ≥ r2.horas, r1.minutos ≤ r2.minutos, r1.segundos ≤ r2.segundos
def test_comparacao_5():
    r1 = Relogio(12, 15, 30)
    r2 = Relogio(11, 30, 40)
    assert r1 < r2

# r1.horas ≥ r2.horas, r1.minutos ≤ r2.minutos, r1.segundos ≥ r2.segundos
def test_comparacao_6():
    r1 = Relogio(20, 10, 25)
    r2 = Relogio(19, 50, 30)
    assert r1 > r2

# r1.horas ≥ r2.horas, r1.minutos ≥ r2.minutos, r1.segundos ≤ r2.segundos
def test_comparacao_7():
    r1 = Relogio(14, 35, 10)
    r2 = Relogio(14, 20, 20)
    assert r1 > r2

# r1.horas ≥ r2.horas, r1.minutos ≥ r2.minutos, r1.segundos ≥ r2.segundos
def test_comparacao_8():
    r1 = Relogio(23, 59, 41)
    r2 = Relogio(22, 59, 37)
    assert r1 > r2

# r1.horas = r2.horas, r1.minutos = r2.minutos, r1.segundos = r2.segundos
def test_comparacao_limite():
    r1 = Relogio(20, 15, 20)
    r2 = Relogio(20, 15, 20)
    assert not r1 < r2

# (r1.segundos + r2.segundos) < 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) < 24
def test_adicao_1():
    r1 = Relogio(12, 30, 45)
    r2 = Relogio(4, 15, 10)
    resultado = r1 + r2
    assert str(resultado) == "16:46:55"

# (r1.segundos + r2.segundos) < 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) ≥ 24
def test_adicao_2():
    r1 = Relogio(20, 45, 30)
    r2 = Relogio(5, 10, 25)
    resultado = r1 + r2
    assert str(resultado) == "02:55:55"

# (r1.segundos + r2.segundos) < 60, (r1.minutos + r2.minutos) ≥ 60, (r1.horas + r2.horas) < 24
def test_adicao_3():
    r1 = Relogio(8, 30, 45)
    r2 = Relogio(6, 45, 20)
    resultado = r1 + r2
    assert str(resultado) == "15:16:05"

# (r1.segundos + r2.segundos) < 60, (r1.minutos + r2.minutos) ≥ 60, (r1.horas + r2.horas) ≥ 24
def test_adicao_4():
    r1 = Relogio(23, 45, 55)
    r2 = Relogio(3, 20, 35)
    resultado = r1 + r2
    assert str(resultado) == "03:06:30"

# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) < 24
def test_adicao_5():
    r1 = Relogio(9, 15, 20)
    r2 = Relogio(6, 25, 50)
    resultado = r1 + r2
    assert str(resultado) == "15:41:10"

# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) < 60, (r1.horas + r2.horas) ≥ 24
def test_adicao_6():
    r1 = Relogio(18, 55, 40)
    r2 = Relogio(8, 20, 25)
    resultado = r1 + r2
    assert str(resultado) == "03:16:05"

# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) ≥ 60, (r1.horas + r2.horas) < 24
def test_adicao_7():
    r1 = Relogio(14, 30, 45)
    r2 = Relogio(7, 40, 55)
    resultado = r1 + r2
    assert str(resultado) == "22:11:40"

# (r1.segundos + r2.segundos) ≥ 60, (r1.minutos + r2.minutos) ≥ 60, (r1.horas + r2.horas) ≥ 24
def test_adicao_8():
    r1 = Relogio(23, 59, 59)
    r2 = Relogio(0, 0, 1)
    resultado = r1 + r2
    assert str(resultado) == "00:00:00"

# (r1.segundos - r2.segundos) ≥ 0, (r1.minutos - r2.minutos) ≥ 0, (r1.horas - r2.horas) ≥ 0
def test_subtracao_1():
    r1 = Relogio(14, 30, 45)
    r2 = Relogio(5, 15, 10)
    resultado = r1 - r2
    assert str(resultado) == "09:15:35"

# (r1.segundos - r2.segundos) ≥ 0, (r1.minutos - r2.minutos) ≥ 0, (r1.horas - r2.horas) < 0
def test_subtracao_2():
    r1 = Relogio(10, 45, 30)
    r2 = Relogio(3, 10, 25)
    resultado = r1 - r2
    assert str(resultado) == "07:35:05"

# (r1.segundos - r2.segundos) ≥ 0, (r1.minutos - r2.minutos) < 0, (r1.horas - r2.horas) ≥ 0
def test_subtracao_3():
    r1 = Relogio(18, 30, 45)
    r2 = Relogio(8, 45, 20)
    resultado = r1 - r2
    assert str(resultado) == "09:45:25"

# (r1.segundos - r2.segundos) ≥ 0, (r1.minutos - r2.minutos) < 0, (r1.horas - r2.horas) < 0
def test_subtracao_4():
    r1 = Relogio(2, 45, 55)
    r2 = Relogio(3, 20, 35)
    resultado = r1 - r2
    assert str(resultado) == "23:25:20"

# (r1.segundos - r2.segundos) < 0, (r1.minutos - r2.minutos) ≥ 0, (r1.horas - r2.horas) ≥ 0
def test_subtracao_5():
    r1 = Relogio(14, 15, 20)
    r2 = Relogio(6, 25, 50)
    resultado = r1 - r2
    assert str(resultado) == "07:49:30"

# (r1.segundos - r2.segundos) < 0, (r1.minutos - r2.minutos) ≥ 0, (r1.horas - r2.horas) < 0
def test_subtracao_6():
    r1 = Relogio(18, 55, 40)
    r2 = Relogio(8, 20, 25)
    resultado = r1 - r2
    assert str(resultado) == "10:35:15"

# (r1.segundos - r2.segundos) < 0, (r1.minutos - r2.minutos) < 0, (r1.horas - r2.horas) ≥ 0
def test_subtracao_7():
    r1 = Relogio(23, 30, 45)
    r2 = Relogio(7, 40, 55)
    resultado = r1 - r2
    assert str(resultado) == "15:49:50"

# (r1.segundos - r2.segundos) < 0, (r1.minutos - r2.minutos) < 0, (r1.horas - r2.horas) < 0
def test_subtracao_8():
    r1 = Relogio(1, 0, 0)
    r2 = Relogio(2, 0, 0)
    resultado = r1 - r2
    assert str(resultado) == "23:00:00"
