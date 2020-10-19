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


-- DADOS BASICOS MAIORES LITIGANTES
create table tb_proc_maiores_litigantes (
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
)

-- POPULA DADOS BÁSICOS ML
insert into tb_proc_maiores_litigantes 
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
from tb_processo tp where substr(nr_doc_principal_pessoa, 1, 8) in (
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


-- tabela de partes de processo de ML
create table tb_proc_parte_ml (
	nr_processo varchar(20),
	nr_chave_proc varchar(40),
	nm_pessoa varchar(300),
	nr_doc_principal_pessoa varchar(50)
);


insert into tb_proc_parte_ml 
select 
	distinct substr(nr_processo, length(nr_processo) - 19, length(nr_processo)),
	nr_processo,
	nm_pessoa,
	nr_doc_principal_pessoa
from tb_processo tp where substr(nr_doc_principal_pessoa, 1, 8) in (
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

-- tabela de assuntos dos processos ML
create table tb_proc_assuntos_ml (
	nr_processo varchar(20),
	nr_chave_proc varchar(40),
	cd_nacional_assunto integer,
	cd_assunto_principal boolean
);


insert into tb_proc_assuntos_ml 
select 
	distinct substr(nr_processo, length(nr_processo) - 19, length(nr_processo)),
	nr_processo,
   	cd_nacional_assunto,
	cd_assunto_principal
from tb_processo tp where substr(nr_doc_principal_pessoa, 1, 8) in (
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


create table tb_proc_movimentos_ml (
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

insert into tb_proc_movimentos_ml 
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
from tb_processo tp where substr(nr_doc_principal_pessoa, 1, 8) in (
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

update tb_proc_movimentos_ml set ds_movimento = (select descricao from "tb_cod_movimentos_CNJ" where codigo::text = cd_movimento_nacional) where 1 = 1;

update tb_proc_movimentos_ml  mml
set 
	ds_movimento_complementos = ds_movimento || coalesce(
		(
		 select 
		   ' ' || string_agg(t1.ds_valor_complemento, ' ' )
		 from 
			(
			select 
				distinct tc.cd_tipo_complemento, vc.ds_valor_complemento 
			from tb_processo p, tb_tipo_complementos_cnj tc, tb_valores_complementos_cnj vc
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

