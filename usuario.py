from database import ler_dados, escrever_dados

def criar_usuario(lista_de_usuarios):
    if not (lista_de_usuarios):
        print("Você ainda não tem uma conta. Vamos criar uma! \n")
        nomeUsuario = input("Crie seu nome de usuário: \n")
        dataNascimento = input("Digite sua data de nascimento: \n")
        senhaUsuario = input("Crie uma senha: \n")

        id_usuario = len(lista_de_usuarios) + 1

        usuario = {
            "id": id_usuario,
            "nome": nomeUsuario,
            "nascimento": dataNascimento,
            "senha": senhaUsuario
        }

        lista_de_usuarios.append(usuario)
        escrever_dados(lista_de_usuarios, "usuario")

def mostrar_meus_dados (usuario):
    print("-------SEUS DADOS---------\n")
    print(f"Nome: {usuario['nome']}")
    print(f"Data de nascimento: {usuario['nascimento']}")

    opcao = input("Deseja ver sua senha? S/N \n")
    if opcao.lower() == 's':
        print(usuario["senha"])
        
    else:
        print("Ok. Vamos proseguir então.")

def login_usuario(lista):
    nome = input("Digite seu nome: \n")
    senha = input("Digite sua senha: \n")

    for usuario in lista:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            print("Login bem-sucedido :D")
            print("Bem-vindo", usuario["nome"]) 
            return
    print("Usuário ou senha incorretos. ")
    
    lista_de_usuarios = ler_dados("usuario")

    nomeUsuario = input("Digite o nome do usuário: \n")

def excluir_usuario (lista):
    nome = input("Digite seu nome: \n")
    senha = input("Digite sua senha: \n")

    for usuario in lista:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            lista.remove(usuario)
            escrever_dados(lista, "usuario")
            print("Conta excluída com sucesso!")

def alterar_usuario(lista):

    nome= input("Digite seu nome: \n")
    senha = input("Digite sua senha: \n")

    for usuario in lista:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            print("O que deseja alterar? \n")
            print("1 - NOME DE USUÁRIO: ")
            print("2- Senha")
            print("Data de nascimento:")
            opcao = int(input("Digite a opção desejada: \n"))

            if opcao == 1:
                novoNome = input("Qual será seu novo nome de usuário? \n")
                usuario["nome"] = novoNome
                escrever_dados(lista, "usuario")
            elif opcao == 2:
                novaSenha = input("Qual será sua nova senha? \n")
                usuario["senha"] = novaSenha

                escrever_dados(lista, "usuario")
            elif opcao == 3:
                novaDNascimento = input("Qual sua data de nascimento? \n")

                usuario["nascimento"] = novaDNascimento

            escrever_dados(lista, "usuario")
            return
    print("Usuário ou senha incorretos. ")
    
def menu():
    lista_de_usuarios = ler_dados("usuario")

    print("--------MENU--------")
    print("1- Criar uma conta \n")
    print("2- Entrar numa conta \n")
    print("3- Excluir uma conta \n")
    print("4- Alterar dados de uma conta \n")
    opcao = int(input("O que você deseja fazer? \n"))
    
    
    if opcao == 1:
        criar_usuario (lista_de_usuarios)
    elif opcao == 2:
        login_usuario (lista_de_usuarios)
    elif opcao == 3:
        excluir_usuario (lista_de_usuarios)
    elif opcao == 4:
        alterar_usuario (lista_de_usuarios)
    else:
        print("opção inválida!")