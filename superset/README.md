# Superset
## Instalação
`docker build . -t mineiros/superset:latest`
## Execução
```
docker run --net=host -d -p 8080:8080 --name superset mineiros/superset

docker exec -it superset superset fab create-admin \
               --username admin \
               --firstname Superset \
               --lastname Admin \
               --email admin@superset.com \
               --password admin

docker exec -it superset superset db upgrade

docker exec -it superset superset init
```

http://localhost:8080/login/ -- u/p: [admin/admin]