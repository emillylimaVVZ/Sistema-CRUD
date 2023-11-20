import mysql.connector
from biblioteca import *


while True:
    menu=input(f"Bem vindo(a) ao menu de Cadastros.\n"
          f"1 para Alunos\n"
          f"2 para Modalidades\n"
          f"3 para Funcionários\n"
          f"4 para Personal\n"
          f"5 para Sair: ")

    if menu==1:
        while True:
            opcs = input(f"1 para Cadastrar\n"
                         "2 para Deletar\n"
                         "3 para Mostrar Alunos\n"
                         "4 para Retornar ao menu de Cadastros: ")

            if opcs == 1:
                alunos_cadastro()
            if opcs == 2:
                alunos_delete()
            if opcs == 3:
                alunos_delete()
            if opcs == 4:
                break

    if menu==2:

    if menu==3:

    if menu==4:

    if menu==5:
        print("Encerrando...")
        break