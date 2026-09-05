from conexao_banco import ConexaoBanco
from modelos import Motorista, Passageiro


class MotoristaRepositorio:

    def salvar(self, motorista: Motorista) -> None:
        """Salva um motorista no banco usando o método estático ConexaoBanco.obter_conexao()"""
        with ConexaoBanco.obter_conexao() as conexao:
            cursor = conexao.cursor()

            # Converte a regra de negócio (True/False) em número (0/1) para o SQLite
            status_bloqueio = 1 if not motorista.esta_apto() else 0

            cursor.execute(
                "INSERT INTO motoristas (nome, carteira_bloqueada) VALUES (?, ?);",
                (motorista.nome, status_bloqueio),
            )
            conexao.commit()
            print(f"💾 Motorista '{motorista.nome}' salvo no banco de dados!")


class PassageiroRepositorio:

    def salvar(self, passageiro: Passageiro) -> None:
        """Salva um passageiro no banco usando o método estático ConexaoBanco.obter_conexao()"""
        with ConexaoBanco.obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute(
                "INSERT INTO passageiros (nome, saldo_devedor) VALUES (?, ?);",
                (passageiro.nome, passageiro.obter_saldo_devedor()),
            )
            conexao.commit()
            print(f"💾 Passageiro '{passageiro.nome}' salvo no banco de dados!")