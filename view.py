# importanto SQLite3
import sqlite3

# criando conexao
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizado com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados')

# tabela de cursos ---------------------------------------------

# criar cursos ( Create C )
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query, i)    

#criar_curso(['Python', '2 semanas', 50])        

# ver todos os cursos ( Read R ) 
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

print(ver_cursos())

# atualizar os  cursos ( Update U )
def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id="
        cur.execute(query, i) 

l = ['Python', '2 Semanas', 50.0, 1] 
#atualizar_curso(1)

# deletar os  cursos ( Delete D )
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cursos WHERE id=?"
        cur.execute(query, i) 

#deletar_curso([1])

# tabela de turmas ---------------------------------------------

# criar turmas
def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO turmas (nome, curso_nome, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, i)

# ver todas as turmas ( Read R ) 
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

