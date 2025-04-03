def exercicio1():
    print("\n--- Exercício 1: Pilha Simples ---")
    pilha = []

    pilha.append(5)
    pilha.append(10)
    pilha.append(15)

    print("Pilha após empilhamento:", pilha)

    print("Topo da pilha:", pilha[-1])

    pilha.pop()
    print("Pilha após desempilhamento:", pilha)
    print("Novo topo da pilha:", pilha[-1])

    print("A pilha está vazia?", len(pilha) == 0)
    print("Resultado da Pilha ", pilha)

def exercicio2():
    print("\n--- Exercício 2: Manipulação de Pilha ---")
    pilha = []

    pilha.append(7)
    pilha.append(14)
    pilha.append(21)

    print("Pilha após empilhamento:", pilha)

    print("Topo da pilha:", pilha[-1])

    pilha.pop()
    print("Pilha após desempilhamento:", pilha)
    print("Novo topo da pilha:", pilha[-1])

    pilha.pop()
    pilha.pop()

    print("A pilha está vazia?", len(pilha) == 0)
    print("Resultado da Pilha ", pilha)


def exercicio3():
    print("\n--- Exercício 3: Desfazer/Refazer Editor de Texto ---")
    acoes = []
    acoes_desfeitas = []
    documento = []

    while True:
        print("\nDocumento atual:", " ".join(documento))
        print("1 - Adicionar palavra")
        print("2 - Desfazer")
        print("3 - Refazer")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            palavra = input("Digite uma palavra para adicionar: ")
            documento.append(palavra)
            acoes.append(("adicionar", palavra))
            acoes_desfeitas = []

        elif opcao == "2":
            if acoes:
                acao = acoes.pop()
                if acao[0] == "adicionar":
                    palavra = documento.pop()
                    acoes_desfeitas.append(acao)
                    print(f"Desfeito: removida a palavra '{palavra}'")
            else:
                print("Não há ações para desfazer")

        elif opcao == "3":
            if acoes_desfeitas:
                acao = acoes_desfeitas.pop()
                if acao[0] == "adicionar":
                    documento.append(acao[1])
                    acoes.append(acao)
                    print(f"Refeito: adicionada a palavra '{acao[1]}'")
            else:
                print("Não há ações para refazer")

        elif opcao == "4":
            break

        else:
            print("Opção inválida!")

def exercicio4():
    print("\n--- Exercício 4: Fila Simples ---")
    fila = []

    fila.append(3)
    fila.append(6)
    fila.append(9)

    print("Primeiro elemento da fila:", fila[0])

    fila.pop(0)
    print("Novo primeiro elemento da fila:", fila[0])

    fila.pop(0)

    print("A fila está vazia?", len(fila) == 0)

def exercicio5():
    print("\n--- Exercício 5: Consultório Odontológico ---")
    fila_pacientes = []

    while True:
        print("\n1 - Adicionar paciente à fila")
        print("2 - Chamar próximo paciente")
        print("3 - Visualizar fila")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do paciente: ")
            fila_pacientes.append(nome)
            print(f"Paciente {nome} adicionado à fila. Posição: {len(fila_pacientes)}")

        elif opcao == "2":
            if fila_pacientes:
                paciente = fila_pacientes.pop(0)
                print(f"Chamando paciente: {paciente}")
                if fila_pacientes:
                    print(f"Próximo paciente: {fila_pacientes[0]}")
                else:
                    print("Não há mais pacientes na fila")
            else:
                print("Não há pacientes na fila")

        elif opcao == "3":
            if fila_pacientes:
                print("Fila atual:")
                for i, paciente in enumerate(fila_pacientes, 1):
                    print(f"{i}. {paciente}")
            else:
                print("A fila está vazia")

        elif opcao == "4":
            break

        else:
            print("Opção inválida!")

def exercicio6():
    print("\n--- Exercício 6: Fila de Impressão ---")
    fila_impressao = []

    fila_impressao.append("relatorio.pdf")
    fila_impressao.append("apresentacao.pptx")
    fila_impressao.append("contrato.docx")

    print("Fila de impressão:", fila_impressao)

    print("Próximo documento a ser impresso:", fila_impressao[0])

    documento_impresso = fila_impressao.pop(0)
    print(f"Imprimindo: {documento_impresso}")

    print("Próximo documento a ser impresso:", fila_impressao[0])

    print("Ainda há documentos na fila?", len(fila_impressao) > 0)
    print("Documentos restantes:", len(fila_impressao))

def exercicio7():
    print("\n--- Exercício 7: Central de Atendimento ---")
    pilha_chamadas = []

    pilha_chamadas.append(101)
    pilha_chamadas.append(102)
    pilha_chamadas.append(103)

    print("Pilha de chamadas:", pilha_chamadas)

    print("Próxima chamada a ser atendida:", pilha_chamadas[-1])

    chamada_atendida = pilha_chamadas.pop()
    print(f"Atendendo chamada: {chamada_atendida}")

    if pilha_chamadas:
        print("Nova chamada no topo:", pilha_chamadas[-1])
    else:
        print("Não há mais chamadas na pilha")

    print("Ainda há chamadas na pilha?", len(pilha_chamadas) > 0)
    print("Chamadas restantes:", len(pilha_chamadas))

def exercicio8():
    print("\n--- Exercício 8: Histórico de Navegação ---")
    historico = []
    paginas_avancadas = []

    paginas = ["google.com", "wikipedia.org", "python.org"]
    for pagina in paginas:
        historico.append(pagina)
        print(f"Acessando: {pagina}")

    print("\nÚltima página visitada:", historico[-1])

    pagina_atual = historico.pop()
    paginas_avancadas.append(pagina_atual)
    print(f"\nVoltando da página: {pagina_atual}")

    print("Página atual após voltar:", historico[-1])

    if paginas_avancadas:
        pagina_avancada = paginas_avancadas.pop()
        historico.append(pagina_avancada)
        print(f"\nAvançando para: {pagina_avancada}")
        print("Página atual após avançar:", historico[-1])

def main():
    while True:
        print("\n==== MENU DE EXERCÍCIOS ====")
        print("1 - Exercício 1: Pilha Simples")
        print("2 - Exercício 2: Manipulação de Pilha")
        print("3 - Exercício 3: Desfazer/Refazer Editor de Texto")
        print("4 - Exercício 4: Fila Simples")
        print("5 - Exercício 5: Consultório Odontológico")
        print("6 - Exercício 6: Fila de Impressão")
        print("7 - Exercício 7: Central de Atendimento")
        print("8 - Exercício 8: Histórico de Navegação")
        print("0 - Sair")

        opcao = input("\nEscolha um exercício para executar: ")

        if opcao == "1":
            exercicio1()
        elif opcao == "2":
            exercicio2()
        elif opcao == "3":
            exercicio3()
        elif opcao == "4":
            exercicio4()
        elif opcao == "5":
            exercicio5()
        elif opcao == "6":
            exercicio6()
        elif opcao == "7":
            exercicio7()
        elif opcao == "8":
            exercicio8()
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida! Por favor, escolha um número entre 0 e 8.")

main()
