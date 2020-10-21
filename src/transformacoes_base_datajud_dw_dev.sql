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


-- Filtros para os movimentos relevantes
create table minerador_processos.tb_filtro_movimentos(cd_movimento_nacional text, ds_movimento_complementos text);
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('11','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('26','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('36','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('123','Remessa em grau de recurso');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('133','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('132','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('163','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('160','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('193','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('196','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('198','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('200','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('207','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('219','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('220','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('221','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('235','Não Conhecimento de recurso Petição (outras)');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('237','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('238','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('239','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('240','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('241','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('242','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('245','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('246','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('247','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('265','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('272','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('276','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('332','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('335','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('348','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('377','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('378','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('385','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('431','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('434','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('454','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('455','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('457','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('458','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('459','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('460','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('461','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('462','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('463','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('464','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('465','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('466','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('471','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('472','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('473','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('785','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('804','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('817','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('848','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('871','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('888','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('889','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('898','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('941','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('944','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('968','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('970','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('972','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('1013','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('1060','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('1059','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('10966','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('11012','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('11015','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('11021','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('11373','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('11384','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('11385','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('11795','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('11975','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('12068','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('12100','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('12164','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('12185','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('901','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('236','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('228','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('218','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('472','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('473','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('861','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('48','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('245','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('246','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('12430','');
insert into minerador_processos.tb_filtro_movimentos(cd_movimento_nacional,ds_movimento_complementos) values('1013','');

drop MATERIALIZED VIEW if exists minerador_processos.mv_maiores_litigantes_arquivados;
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
create index idx_proc_maiores_litigantes_1 on minerador_processos.tb_proc_maiores_litigantes(nr_chave_proc);
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
SELECT distinct 
    mov_ml.nr_chave_proc,
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
	DATE_PART('day', ultmo_mov.dt_arquivamento - proc_ml.dt_ajuizamento) as dias_duracao_processo
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
	 ) ultmo_mov on mov_ml.nr_chave_proc = ultmo_mov.nr_chave_proc,
	 minerador_processos.tb_filtro_movimentos filtro
   where
	 exists (
		 select 1
		 from minerador_processos.tb_proc_movimentos_ml mov_ml2
		 where 
		 mov_ml2.nr_chave_proc = mov_ml.nr_chave_proc
		 and mov_ml2.cd_movimento_nacional in (
			 -- Processos com movimento de arquivamento
			'228',
			'218',
			'472',
			'473',
			'861',
			'48',
			'245',
			'246',
			'12430',
			'1013'
		)
	 ) and
	 not exists (
		 select 1
		 from minerador_processos.tb_proc_movimentos_ml mov_ml2
		 where 
		 mov_ml2.nr_chave_proc = mov_ml.nr_chave_proc
		 and mov_ml2.cd_movimento_nacional in (
			 -- Processos com movimentos que não devem ser incluídos nas análises
			'218',
			'228',
			'454',
			'455',
			'456',
			'457',
			'458',
			'459',
			'460',
			'461',
			'462',
			'463',
			'464',
			'465',
			'471',
			'472',
			'473',
			'11795'
		)
	 ) and (
		 (
			 filtro.cd_movimento_nacional = mov_ml.cd_movimento_nacional
			 and filtro.ds_movimento_complementos = ''
		 ) or (
			 filtro.cd_movimento_nacional = mov_ml.cd_movimento_nacional
			 and filtro.ds_movimento_complementos != ''
			 and mov_ml.ds_movimento_complementos = filtro.ds_movimento_complementos
		 )
	 )
	 ;