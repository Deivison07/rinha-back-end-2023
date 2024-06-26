CREATE EXTENSION IF NOT EXISTS "uuid-ossp";  
CREATE EXTENSION IF NOT EXISTS PG_TRGM;

CREATE TABLE IF NOT EXISTS PESSOAS (
    ID uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    APELIDO VARCHAR(32) Unique,
    NOME VARCHAR(100)  NOT NULL,
    NASCIMENTO date  NOT NULL,
    STACK json,
    BUSCA_TRGM TEXT GENERATED ALWAYS AS (
        NOME || APELIDO || COALESCE(STACK::text, '')
    ) STORED
);


-- Editado
-- https://github.com/viniciusfonseca/rinha-backend-rust/blob/master/init.sql