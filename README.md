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
## Requisítos
- Conta [Telegram](https://my.telegram.org/) para gerar as credenciais.
- Credenciais necessárias ...

--- 
## Container
Para executar o bot em um container, basta executar os seguintes comandos:

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

