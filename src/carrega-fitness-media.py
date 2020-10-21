#!/usr/bin/env python3
# coding: utf-8

# In[52]:

import psycopg2
import psycopg2.sql as sql
import pandas as pd
from pandas.io.json import json_normalize
import json
from sqlalchemy import create_engine
import os
import hashlib

def pesquisa_duracao(codigoOrgao, radicalCNPJ, df):
    return df[(df['cd_orgao'] == int(codigoOrgao)) & (df['radical_cnpj'] == radicalCNPJ)].iloc[0]['duracao']

def toMD5(texto):
    result = hashlib.md5(texto.encode())
    return result.hexdigest()


# In[69]:
def run():
    pasta_raiz = "/home/rmpossa/TRT/Inova CNJ/AnaliseLitigantes"

    url_banco = 'postgresql://minerador_processos:5448minerador@10.3.192.85:5448/<senha>'

    engine = create_engine(url_banco)

    # carga de DataFrame lido do banco com duracão média de processos por empresa e unidade do tribunal
    df = pd.read_sql(sql="""select 
  cd_orgao, radical_cnpj, round(cast(avg(duracao_processo) as numeric), 2) duracao
from (
select cd_orgao, substr(nr_doc_principal_pessoa, 1, 8) radical_cnpj, nr_chave_proc, min(dias_duracao_processo) duracao_processo from mv_maiores_litigantes_arquivados mmla 
group by 
  nr_chave_proc, 
  cd_orgao, 
  substr(nr_doc_principal_pessoa, 1, 8) 
) tmp1
group by cd_orgao, radical_cnpj""", con=engine)


    con = psycopg2.connect(dbname="dw_dev", user="minerador_processos", password="<senha>", host="10.3.192.85", port="5448")
    cur = con.cursor()    

    # Lê estrutura de pastas com arquivos json contendo average fitness por empresa e unidade do tribunal
    for cnpj in os.listdir(pasta_raiz): # pastas de cnpj
        path_cnpj = os.path.join(pasta_raiz,cnpj)
        if(os.path.isdir(path_cnpj)):
            for codigoOrgao in os.listdir(path_cnpj): # pastas de codigoOrgao
                path_codigoOrgao = os.path.join(path_cnpj,codigoOrgao)
                if(os.path.isdir(path_codigoOrgao)):
                    path_json = os.path.join(path_codigoOrgao,'FitnessLitigante' + cnpj + 'Vara' + codigoOrgao + '.json')
                    if(os.path.exists(path_json)):
                        with open(path_json) as f:
                            d = json.load(f)
                            # insere no banco o average fitness, lido do arquivo, e a duração em média, lida do banco, por grupo (empresa, unidade do tribunal)
                            cur.execute("INSERT INTO tb_fitness_vara (nr_doc_principal_pessoa, cd_orgao, vl_fitness, nr_dias) VALUES(%s, %s, %s, %s)", (toMD5(cnpj), codigoOrgao, d['averageFitness'], pesquisa_duracao(codigoOrgao, cnpj, df)))
    con.commit()
    cur.close()
    con.close()


            
    print("Carga finalizada!")


#In[]:
run()


# escrever no postgres

# In[68]:


#df_banco.count()

