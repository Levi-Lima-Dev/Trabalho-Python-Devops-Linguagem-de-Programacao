# ==============================================================================
# 1. DEFINIÇÃO DAS FUNÇÕES
# O código está modularizado em funções para facilitar a reutilização e organização.
# ==============================================================================

def adicionar_notas():
    """
    Função para coletar as notas do aluno usando uma Estrutura de Repetição.
    """
    notas = []  # Armazena as notas em uma lista
    print("\n--- CADASTRO DE NOTAS ---")
    print("Digite as notas (ex: 8.5) e 'FIM' para finalizar a inserção.")

    # Estrutura de Repetição (Loop while) para entrada de dados
    while True:
        entrada = input("Nota: ").strip().lower()

        if entrada == 'fim':
            break  # Sai do loop

        try:
            nota = float(entrada)
            # Verifica se a nota está em um intervalo válido (opcional, mas boa prática)
            if 0.0 <= nota <= 10.0:
                 notas.append(nota)
            else:
                print("Nota fora do intervalo (0 a 10). Tente novamente.")
        except ValueError:
            # Captura erro se o usuário digitar texto inválido
            print("Entrada inválida. Por favor, digite um número ou 'FIM'.")

    return notas


def calcular_media(lista_notas):
    """
    Função para calcular a média aritmética das notas.
    """
    # Evita erro de divisão por zero caso a lista esteja vazia
    if not lista_notas:
        return 0.0

    soma = sum(lista_notas) # Soma todos os elementos da lista
    quantidade = len(lista_notas) # Conta a quantidade de elementos
    media = soma / quantidade

    return media


def determinar_situacao(media):
    """
    Função que usa Estrutura Condicional (if/else) para definir a situação do aluno.
    """
    NOTA_MINIMA_APROVACAO = 7.0

    # Estrutura Condicional
    if media >= NOTA_MINIMA_APROVACAO:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    return situacao


def exibir_relatorio(notas, media, situacao):
    """
    Função que exibe o relatório final formatado.
    """
    print("\n" + "="*40)
    print("        RELATÓRIO DE NOTAS DO ALUNO")
    print("="*40)

    print(f"Notas Inseridas: {notas}")
    # Formata a média com duas casas decimais
    print(f"Média Final: {media:.2f}")

    # Exibe a situação com destaque visual
    if situacao == "APROVADO":
        print(f"Situação: {situacao} ")
    else:
        print(f"Situação: {situacao} ")

    print("="*40)

# ==============================================================================
# 2. FLUXO PRINCIPAL DO SISTEMA
# ==============================================================================

def iniciar_sistema_notas():
    """
    Função que coordena a execução de todo o sistema.
    """

    # 1. Coletar Notas (Usa Repetição)
    notas_do_aluno = adicionar_notas()

    if not notas_do_aluno:
        print("\n--- Nenhuma nota inserida. O relatório não foi gerado. ---")
        return

    # 2. Calcular Média (Usa Função)
    media_final = calcular_media(notas_do_aluno)

    # 3. Determinar Situação (Usa Condicional)
    situacao_final = determinar_situacao(media_final)

    # 4. Exibir Relatório
    exibir_relatorio(notas_do_aluno, media_final, situacao_final)

# INICIA A EXECUÇÃO DO SISTEMA
iniciar_sistema_notas()