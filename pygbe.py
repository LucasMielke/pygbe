## pygbe.py

def igbe_pam(ano="2019",var="216",loc="1",geo="1",rel="5457"):
    
    import pandas as pd
    from pandas.io.json import json_normalize
    import requests
    
    url = "https://servicodados.ibge.gov.br/api/v3/agregados/"+rel+"/periodos/"+ano+"/variaveis/"+var+"%7C214%7C215?localidades=N"+geo+"["+loc+"]&classificacao=782[all]"
    dataAPI = requests.get(url) #request get do api - url formado acima
    dic = dataAPI.json() #convertendo em json
    dados = pd.json_normalize(dic,record_path=['resultados','series'],meta=['variavel','unidade',"id"]) #usando normalize pela primeira vez 
    dados2 = pd.json_normalize(dic,record_path=['resultados','classificacoes'],meta=['variavel','unidade']) 
    dados3 = dados.merge(dados2, left_index=True, right_index=True)
    
    del dataAPI
    del dic
    del dados
    del dados2
    
    dados3.drop(columns=['localidade.id', 'localidade.nivel.id', 'localidade.nivel.nome','id_x','id_y','variavel_y',
       'unidade_y'],inplace=True) #removo essas colunas
    dados3.rename(columns={'serie.'+ano: 'valor', 'variavel_x':'variavel', 'unidade_x':'unidade','localidade.nome':'localidade'},inplace=True)
    #renomeio as colunas acima, inclusive a "série.2019" (serie.+ano)
    
    #https://stackoverflow.com/questions/33098383/merge-multiple-column-values-into-one-column-in-python-pandas
    dados3['Categoria'] = dados3.filter(like="categoria").apply(lambda x: ','.join(x.dropna().astype(str)),axis=1)
    
    dados3["ano"]=ano
    
    for coluna in dados3.columns:
        if coluna[:10] =="categoria.":
            dados3.drop(columns=[coluna],inplace=True)
    
    return dados3 

def ibge_help(a="pt"):
    if a == "pt":
        print("1- Para ver os códigos das cidades acesse: https://www.ibge.gov.br/explica/codigos-dos-municipios.php\n")
        print("2- Acesse o Querybuilder para ideia dos parametros: https://servicodados.ibge.gov.br/api/docs/agregados?versao=3#api-bq\n")
        print("3- geo é o nível geográfico. Use geo=1 para Brasil, geo=2 para Regiao (N,S,SE,NO,CO), geo=3 para estados, geo=6 para municipio, geo=8 para mesoregião, geo=9 para microregiao")
    else: 
        print("1- To see the location codes, go to: https://www.ibge.gov.br/explica/codigos-dos-municipios.php\n")
        print("2- To see the Querybuilder, go to: https://servicodados.ibge.gov.br/api/docs/agregados?versao=3#api-bq\n")        
        print("3- geo is the 'nível geográfico'. Use geo=1 for Brazil, geo=2 for Region (N,S,SE,NW,CW), geo=3 for states, geo=6 for cities, geo=8 for mesoregion, geo=9 for microregion")