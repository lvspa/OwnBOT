# OwnSupervision

![Header](./theown.png)

O OwnSupervision é um bot moderador criado para auxiliar na gestão e na manutenção de comunidades no Reddit. Ele é projetado para automatizar tarefas de supervisão e garantir a conformidade com as diretrizes da comunidade.
Funcionalidades Principais:

    Supervisão de links: Remove links que não estão em uma lista permitida, bloqueando spam e conteúdo impróprio com base nas diretrizes do subreddit.
    Notificações: Informa os moderadores sobre atividades suspeitas ou contra as regras.
    Configurações Personalizáveis: Adapta-se às necessidades específicas de cada subreddit com opções de configuração flexíveis.

Tecnologias Utilizadas:

    Python: Linguagem de programação principal.
    PRAW (Python Reddit API Wrapper): Biblioteca para interação com a API do Reddit.
    OAuth: Autenticação segura para acesso à API do Reddit.

Instalação e Uso:

Para usar o OwnSupervision, siga estas etapas:

     ## Instalação e Uso

      1. Clone o repositório:
     ```bash
      git clone https://github.com/lvspa/OwnBOT.git
      cd OwnBOT
      
      2. Instale as dependências:
      pip install -r requirements.txt

      3. Crie um arquivo .env com suas credenciais do Reddit:
      REDDIT_CLIENT_ID=xxx
      REDDIT_CLIENT_SECRET=xxx
      REDDIT_USERNAME=seu_usuario
      REDDIT_PASSWORD=sua_senha
      REDDIT_USER_AGENT=OwnSupervisionBot
      WHITELIST=https://www.kabum.com.br/,https://www.amazon.com.br/

      4. Execute o bot:
      python bot.py



Contribuições são sempre bem vindas!
