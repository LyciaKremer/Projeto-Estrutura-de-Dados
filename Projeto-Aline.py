from string import *

lquestao = []
lnivel = []
lmenu = []
lsalvar = [lquestao, lnivel, lmenu]
lprofessor = []
ldisciplina = []
cadastro_prof_disciplina = []
lalternativas = []

questao = 0
nivel = 0
lmenu = 0
professor = 0
disciplina = 0


def main():
    menu_principal()


def menu_professor():
    print("Menu Professor")
    print("    1 - Cadastrar Questão\n    "
          "2 - Remover Questão\n    "
          "3 - Minhas Questões\n    "
          "4 - Gerar exercício ou prova\n    "
          "5 - Acessar provas anteriores e gabaritos\n    "
          "6 - Avaliar questões de outros professores\n    "
          "0 - Sair")
    opcao = input("Digite a opção desejada: ")
    while opcao > '0':
        if opcao == '1':
            cadastrar_questao()
        elif opcao == '2':
            remover_questao()
        elif opcao == '3':
            listar_questoes()
        elif opcao == '4':
            gerar_provas()
        elif opcao == '5':
            provas_anteriores()
        elif opcao == '6':
            avaliar_provas()
        elif opcao == 0:
            pass
        else:
            print("Opção inválida")

        opcao = main()


def cadastrar_questao():
    questao = str(input("Digite o enunciado da questão: "))
    questao = questao.upper()
    if questao in lquestao:
        print("Questão já existente! Tente outra.")
    else:
        lquestao.append(questao)
        nivel = int(input("Digite o nivel de dificuldade da questão:\n    "
                          "1 - Fácil\n    "
                          "2 - Intermediário\n    "
                          "3 - Difícil\n>>> "))
        lnivel.append(lnivel)
        op = int(input("A questão será aberta ou fechada?\n    "
                       "1 - Aberta (questão subjetiva)\n    "
                       "2 - Fechada (questão objetiva)\n>>> "))
        if op == 2:
            quant = int(input("Quantas alternativas deseja adicionar?\n>>> "))
            for i in range(quant):
                alternativa = str(input("Digite a alternativa: "))
                lalternativas.append(alternativa)
                i + 1

        else:
            print("Questão cadastrada com sucesso!")


def remover_questao():
    questao = str(input("Digite a questão a ser excluída: "))
    questao = questao.upper()
    if questao in lquestao:
        lquestao.remove(questao)
        print("Questão removida")
    else:
        print("Essa questão não está cadastrada. Tente outra.")
        menu_professor()
    pass


def minhas_questoes():
    print("Questões salvas ", lquestao)
    pass


def gerar_provas():
    nome_prova = input('Digite o nome da prova: ')
    arquivo = open(nome_prova + ".txt", 'w+')

    arquivo.writelines('===================  Prova de ' + nome_prova + '  ===================\n')

    arquivo.write('{}\n'.format(lquestao[0]))
    arquivo.write('{}\n'.format(lquestao[1]))
    arquivo.write('{}\n'.format(lquestao[2]))
    arquivo.write('{}\n'.format(lquestao[3]))
    print('Prova criada com sucesso')
    arquivo.close()

def provas_anteriores():
    nome_prova = input("Digite o nome da prova desejada: ")
    arquivo = open ("C:/Users/lycia.kremer.ext/PycharmProjects/WorspacePython/" + nome_prova + ".txt", 'r')
    for linha in arquivo:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()
    pass


def avaliar_provas():
    print(listar_questoes())
    pergunta = str(input("Digite a questão a ser avaliada: "))
    pergunta = pergunta.upper()
    if pergunta in lquestao:
        per = str(input(
            "1 - Questão reprovada (muito fácil ou incorreta)\n    2 - Questão incompleta\n    3 - Questão aprovada\n"))
        print("A nota {} é {}".format(per, pergunta))
        if per == '1':
            print("Questão reprovada")
        else:
            print("Questão ")
    else:
        print("Essa questão não está cadastrada.")
        # menu()
    pass


