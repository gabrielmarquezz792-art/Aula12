import statistics
from datetime import datetime, timedelta

pacientes = []

# ─────────────────────────────────────────
# 1. Cadastro do Paciente
# ─────────────────────────────────────────
def cadastrar_paciente():
    nome      = input("Nome: ")
    idade     = int(input("Idade: "))
    peso      = float(input("Peso (kg): "))
    altura    = float(input("Altura (m): "))
    sistolica = int(input("Pressão sistólica (mmHg): "))
    diastolica= int(input("Pressão diastólica (mmHg): "))
    atividade = int(input("Nível de atividade física (0-10): "))
    alcool    = int(input("Consumo semanal de álcool: "))
    objetivo  = int(input("Objetivo (1=Baixo risco / 2=Médio risco / 3=Manter): "))

    paciente = [nome, idade, peso, altura, sistolica, diastolica,
                atividade, alcool, objetivo]
    pacientes.append(paciente)
    return paciente

# ─────────────────────────────────────────
# 2. IMC
# ─────────────────────────────────────────
def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc <= 24.9:
        return "Normal"
    elif imc <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# ─────────────────────────────────────────
# 3. Pressão
# ─────────────────────────────────────────
def classificar_pressao(sistolica, diastolica):
    if sistolica < 120 and diastolica < 80:
        return "Normal"
    elif sistolica <= 129 and diastolica <= 80:
        return "Elevada"
    else:
        return "Hipertensao"

# ─────────────────────────────────────────
# 4. Risco Atual
# ─────────────────────────────────────────
def calcular_risco(imc, sistolica, atividade, alcool):
    risco = (imc * 0.3) + ((sistolica / 120) * 0.3) + ((10 - atividade) * 0.2) + ((alcool / 10) * 0.2)
    return round(risco, 2)

# ─────────────────────────────────────────
# 5. Simulação de Cenários
# ─────────────────────────────────────────
def simular_melhoria(imc, sistolica, atividade, alcool):
    imc_novo       = imc * 0.95
    sistolica_nova = sistolica * 0.95
    atividade_nova = min(atividade + 2, 10)
    alcool_novo    = alcool * 0.80
    return calcular_risco(imc_novo, sistolica_nova, atividade_nova, alcool_novo)

def simular_estabilidade(imc, sistolica, atividade, alcool):
    return calcular_risco(imc, sistolica, atividade, alcool)

def simular_piora(imc, sistolica, atividade, alcool):
    imc_novo       = imc * 1.05
    sistolica_nova = sistolica * 1.05
    atividade_nova = max(atividade - 2, 0)
    alcool_novo    = alcool * 1.20
    return calcular_risco(imc_novo, sistolica_nova, atividade_nova, alcool_novo)

# ─────────────────────────────────────────
# 6. Lista de Riscos
# ─────────────────────────────────────────
def gerar_lista_riscos(imc, sistolica, atividade, alcool):
    return [
        simular_melhoria(imc, sistolica, atividade, alcool),
        simular_estabilidade(imc, sistolica, atividade, alcool),
        simular_piora(imc, sistolica, atividade, alcool)
    ]

# ─────────────────────────────────────────
# 7. Estatísticas dos Cenários
# ─────────────────────────────────────────
def calcular_estatisticas(lista_riscos):
    media   = round(statistics.mean(lista_riscos), 2)
    mediana = round(statistics.median(lista_riscos), 2)
    desvio  = round(statistics.stdev(lista_riscos), 2)
    return media, mediana, desvio

# ─────────────────────────────────────────
# 8. Classificação Final
# ─────────────────────────────────────────
def classificar_risco(media):
    if media < 5:
        return "Baixo risco"
    elif media <= 8:
        return "Medio risco"
    else:
        return "Alto risco"

# ─────────────────────────────────────────
# 9. Avaliação do Objetivo
# ─────────────────────────────────────────
def avaliar_objetivo(objetivo, media_riscos, risco_atual):
    if objetivo == 1:
        return media_riscos < 5
    elif objetivo == 2:
        return media_riscos <= 8
    elif objetivo == 3:
        return media_riscos <= risco_atual
    return False

