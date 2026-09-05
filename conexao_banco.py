import sqlite3

# Nome do arquivo de banco de dados
NOME_BANCO = "sistema_frota.db"


class ConexaoBanco:
    """
    Classe de infraestrutura responsável EXCLUSIVAMENTE por abrir conexões
    e inicializar a estrutura de tabelas no banco de dados.
    """

    @staticmethod
    def obter_conexao() -> sqlite3.Connection:
        """
        Método Estático: Não precisa de 'self' ou de instanciar a classe.
        Abre e retorna um canal de comunicação direta com o banco.
        """
        return sqlite3.connect(NOME_BANCO)

    @classmethod
    def inicializar_banco(cls) -> None:
        """
        Lê a estrutura SQL e garante que as tabelas necessárias existam.
        """
        with cls.obter_conexao() as conexao:
            cursor = conexao.cursor()

            # Tabela de Motoristas
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS motoristas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                carteira_bloqueada INTEGER NOT NULL
            );
            """)

            # Tabela de Passageiros
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS passageiros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                saldo_devedor REAL NOT NULL
            );
            """)

            # Confirma a criação das tabelas no arquivo .db
            conexao.commit()
            print("⚡ Banco de dados e tabelas inicializados com sucesso!")