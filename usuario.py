import sqlite3

def criar_usuario():
        print("Você ainda não tem uma conta. Vamos criar uma! \n")
        nomeUsuario = input("Crie seu nome de usuário: \n")
        dataNascimento = input("Digite sua data de nascimento: \n")
        senhaUsuario = input("Crie uma senha: \n")

        conn = sqlite3.connect("denuncias.db")
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
             INSERT INTO usuarios (nome_usuario, data_nascimento, senha) VALUES (?, ?, ?)""", (nomeUsuario, dataNascimento, senhaUsuario))
            
            conn.commit()
            print("USUÁRIO CADASTRADO COM SUCESSO!\n\n\n\n\n")
            
        except sqlite3.IntegrityError:
            print("Erro: Nome de usuário já cadastrado. ")
        finally:
            conn.close()
        menu()
        

def mostrar_meus_dados (usuario):
    print("-------SEUS DADOS---------\n")
    print(f"Nome: {usuario[1]}")
    print(f"Data de nascimento: {usuario[2]}")

    opcao = input("Deseja ver sua senha? S/N \n")
    if opcao.lower() == 's':
        conn = sqlite3.connect("denuncias.db")
        cursor = conn.cursor()
        cursor.execute("SELECT senha FROM usuarios WHERE id=?", (usuario[0],))
        senha = cursor.fetchone()[0]
        print(senha)
        conn.close()
        
    else:
        print("Ok. Vamos proseguir então.")

def login_usuario():
    nome = input("Digite seu nome: \n")
    senha = input("Digite sua senha: \n")

    conn = sqlite3.connect("denuncias.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, nome_usuario, data_nascimento FROM usuarios WHERE nome_usuario=? AND senha=?""", (nome, senha))
    
    usuario = cursor.fetchone()
    
    conn.close()
    
    if usuario:
        print("Login bem-sucedido :D")
        print("Bem-vindo", usuario[1])
        
        while True:
            print("O que você deseja fazer? \n")
            print("1- Ver meus dados")
            print("2- Alterar meus dados")
            print("3- Excluir uma conta")
            print("4- Sair")
            opcao = input("Escolhar uma opção: \n")
            
            if opcao == '1':
                mostrar_meus_dados(usuario)
            elif opcao == '2':
                alterar_usuario()
            elif opcao == '3':
                excluir_usuario()
            elif opcao == '4':
                menu()
            else:
                print("Opção inválida")
    else:
     print("Usuário ou senha incorreto. ")
     menu()

def excluir_usuario ():
    nome = input("Digite seu nome: \n")
    senha = input("Digite sua senha: \n")

    conn = sqlite3.connect("denuncias.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM usuarios WHERE nome_usuario=? AND senha=?
                   """, (nome, senha))
    conn.commit()
    
    if cursor.rowcount == 0:
        print("Usuário ou senha incorretos.")
    else:
        print("Conta excluída com sucesso!")
    conn.close()
    
def alterar_usuario():

    nome= input("Digite seu nome: \n")
    senha = input("Digite sua senha: \n")

    conn = sqlite3.connect("denuncias.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM usuarios WHERE nome_usuario=? AND senha=?""", (nome, senha))
    usuario = cursor.fetchone()
   
    if usuario:
        print("O que deseja alterar? \n")
        print("1- Nome de usuário")
        print("2- Senha")
        print("3- Data de nascimento")
        opcao = input("Digite a opção desejada: \n")
        
        if opcao == '1':
            novoNome = input("Qual será seu novo nome de usuário? \n")
            cursor.execute("UPDATE usuarios SET senha=? WHERE id=?", (novoNome, usuario[0]))
            print("Nome de usuário alterado com sucesso")
        elif opcao == '2':
            novaSenha = input("Qual será sua nova senha? \n")
            cursor.execute("UPDATE usuarios SET senha=? WHERE id=?", (novaSenha, usuario[0]))
            print("Senha alterada com sucesso!")
        elif opcao == '3':
            novaData = input("Qual será sua nova data de nascimento? \n")
            cursor.execute("UPDATE usuarios SET senha=? WHERE id=?", (novaData, usuario[0]))
            conn.commit()
            print("Data de nascimento alterada com sucesso!")
    
def menu():

    print("--------MENU--------")
    print("1- Criar uma conta \n")
    print("2- Entrar numa conta \n")
    opcao = input("O que você deseja fazer? \n")
    
    
    if opcao == '1':
        criar_usuario()
    elif opcao == '2':
        login_usuario()
    else:
        print("\nopção inválida!\n")
    menu()