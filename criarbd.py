# importando SQLite3
import sqlite3

# criando conexão
try:
    con = sqlite3.connect("cadastro_alunos.db")
    print("Conexão com o banco de dados realizado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

# Criando tabela de cursos
try:
    with con:
        cur = con.cursor()
        cur.execute(
            """ CREATE TABLE IF NOT EXISTS cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            duracao TEXT,
            preco reals
             
           )"""
        )
        print("Tabela Cursos criado com sucesso!")


except sqlite3.Error as e:
    print("Erro ao criar tabela cursos:", e)

# Criando tabela de turmas


try:
    with con:
        cur = con.cursor()
        cur.execute(
            """ CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            curso_nome TEXT,
            data_inicio DATE,
            FOREIGN KEY (curso_nome) REFERENCES curso (nome) ON UPDATE CASCADE ON DELETE CASCADE
                    
           )"""
    )
        print("Tabela Turmas criado com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar tabela turmas:", e)


# Criando tabela de alunos


try:
    with con:
        cur = con.cursor()
        cur.execute(
            """ CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            sexo TEXT,
            imagem TEXT,
            data_nascimento DATE,
            cpf TEXT,
            turma_nome TEXT,
            FOREIGN KEY (turma_nome) REFERENCES cturmas (nome) ON DELETE CASCADE
                    
        )"""
        )
        print("Tabela Alunos criado com sucesso!")

except sqlite3.Error as e:
    print("Erro ao criar tabela alunos:", e)
