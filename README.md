# Minerador de processos

## Instalar visualizador

`sudo npm install -g cubejs-cli`

## Configurar dados de conexão com base do projeto

`cd cube-js/minerador-processos`

`vim .env`

CUBEJS_DB_HOST=<host>
  
CUBEJS_DB_PORT=<port>
  
CUBEJS_DB_NAME=<db>
  
CUBEJS_DB_USER=<user>
  
CUBEJS_DB_PASS=<passord>
  
CUBEJS_WEB_SOCKETS=true

CUBEJS_DB_TYPE=postgres

## Instalar as dependências

`npm install`

## Iniciar API do cubejs

`npm run dev`

## Instalar analisador de processos

`cd cubejs/frontend/minerador-processos/`

`sudo npm install -g @angular/cli`

`npm install`

## Iniciar o analisador de processos

`ng serve`

## Avessar o analisador

http://localhost:4200
