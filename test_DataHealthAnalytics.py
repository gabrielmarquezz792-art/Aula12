import DataHealthAnalytics as da

def test_calculo_imc():
    assert da.calcular_imc(80, 1.80) == 24.69
    
def test_classificacao_imc_abaixo_peso():
    assert da.classificar_imc(18.4) == 'Abaixo do peso'
    
def test_classificacao_imc_normal():
    assert da.classificar_imc(18.5) == 'Normal'
    assert da.classificar_imc(24.9) == 'Normal'
    
def test_classificacao_imc_sobrepeso():
    assert da.classificar_imc(25) == 'Sobrepeso'
    assert da.classificar_imc(29.9) == 'Sobrepeso'

def test_classificacao_imc_obesidade():
    assert da.classificar_imc(30) == 'Obesidade'

def test_classificacao_pressao_normal():
    assert da.classificar_pressao(119, 79) == 'Normal'
    
def test_classificacao_pressao_elevada():
    assert da.classificar_pressao(129, 80) == 'Elevada'

def test_classificacao_pressao_hipertensao():
    assert da.classificar_pressao(130, 80) == 'Hipertensão'

def test_calcular_risco():
    assert da.calcular_risco(24.9, 129, 8, 5) == 8.9
    
def test_classificar_risco_baixo_risco():
    assert da.classificar_risco(4.99) == 'Baixo risco'

def test_classificar_risco_media_risco():
    assert da.classificar_risco(5) == 'Médio risco'
    assert da.classificar_risco(8) == 'Médio risco'

def test_classificar_risco_alto_risco():
    assert da.classificar_risco(4.99) == 'Alto risco'

def test_avaliar_objetivo_um():
    assert da.avaliar_objetivo(1, 4.99, 4.99) == True
    assert da.avaliar_objetivo(1, 4.99, 5) == False

def test_avaliar_objetivo_dois():
    assert da.avaliar_objetivo(1, 7.99, 7.99) == True
    assert da.avaliar_objetivo(1, 7.99, 8) == False
    
def test_avaliar_objetivo_tres():
    assert da.avaliar_objetivo(1, 4.99, 4.99) == True
    assert da.avaliar_objetivo(1, 4.99, 5) == False