from conexao_banco import ConexaoBanco
from modelos import Motorista, Passageiro
from repositorios import MotoristaRepositorio, PassageiroRepositorio


def run():
    # 1. Garante que as tabelas existem
    ConexaoBanco.inicializar_banco()

    # 2. Instancia os repositórios (sem precisar passar nada nos parênteses)
    repo_motorista = MotoristaRepositorio()
    repo_passageiro = PassageiroRepositorio()

    # 3. Cria os objetos de negócio em memória
    motorista_ok = Motorista(nome="Carlos Silva", carteira_bloqueada=False)
    passageiro_devedor = Passageiro(nome="Ana Lima", saldo_devedor=45.50)

    # 4. Exibe a verificação na tela
    print(f"Motorista {motorista_ok.nome} está apto? {motorista_ok.esta_apto()}")
    print(f"Passageira {passageiro_devedor.nome} está apta? {passageiro_devedor.esta_apto()}")

    # 5. Salva persistentemente no banco de dados
    repo_motorista.salvar(motorista_ok)
    repo_passageiro.salvar(passageiro_devedor)


if __name__ == "__main__":
    run()