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
00360305
60701190
33582750
06981180
33224254
60746948
00000000
33000118
02455233
04641376
*/


drop materialized view if exists minerador_processos.mv_maiores_litigantes;
drop table if exists minerador_processos.tb_proc_maiores_litigantes;
drop table if exists minerador_processos.tb_proc_parte_ml;
drop table if exists minerador_processos.tb_proc_assuntos_ml;
drop table if exists minerador_processos.tb_proc_movimentos_ml;

-- DADOS BASICOS MAIORES LITIGANTES
create table minerador_processos.tb_proc_maiores_litigantes (
	nr_processo varchar(20),
	nr_chave_proc varchar(40),
	dt_ajuizamento date,
	nr_classe_processual integer,
	cd_orgao integer,
	nm_orgao varchar(500),
	cd_municipio_ibge integer,
	ds_grau varchar(2),
	sg_tribunal varchar(6),
	vl_causa float
);

-- POPULA DADOS BÁSICOS ML
insert into minerador_processos.tb_proc_maiores_litigantes 
select 
	distinct substr(nr_processo, length(nr_processo) - 19, length(nr_processo)),
	nr_processo,
	dt_ajuizamento,
	nr_classe_processual,
	cd_orgao,
	nm_orgao,
	cd_municipio_ibge,
	ds_grau_orgao,
	sg_tribunal,
	vl_causa
from minerador_processos.tb_processo tp;
/*
where substr(nr_doc_principal_pessoa, 1, 8) in (
'00360305',
'60701190',
'33582750',
'06981180',
'33224254',
'60746948',
'00000000',
'33000118',
'02455233',
'04641376'
);
*/

-- índices
create index idx_processo_1 on minerador_processos.tb_proc_maiores_litigantes.
-- tabela de partes de processo de ML
create table minerador_processos.tb_proc_parte_ml (
	nr_processo varchar(20),
	nr_chave_proc varchar(40),
	nm_pessoa varchar(600),
	nr_doc_principal_pessoa varchar(50)
);


insert into minerador_processos.tb_proc_parte_ml 
select 
	distinct substr(nr_processo, length(nr_processo) - 19, length(nr_processo)),
	nr_processo,
	nm_pessoa,
	nr_doc_principal_pessoa
from minerador_processos.tb_processo tp;
/*
where substr(nr_doc_principal_pessoa, 1, 8) in (
'00360305',
'60701190',
'33582750',
'06981180',
'33224254',
'60746948',
'00000000',
'33000118',
'02455233',
'04641376'
);
*/

-- tabela de assuntos dos processos ML
create table minerador_processos.tb_proc_assuntos_ml (
	nr_processo varchar(20),
	nr_chave_proc varchar(40),
	cd_nacional_assunto integer,
	cd_assunto_principal boolean
);


insert into minerador_processos.tb_proc_assuntos_ml 
select 
	distinct substr(nr_processo, length(nr_processo) - 19, length(nr_processo)),
	nr_processo,
   	cd_nacional_assunto,
	cd_assunto_principal
from minerador_processos.tb_processo tp;
/*
where substr(nr_doc_principal_pessoa, 1, 8) in (
'00360305',
'60701190',
'33582750',
'06981180',
'33224254',
'60746948',
'00000000',
'33000118',
'02455233',
'04641376'
);
*/

create table minerador_processos.tb_proc_movimentos_ml (
	nr_processo varchar(20),
	nr_chave_proc varchar(40),
	cd_movimento_nacional varchar(5),
	dt_lancamento_movimento timestamp,
	cd_orgao_movimento integer,
	nm_orgao_movimento varchar(300),
	cd_municipio_orgao_movimento integer,
	ds_movimento varchar(300),
	ds_movimento_complementos varchar(1000)
);

insert into minerador_processos.tb_proc_movimentos_ml 
select 
	distinct substr(nr_processo, length(nr_processo) - 19, length(nr_processo)),
	nr_processo,
	cd_movimento_nacional,
	dt_lancamento_movimento ,
	cd_orgao_movimento,
	nm_orgao_movimento,
	cd_municipio_orgao_movimento,
	null,
	null
from minerador_processos.tb_processo tp;
/*
where substr(nr_doc_principal_pessoa, 1, 8) in (
'00360305',
'60701190',
'33582750',
'06981180',
'33224254',
'60746948',
'00000000',
'33000118',
'02455233',
'04641376'
);
*/
update minerador_processos.tb_proc_movimentos_ml 
set ds_movimento = (
	select descricao 
	from minerador_processos."tb_cod_movimentos_CNJ" 
	where codigo::text = cd_movimento_nacional) where 1 = 1;

