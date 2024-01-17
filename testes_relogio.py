from relogio import Relogio

def test_modifica_s():
    r = Relogio(20, 30, 5)
    r.incrementar()
    assert str(r) == "20:30:06"

def test_modifica_sm():
    r = Relogio(0, 15, 59)
    r.incrementar()
    assert str(r) == "00:16:00"

def test_modifica_smh():
    r = Relogio(8, 59, 59)
    r.incrementar()
    assert str(r) == "09:00:00"

def test_reset_clock():
    r = Relogio(23, 59, 59)
    r.incrementar()
    assert str(r) == "00:00:00"

def test_tempo_igual():
    r1 = Relogio(15, 15, 15)
    r2 = Relogio(15, 15, 15)
    assert not r1 < r2

def test_r1_antes_hm():
    r1 = Relogio(23, 17, 10)
    r2 = Relogio(23, 17, 15)
    assert r1 < r2

def test_r1_antes_h():
    r1 = Relogio(14, 12, 50)
    r2 = Relogio(14, 17, 15)
    assert r1 < r2

def test_r1_antes():
    r1 = Relogio(0, 58, 50)
    r2 = Relogio(2, 17, 15)
    assert r1 < r2

def test_r1_depois_hm():
    r1 = Relogio(23, 17, 15)
    r2 = Relogio(23, 17, 10)
    assert r1 > r2

def test_r1_depois_h():
    r1 = Relogio(14, 17, 15)
    r2 = Relogio(14, 12, 50)
    assert r1 > r2

# adicionar teste de limite onde: r1 == r2+1s

def test_r1_depois():
    r1 = Relogio(2, 17, 15)
    r2 = Relogio(0, 58, 50)
    assert r1 > r2

# 
def test_soma_proximo_dia():
    r1 = Relogio(18, 50, 13)
    r2 = Relogio(8, 20, 40)
    assert str(r1 + r2) == "03:10:53"

def test_soma_dia_atual():
    r1 = Relogio(18, 51, 13)
    r2 = Relogio(2, 11, 59)
    assert str(r1 + r2) == "21:03:12"

def test_sub_proximo_dia():
    r1 = Relogio(18, 50, 13)
    r2 = Relogio(8, 20, 40)
    assert str(r1 - r2) == "10:29:33"

def test_sub_dia_atual():
    r1 = Relogio(18, 51, 13)
    r2 = Relogio(2, 11, 59)
    assert str(r1 - r2) == "16:39:14"

# adicionar testes de limite onde r1 + r2 == 00:00
