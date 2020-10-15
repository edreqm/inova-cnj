#!/usr/bin/env python3
# coding: utf-8

# In[52]:


import pandas as pd
from pandas.io.json import json_normalize
import json
from sqlalchemy import create_engine
import os

import operator as op
import functools as fct  # reduce is in functools in python 3+
def listagg(L):
    return fct.reduce(op.concat, L)
#from pyhive import hive


# In[53]:


#df = pd.read_json (r'/home/lemos/trt3/Inova/justica_trabalho/processos-trt3/processos-trt3_5.json')
#df.head()


# In[54]:

def normaliza_processos(d, engine, apagar_banco):
    df = json_normalize(d,record_path= 'processos')
    df = df.reindex(sorted(df.columns, reverse=False, key=len), axis=1)
    df.rename({'dpj_identificadorProcesso':'processos.dpj_identificadorProcesso'}, axis=1,inplace=True)
    df.columns

    colunas = ['processos.dpj_identificadorProcesso',
            'grau',
            'siglaTribunal',
            'dadosBasicos.valorCausa',
            'dadosBasicos.numero',
            'dadosBasicos.dataAjuizamento',
            'dadosBasicos.classeProcessual',
            'dadosBasicos.orgaoJulgador.codigoOrgao',
            'dadosBasicos.orgaoJulgador.nomeOrgao',
            'dadosBasicos.orgaoJulgador.codigoMunicipioIBGE']
    df = df[colunas]
    
    df_processo = pd.DataFrame()
    df_processo['nr_processo'] = df['processos.dpj_identificadorProcesso']
    df_processo['dt_ajuizamento'] = pd.to_datetime(df['dadosBasicos.dataAjuizamento'], format='%Y%m%d%H%M%S')
    df_processo['nr_classe_processual'] = df['dadosBasicos.classeProcessual']
    df_processo['cd_orgao'] = df['dadosBasicos.orgaoJulgador.codigoOrgao']
    df_processo['nm_orgao'] = df['dadosBasicos.orgaoJulgador.nomeOrgao']
    df_processo['cd_municipio_ibge'] = df['dadosBasicos.orgaoJulgador.codigoMunicipioIBGE']
    df_processo['ds_grau_orgao'] = df['grau']
    df_processo['sg_tribunal'] = df['siglaTribunal']
    df_processo['vl_causa'] = df['dadosBasicos.valorCausa']

    tipo_operacao_banco = "append"

    if apagar_banco:
        tipo_operacao_banco = "replace"

    df.to_sql(name='tb_processo', con=engine, if_exists=tipo_operacao_banco)

    df.head()


    caminho_registro = ['processos','dadosBasicos','polo','parte','advogado']
    meta_info = [['processos','dpj_identificadorProcesso'],
                ['processos','dadosBasicos','polo','polo'],
                ['processos','dadosBasicos','polo','parte','pessoa','nome'],
                ['processos','dadosBasicos','polo','parte','pessoa','numeroDocumentoPrincipal']
                ]

    df_advogado = json_normalize(d,record_path =caminho_registro,record_prefix='advogado.',meta=meta_info,max_level=2)
    #df = df.reindex(sorted(df.columns, reverse=False, key=len), axis=1)
    df_advogado.head()

    df_processo_parte = pd.DataFrame()
    df_processo_parte['nr_processo'] = df_advogado['processos.dpj_identificadorProcesso']
    df_processo_parte['tp_polo'] = df_advogado['processos.dadosBasicos.polo.polo']
    df_processo_parte['nm_pessoa'] = df_advogado['processos.dadosBasicos.polo.parte.pessoa.nome']
    df_processo_parte['nr_doc_principal_pessoa'] = df_advogado['processos.dadosBasicos.polo.parte.pessoa.numeroDocumentoPrincipal']
    df_processo_parte['nm_advogado'] = df_advogado['advogado.nome']
    df_processo_parte['nr_inscricao_advogado'] = df_advogado['advogado.inscricao']
    df_processo_parte['tp_representante'] = df_advogado['advogado.tipoRepresentante']

    df_processo_parte.to_sql(name='tb_processo_parte', con=engine, if_exists=tipo_operacao_banco)


    df = df.merge(df_advogado,on='processos.dpj_identificadorProcesso')
    df.head()


    df.count()

    caminho_registro = ['processos','movimento','complementoNacional']
    meta_info = [['processos','dpj_identificadorProcesso'],
                ['processos','movimento','identificadorMovimento'],
                ['processos','movimento','dataHora'],
                ['processos','movimento','movimentoNacional','codigoNacional'],
                ['processos','movimento','orgaoJulgador','codigoOrgao'],
                ['processos','movimento','orgaoJulgador','nomeOrgao'],
                ['processos','movimento','orgaoJulgador','instancia'],
                ['processos','movimento','orgaoJulgador','codigoMunicipioIBGE']
                ]

    df_complemento = json_normalize(d,record_path =caminho_registro,record_prefix='complemento.',meta=meta_info)
    #colunas_movimento = ['processos.dpj_identificadorProcesso',
    #                     'movimento.movimentoNacional.codigoNacional',
    #                     'movimento.dataHora',
    #                     'movimento.orgaoJulgador.codigoOrgao',
    #                     'movimento.orgaoJulgador.nomeOrgao',
    #                     'movimento.orgaoJulgador.instancia',
    #                     'movimento.orgaoJulgador.codigoMunicipioIBGE',
    #                     'movimento.complementoNacional'
    #                    ]
    #df = df.reindex(sorted(df.columns, reverse=False, key=len), axis=1)
    #df_movimento = df_movimento[colunas_movimento]
    df_complemento.head()
    print(df_complemento.head(10))                

    grupo = ['processos.dpj_identificadorProcesso',
                'processos.movimento.identificadorMovimento',
                'processos.movimento.dataHora',
                'processos.movimento.movimentoNacional.codigoNacional',
                'processos.movimento.orgaoJulgador.codigoOrgao',
                'processos.movimento.orgaoJulgador.nomeOrgao',
                'processos.movimento.orgaoJulgador.instancia',
                'processos.movimento.orgaoJulgador.codigoMunicipioIBGE']

    df_complemento = df_complemento.groupby(grupo)['complemento.descricaoComplemento'].apply(listagg)

    print(df_complemento.head(10))                

    #df_complemento.groupby(['processos.dpj_identificadorProcesso','processos.movimento.dataHora','complemento.codComplemento']).agg('min').head()


    df_complemento.count()

    df = df.merge(df_complemento,on='processos.dpj_identificadorProcesso')
    df.count()

    caminho_registro = ['processos','dadosBasicos','assunto']
    meta_info = [['processos','dpj_identificadorProcesso']
                ]

    df_assunto = json_normalize(d,record_path =caminho_registro,record_prefix='assunto.',meta=meta_info)
    colunas_assunto = ['processos.dpj_identificadorProcesso',
                    'assunto.codigoNacional',
                    'assunto.principal'
                        ]
    #df = df.reindex(sorted(df.columns, reverse=False, key=len), axis=1)
    df_assunto = df_assunto[colunas_assunto]
    df_assunto.count()

    df = df.merge(df_assunto,on='processos.dpj_identificadorProcesso')
    df.count()

    df.dtypes

    return(df)

