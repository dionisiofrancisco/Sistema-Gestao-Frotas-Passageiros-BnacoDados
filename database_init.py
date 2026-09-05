# database_init.py

# ler o aquivo SQL e executar os comandos para criar as tabelas no banco de dados

import sqlite3
from database import DatabaseMagager

def inicializador_banco():
    """"le o arquivo schema.sql e constroi a estrutura no banco de dados """
    try :
        # Estabelece a conexao com o banco de dados 
        conexao = DatabaseMagager.get_connection()
        if conexao is None:
            print("Falha ao conectar ao banco de dados. Inicialização abortada.")
            return

        # Lê o arquivo SQL
        with open("schema.sql", "r") as arquivo_sql:
            comandos_sql = arquivo_sql.read()
            conexao.executescript(comandos_sql)
            print("Banco de dados inicializado com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        if conexao:
            conexao.close()