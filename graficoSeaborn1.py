import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='ticks')



df = pd.read_csv('/home/wanderson/workplace/datascience/imigrantes_canada.csv') # carregar o arquivo em uma variável 'data frame'
df.set_index('País',inplace=True)  # mudar o indice do arquivo e o inplace dispensa a criação de um novo data frame
top_10=df.sort_values('Total',ascending=False).head(10) # Criar Data Frame Ordenado pela coluna Total. O head(10) pega os 10 primeiros



def gerar_grafico_paleta(palette):
    # sns.barplot(data=top_10,x=top_10.index,y='Total')
    fig , ax = plt.subplots(figsize=(8,4))
    ax = sns.barplot(data=top_10, y=top_10.index,x='Total', orient='h',palette=palette) #invertendo x com y
    ax.set_title('Paises com maior imigração para o Canada \n 1980 a 2013',loc='left',fontsize=18) 
    ax.set_xlabel('Numero de Imigrantes',fontsize=14) 
    ax.set_ylabel('')
    sns.despine()

    plt.show()

gerar_grafico_paleta('tab10')