# Parte do coordenador

def menu_coordenador():
    print('Menu Coordenador\n'
          '1 - Listar Questões\n'
          '2 - Listar disciplinas\n'
          '3 - Cadastrar disciplinas\n'
          '4 - Cadastrar professor à disciplina\n'
          '0 - Sair\n')
    op = input("Digite a opção desejada: ")

    # op = menu_principal()
    if op == '1':
        listar_questoes()
    elif op == '3':
        cadastrar_disciplina()
    elif op == '2':
        listar_disciplina()
    elif op == '4':
        cadastrar_professor()
    elif op == '0':
        pass
    else:
        while op >= '5':
            print("Opção inválida! Tente Novamente:")
            menu_coordenador()


def listar_questoes():
    print("Lista de questões: ", lquestao)
    pass

def listar_disciplina():
    print("Lista de disciplinas: ", ldisciplina)
    pass


def cadastrar_disciplina():
    disciplina = str(input("Digite a disciplina: "))
    disciplina = disciplina.upper()
    if disciplina in ldisciplina:
        print("Disciplina já cadastrada! Tente outra.")
    else:
        ldisciplina.append(disciplina)
        cadastro_prof_disciplina.append(disciplina)
        print("Disciplina cadastrada com sucesso!")


def cadastrar_professor():
    professor = str(input("Digite o nome professor: "))
    professor = professor.upper()
    if professor in cadastro_prof_disciplina:
        print("Professor já cadastrado nesta disciplina! Tente outro.")
    else:
        cadastro_prof_disciplina.append(professor)
        print('Professor cadastrado com sucesso!')


def menu_principal():
    while True:
        try:
            print("Menu")
            user = int(input("    1 - Professor\n    "
                             "2 - Coordenador\n    "
                             "3 - Coordenador Professor\n    "
                             "0 - Sair\n"
                             ">>>"))
            if not 0 <= user <= 4:
                raise ValueError("opção fora do range permitido")
        except ValueError as e:
            print("Valor inválido")
        else:
            pass
        if user == 0:
                print("Saída com sucesso!")
                break
        elif user == 1:
                menu_professor()
        elif user == 2:
                menu_coordenador()
        elif user >= 4:
            print("Opção Inválida! "
                    "Tente Novamente: ")
            menu_principal()
            while user >= 4:
                    print("Opção Inválida! "
                          "Tente Novamente: ")
                    menu_principal()

        elif user == 3:
            menu_professor_coordenador()
        else:
                print("Opção inválida!")
        pass


def menu_professor_coordenador():
    print("Menu Professor Coordenador")
    print("    1 - Cadastrar Questão\n    "
          "2 - Remover questão\n    "
          "3 - Minhas Questões\n    "
          "4 - Gerar exercício ou prova\n    "
          "5 - Acessar provas anteriores e gabaritos\n    "
          "6 - Avaliar questões de outros professores\n    "
          "7 - Listar Questões\n    "
          "8 - Cadastrar disciplinas\n    "
          "9 - Cadastrar professor à disciplina\n    "
          "0 - Sair\n>>> ")
    opcao = input("Digite a opção desejada: ")
    while opcao != '0':
        if opcao == '1':
            cadastrar_questao()
        elif opcao == '2':
            remover_questao()
        elif opcao == '3':
            listar_questoes()
        elif opcao == '4':
            gerar_provas()
        elif opcao == '5':
            provas_anteriores()
        elif opcao == '6':
            avaliar_provas()
        elif opcao == '7':
            listar_questoes()
        elif opcao == '8':
            cadastrar_disciplina()
        elif opcao == '9':
            cadastrar_professor()
        elif opcao >= '10':
            print("Opção inválida! Tente novamente.")
            menu_professor_coordenador()
        else:
            print("Opção inválida! Tente novamente.")
            menu_professor_coordenador()

        opcao = main()

main()
