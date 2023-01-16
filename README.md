API REST – BRASILPREV

Esse projeto foi desenvolvido utilizando as seguintes tecnologias: PYTHON,
DJANGO, DJANGO REST FRAMEWORK, SQLITE, DOCKER e DOCKER
COMPOSE.
O objetivo do projeto é uma API REST capaz de executar as seguintes ações:
• Cadastro de cliente
• Cadastro de produto
• Contratação de plano
• Resgate de plano
• Aporte extra

Seguindo as regras impostas pelo desafio da brasilprev.

EXECUÇÃO DO PROJETO
DOCKER:
Após descompactar o projeto, presumindo que o usuário já tenha o Docker e o
DOCKER COMPOSE instalados em sua máquina, dentro do diretório raiz do projeto
onde se encontra o arquivo “docker-compose.yml” digite os seguintes comandos:

1. docker-compose up -d
2. após a finalização da execução do docker compose, acessar a aplicação no seu
navegador (GOOGLE, BRAVE, FIREFOX, EDGE) pelo seu endereço IP
local, exemplo: “192.168.1.10”.
obs: para descobrir o seu endereço IP, no promp de comando ou terminal, você
dará o seguinte comando no seu terminal:
• WINDOWS – ipconfig
• LINUX – ifconfig


EXECUÇÃO MANUAL:
Caso o usuário não tenha o docker e o docker compose instalados em sua máquina, siga
os passos abaixo para uma execução do projeto alternativa.
Dentro do diretório raiz do projeto, onde se encontra o arquivo “manage.py” faça:

1. CRIE UMA VENV
• No terminal digite: python -m venv .venv
2. ATIVAR VENV
• WINDOWS - .venv\Scripts\activate.bat
• LINUX – source .venv/bin/activate
3. INTALANDO OS PACOTES DO PROJETO DENTRO DA VENV
• No terminal digite: pip install -r requirements.txt
4. ACESSANDO A APLICAÇÃO
• No terminal digite: python manage.py runserver
• No seu navegador acessa a aplicação pelo endereço IP:
“http://127.0.0.1:8000/”