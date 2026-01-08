# Bot Telegram

Este é um projeto de **bot para o Telegram** desenvolvido em **Python**.  

O objetivo deste projeto é servir como base de estudo para desenvolvimento de bots no Telegram, oferecendo uma estrutura inicial que pode ser facilmente expandida e aprimorada com novas funcionalidades.

---

## Tecnologias utilizadas
- Python **3.9+**
- [Pyrogram](https://docs.pyrogram.org/) biblioteca utilizada para gerar o cliente do Telegram.
- [TgCrypto](https://pypi.org/project/TgCrypto/) para melhor performance.
- [Pytest](https://docs.pytest.org/en/stable/) biblioteca de testes para garantir o funcionamento esperado do bot.
---
## Credenciais
Para gerar as credenciais, é necessário ter uma conta [telegram](https://my.telegram.org/). Para gerar o **bot_name** e o **bot_token** será necessário iniciar uma conversa com o @BotFather no Telegram e enviar o comando `/newbot`.
O BotFather irá pedir o nome desejado para o bot (exibido) e um username (terminado em bot, exemplo: meu_bot). Para obter a **api_id** e a **api_hash** será necessário acessar o site do [telegram](my.telegram.org), fazer login com o número de telefone vinculado à sua conta do Telegram.
Após, abrir a API Development Tools e criar um novo aplicativo preenchendo os dados obrigatórios. Ao terminar, terá acesso as credenciais.

- Credenciais necessárias:
  - bot_name
  - bot_token
  - api_id
  - api_hash
--- 
## Container
Para executar o bot em um container, é necessário ter o docker instalado e executar os seguintes comandos dentro do diretório do projeto.
- Construção do container:
```bash
  docker build -t bot_telegram:V0.1 .
```
- Rodar o container:
```bash
  docker run --name bot_telegram1 -d bot_telegram:V0.1
```
- Ou apenas um comando utilizando o docker compose:
```bash
  docker compose up --build -d
```
---

*Nota: Este README será atualizado para refletir as mudanças e melhorias.*

