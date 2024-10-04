import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/wanderson/workplace/datascience/imigrantes_canada.csv') # carregar o arquivo em uma variável 'data frame'
# print(df) exibe o conteúdo do arquivo
# df.info() mostra informações principais do arquivo
df.set_index('País',inplace=True)  # mudar o indice do arquivo e o inplace dispensa a criação de um novo data frame
anos=list(map(str,range(1980,2014)))# criar variável para armazenas as colunas de anos, é criada uma lista e a função MAP serve para aplicar a transformacao do intervalo em string
# print (anos)
brasil=df.loc['Brasil',anos] # pegar somente os dados do Brasil, a propriedade LOC consegue pegar rótulos específicos dentro de um dataframe
# print (brasil)
brasil_dict={'ano':brasil.index.tolist(),'imigrantes':brasil.values.tolist() } #criar um dicionario com os títulos ano e imigrantes pegando da lista brasil os anos e os valores por anos

dados_brasil=pd.DataFrame(brasil_dict)
IPython_default = plt.rcParams.copy() # guarda os stilos "padrão" do matplot em uma variavel
## plt.style.use('fivethirtyeight')      # altera o estilo padrão par ao que estiver em ' ' ver estilos em print(plt.style.available)

"""
fig,ax = plt.subplots(figsize=(10,6))

ax.plot(dados_brasil['ano'],dados_brasil['imigrantes'], label='Brasil',lw=3,marker='o',color='g')
ax.set_title('Imigracao do Brasil para o Canada \n de 1980 a 2013', fontsize=18,loc='left') 
ax.xaxis.set_major_locator(plt.MultipleLocator(5)) # setando os valores de anos
ax.set_xlabel('Ano', fontsize=15)               # setando label em eixo x
ax.set_ylabel('Imigrantes', fontsize=15)        # setando label em eixo y
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
"""
america_sul=df.query('Região=="América do Sul"')

america_sul_sorted=america_sul.sort_values('Total',ascending=True)

cores = []
for pais in america_sul_sorted.index:
    if pais=='Brasil':
        cores.append('green')
    else:
        cores.append('silver')

fig, ax = plt.subplots(figsize=(12,5))
ax.barh(america_sul_sorted.index, america_sul_sorted['Total'],color=cores)
ax.set_title('America do SUL: Brasil foi o 4º pais com mais imigrantes \n para o Canadá no periodo de 1980 a 2013', loc='left',fontsize=18)
ax.set_xlabel('Numero de Imigrantes',fontsize=14)
ax.set_ylabel('')
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)
for i , v in enumerate(america_sul_sorted['Total']):
    ax.text(v + 20, i, str(v),color='k',fontsize=10,ha='left',va='center')
ax.set_frame_on(False)
ax.get_xaxis().set_visible(False)
ax.tick_params(axis='both', which='both', length=0) 

fig.savefig('dadosbrasils.png', transparent=False, dpi=500, bbox_inches='tight')
plt.show()
# print(fig.canvas.get_supported_filetypes()) buscar os formatos possiveis
