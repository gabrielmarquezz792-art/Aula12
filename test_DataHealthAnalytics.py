import DataHealthAnalytics as da

# ─────────────────────────────────────────
# IMC
# ─────────────────────────────────────────
def test_calculo_imc():
    assert da.calcular_imc(80, 1.80) == 24.69

def test_classificacao_imc_abaixo_peso():
    assert da.classificar_imc(18.4) == "Abaixo do peso"

def test_classificacao_imc_normal():
    assert da.classificar_imc(18.5) == "Normal"
    assert da.classificar_imc(24.9) == "Normal"

def test_classificacao_imc_sobrepeso():
    assert da.classificar_imc(25)   == "Sobrepeso"
    assert da.classificar_imc(29.9) == "Sobrepeso"

def test_classificacao_imc_obesidade():
    assert da.classificar_imc(30) == "Obesidade"
    assert da.classificar_imc(32) == "Obesidade"

# ─────────────────────────────────────────
# Pressão
# ─────────────────────────────────────────
def test_classificacao_pressao_normal():
    assert da.classificar_pressao(119, 79) == "Normal"

def test_classificacao_pressao_elevada():
    assert da.classificar_pressao(125, 79) == "Elevada"

def test_classificacao_pressao_hipertensao():
    # CORREÇÃO: o módulo retorna "Hipertensao" (sem acento), alinhado com o PDF
    assert da.classificar_pressao(130, 80) == "Hipertensao"
    assert da.classificar_pressao(140, 90) == "Hipertensao"

# ─────────────────────────────────────────
# Risco
# ─────────────────────────────────────────
def test_calcular_risco():
    # risco = (24.9*0.3) + (129/120*0.3) + ((10-8)*0.2) + (5/10*0.2)
    # = 7.47 + 0.3225 + 0.4 + 0.1 = 8.29
    resultado = da.calcular_risco(24.9, 129, 8, 5)
    assert resultado == round(resultado, 2)   # garante arredondamento
    assert resultado == 8.29

# ─────────────────────────────────────────
# Classificação de risco
# ─────────────────────────────────────────
def test_classificar_risco_baixo():
    assert da.classificar_risco(4.99) == "Baixo risco"

def test_classificar_risco_medio():
    assert da.classificar_risco(5)   == "Medio risco"
    assert da.classificar_risco(8)   == "Medio risco"

def test_classificar_risco_alto():
    # CORREÇÃO: o teste original usava 4.99 → "Alto risco", o que está errado
    assert da.classificar_risco(8.01) == "Alto risco"
    assert da.classificar_risco(10)   == "Alto risco"

# ─────────────────────────────────────────
# Avaliação de objetivo
# ─────────────────────────────────────────
def test_avaliar_objetivo_um():
    assert da.avaliar_objetivo(1, 4.99, 6.0) == True
    assert da.avaliar_objetivo(1, 5.0,  6.0) == False

def test_avaliar_objetivo_dois():
    # CORREÇÃO: o teste original usava objetivo=1 para todos os casos
    assert da.avaliar_objetivo(2, 7.99, 9.0) == True
    assert da.avaliar_objetivo(2, 8.0,  9.0) == True    # média == 8 → ainda médio
    assert da.avaliar_objetivo(2, 8.01, 9.0) == False

def test_avaliar_objetivo_tres():
    # CORREÇÃO: idem, usando objetivo=3
    assert da.avaliar_objetivo(3, 4.99, 5.0) == True    # média <= risco_atual
    assert da.avaliar_objetivo(3, 5.01, 5.0) == False   # média > risco_atual
