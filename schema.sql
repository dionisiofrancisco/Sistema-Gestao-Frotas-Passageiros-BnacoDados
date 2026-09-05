--schema.sql (Criação das tabelas do banco de dados)

CREATE TABLE IF NOT EXISTS motoristas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    carteira_bloqueada INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS passageiros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    saldo_devedor REAL NOT NULL

);