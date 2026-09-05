# 🚘 Sistema de Gestão de Frota e Passageiros

> Sistema corporativo modular desenvolvido em Python e SQLite com foco em Arquitetura Orientada a Objetos (POO), Separação de Responsabilidades (SOLID) e Persistência Segura de Dados.

---

## 📐 Arquitetura do Software

O projeto adota uma **Arquitetura em Camadas (Layered Architecture)** para garantir manutenibilidade, testabilidade e isolamento de responsabilidades:

```text
sistema-gestao-frotas-passageiros/
│
├── conexao_banco.py    # [Infraestrutura] Conexões SQLite e inicialização de tabelas
├── modelos.py          # [Domínio / POO] Entidades de Negócio (Abstração, Herança, Encapsulamento)
├── repositorios.py     # [Persistência] Padrão Repository para operações SQL (CRUD)
└── main.py             # [Orquestração] Ponto de entrada e fluxo da aplicação
