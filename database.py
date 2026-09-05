
#database.py

import sqlite3

from config import DB_NAME

class DatabaseMagager:
    """Gerencia a conexão com o banco de dados SQLite."""
    @staticmethod
    def get_connection() -> sqlite3.Connection:
        """Estabelece e retorna uma conexão com o banco de dados."""
        try:
            conexao = sqlite3.connect(DB_NAME)
            return conexao
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None