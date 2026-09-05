from conexao_banco import ConexaoBanco
from modelos import Motorista, Passageiro

class MotoristaRepositorio:
    """Classe responsável EXCLUSIVAMENTE pelas operações de banco do Motorista."""
    
    def __init__(self, gerenciador_banco: ConexaoBanco):
        self.gerenciador_banco = gerenciador_banco

    def salvar(self, motorista: Motorista) -> None:
        """Salva um objeto Motorista dentro da tabela 'motoristas'."""
        status_bloqueio = 1 if not motorista.esta_apto() else 0
        
        with self.gerenciador_banco.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO motoristas (nome, carteira_bloqueada) VALUES (?, ?);",
                (motorista.nome, status_bloqueio)
            )
            conexao.commit()
            print(f"💾 Motorista '{motorista.nome}' salvo no banco de dados!")


class PassageiroRepositorio:
    """Classe responsável EXCLUSIVAMENTE pelas operações de banco do Passageiro."""
    
    def __init__(self, gerenciador_banco: ConexaoBanco):
        self.gerenciador_banco = gerenciador_banco

    def salvar(self, passageiro: Passageiro) -> None:
        """Salva um objeto Passageiro dentro da tabela 'passageiros'."""
        with self.gerenciador_banco.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO passageiros (nome, saldo_devedor) VALUES (?, ?);",
                (passageiro.nome, passageiro.obter_saldo_devedor())
            )
            conexao.commit()
            print(f"💾 Passageiro '{passageiro.nome}' salvo no banco de dados!")