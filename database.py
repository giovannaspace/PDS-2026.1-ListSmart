import sqlite3 

######################## Parte do Banco de Dados ######################################
def bancoDados():
    
    conexao = psycopg2.connect(os.environ.get("DATABASE_URL"))
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(
                    idUsuario TEXT NOT NULL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL
                    )""")
    conexao.commit()
  
    cursor.execute("""CREATE TABLE IF NOT EXISTS listas(
                    idLista TEXT NOT NULL PRIMARY KEY,
                    nomeLista TEXT NOT NULL,
                    tetoOrcamentario REAL,
                    observacoes TEXT,
                    dataLista TEXT NOT NULL,
                    idDono TEXT NOT NULL
                    )""")
    conexao.commit()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS itens(
                    idItem TEXT NOT NULL PRIMARY KEY,
                    nomeItem TEXT NOT NULL,
                    quantidade INTEGER NOT NULL,
                    unidade TEXT,
                    precoUnitario REAL NOT NULL,
                    desconto REAL,
                    statusCompra INTEGER NOT NULL,
                    idDonoItem TEXT NOT NULL, 
                    observacoesItem TEXT,
                    idCategoria TEXT
                    )""")
    conexao.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS categorias(
                        nomeCategoria TEXT NOT NULL PRIMARY KEY
                    )""")
    conexao.commit()

    conexao.close()


if __name__ == "__main__":    
    bancoDados()

