Plaintext

meu_sistema_frota/
│
├── conexao_banco.py    # PROBLEMA: Como comunicar e gerenciar o Banco de Dados?
├── modelos.py          # PROBLEMA: Como representar os objetos do mundo real em memória?
├── repositorios.py     # PROBLEMA: Como salvar, buscar e atualizar dados no Banco?
└── main.py             # PROBLEMA: Como juntar tudo e executar o programa?


###---------------------------------Atualizão

meu_projeto/
│
├── config.py           # 1. Guarda apenas a URL e senhas do Banco
├── database.py         # 2. Conecta ao Banco (Driver de Conexão)
├── schema.sql          # 3. Arquivo puramente SQL com a estrutura das Tabelas
├── modelos.py          # 4. Regras das entidades (POO pura)
├── repositorios.py     # 5. Executa os comandos no banco
└── main.py             # 6. Ponto de entrada do sistema