CREATE INDEX CONCURRENTLY IF NOT EXISTS IDX_PESSOAS_BUSCA_TGRM ON PESSOAS USING GIST (BUSCA_TRGM GIST_TRGM_OPS(SIGLEN=64));