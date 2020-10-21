{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 168,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import glob\n",
    "import json\n",
    "from sqlalchemy import create_engine\n",
    "import pandas as pd\n",
    "import psycopg2 as pg\n",
    "import pandas.io.sql as psql\n",
    "from pm4py.objects.log.util import dataframe_utils\n",
    "from pm4py.objects.conversion.log import converter as log_converter\n",
    "from pm4py.objects.log.exporter.xes import exporter as xes_exporter\n",
    "from pm4py.objects.log.importer.xes import importer as xes_importer\n",
    "from pm4py.objects.petri.exporter import exporter as pnml_exporter\n",
    "from pm4py.objects.petri.importer import importer as pnml_importer\n",
    "from pm4py.algo.discovery.inductive import algorithm as inductive_miner\n",
    "from pm4py.visualization.petrinet import visualizer as pn_visualizer\n",
    "from pm4py.evaluation.replay_fitness import evaluator as replay_fitness_evaluator\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "metadata": {},
   "outputs": [],
   "source": [
    "def obtem_conexao():\n",
    "    DATABASES = {\n",
    "        'dw_dev':{\n",
    "            'NAME': 'dw_dev',\n",
    "            'USER': 'minerador_processos',\n",
    "            'PASSWORD': '5448minerador',\n",
    "            'HOST': '10.3.192.85',\n",
    "            'PORT': 5448,\n",
    "        },\n",
    "    }\n",
    "    db = DATABASES['dw_dev']\n",
    "    engine_string = \"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}\".format(\n",
    "    user = db['USER'],\n",
    "    password = db['PASSWORD'],\n",
    "    host = db['HOST'],\n",
    "    port = db['PORT'],\n",
    "    database = db['NAME'],\n",
    "    )\n",
    "    return create_engine(engine_string)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Exporta Logs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [],
   "source": [
    "def cria_sql(litigante,orgao) :\n",
    "    sql_str = f\"\"\"select \n",
    "        ml.nr_processo, \n",
    "        ml.dt_lancamento_movimento, \n",
    "        ml.ds_movimento_complementos\n",
    "    from \n",
    "        minerador_processos.mv_maiores_litigantes_arquivados ml\n",
    "        join (\n",
    "            -- k processos com menor duracao\n",
    "            select \n",
    "                ml2.nr_processo, \n",
    "                ml2.dias_duracao_processo\n",
    "            from \n",
    "                minerador_processos.mv_maiores_litigantes_arquivados ml2\n",
    "            where \n",
    "    \"\"\"\n",
    "    if len(litigante) > 0:\n",
    "        sql_str += f\"\"\"\n",
    "           nr_doc_principal_pessoa ilike '{litigante}%' and\n",
    "        \"\"\"\n",
    "\n",
    "    if len(orgao) > 0:\n",
    "        sql_str += f\"\"\"\n",
    "           cd_orgao_movimento = '{orgao}' and\n",
    "        \"\"\"\n",
    "    sql_str += \"\"\"\n",
    "                -- Ajuste aqui a classe processual\n",
    "                ml2.nr_classe_processual = 985\n",
    "                --and ml2.nr_processo = '00105530220165030111'\n",
    "            group by \n",
    "                ml2.nr_processo, \n",
    "                ml2.dias_duracao_processo\n",
    "            order by ml2.dias_duracao_processo asc\n",
    "            -- Ajuste aqui o numero de processos a sererm considerados\n",
    "            -- limit 500\n",
    "        ) melhores on melhores.nr_processo = ml.nr_processo\n",
    "    group by ml.nr_processo, ml.dt_lancamento_movimento, ml.ds_movimento_complementos\n",
    "    order by ml.nr_processo, ml.dt_lancamento_movimento\n",
    "    \"\"\"\n",
    "    return sql_str"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "metadata": {},
   "outputs": [],
   "source": [
    "def obtem_varas_litigante(litigante):\n",
    "    varas = []\n",
    "    sql_str = f\"\"\"select \n",
    "        ml.cd_orgao\n",
    "    from \n",
    "        minerador_processos.mv_maiores_litigantes_arquivados ml\n",
    "        join (\n",
    "            -- k processos com menor duracao\n",
    "            select \n",
    "                ml2.nr_processo, \n",
    "                ml2.dias_duracao_processo\n",
    "            from \n",
    "                minerador_processos.mv_maiores_litigantes_arquivados ml2\n",
    "            where \n",
    "                -- Ajuste aqui o identificador do litigante\n",
    "                nr_doc_principal_pessoa ilike '{litigante}%' and\n",
    "                -- Ajuste aqui a classe processual\n",
    "                ml2.nr_classe_processual = 985\n",
    "                --and ml2.nr_processo = '00105530220165030111'\n",
    "            group by \n",
    "                ml2.nr_processo, \n",
    "                ml2.dias_duracao_processo\n",
    "            order by ml2.dias_duracao_processo asc\n",
    "            -- Ajuste aqui o numero de processos a sererm considerados\n",
    "            -- limit 500\n",
    "        ) melhores on melhores.nr_processo = ml.nr_processo\n",
    "    group by ml.cd_orgao\n",
    "    \"\"\"\n",
    "    df_varas = pd.read_sql(sql_str,engine)\n",
    "    varas = df_varas.values.tolist()\n",
    "    varas = [vara for sublist in varas for vara in sublist]\n",
    "    #print(varas)\n",
    "    return varas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "metadata": {},
   "outputs": [],
   "source": [
    "def exporta_log(df,caminho_exportacao_log):\n",
    "\n",
    "    df_log = pd.DataFrame()\n",
    "    df_log['case:concept:name'] = df['nr_processo'] \n",
    "    df_log['time:timestamp'] = df['dt_lancamento_movimento']\n",
    "    df_log['concept:name'] = df['ds_movimento_complementos']\n",
    "    #log_processos = dataframe_utils.convert_timestamp_columns_in_df(df_log)\n",
    "    log_processos = df_log\n",
    "    log_processos = log_processos.sort_values('time:timestamp')\n",
    "    event_log_processos = log_converter.apply(log_processos)\n",
    "    xes_exporter.apply(event_log_processos, caminho_exportacao_log)\n",
    "    return event_log_processos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "metadata": {},
   "outputs": [],
   "source": [
    "def exporta_log_varas(litigante,caminho_exportacao_log_litigante):\n",
    "    varas_litigante = obtem_varas_litigante(litigante)\n",
    "    for vara in varas_litigante:\n",
    "        #print(vara)\n",
    "        caminho_vara = caminho_exportacao_log_litigante+f'{vara}/'\n",
    "        if not os.path.exists(caminho_vara):\n",
    "            os.makedirs(caminho_vara)\n",
    "        sql_str = cria_sql(litigante,str(vara))\n",
    "        df = pd.read_sql(sql_str,engine)\n",
    "        event_log_processos = exporta_log(df,caminho_vara + f'{litigante}V{vara}.xes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [],
   "source": [
    "def exporta_log_geral(caminho_exportacao):\n",
    "    if not os.path.exists(caminho_exportacao):\n",
    "        os.makedirs(caminho_exportacao)\n",
    "    sql_str = cria_sql(\"\",\"\")\n",
    "    df = pd.read_sql(sql_str,engine)\n",
    "    event_log_processos = exporta_log(df,caminho_exportacao + 'ProcessoGeral.xes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {},
   "outputs": [],
   "source": [
    "def exporta_logs(caminho_exportacao,engine,litigantes):\n",
    "    print('Obtenção de logs')\n",
    "\n",
    "    exporta_log_geral(caminho_exportacao)\n",
    "\n",
    "    for dados_litigante in litigantes:\n",
    "        litigante = dados_litigante[0]\n",
    "        print(litigante)\n",
    "        sql_str = cria_sql(litigante,'')\n",
    "        df = pd.read_sql(sql_str,engine)\n",
    "        caminho_exportacao_log = f'{caminho_exportacao}'+f'{litigante}/'\n",
    "        if not os.path.exists(caminho_exportacao_log):\n",
    "            os.makedirs(caminho_exportacao_log)\n",
    "        event_log_processos = exporta_log(df,caminho_exportacao_log + f'{litigante}.xes')\n",
    "        obtem_varas_litigante(litigante)\n",
    "        exporta_log_varas(litigante,caminho_exportacao_log)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Process Discovery"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "metadata": {},
   "outputs": [],
   "source": [
    "# inductive miner\n",
    "def descobre_processo_im(event_log_processos,caminho_exportacao_processo,nome_arquivo):\n",
    "    \n",
    "    if nome_arquivo == '00360305':\n",
    "        noise_thresold = 0.3\n",
    "    else:\n",
    "        noise_thresold = 0.2\n",
    "        \n",
    "    net, initial_marking, final_marking = inductive_miner.apply(event_log_processos, variant=inductive_miner.Variants.IMf,parameters={\n",
    "            inductive_miner.Variants.IMf.value.Parameters.NOISE_THRESHOLD: noise_thresold})\n",
    "    \n",
    "    parameters = {pn_visualizer.Variants.WO_DECORATION.value.Parameters.FORMAT:\"png\"}\n",
    "    gviz = pn_visualizer.apply(net, initial_marking, final_marking, parameters=parameters) \n",
    "    pn_visualizer.save(gviz, caminho_exportacao_processo + f'{nome_arquivo}.png')\n",
    "    #pn_visualizer.view(gviz)\n",
    "    gviz = pn_visualizer.apply(net, initial_marking, final_marking, parameters=parameters, variant=pn_visualizer.Variants.FREQUENCY, log=event_log_processos)\n",
    "    pn_visualizer.save(gviz, caminho_exportacao_processo + f'{nome_arquivo}_frequencia.png')\n",
    "    gviz = pn_visualizer.apply(net, initial_marking, final_marking, parameters=parameters, variant=pn_visualizer.Variants.PERFORMANCE, log=event_log_processos)\n",
    "    pn_visualizer.save(gviz, caminho_exportacao_processo + f'{nome_arquivo}_desempenho.png')\n",
    "    # exporta processos\n",
    "    pnml_exporter.apply(net, initial_marking, caminho_exportacao_processo + f'{nome_arquivo}_petri_final.pnml', final_marking=final_marking)\n",
    "#    pn_visualizer.view(gviz)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "metadata": {},
   "outputs": [],
   "source": [
    "def descobre_processo_varas(litigante,caminho_log_litigante):\n",
    "    varas_litigante = obtem_varas_litigante(litigante)\n",
    "    for vara in varas_litigante:\n",
    "        #print(vara)\n",
    "        caminho_log_vara = caminho_log_litigante+f'{vara}/'\n",
    "        caminho_arquivo_vara = caminho_log_vara+f'{litigante}V{vara}.xes'\n",
    "        event_log_processos = xes_importer.apply(caminho_arquivo_vara)\n",
    "        descobre_processo_im(event_log_processos,caminho_log_vara,f'{litigante}V{vara}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "metadata": {},
   "outputs": [],
   "source": [
    "def descobre_processo_geral(caminho_exportacao):\n",
    "    caminho_arquivo_geral = caminho_exportacao+'ProcessoGeral.xes'\n",
    "    event_log_processos = xes_importer.apply(caminho_arquivo_geral)\n",
    "    descobre_processo_im(event_log_processos,caminho_exportacao,'ProcessoGeral')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [],
   "source": [
    "def descobre_processos(caminho_exportacao):\n",
    "    print('Descoberta de processos')\n",
    "    descobre_processo_geral(caminho_exportacao)\n",
    "    caminhos_log = glob.glob(f'{caminho_exportacao}*/')\n",
    "\n",
    "    for caminho_log in caminhos_log:\n",
    "        litigante = caminho_log.split('/')[-2]\n",
    "        print(litigante)\n",
    "        caminho_arquivo_log = f'{caminho_log}{litigante}.xes'\n",
    "        event_log_processos = xes_importer.apply(caminho_arquivo_log)\n",
    "        descobre_processo_im(event_log_processos,caminho_log,litigante)\n",
    "        descobre_processo_varas(litigante,caminho_log)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Fitness"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calcula_fitness(net, initial_marking, final_marking, caminho_arquivo_log, nome_arquivo_fitness):\n",
    "    log = xes_importer.apply(caminho_arquivo_log)\n",
    "    fitness = replay_fitness_evaluator.apply(log, net, initial_marking, final_marking, variant=replay_fitness_evaluator.Variants.ALIGNMENT_BASED)\n",
    "    caminho_array = caminho_arquivo_log.split('/')\n",
    "    del(caminho_array[-1])\n",
    "    arquivo_fitness = \"/\".join(caminho_array)\n",
    "    with open(f'{arquivo_fitness}/{nome_arquivo_fitness}.json', 'w') as outfile:\n",
    "        json.dump(fitness, outfile)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calcula_fitness_varas(litigante,caminho_log_litigante):\n",
    "    print(f'Fitness das varas do {litigante}')\n",
    "    net_litigante, initial_marking_litigante, final_marking_litigante = pnml_importer.apply(f'{caminho_log_litigante}{litigante}_petri_final.pnml')\n",
    "    varas_litigante = obtem_varas_litigante(litigante)\n",
    "    for vara in varas_litigante:\n",
    "        #print(vara)\n",
    "        caminho_log_vara = caminho_log_litigante+f'{vara}/'\n",
    "        caminho_arquivo_vara = caminho_log_vara+f'{litigante}V{vara}.xes'\n",
    "        nome_arquivo_fitness = f'FitnessLitigante{litigante}Vara{vara}'\n",
    "        calcula_fitness(net_litigante, initial_marking_litigante, final_marking_litigante, caminho_arquivo_vara, nome_arquivo_fitness)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calcula_fitness_processos(caminho_exportacao):\n",
    "    print('Fitness de processos')\n",
    "\n",
    "    # Processos litigantes x processo geral\n",
    "\n",
    "    print('Fitness litigante x processo geral')\n",
    "    net_geral, initial_marking_geral, final_marking_geral = pnml_importer.apply(f'{caminho_exportacao}ProcessoGeral_petri_final.pnml')\n",
    "\n",
    "    caminhos_log = glob.glob(f'{caminho_exportacao}*/')\n",
    "    for caminho_log in caminhos_log:\n",
    "        litigante = caminho_log.split('/')[-2]\n",
    "        print(litigante)\n",
    "        caminho_arquivo_log = f'{caminho_log}{litigante}.xes'\n",
    "        nome_arquivo_fitness = f'FitnessProcGeral{litigante}'\n",
    "        #calcula_fitness(net_geral, initial_marking_geral, final_marking_geral, caminho_arquivo_log, nome_arquivo_fitness)\n",
    "        calcula_fitness_varas(litigante,caminho_log)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [],
   "source": [
    "def run():\n",
    "    caminho_exportacao = '/home/dataeng/Inova/AnaliseLitigantes/'\n",
    "    engine = obtem_conexao()\n",
    "    litigantes = ['60701190','00360305']\n",
    "    exporta_logs(caminho_exportacao,engine,dados_litigantes)\n",
    "    descobre_processos(caminho_exportacao)\n",
    "    calcula_fitness_processos(caminho_exportacao)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Obtenção de logs\n",
      "60701190\n",
      "00360305\n",
      "Descoberta de processos\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "fd1bddefd4e348939dfa6faf1dc0b8c2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2319.0), HTML(val…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "60701190\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e4673fccbf424810ad16603b790013d6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=331.0), HTML(valu…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b46b0b6e8bd34c4999270f7efcecebe0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4ef63d0bb4464aa48cf2ed260bd935df",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e3c9e7f4594943ff9d25fd6e363dc5f0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a82f98bd903c41659e02014c9d69e998",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "18a91edcc6964b259fd0c2a81e1721bc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "accc3324af5b43409b6a0b0f60d8e9b0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5d9fe11fa2c74fbb8db84525dd873583",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3a2a3e5d7c3340b4b301a7acd2386f28",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1616e48c8e924cb8955a703a452a8d35",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8b2e30fbf7714f2f9ec9a904215307f3",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e397f07ad83442e899c3f48fd2680a5d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ae54d71ef36d4411ab413fa7b485bdfc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "67e61757622c475a8a540638c97364cf",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=10.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "528dd9e2d84d4a4a85ae943d72fe89de",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6978c94e035f4856ac8a2c6769cc0cfe",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "77745465db0547a3b13fca8d25a349e9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b271eb7008c146cca3535b0cb17a248d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1083f8477b8341cbb5f8cf1a40e1d14c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "701c46bbf93048cc88e42884173b0ddf",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "469dbd2d1cc843f99515e3b8a07c935d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "db9a033fc41b4853834ccc2cc009a003",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f8cdedeebb77482d9566c239eb9320b9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a2ead461940c4d8dba414e723274b761",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ef7d49bdf57a484baa43e70b8868a1e9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "65caf620c486432fb88047c86ab37099",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1d3340586d264501ba1ff3b45f3d8e5d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c693b8c4c844403cbbe94cf68a940f16",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=10.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "370cdd4b6c7e461fae2c1529e0df5732",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e17c3546b7bf4a168c4f59b9928d2346",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "14559f1fcc6b424f8bf5cadd6efd29c2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "69781be501aa45ce81f505ef4132f244",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ad1bb52fe4f4472f8737fb65ee92ffce",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "150fcaf7285443d695bb8c3ac3525814",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=10.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "17e37bd9b35847fd983499d3014a6cf9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f7a02b814de240e5b38650be7fda06a2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3b8e63f746794e5fae898405e8caa5c0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c59368ff54d14c29ab6400a6490f224c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "254f8a3781ad453ab2e7d5e8a3139dd0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "61e6d30e4cb846f2b6d5e3a99b7e8a16",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d4415cacb87f498693beb433eb67876c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "efc6fd95883544e7a9c5b858c1c2a528",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "94d764c29a7f465d8d0099a4057433b3",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0f5c6ae8016c4bb6baae75ea82a6fd43",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "fb34d37fa28a44858983ef884bdbe067",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "842dffa195d344899955523c374a23fa",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e10abf56433340e39fbfc313b38bd5c7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bc2dd30825fd471f919f5e0341a3a663",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "53473f45ce2143ea993f67ee6a9cb4a2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9e90b18d29cf4ebabbc6ab2a637080cb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "170b2097c56a4874bde4d45c4f5c4629",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "880b0d71942f4030b4a871b28fc018e9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d06f1bb88a7f4df9b9df69bc4f7b1590",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "747fd5316be4489992aeda6f25e68d57",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f9896beefc8f42d8aafc078302c44326",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=9.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3bbdc058b93a465888e06c395b65c448",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a69e1fd8b45e43f99c87d21a31735673",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2210d12ef6714fc7967716d4334e8831",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "76c7bd2ec884469684975f9ba6148ffa",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2ab5e30af780497c860aef05f2fb6dd2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e0da6b3539f24613a9e3881a33c95ee6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c852b9359ec342a6a5194a03d18643a5",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c6141aacf0ff4ec69114614efc8b9524",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6059b34bf9ad45babddeb2da36f303ba",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5d94b945ec734be0ac5439db23627396",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ef6370e2b4894db18c00576cd1268c5e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "62fa8d178306484f9d80969ff6f2d81a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "37467303660e472fbe97c94db0ba3258",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9b9c31d4c4d94e36bbb324a45a541d3c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=12.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "adb1a1fcdbc54ec4ab1f76a88ee53a2d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a7153ff650914bf3b8628a28f80399c4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2c73c158e0ff4414b2cc0ae730b7b149",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c2810b61dcf44f278b701cd79a8ef07e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0ab357d57f834035a5c66905e1823a54",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1adda25ac82346bb8db6922807e3475a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ce9f74d99af94aec81e3d9da0d433d40",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "09e01d2e665a41188f971dad4912a43d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0415764756fe44adad93a2172bde5cc8",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "710ee2171d2b4b6e8b93407b95aeed30",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d0413682e4c94b9398d2c6a0cc97bb39",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9691bdf59fbc4e0d99abd6cb51b967df",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2e6d1b0a96c34b5ea38ce94f58fe137b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "51bf45995d684546b09ef94d10fe130e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ca4b12a7d77648e8b6745becd584da23",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "66cfd99dbb494fbd97cdd7f8b5927a15",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=9.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "245c60c64e3140a0a911fae19ab43e7d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6a89a109aed7462aa37ab5a1c48abcef",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "48e5f829077941e9bca3540f645175ce",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=10.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "cc7ec3fd616347e28398eeba778fe7dc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3d86d781437f44ca90fb4eb8b9eec0ed",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2e0c4605d0fe444d98b60abc4f6381c3",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c804c3d41a9b46289a6185e5991475c5",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ec89b40aa8004f16b14798cdbbd1cd76",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "696228bf9d12417684e4b49dd723fc55",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b00f8f415df44ad88f9946da56d56203",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e208e7d2957d4da5890c9cd84fb0bfd1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f03c6f65999148e8b8e61e6b487148cf",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e96d60fc4c2d4d658d628edf4619623a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "00360305\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9c53162edb1347a78fb35684caa8396b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=298.0), HTML(valu…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "de27887f9f6b482ab905c8814eb2a7d9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bfa6b780014a4f4485b6625c1bbfb071",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ba3114a84af346eaac4ec42f5fe7912f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "df31cd8429ad4df98ddddb415f86ad82",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "55a1d3b4f40044d0aedcb779ae2838ad",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a46fec9345cd4a1bbdb78e9f1e46617b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=10.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3fd7a3fa73c34daab25a3e3a48e18f63",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9408ac6678b54c5bbe30de14e7de85fe",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ec6b2e7870d045b0836ead4524cdf699",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "95b5a357684b4d758c8f8c80a6e759aa",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1c152aff347d44539e09a3b65c0d3eac",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f71c1d1dbab24e0a9820cfdcdc181b1d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8935db27f7174e609ab42aad928ee9c0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f34989bd4a5a42cebe3a179caf143a68",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "161d34e6bdd0478dacad2abd1f565259",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9d086160a3f64c328c52f3d1d562637a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "97bcda0c2f03403a9f77d8c1d372e219",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "96d074f7733f4120be0da528bc21f22e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ad69dff103654c3da63cd746cf9ddc25",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a440fadf54864e44b4b3595feb3e656f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "24c81ac0f9084d7e80da1596f4c5c691",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dad4fa408bff4625aea4eb809205e722",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "63fe0359c2714e35b6bccc4aa8f71c22",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "05966fd8b8b543bc8fb9d313687f2222",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3139be4d93d946b3aa5b1838ce8947ba",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0772e78ad8f842f2949b2a0b94376f0a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d0d46452525b4e69a056e1f89fa5f8a9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ff8281b546384e56af55ab04e9406086",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "23034e1c2d6144c8ac529da92aabd062",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "67b2d937562a484ca424d40d1d3cdc99",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9b7d84191495484f8cafd9e9f3df6bb1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b73e2d6aba4e4cc18611261eac521ef2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1c8a091f4bc24b21992d88180a3e3263",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "57d6bf4d6684488fadfa2631baf67988",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "43013bde6c774d06b76c447020d0ff9e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9dd13aa10eec419f9584e14c257161b4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "01f80ba1f06b4a519f6e5efe02228fc6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8ad5fff60ea1488fa543eff6065acb65",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "324faec3f1824116a9dc71512445e592",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b858bb8cb21b436f87cf22f07a4b11dd",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c4895b54eed24f6fbca98a7ee9b1bc3c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8cdc7f4b38a749a7a1b0a5a94c85ae08",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1884862f6951469892f6a30e1a689266",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1f885eed6d7e409591b306fb94149e50",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "12ab3a7d02b041c68a31698513df72a6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "38a345d626a242698904d961d0914acb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a815da6a250040b084b2ec361a7256a2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6653433f9d3d4fc69c796ce661ae39f4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6dd040852c09490289ef6b8239ac45d9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "41c9b47d5e7746b0b7758a9f3e152e23",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ff5d6e0a21a84ab6b8df8b6bb5fdaabc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c2043ab89d9544e195c20392106549e1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6563c11f0d37443d99b115168d2b5426",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5be9544d957447bdbacad1bbbd21654a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7edf5a62e7ff482d85a2e5e9ca2f6ba0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "977c75b1d4a64d3ea3346fcfa4fb3f6f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "525c9563ff574d39afbbeefea977fca9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b44d0bdbd665475f89dec5b3bf4884fa",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8323fc6260e34d788d101f00a76b52a8",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ef4e1155fdda4dc78eaf2275a0d1ff7c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4b23cbef3eec4c5a88cded55089814bf",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1d93adb04e6340edbfe599acc48fad39",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "92ac2a87e89c4bf7b68b2cf562dd531f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "deac60295aa54c09aef3954cd90a5a21",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "59416667f5da4f89bda93e460ba333f0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ea4ee67d8db94e9f909eddab18cfa718",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4716121e9c7c42d9bf09a5f9412b38db",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8bc6d3951d3943098ee099ac5aefacaa",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2b9f4ca24e824830817658b4538cca32",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9c57233f74f947698ae83cc4bb1f675e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a84db6ce6210487b9a7668465162a896",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4328bc1bba84445e8c0b603ebb644463",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4914b377690045cf95e04250f7272fa9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b267937a7e3f4c5fbc4c7a54f1ca8e92",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f6de2d161558449ca84afa389846fd9e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2e8b0d2bdd414a218206c6513ef751e0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4424c32df55d478991665db9441b5991",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e1c8b4fc58514feb86fb21589cc33cfe",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5201d02039284543b824a0ecac5d8678",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f43a8620455745ff8fc762595def020e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8d927d6bd6f64c0ca0c987912c9dd3ee",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7f2ba1fcd78e468e928c4352bfac7991",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0a165ce43792475398dc66a1e8a03bde",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "384115802355413d826a97e955127427",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5938188ab3034d33a32d62d60ef5dd38",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6d2972596a064cd6aaf5dddde5e5bf85",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=13.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c4f8aa6e74284663b39a3ae3e1b602bb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6e2bcbf3215641d0880a0542a135a313",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d7f394967ef4456a900979075544933c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d59c1d08c91d496f97d4f3ac7c6d2073",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "82dbef6df0814ae5a0799ea5cee5f579",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "411e2dd377044314b29d8e29c43c5961",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a1bcb03077054620993b7958118e3da1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4cd9a035ee394fd9820d600d42b575d6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "be7486c97fe74927a61cb2cca246fe26",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "030f3232833a4759a03f8e09835c3ab3",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "19dad3779e2f41c9b11d5f51f814a577",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0feda43b2ab7435092bc5bf32ce16023",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d378f1892a854da19382ccf72917a5d7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "53a06a423a6d477bb1504a34072efdcf",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b4d6da9fa1334de282b3a993e0a16cef",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "fecb239d91b14151b09a6fe2aa582b08",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0b21a6ae32b6474c8b61dbc0cd83a521",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3f4b3e54d84b4dab8d2f3eae4363121f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "946770732942483da6cdec193386ae76",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0e36a204be134e619bb9afea670b04ae",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "02ba1f8eb1ff4472a140994f6cb3776a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "fa02fffb897f42d09d3a96431cd42aed",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8f73dca2eae6427e9a8fd574cf13de69",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bb3b67be8a734398be4493d615e2b700",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "14547a71bfc34658884dce92a1a2dcb6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "494f7b8c1a9a4ad78b4f904c3bcb59a6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "023cc01091c94adbab082c91d24bf12e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Fitness de processos\n",
      "Fitness litigante x processo geral\n",
      "60701190\n",
      "Fitness das varas do 60701190\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6ecc9f9fc0b54155a88377a5954bdb8b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b848eb2a7a7d40a793910879a52f2791",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d346f883c2ee4d7491bc75e415d70e93",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3064289a0bad4612ab40443f26e88242",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "41ec8b31b0f34eedbc5ef2628c83db46",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "55aa2809dd344ecd87dffcf2b373f2d8",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "adf0b66f80f24504bb4e5e4c2f0af2ee",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b2182824c68147f99f38297706de041c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "edfcbd00aaa34da5a6139de7a632b8fc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5bd37a5801074a18a1a2821711cf1f31",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "fc255b8c68f24ea387fd81accbe46a27",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "87ad7f818e6b4cc7aa1f6533e21cceae",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "42ad202f6113487cac1569da314c3d94",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=10.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "90ae1418ae5f43f3ba6ce46881def430",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "225fc3f7bec4470fb60c4bbe4607c0a9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "90e443ea00c54d5db4446fb47ce635cf",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "75de4a5fec684573b404e5f34c40f9d8",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0f0535f96d0146a8bbc68128316fd956",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "892724cd555a42fa8f6f43758e173eaa",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ddc1dd62eb984be6af27cb1c18dc87ac",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9b667992ea234d7fa148a390527d2ea7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2a5e3f25fc7e47e39123fd52bebb834b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "246f736508f64e698fd52d1bd8889fcb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b52b5d80e81b4316af37731f1bcabb7f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0b84ae951d3341ddbfa9329a78ebd280",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b2348cbf3b08486283fb088eafc8651b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9816dbdd28d34faea9adc0eabd3d0e8a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=10.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dc69066ce2c64220956000431fc7113b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1b7bf1dcb20e4a86a2c678d2382cd1e2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9caf5899df374c359221ebea5da3ed37",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1be87a2357c342c999d90c7fbeeae51f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "da8434eff5e24d9cade25b56ff6b9010",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b1a3429d7c05460ab4589311e0520e8d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=10.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e6da0d05e50d40b39c666ac7c9b0146d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0b362b687eec4d878ede7e28cb8560dc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b63c3cb7efe3482788ea6d0f6e8d04b1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "fb0d58b6471a4aaeb3e6f215404b2d99",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "85fa4ef0b1a5493e8e19571f6efab6af",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3217157223b645ae9a1a735235dec37b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7999b259e36a41fa8e46d62d73171e56",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c5f2c75fac094ad98122a409d3fb1336",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "538aba378be44e7481f4a40248b9f0ac",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0035347bac6044d3a16ab4ccd853fc3a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f025f1545cf140c8bac1aac78d9f2854",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "767f88a705d14a2abaf42d7f3144296c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "82a36ead49f44f65959a77ef7171b779",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "20583c007ba64ea589927148bc2532c9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0c002ae870f741f59b6668282ce56539",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3b011ccff95c49d6a84a67e4e4ac23cd",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c0d6ab2f7fff4f28bb6aeb30a0732d6d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e1272950e9ac41638a1745d22bc4510d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "77bcf322f1c7410e9f3eda432a688109",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "78472c011dad4e93854215795a774444",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "62ddae5ac0924e76844a765c4de3d6a2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=9.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8444c8679dd544c596f0af774464f2f4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d9eb15a273f0431ebda77bc033aa25ae",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dc8e3473679b463b9512e5b0013f4747",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "580a039ffc254f499326c3cf9ab6f7bb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "29c0154ee0a34d8b9529224749f35579",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ce375f4542ac410585ccf154367a2b9d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "146325e58f0e4857a6514dc713bb3765",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0854f0dee63245e6ae26152940fa1153",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2e7d9f910db542e88f0d2f253b358e53",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1b659864e7654f889799d119c23a2521",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ea1725c723a84ca8ada62e5d722ca785",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d4e3dc2e28264ff2bbcfda2e9dd27edb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1a158a8acf6843e3b7ea717dcb8a0603",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "29700f089a7a4dccaa083df31377e96b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=12.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "91b34c38c44c4bcc8e5c33d94c443c0c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5f8360ad2b8548b4ae9f85d7c7cf920b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9f7e1f3efce54485b883ce1b2cf0338c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d3b2b7a29b004102813244030630babc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0255e16f9c7240d3a8f3f3f0c25742db",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1d1845dd1388408b8c99d968c7050701",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b2f150d3e9774d828430c4872f5d1ad9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8c1ceff717d34f9bab5a079c169ea1cd",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "173f7b58c35d44c2930c07471489e44d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "593859cf505346eca229005e4a9e89a0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "634bb728a4fa44db8171b5039b453a43",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f1094f1f8cd44e58901580644d53405b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6bd26c96a656453393c6b9756923c02d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e24b3420535f4bc0813e042948ce3e5e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "77e85d3c56204feba478d2385cf2fb3d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1ed18d04f7c94cae806ba7506ea1defe",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=9.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "754736ca06b2477bb0d8dabe255f05ff",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d151458bcca34995abbd10b1012e4d3f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "731808729968471da80b1741171cdb21",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=10.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "177d652d9ced4917a9055d5116ec8652",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "206ab55140424660ac4287aad8860255",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "13b81f5fa6e34612a984b8c84fcd6ba4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "47bd0207a0394218b3de13398927e598",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "32e478af9ad443b0ad69669defa9b185",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "febcb851b7cf4f9394ccbd952df66edd",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "16c7036999754bdba5f1b99784e0ed52",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "79facbfea12045db842dae221a59fff0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "198ce23df35c45bdb9dadaf903b70c74",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e7b957927364443b99ade7c7877bab22",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "00360305\n",
      "Fitness das varas do 00360305\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b1c424055f3e49b4aa466d4cef0da269",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8f102d55dede4446b4382b6f201de949",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "83392453b5394b81a6d30d5f130dca78",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "256895d2a5ac4db8bad95e0932fb558c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6c4a2a9421434ad1a272e7d0ef348103",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "132b2814494e46d2bc2a01bb11049ff1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=10.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b1d4c1497a9744b380a7f8cf56d3c375",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0dc78d6f713b4e628a1978edfad7e481",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2e4207c4582942d2a54372b186026a64",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "534749244eeb4e2b8d205ca446019ed2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "eeb1bd81375a4fdb94ddd8c26c63dc28",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "50477ea463384e95bcb61fc779035188",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "cd84651647184b3abbd04a7e1f8fdab2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e6b2a35b28e94e6ab449db38f367967d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "76c869e13fdd483caeedffca5cd27115",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9dd15f34dca848c19f6da42f23d625ec",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "574337dda7014228aa012f25ace80db5",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "17d719796d894423bf2d34e6cb30e6ef",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9a1e954860fa466aaae82ef831bec5e4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "62871a7e84f7446ea214c36078e3a20e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0f61380b2e254b1e8403a76f0cb3dc75",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1aa994ebe23d4b439e659efb52e82c90",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=7.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5b5afc0367704b509b03e6b441046a4f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "fb3c852f457a4e34be2939526ef0d461",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "950fd8f8f61b47f4a9c7390895b22f68",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "383bb83554284caabd7922c1800ca79e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "faf994f2fa524a07a5d23e651affd0d7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e55f9dcfbf0b4756a6c178cdcd732976",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "09ddcd7ec37b4258bfb7274f2300bc62",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "693d2e4a227246128252a4fa8013e8dd",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "31895774d96f49c3bb947405b13523e1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "33ac3e67d75c4706be408d349cca4338",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "40a42275b0c746af9236b192facee3f2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d845430c39e44dceb771d6818e65ccd1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "cbd807f0e8c242dca432bb153f9ec90a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a3888eb6b091478aad193430653aa65e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "20b0b641cd41493f87f022fb84a28d74",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8f58f2bff4044d6890a70384d7f40db7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4e75158d569e4ad6b924346752925feb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b6727d1b6d2b44f19d40155524d76199",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "06d59cdb6f564eaf88875d6446b30090",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7e49fc22c3414c439b8d9087e1a3162b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d8bc439fe98c4310b211e002e21e15aa",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "92427f82fc1b4d54b686d2aced9fa406",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a83dfc72e38844c5b637c6c0b9948d52",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e1119f34376b49b2adba72a310c58f15",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c41395e48d2344aea952b10e7227b29d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "40865540205d4bf0a5c2477512587828",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7d6d8465f2d44b1cba048a09ee487141",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0488881156eb401eb5e8228d765994e5",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "609b13b6981a4e4eafd742fbef9a04da",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dde061a9fd9345ff8e512670ee3cba1a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "52014f959e0d41a89e567506b328941f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "15b651789d56475fbfb5a09158da57ed",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dfb4435ecf6844099eac6bc7655be37b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "abb8f853e5004bcf86ef1b990b852690",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e8d6ec4f6f524a08a9b90ac13ac99da0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bea564f144d147c2a2bae2dca56bdaa8",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "36c2686647a343d2bc9969f51c5ce690",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dcde3f0ca79a4d1bac5964cf730e9643",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "88d81c729fcd4febac1489bf1deccc66",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=6.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "69983875d815441d88b2ced8493bfc19",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e6e7545fc359435eb5a0736f9d8db935",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dddcbb3f74674452a95d264de4c5ad3c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d47b1155a6aa4828aef3aa6e47835fa6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f96a6588c3d448ee89de8b9458a5f6d6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "96cdaddbba964414bef7ad6a79c2f5f0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "06d89d630ee041aa9f0b28e2365141e4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "68fadbc5ff104febbc4cc50f00760011",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e628e24d3a984c35a07a4722b5375825",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e8cd0ff6cfa64190885bcb8465a40876",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "963a23f961614931bb01c0f4db560fc7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8dee89f1a3a84503ba29278da87afea5",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4d76e13afdd045d185d2331616210d93",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "baef4367436649a8bb5be758deb7fd27",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "638fe21eec9341aea90a1d729afc01cb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7cfb4746474f4fcda7d2506d5fb7f1f2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "17d776764ff44866ba0f4efad4e8f529",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "db54f0632ec94f1f943e201a1c421428",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0be883c4d8434aef933ac21cb8cc4043",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "40cd417f5775473a95e8c22b9177b67c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4d026b60289c42f8b47561fd6ba38c2d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "713c94f2ab9d42f4aa62a8dd6caa3334",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c7e9a62bd1a740b086b6763fc9c83da7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "510db28c84c14785b23470290edb08bd",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "cf7a01d750bb45c580b9c9ec7c666de6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=13.0), HTML(value…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7bb09fb258b643e4bee66795a1d7dfed",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=4.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dcad1232e58e49d7a7b1e582ea96cefa",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "76c83a21153641b580706d2daae61d6e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d452bfe6ecea42a6b2b66c3a74542779",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "09c8777b13de49f893f70e6220ae4b7d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4825ed6fb2c045c883d7b81f1badc078",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "73e7ab2f2fe5442aa8111d59cf3f0a87",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ec8a827790b24c8ebe711eb059fe6c94",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=8.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "01cbd076f70f4b14af0556641876dd5c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0e1639267c394bcda80f1e2d0f982aeb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ec3c10130dda40e7a43143bbd931ec4a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=5.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "931dcb74cbf34a74af2c0a475b1988e5",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5582820382434ae5985a25bb8888f24e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4bfae7a6dbc54ff1b66a0ad40b5755b2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5126d295afab4f7fb684b3814b04eb29",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "00cb0488978d400ab5ae7e7b452d96d5",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7fd0b375c5e24cf6861555d8cec0ac1d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d19880e03a0046c7a791338d0789d36c",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "35fb65b84de94aea98b5e0bc777b51de",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5981bf82dc7a43d69958842ddc7ea4d7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ba8a7c2bd16b458db7fc56dedba0ab5a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d34d51edc2104bf7981f508de01d9f75",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5ae574a66b4448f8a7b54fba56fc7996",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "232e1fdb9c35435cb1b1b5b763ee1008",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8dc4e54089d14d9086c1b9db1397aa49",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=1.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "fbf553cf820d46daad4485b7bd912459",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=2.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4b5987790ad2403db80144d1f95a06b4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(HTML(value='parsing log, completed traces :: '), FloatProgress(value=0.0, max=3.0), HTML(value=…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "run()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Alinment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Alignment\n",
    "#from pm4py.algo.discovery.inductive import algorithm as inductive_miner\n",
    "#from pm4py.algo.conformance.alignments import algorithm as alignments\n",
    "\n",
    "#net, initial_marking, final_marking = inductive_miner.apply(event_log_processos, variant=inductive_miner.Variants.IM)\n",
    "#aligned_traces = alignments.apply_log(event_log_processos2, net, initial_marking, final_marking)\n",
    "#print(aligned_traces)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
