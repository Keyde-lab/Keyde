# Jogo NIM com IA Minimax usando Árvore de Decisão
# ---------- Estrutura de Dados para o Ranking ----------
ranking = []

def ordenar_rank():
    # Ordena o ranking de forma decrescente pelas vitórias
    n = len(ranking)
    for i in range(n):
        for j in range(n - i - 1):
            if ranking[j]['vitorias'] < ranking[j + 1]['vitorias']:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

def mostrar_rank():
    print("\n--- RANKING ---")
    ordenar_rank()
    for p in ranking:
        print(f"{p['nome']}: {p['vitorias']} vitória(s)")

def registrar(nome):
    # Atualiza ou adiciona jogador ao ranking
    for p in ranking:
        if p['nome'] == nome:
            p['vitorias'] += 1
            return
    ranking.append({'nome': nome, 'vitorias': 1})

# ---------- Estrutura da Árvore Minimax ----------
class NoArvore:
    def __init__(self, palitos, maximizando, profundidade):
        self.palitos = palitos                # Estado atual (quantidade de palitos)
        self.maximizando = maximizando        # Se é turno da IA (True) ou jogador (False)
        self.profundidade = profundidade      # Profundidade restante de busca
        self.filhos = []                      # Lista de filhos (próximos estados possíveis)
        self.valor = None                     # Valor Minimax deste nó (a ser calculado)

    def gerar_filhos(self):
        # Cria os filhos (próximas jogadas possíveis)
        for i in [1, 2, 3]:
            novo_palitos = self.palitos - i
            if novo_palitos >= 0:
                filho = NoArvore(novo_palitos, not self.maximizando, self.profundidade - 1)
                self.filhos.append(filho)

# Função que calcula o valor Minimax de um nó
def calcular_minimax(no):
    # Caso base: jogo acabou ou profundidade limite
    if no.palitos == 0:
        no.valor = -1 if no.maximizando else 1
        return no.valor
    if no.profundidade == 0:
        no.valor = 0
        return no.valor

    # Gera os próximos movimentos possíveis
    no.gerar_filhos()

    # Se for a vez da IA → quer maximizar o valor
    if no.maximizando:
        no.valor = float('-inf')
        for filho in no.filhos:
            val = calcular_minimax(filho)
            no.valor = max(no.valor, val)
    else:
        # Se for a vez do jogador → IA assume que o humano vai tentar minimizar
        no.valor = float('inf')
        for filho in no.filhos:
            val = calcular_minimax(filho)
            no.valor = min(no.valor, val)

    return no.valor

# ---------- Jogada da IA usando a Árvore Minimax ----------
def jogada_ia(palitos, nivel):
    profs = {"facil": 1, "medio": 4, "dificil": 10}
    profundidade = profs[nivel]

    raiz = NoArvore(palitos, True, profundidade)
    raiz.gerar_filhos()
    melhor_valor = float('-inf')
    melhor_jogada = 1

    print("\n[IA está analisando as possibilidades...]")

    for filho in raiz.filhos:
        val = calcular_minimax(filho)
        jogada_feita = palitos - filho.palitos
        print(f"Se a IA tirar {jogada_feita} palito(s) → avaliação: {val}")
        if val > melhor_valor:
            melhor_valor = val
            melhor_jogada = jogada_feita

    print(f"A IA decidiu tirar {melhor_jogada} palito(s)\n")
    return melhor_jogada

# ---------- Jogada do Jogador Humano ----------
def jogada_humana(palitos):
    while True:
        try:
            n = int(input(f"Restam {palitos} palitos. Quantos quer tirar? (1, 2 ou 3): "))
            if n in [1, 2, 3] and n <= palitos:
                return n
            print("Número inválido! Tente de novo.")
        except ValueError:
            print("Digite apenas números!")

# ---------- Lógica Principal do Jogo ----------
def jogar():
    nome = input("Seu nome: ")
    nivel = input("Escolha dificuldade (facil / medio / dificil): ").lower()
    while nivel not in ["facil", "medio", "dificil"]:
        nivel = input("Opção inválida! Escolha: facil / medio / dificil: ").lower()

    palitos = 15
    turno = True  # True = jogador humano / False = IA

    print(f"\nJogo começou com {palitos} palitos. Quem tirar o último... PERDE!\n")

    while palitos > 0:
        if turno:
            tirar = jogada_humana(palitos)
            palitos -= tirar
            if palitos == 0:
                print("\nVocê tirou o último palito... Perdeu!")
                registrar("IA")
                break
        else:
            tirar = jogada_ia(palitos, nivel)
            palitos -= tirar
            print(f"A IA tirou {tirar} palito(s)")
            if palitos == 0:
                print("\nA IA tirou o último palito... Você venceu!")
                registrar(nome)
                break
        turno = not turno

    mostrar_rank()

# ---------- Loop para Jogar Várias Vezes ----------
if __name__ == "__main__":
    while True:
        jogar()
        novo = input("\nJogar novamente? (s/n): ").lower()
        if novo != 's':
            print("\nObrigado por jogar! Até mais :)")
            break
