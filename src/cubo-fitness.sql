CREATE TABLE minerador_processos.tb_fitness_vara
(
    nm_pessoa text COLLATE pg_catalog."default",
    nr_doc_principal_pessoa text COLLATE pg_catalog."default",
    nm_orgao text COLLATE pg_catalog."default",
    cd_orgao text COLLATE pg_catalog."default",
    nr_processos integer,
    vl_fitness numeric
);

ALTER TABLE minerador_processos.tb_fitness_vara
    OWNER to minerador_processos;


-- Para popular com dados de teste
select 
	'insert into minerador_processos.tb_fitness_vara (nm_orgao, cd_orgao, nm_pessoa, vl_fitness) values (' ||
    '''' || upper(nm_orgao) || ''',' ||
    '''' || cd_orgao || ''',' ||
    '''' || upper(nm_pessoa) || ''',' ||
    vl_fitness || ');'
from
    (
        select distinct nm_orgao, cd_orgao, nm_pessoa, random() as vl_fitness
        from minerador_processos.mv_maiores_litigantes_arquivados
    ) x;