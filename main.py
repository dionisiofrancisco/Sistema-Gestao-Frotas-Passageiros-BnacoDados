from conexao_banco import ConexaoBanco
from modelos import Motorista, Passageiro
from repositorios import MotoristaRepositorio, PassageiroRepositorio

def run():
    # 1. Configurar e preparar o banco de dados
    banco = ConexaoBanco()
    banco.inicializar_tabelas()

    # 2. Instanciar os Repositórios
    repo_motorista = MotoristaRepositorio(banco)
    repo_passageiro = PassageiroRepositorio(banco)

    # 3. Criar os Objetos de Negócio em Memória
    motorista_ok = Motorista(nome="Carlos Silva", carteira_bloqueada=False)
    passageiro_devedor = Passageiro(nome="Ana Lima", saldo_devedor=45.50)

    # 4. Validar as regras de negócio
    print(f"Motorista {motorista_ok.nome} está apto? {motorista_ok.esta_apto()}")
    print(f"Passageira {passageiro_devedor.nome} está apta? {passageiro_devedor.esta_apto()}")

    # 5. Salvar os dados persistentemente
    repo_motorista.salvar(motorista_ok)
    repo_passageiro.salvar(passageiro_devedor)

if __name__ == "__main__":
    run()