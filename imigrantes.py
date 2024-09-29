import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/wanderson/workplace/datascience/imigrantes_canada.csv') # carregar o arquivo em uma variável 'data frame'
# print(df) exibe o conteúdo do arquivo
# df.info() mostra informações principais do arquivo
df.set_index('País',inplace=True)  # mudar o indice do arquivo e o inplace dispensa a criação de um novo data frame
anos=list(map(str,range(1980,2014)))# criar variável para armazenas as colunas de anos, é criada uma lista e a função MAP serve para aplicar a transformacao do intervalo em string
# print (anos)
brasil=df.loc['Brasil',anos] # pegar somente os dados do Brasil, a propriedade LOC consegue pegar rótulos específicos dentro de um dataframe
argentina=df.loc['Argentina', anos]
# print (brasil)
brasil_dict={'ano':brasil.index.tolist(),'imigrantes':brasil.values.tolist() } #criar um dicionario com os títulos ano e imigrantes pegando da lista brasil os anos e os valores por anos
argentina_dict={'ano':argentina.index.tolist(),'imigrantes':argentina.values.tolist()}

dados_brasil=pd.DataFrame(brasil_dict)
dados_argentina=pd.DataFrame(argentina_dict)
# print(dados_brasil) 

""" Olá! Nessa aula, aprendemos a importar dados de um arquivo CSV para o Pandas e a manipulá-los para extrair informações específicas.

Começamos importando a biblioteca Pandas e carregando o arquivo "imigrantes-canada.csv" que contém dados sobre imigração para o Canadá.

Depois, exploramos o dataframe usando o método info() para entender a estrutura dos dados e verificar se há valores nulos.

Em seguida, alteramos o índice do dataframe para ser o país, para facilitar o acesso aos dados do Brasil.

Criamos uma lista com os anos de 1980 a 2013 para usar como intervalo de tempo na análise.

Por fim, extraímos os dados do Brasil e os organizamos em um novo dataframe com as colunas "ano" e "imigrantes".

Agora estamos prontos para visualizar esses dados e entender as tendências de imigração do Brasil ao longo dos anos! 
"""
"""Criação de gráfico com módulo pyplot

Primeiro, vamos fazer a importação do módulo. Em uma nova linha do Google Colab, escrevemos import matplotlib.pyplot e vamos apelidar esse módulo como plt. Podemos executar a célula.
usar uma função chamada plot(). Desse modo, é gerado automaticamente um gráfico de linhas. Como primeiro argumento, precisamos colocar os dados que estarão no eixo horizontal do gráfico. No nosso caso, os anos.Como segundo argumento, precisamos colocar os dados para o eixo vertical do gráfico
Melhora na visualização do gráfico
Escolhendo quais anos aparecerem no eixo x com plt.xticks e as referencias de quantidades no eixo y com o plt.yticks
uma função do Matplotlib chamada show() que faz com que apenas o gráfico seja exibido.
Atenção: códigos escritos abaixo de plt.show() não serão executados, pois o Python interrompe a execução dos códigos.

"""
# Formatação do grafico - tamanho, dados, titulo, titulo dos eixos, legenda 
plt.figure(figsize=(10,4))
plt.plot(dados_brasil['ano'],dados_brasil['imigrantes'], label='Brasil')
plt.plot(dados_argentina['ano'],dados_argentina['imigrantes'], label='Argentina')
plt.title('Comparativo Imigração do Brasil e Argentina para o Canadá')
plt.xlabel('Ano')
plt.ylabel('Numero de Imigrantes')
plt.legend()
plt.xticks(['1980', '1985','1990', '1995', '2000', '2005','2010'])
plt.yticks([500,1000,1500,2000,2500,3000])
plt.show()