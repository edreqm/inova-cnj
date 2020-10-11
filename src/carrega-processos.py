import json
import argparse
import os
import re
import pandas as pd

padrao_array = re.compile("(.*)\[(.*)\](?:\{(.*)\})?")

def recuperar_campo(elemento_processo, nome_campo, i):
    array_predicado = padrao_array.match(nome_campo[i])
    if array_predicado is None:
        if i == len(nome_campo)-1:
            return elemento_processo.get(nome_campo[i])
        else:
            val_elemento_tmp = elemento_processo.get(nome_campo[i])
            if val_elemento_tmp is not None:
                return recuperar_campo(elemento_processo[nome_campo[i]], nome_campo, i+1)
            else:
                return None
    else:
        nome_campo_array = array_predicado.group(1)
        predicado = array_predicado.group(2)
        campos_grupo = array_predicado.group(3)
        itens = elemento_processo[nome_campo_array]
        campo_predicado = None
        valor_esperado_campo_predicado = None
        if predicado != "":
            predicado = predicado.split("=")
            campo_predicado = predicado[0]
            valor_esperado_campo_predicado = predicado[1].replace("'","")

        valores = []

        # Faz loop no array de elementos do processo
        for index, item in enumerate(itens):

            valores_grupo = "#$%"

            if campos_grupo is not None:
                campos_item_grupo = campos_grupo.split(",")
                campos_item_grupo = [x.split(".") for x in campos_item_grupo]
                
                # Busca cada um dos campos para agrupar os valores
                valores_grupo = {}
                for campo_item_grupo in campos_item_grupo:
                    val = "#$%"
                    if campo_predicado is not None:
                        valor_campo = item[campo_predicado]
                        if valor_campo == valor_esperado_campo_predicado:
                            val = recuperar_campo(item, campo_item_grupo, 0)
                    else:
                        val = recuperar_campo(item, campo_item_grupo, 0)
                    
                    if val != "#$%":
                        valores_grupo[".".join(campo_item_grupo)] = val
            else:
                if campo_predicado is not None:
                    valor_campo = item[campo_predicado]
                    if valor_campo == valor_esperado_campo_predicado:
                        valores_grupo = recuperar_campo(item, nome_campo, i+1)
                else:
                    valores_grupo = recuperar_campo(item, nome_campo, i+1)
            
            if valores_grupo != "#$%":
                valores.append(valores_grupo)

        return valores

def planificar_processo(processo, campos):
    '''
    Transforma documento do processo em tabela de duas dimensões
    '''
    campos_recuperados = []

    for caminho in campos:
        
        processo_plano = {}
        valor_campo = recuperar_campo(processo, caminho, 0)
        campos_recuperados.append(valor_campo)


    js = {
        "processo": [campos_recuperados]
    }

    with open("/tmp/processo.json", "w") as f:
        json.dump(js, f)

    tabela = pd.read_json("/tmp/processo.json")

    tabela.head()

    print(campos_recuperados)


def carregar_json_processos(arquivo_json):
    '''
    Carrega um arquivo json com processos.
    O deve estar no formato CNJ
    '''
    processos = None
    with open(arquivo_json) as f:
        processos = json.load(f)
    return processos

def planificar_todos(processos, campos, processador_processo):
    '''
    Dada uma lista de objetos carregados a partir do JSON, planifica cada um deles.
    Para cada processo planificado, executa a função especificada no parâmetro processador_processo
    '''
    for processo in processos:
        tabela_processo = planificar_processo(processo, campos)
        if processador_processo is not None:
            processador_processo(tabela_processo)


campos = [
        ["dadosBasicos", "numero"],
        ["dadosBasicos","dataAjuizamento"],
        ["dadosBasicos","classeProcessual"],
        ["dadosBasicos","orgaoJulgador","codigoOrgao"],
        ["dadosBasicos","orgaoJulgador","nomeOrgao"],
        ["dadosBasicos","orgaoJulgador","codigoMunicipioIBGE"],
        ["dadosBasicos","grau"],
        ["dadosBasicos","siglaTribunal"],
        ["dadosBasicos","valorCausa"],
        ["dadosBasicos", "polo[polo='PA']", "parte[]{pessoa.nome,pessoa.numeroDocumentoPrincipal,pessoa.tipoPessoa}"],
        ["dadosBasicos", "polo[polo='AT']", "parte[]{pessoa.nome,pessoa.numeroDocumentoPrincipal,pessoa.tipoPessoa}"],
        ["dadosBasicos","valorCausa"],
        ["dadosBasicos","assunto[]{codigoNacional,principal}"],
        ["movimento[]{movimentoNacional.codigoNacional,dataHora,orgaoJulgador.codigoOrgao,orgaoJulgador.nomeOrgao,orgaoJulgador.codigoMunicipioIBGE}"]
    ] 


def run():

    parser = argparse.ArgumentParser(description='Carrega processo JSON em base relacional')
    parser.add_argument('-pasta_dados', dest='pasta_dados', type=str, required=True,
                    help='Pasta onde estão os arquivos JSON')

    #parser.add_argument('-campos', dest='campos', type=str, required=True,
    #                help='Campos que serão buscados no processo')

    # Carrega cada um dos arquivos
    args = parser.parse_args()

    pasta_dados = args.pasta_dados

    arquivos = os.listdir(pasta_dados)

    #campos = args.campos.split(",")

    for aqr_json in arquivos:
        caminho_arquivo = pasta_dados + "/" + aqr_json
        processos = carregar_json_processos(caminho_arquivo)
        processos = processos["processos"]
        planificar_todos(processos, campos, None)




    pass

run()