# ─────────────────────────────────────────
# 10. Melhor e Pior Cenário
# ─────────────────────────────────────────
def identificar_cenarios(lista_riscos):
    return min(lista_riscos), max(lista_riscos)

# ─────────────────────────────────────────
# 11. Relatório Individual
# ─────────────────────────────────────────
def gerar_relatorio(paciente):
    nome, idade, peso, altura, sistolica, diastolica, atividade, alcool, objetivo = paciente

    imc              = calcular_imc(peso, altura)
    class_imc        = classificar_imc(imc)
    class_pressao    = classificar_pressao(sistolica, diastolica)
    risco_atual      = calcular_risco(imc, sistolica, atividade, alcool)
    lista_riscos     = gerar_lista_riscos(imc, sistolica, atividade, alcool)
    media, mediana, desvio = calcular_estatisticas(lista_riscos)
    class_risco      = classificar_risco(media)
    objetivo_ok      = avaliar_objetivo(objetivo, media, risco_atual)
    melhor, pior     = identificar_cenarios(lista_riscos)

    hoje        = datetime.today()
    reavaliacao = hoje + timedelta(days=30)

    objetivos_str = {1: "Reduzir para baixo risco",
                     2: "Reduzir para médio risco",
                     3: "Manter estado atual"}

    print("=" * 50)
    print(f"  RELATÓRIO DE SAÚDE — {nome.upper()}")
    print("=" * 50)
    print(f"  Data da análise   : {hoje.strftime('%d/%m/%Y')}")
    print(f"  Data de reavaliação: {reavaliacao.strftime('%d/%m/%Y')}")
    print("-" * 50)
    print(f"  IMC               : {imc:.2f} ({class_imc})")
    print(f"  Pressão           : {sistolica}/{diastolica} mmHg ({class_pressao})")
    print(f"  Risco atual       : {risco_atual:.2f}")
    print("-" * 50)
    print("  Cenários simulados:")
    print(f"    Melhoria        : {lista_riscos[0]:.2f}")
    print(f"    Estabilidade    : {lista_riscos[1]:.2f}")
    print(f"    Piora           : {lista_riscos[2]:.2f}")
    print("-" * 50)
    print(f"  Média             : {media:.2f}")
    print(f"  Mediana           : {mediana:.2f}")
    print(f"  Desvio padrão     : {desvio:.2f}")
    print(f"  Classificação     : {class_risco}")
    print("-" * 50)
    print(f"  Objetivo          : {objetivos_str.get(objetivo, '?')}")
    print(f"  Objetivo atingido : {'✔ Sim' if objetivo_ok else '✘ Não'}")
    print(f"  Melhor cenário    : {melhor:.2f}")
    print(f"  Pior cenário      : {pior:.2f}")
    print("=" * 50)

# ─────────────────────────────────────────
# 12. Estatísticas Gerais da Clínica
# ─────────────────────────────────────────
def gerar_estatisticas_gerais(pacientes):
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    riscos = []
    for p in pacientes:
        nome, idade, peso, altura, sistolica, diastolica, atividade, alcool, objetivo = p
        imc   = calcular_imc(peso, altura)
        risco = calcular_risco(imc, sistolica, atividade, alcool)
        riscos.append((nome, risco))

    media_geral  = round(sum(r for _, r in riscos) / len(riscos), 2)
    maior        = max(riscos, key=lambda x: x[1])
    menor        = min(riscos, key=lambda x: x[1])

    baixo = sum(1 for _, r in riscos if r < 5)
    medio = sum(1 for _, r in riscos if 5 <= r <= 8)
    alto  = sum(1 for _, r in riscos if r > 8)

    print("\n" + "=" * 50)
    print("  ESTATÍSTICAS GERAIS DA CLÍNICA")
    print("=" * 50)
    print(f"  Total de pacientes   : {len(pacientes)}")
    print(f"  Média geral de risco : {media_geral:.2f}")
    print(f"  Maior risco          : {maior[0]} ({maior[1]:.2f})")
    print(f"  Menor risco          : {menor[0]} ({menor[1]:.2f})")
    print(f"  Baixo risco          : {baixo} paciente(s)")
    print(f"  Médio risco          : {medio} paciente(s)")
    print(f"  Alto risco           : {alto} paciente(s)")
    print("=" * 50)