-- Índices 
create index idx_processo_1 on minerador_processos.tb_processo (nr_processo);
create index idx_processo_2 on minerador_processos.tb_processo (dt_lancamento_movimento);
create index idx_processo_3 on minerador_processos.tb_processo (cd_movimento_nacional);
create index idx_processo_4 on minerador_processos.tb_processo (cd_complemento_movimento_nacional);
create index idx_processo_5 on minerador_processos.tb_processo (cd_complemento_movimento_nacional_tabelado);
create index idx_proc_movimentos_ml_1 on minerador_processos.tb_proc_movimentos_ml(nr_chave_proc);
create index idx_proc_movimentos_ml_2 on minerador_processos.tb_proc_movimentos_ml(dt_lancamento_movimento);
create index idx_proc_movimentos_ml_3 on minerador_processos.tb_proc_movimentos_ml(cd_movimento_nacional);


update minerador_processos.tb_proc_movimentos_ml  mml
set 
	ds_movimento_complementos = ds_movimento || coalesce(
		(
		 select 
		   ' ' || string_agg(t1.ds_valor_complemento, ' ' )
		 from 
			(
			select 
				distinct tc.cd_tipo_complemento, vc.ds_valor_complemento 
			from minerador_processos.tb_processo p, 
				minerador_processos.tb_tipo_complementos_cnj tc, 
				minerador_processos.tb_valores_complementos_cnj vc
			where p.nr_processo = mml.nr_chave_proc
				and p.dt_lancamento_movimento = mml.dt_lancamento_movimento 
				and p.cd_movimento_nacional::text = mml.cd_movimento_nacional
				and tc.cd_tipo_complemento = p.cd_complemento_movimento_nacional
				and tc.cd_classificacao = 'T'
				and vc.cd_valor_complemento = p.cd_complemento_movimento_nacional_tabelado 
			order by tc.cd_tipo_complemento 
			) t1
		), '')
where 1 = 1;

CREATE MATERIALIZED VIEW minerador_processos.mv_maiores_litigantes_arquivados
TABLESPACE pg_default
AS
 SELECT mov_ml.nr_chave_proc,
    mov_ml.nr_processo,
    mov_ml.cd_movimento_nacional,
    mov_ml.dt_lancamento_movimento,
    mov_ml.cd_orgao_movimento,
    mov_ml.nm_orgao_movimento,
    mov_ml.cd_municipio_orgao_movimento,
    mov_ml.ds_movimento,
    mov_ml.ds_movimento_complementos,
    proc_ml.dt_ajuizamento,
    proc_ml.nr_classe_processual,
    proc_ml.cd_orgao,
    proc_ml.nm_orgao,
    proc_ml.cd_municipio_ibge,
    proc_ml.ds_grau,
    proc_ml.sg_tribunal,
    proc_ml.vl_causa,
    parte_ml.nm_pessoa,
    parte_ml.nr_doc_principal_pessoa,
	ultmo_mov.dt_arquivamento,
	ultmo_mov.dt_arquivamento - proc_ml.dt_ajuizamento as dias_duracao_processo
   FROM minerador_processos.tb_proc_movimentos_ml mov_ml
     JOIN minerador_processos.tb_proc_maiores_litigantes proc_ml ON mov_ml.nr_chave_proc::text = proc_ml.nr_chave_proc::text
     JOIN minerador_processos.tb_proc_parte_ml parte_ml ON mov_ml.nr_chave_proc::text = parte_ml.nr_chave_proc::text
	 JOIN (
		 select 
		 	nr_chave_proc,
		 	max(dt_lancamento_movimento) as dt_arquivamento
		 from 
		 	minerador_processos.tb_proc_movimentos_ml
		 group by
		 	nr_chave_proc
	 ) ultmo_mov on mov_ml.nr_chave_proc = ultmo_mov.nr_chave_proc
   where
	 exists (
		 select 1
		 from minerador_processos.tb_proc_movimentos_ml mov_ml2
		 where 
		 mov_ml2.nr_chave_proc = mov_ml.nr_chave_proc
		 and mov_ml2.cd_movimento_nacional in (
			'228',
			'218',
			'472',
			'473',
			'861',
			'48',
			'245',
			'246',
			'12430',
			'1013')
	 );