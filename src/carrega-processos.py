
# coding: utf-8

# In[52]:


import pandas as pd
from pandas.io.json import json_normalize
import json
from sqlalchemy import create_engine
import os
#from pyhive import hive


# In[53]:


#df = pd.read_json (r'/home/lemos/trt3/Inova/justica_trabalho/processos-trt3/processos-trt3_5.json')
#df.head()


# In[54]:

def normaliza_processos(d):
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


    df = df.merge(df_advogado,on='processos.dpj_identificadorProcesso')
    df.head()


    df.count()

    caminho_registro = ['processos','movimento']
    meta_info = [['processos','dpj_identificadorProcesso']
                ]

    df_movimento = json_normalize(d,record_path =caminho_registro,record_prefix='processos.movimento.',meta=meta_info)
    colunas_movimento = ['processos.dpj_identificadorProcesso',
                        'processos.movimento.movimentoNacional.codigoNacional',
                        'processos.movimento.dataHora',
                        'processos.movimento.orgaoJulgador.codigoOrgao',
                        'processos.movimento.orgaoJulgador.nomeOrgao',
                        'processos.movimento.orgaoJulgador.instancia',
                        'processos.movimento.orgaoJulgador.codigoMunicipioIBGE',
                        'processos.movimento.complementoNacional'
                        ]
    #df = df.reindex(sorted(df.columns, reverse=False, key=len), axis=1)
    df_movimento = df_movimento[colunas_movimento]
    df_movimento.count()


    caminho_registro = ['processos','movimento','complementoNacional']
    meta_info = [['processos','dpj_identificadorProcesso'],
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


    df_complemento.groupby(['processos.dpj_identificadorProcesso','processos.movimento.dataHora','complemento.codComplemento']).agg('min').head()


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
    pasta_processos = "/home/lemos/trt3/Inova/teste/"
    #pasta_processos = "/dados/inova-cnj/dados/"
    url_banco = 'postgresql://postgres:postgres@localhost:5432/Inova'


    #engine = hive.Connection(host="", port=PORT, username="YOU")

    engine = create_engine(url_banco)

    for index, arq_processo in enumerate(os.listdir(pasta_processos)):
        nome_arq = pasta_processos + "/" + arq_processo
        print("Carregando ", nome_arq)
        with open(nome_arq) as f:
            d = json.load(f)
            tabela_processos = normaliza_processos(d)
            apagar_banco = False
            if index == 0:
                apagar_banco = True
            carrega_base_processos(tabela_processos, engine, apagar_banco=apagar_banco)
            print("Terminou...")
    print("Carga finalizada!")

#In[]:
run()


# escrever no postgres

# In[68]:


#df_banco.count()

