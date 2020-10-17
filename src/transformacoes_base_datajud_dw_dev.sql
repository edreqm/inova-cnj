-- ÍNDICES - não ajudaram muito (se quiserem sugerir algum outro índice)
create index IDX_PROCESSO_1 on TB_PROCESSO (nm_orgao, substr(nr_doc_principal_pessoa, 1, 8)); 
create index IDX_PROCESSO_2 on TB_PROCESSO (nr_processo);

-- maiores litigantes (pegar os 10 primeiros CNPJ, exceto o null
select substr(nr_doc_principal_pessoa, 1, 8), count(distinct nr_processo)
from tb_processo 
group by 
  substr(nr_doc_principal_pessoa, 1, 8) 
order by count(distinct nr_processo) desc

/*
-- TOP 10 CNPJ até o momento
33582750
00360305
60701190
33224254
04641376
60746948
33592510
06981180
02455233
17224742
*/

-- DADOS BASICOS MAIORES LITIGANTES
create table tb_proc_maiores_litigantes (
	nr_processo varchar(20),
	dt_ajuizamento date,
	nr_classe_processual integer,
	cd_orgao integer,
	nm_orgao varchar(500),
	cd_municipio_ibge integer,
	ds_grau varchar(2),
	sg_tribunal varchar(6),
	vl_causa float
)

-- POPULA DADOS BÁSICOS ML
insert into tb_proc_maiores_litigantes 
select 
	distinct substr(nr_processo, length(nr_processo) - 19, length(nr_processo)),
	dt_ajuizamento,
	nr_classe_processual,
	cd_orgao,
	nm_orgao,
	cd_municipio_ibge,
	ds_grau_orgao,
	sg_tribunal,
	vl_causa
from tb_processo tp where substr(nr_doc_principal_pessoa, 1, 8) in (
'33582750',
'00360305',
'60701190',
'33224254',
'04641376',
'60746948',
'33592510',
'06981180',
'02455233',
'17224742'
);


-- tabela de partes de processo de ML
create table tb_proc_parte_ml (
	nr_processo varchar(20),
	sg_tribunal varchar(6),
	ds_grau varchar(2),
	cd_orgao integer,
	nr_classe_processual integer,
	nm_pessoa varchar(300),
	nr_doc_principal_pessoa varchar(50)
);


insert into tb_proc_parte_ml 
select 
	distinct substr(nr_processo, length(nr_processo) - 19, length(nr_processo)),
    sg_tribunal,
    ds_grau_orgao,
	cd_orgao,
	nr_classe_processual,
	nm_pessoa,
	nr_doc_principal_pessoa
from tb_processo tp where substr(nr_doc_principal_pessoa, 1, 8) in (
'33582750',
'00360305',
'60701190',
'33224254',
'04641376',
'60746948',
'33592510',
'06981180',
'02455233',
'17224742'
);

-- tabela de assuntos dos processos ML
create table tb_proc_assuntos_ml (
	nr_processo varchar(20),
	sg_tribunal varchar(6),
	ds_grau varchar(2),
	cd_orgao integer,
	nr_classe_processual integer,
	cd_nacional_assunto integer,
	cd_assunto_principal boolean
);


insert into tb_proc_assuntos_ml 
select 
	distinct substr(nr_processo, length(nr_processo) - 19, length(nr_processo)),
    sg_tribunal,
    ds_grau_orgao,
	cd_orgao,
	nr_classe_processual,
	cd_nacional_assunto,
	cd_assunto_principal
from tb_processo tp where substr(nr_doc_principal_pessoa, 1, 8) in (
'33582750',
'00360305',
'60701190',
'33224254',
'04641376',
'60746948',
'33592510',
'06981180',
'02455233',
'17224742'
);



