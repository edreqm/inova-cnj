#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine
import pandas as pd
import psycopg2 as pg
import pandas.io.sql as psql
from pm4py.objects.log.util import dataframe_utils
from pm4py.objects.conversion.log import converter as log_converter
from pm4py.objects.log.exporter.xes import exporter as xes_exporter


# In[2]:


DATABASES = {
    'local':{
        'NAME': 'Inova',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    },
}


# In[3]:


db = DATABASES['local']


# In[4]:


engine_string = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
    user = db['USER'],
    password = db['PASSWORD'],
    host = db['HOST'],
    port = db['PORT'],
    database = db['NAME'],
)


# In[5]:


engine = create_engine(engine_string)


# In[6]:


#df = pd.read_sql_table('tb_processo_datajud',engine,schema='datajud')


# In[7]:


df = psql.read_sql('Select * from tb_processo',engine)
#df.set_index('id_processo_datajud')
df.head()


# In[8]:


df.dtypes


# In[9]:


df_codigo_movimento = pd.read_csv('/home/lemos/trt3/Inova/sgt_movimentos.csv',sep=';')
df_codigo_movimento = df_codigo_movimento[['codigo','descricao']]
df_codigo_movimento.rename({'codigo':'cd_movimento_nacional'}, axis=1, inplace=True)
df_codigo_movimento.rename({'descricao':'ds_movimento_nacional'}, axis=1, inplace=True)
df_codigo_movimento.head()


# In[10]:


df = df.merge(df_codigo_movimento,on='cd_movimento_nacional')
df.head()


# In[26]:


df_litigante = df[df['nr_doc_principal_pessoa'] == '08174089000386']
colunas_agrupamento = ['nr_processo','dt_lancamento_movimento'] 
f = {'ds_movimento_nacional': 'first'}
df_litigante = df_litigante.groupby(colunas_agrupamento, as_index=False).agg(f)
df_litigante


# In[12]:


df_log = pd.DataFrame()
df_log['case:concept:name'] = df_litigante['nr_processo'] 
df_log['time:timestamp'] = df_litigante['dt_lancamento_movimento']
df_log['concept:name'] = df_litigante['ds_movimento_nacional']
log_processos = dataframe_utils.convert_timestamp_columns_in_df(df_log)
log_processos = log_processos.sort_values('time:timestamp')
event_log_processos = log_converter.apply(log_processos)
xes_exporter.apply(event_log_processos, '/home/lemos/trt3/Inova/litigante.xes')


# ## Process Discovery

# In[15]:


# inductive miner

from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.visualization.process_tree import visualizer as pt_visualizer

tree = inductive_miner.apply_tree(event_log_processos)
gviz = pt_visualizer.apply(tree)
pt_visualizer.view(gviz)


# In[22]:


# Petri net from tree

from pm4py.objects.conversion.process_tree import converter as pt_converter
from pm4py.visualization.petrinet import visualizer as pn_visualizer
parameters = {pn_visualizer.Variants.WO_DECORATION.value.Parameters.FORMAT:"png"}

net, initial_marking, final_marking = pt_converter.apply(tree, variant=pt_converter.Variants.TO_PETRI_NET)
gviz = pn_visualizer.apply(net, initial_marking, final_marking, parameters=parameters)
pn_visualizer.save(gviz, "inductive.png")
pn_visualizer.view(gviz)


# In[24]:


# Decorated petri net (frequency)

gviz = pn_visualizer.apply(net, initial_marking, final_marking, parameters=parameters, variant=pn_visualizer.Variants.FREQUENCY, log=event_log_processos)
pn_visualizer.save(gviz, "inductive_frequency.png")
pn_visualizer.view(gviz)


# In[25]:


# Decorated petri net (performance)

gviz = pn_visualizer.apply(net, initial_marking, final_marking, parameters=parameters, variant=pn_visualizer.Variants.PERFORMANCE, log=event_log_processos)
pn_visualizer.save(gviz, "inductive_performance.png")
pn_visualizer.view(gviz)


# In[20]:


# Heuristic miner

from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer

heu_net = heuristics_miner.apply_heu(event_log_processos, parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.99})
gviz = hn_visualizer.apply(heu_net)
hn_visualizer.view(gviz)


# In[21]:


from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
net, im, fm = heuristics_miner.apply(event_log_processos, parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.99})

from pm4py.visualization.petrinet import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, im, fm)
pn_visualizer.view(gviz)