# In[68]:
def carrega_base_processos(df, engine, apagar_banco):
    df_banco = pd.DataFrame()
    df_banco['nr_processo'] = df['processos.dpj_identificadorProcesso']
    df_banco['dt_ajuizamento'] = pd.to_datetime(df['dadosBasicos.dataAjuizamento'], format='%Y%m%d%H%M%S')
    df_banco['nr_classe_processual'] = df['dadosBasicos.classeProcessual']
    df_banco['cd_orgao'] = df['dadosBasicos.orgaoJulgador.codigoOrgao']
    df_banco['nm_orgao'] = df['dadosBasicos.orgaoJulgador.nomeOrgao']
    df_banco['cd_municipio_ibge'] = df['dadosBasicos.orgaoJulgador.codigoMunicipioIBGE']
    df_banco['ds_grau_orgao'] = df['grau']
    df_banco['sg_tribunal'] = df['siglaTribunal']
    df_banco['vl_causa'] = df['dadosBasicos.valorCausa']
    df_banco['tp_polo'] = df['processos.dadosBasicos.polo.polo']
    df_banco['nm_pessoa'] = df['processos.dadosBasicos.polo.parte.pessoa.nome']
    df_banco['nr_doc_principal_pessoa'] = df['processos.dadosBasicos.polo.parte.pessoa.numeroDocumentoPrincipal']
    df_banco['nm_advogado'] = df['advogado.nome']
    df_banco['nr_inscricao_advogado'] = df['advogado.inscricao']
    df_banco['tp_representante'] = df['advogado.tipoRepresentante']
    df_banco['cd_nacional_assunto'] = df['assunto.codigoNacional']
    df_banco['cd_assunto_principal'] = df['assunto.principal']
    df_banco['cd_movimento_nacional'] = df['processos.movimento.movimentoNacional.codigoNacional']
    df_banco['dt_lancamento_movimento'] = pd.to_datetime(df['processos.movimento.dataHora'], format='%Y%m%d%H%M%S')
    df_banco['cd_orgao_movimento'] = df['processos.movimento.orgaoJulgador.codigoOrgao']
    df_banco['nm_orgao_movimento'] = df['processos.movimento.orgaoJulgador.nomeOrgao']
    df_banco['cd_municipio_orgao_movimento'] = df['processos.movimento.orgaoJulgador.codigoMunicipioIBGE']
    df_banco['cd_complemento_movimento_nacional'] = df['complemento.codComplemento']
    df_banco['ds_complemento_movimento_nacional'] = df['complemento.descricaoComplemento']
    df_banco['cd_complemento_movimento_nacional_tabelado'] = df['complemento.codComplementoTabelado']

    #df_banco.head()

    tipo_operacao_banco = "append"

    if apagar_banco:
        tipo_operacao_banco = "replace"

    df_banco.to_sql(name='tb_processo', con=engine, if_exists=tipo_operacao_banco)


# In[69]:
def run():
    #pasta_processos = "/home/lemos/trt3/Inova/teste/"
    pasta_processos = "/home/rmpossa/selocnj/exemplosjson"

    #pasta_processos = "/dados/inova-cnj/dados/"
    url_banco = 'postgresql://postgres:postgres@localhost:5432/inova'


    #engine = hive.Connection(host="", port=PORT, username="YOU")

    engine = create_engine(url_banco)

    for index, arq_processo in enumerate(os.listdir(pasta_processos)):
        nome_arq = pasta_processos + "/" + arq_processo
        print("Carreando ", nome_arq)
        with open(nome_arq) as f:
            d = json.load(f)

            apagar_banco = True
            if index == 0:
                apagar_banco = True

            tabela_processos = normaliza_processos(d, engine, apagar_banco)
            
           # carrega_base_processos(tabela_processos, engine, apagar_banco=apagar_banco)
            print("Terminou...")
    print("Carga finalizada!")

#In[]:
run()


# escrever no postgres

# In[68]:


#df_banco.count()

