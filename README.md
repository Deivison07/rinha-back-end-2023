# Projeto [Rinha de Backend 2023](https://github.com/zanfranceschi/rinha-de-backend-2023-q3) feito em python 
### Para mais informações acesse as [instruções](https://github.com/zanfranceschi/rinha-de-backend-2023-q3/blob/main/INSTRUCOES.md)
## Tecnologias usadas: 
  - Flask (framework python)
  - Pydantic (serialização e desserialização)
  - Postgres (banco de dados relacional)
  - Nginx (balanceador de carga)
  - sqlalchemy (ORM para integração com banco de dados)

## fluxo de trabalho
```mermaid
flowchart TD
    G(Stress Test - Gatling) -.-> LB(Load Balancer - Nginx)
      subgraph -
        LB -.-> App1(API-Flask- instância 01)
        LB -.-> App2(API-Flask - instância 02)
        App1 -.-> Db[(Postgres)]
        App2 -.-> Db[(Postgres)]
    end
```


