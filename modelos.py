from abc import ABC, abstractmethod

class Usuario(ABC):
    """Classe base abstrata para todos os usuários do sistema."""
    
    def __init__(self, nome: str):
        self.nome = nome

    @abstractmethod
    def esta_apto(self) -> bool:
        """Cada classe filha decide a sua própria regra para estar apta."""
        pass


class Motorista(Usuario):
    """Representa um Motorista no sistema."""
    
    def __init__(self, nome: str, carteira_bloqueada: bool = False, id_motorista: int = None):
        super().__init__(nome=nome)
        self.id_motorista = id_motorista
        self._carteira_bloqueada = carteira_bloqueada

    def esta_apto(self) -> bool:
        """O motorista só pode dirigir se a carteira NÃO estiver bloqueada."""
        return not self._carteira_bloqueada


class Passageiro(Usuario):
    """Representa um Passageiro no sistema."""
    
    def __init__(self, nome: str, saldo_devedor: float = 0.0, id_passageiro: int = None):
        super().__init__(nome=nome)
        self.id_passageiro = id_passageiro
        self._saldo_devedor = saldo_devedor

    def esta_apto(self) -> bool:
        """O passageiro só pode pedir corrida se NÃO tiver dívidas."""
        return self._saldo_devedor <= 0.0

    def obter_saldo_devedor(self) -> float:
        return self._saldo_devedor