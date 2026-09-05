import os

# config.py

# Em produção esses dados vem de variáveis de ambiente, mas para fins de teste, vamos definir valores padrão aqui.
DB_NAME = os.getenv("DB_NAME", "sistema_frota.db")