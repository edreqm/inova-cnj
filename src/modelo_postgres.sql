-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.2
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database;
-- -- ddl-end --
-- 

-- object: inovacnj | type: SCHEMA --
-- DROP SCHEMA IF EXISTS inovacnj CASCADE;
CREATE SCHEMA inovacnj;
-- ddl-end --
-- ALTER SCHEMA inovacnj OWNER TO postgres;
-- ddl-end --

SET search_path TO pg_catalog,public,inovacnj;
-- ddl-end --

-- object: inovacnj.tb_processo | type: TABLE --
-- DROP TABLE IF EXISTS inovacnj.tb_processo CASCADE;
CREATE TABLE inovacnj.tb_processo (
	nr_processo varchar(50),
	dt_ajuizamento daterange,
	nr_classe_processual integer,
	cd_orgao integer,
	nm_orgao varchar(100),
	cd_municipio_ibge integer,
	ds_grau_orgao varchar(5),
	sg_tribunal varchar(10),
	vl_causa numeric,
	tp_polo varchar(2),
	nm_pessoa varchar(200),
	nr_doc_principal_pessoa varchar(30),
	nm_advogado varchar(200),
	nr_inscricao_advogado varchar(10),
	tp_representante varchar(3),
	cd_nacional_assunto integer,
	cd_assunto_principal boolean,
	cd_movimento_nacional integer,
	dt_lancamento_movimento timestamp,
	cd_orgao_movimento integer,
	nm_orgao_movimento varchar(200),
	cd_municipio_orgao_movimento integer,
	cd_complemento_movimento_nacional integer,
	ds_complemento_movimento_nacional varchar(100),
	cd_complemento_movimento_nacional_tabelado integer,
	sq_pessoa smallint,
	sql_advogado smallint,
	sq_movimento smallint
);
-- ddl-end --
COMMENT ON TABLE inovacnj.tb_processo IS E'Indicador de assunto principal';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.nr_processo IS E'Numero do processo\ndadosBasicos/numero';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.dt_ajuizamento IS E'Data de ajuizamento do processo\ndadosBasicos/dataAjuizamento';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.nr_classe_processual IS E'Numero da classe processual\ndadosBasicos/classeProcessual';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.cd_orgao IS E'Codigo do orgao\ndadosBasicos/orgaoJulgador/codigoOrgao';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.nm_orgao IS E'Nome do orgao julgados\ndadosBasicos/orgaoJulgador/nomeOrgao';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.cd_municipio_ibge IS E'Codigo do municipio do orgao julgador\ndadosBasicos/orgaoJulgador/codigoMunicipioIBGE';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.ds_grau_orgao IS E'Grau do orgao julgador\ndadosBasicos/grau';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.sg_tribunal IS E'Sigla do tribunal\ndadosBasicos/siglaTribunal';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.vl_causa IS E'Valor da causa\ndadosBasicos/valorCausa';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.tp_polo IS E'Tipo do polo\ndadosBasicos/polo/@polo';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.nm_pessoa IS E'dadosBasicos/polo/parte/pessoa/nome';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.nr_doc_principal_pessoa IS E'dadosBasicos/polo/parte/numeroDocumentoPrincipal';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.nm_advogado IS E'Nome do advogado\ndadosBasicos/polo/parte/advogado/nome';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.nr_inscricao_advogado IS E'Numero OAB dos advogados\ndadosBasicos/polo/parte/advogado/inscricao';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.tp_representante IS E'Tipo de representante da parte\ndadosBasicos/polo/parte/advogado/tipoRepesentante';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.cd_nacional_assunto IS E'Codigo nacional do assunto\nmovimento/(iésimo)/movimentoNacional/codigoNacional';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.cd_assunto_principal IS E'Indica se assunto e principal ou nao\nassunto/(iésimo)/principal';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.cd_movimento_nacional IS E'Codigo do movimento nacional.';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.dt_lancamento_movimento IS E'Data do lancamento do movimento\nmovimento/(iésimo)/dataHora';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.cd_orgao_movimento IS E'Codigo do orgao do movimento\nmovimento/(iésimo)/orgaoJulgador/codigoOrgao';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.nm_orgao_movimento IS E'Nome do orgao do movimento\nmovimento/(iésimo)/orgaoJulgador/nomeOrgao';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.cd_municipio_orgao_movimento IS E'Codigo do municipio do orgao do movimento\nmovimento/(iésimo)/orgaoJulgador/codigoMunicipioIBGE';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.cd_complemento_movimento_nacional IS E'Codigo do complemento do movimento nacional\nmovimento/(iésimo)/complementoNacional/codComplemento';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.ds_complemento_movimento_nacional IS E'Descricao do complemento do movimento nacional\nmovimento/(iésimo)/complementoNacional/descricaoComplemento';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.cd_complemento_movimento_nacional_tabelado IS E'Codigo do complemento do movimento nacional tabelado\nmovimento/(iésimo)/complementoNacional/codComplementoTabelado';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.sq_pessoa IS E'Numero sequencial da pessoa no processo';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.sql_advogado IS E'Ordem do advogado no processo';
-- ddl-end --
COMMENT ON COLUMN inovacnj.tb_processo.sq_movimento IS E'Ordem do movimento no processo';
-- ddl-end --


