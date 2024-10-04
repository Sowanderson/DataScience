import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/wanderson/workplace/datascience/imigrantes_canada.csv') # carregar o arquivo em uma variável 'data frame'


df.set_index('País',inplace=True)  # mudar o indice do arquivo e o inplace dispensa a criação de um novo data frame
anos=list(map(str,range(1980,2014)))# criar variável para armazenar as colunas de anos, é criada uma lista e a função MAP serve para aplicar a transformacao do intervalo em string

fig,axs = plt.subplots(2,2,figsize=(10,6))
fig.subplots_adjust(hspace=0.5,wspace=0.3) #ajusta o espaçamento entre os graficos em valores decimais onde 0.5 significa que o espaçamento será de 50% da altura/largura da figura.
                                           # wspace controla o espaçamento horizontal e hspace controla o espaçamento vertical
fig.suptitle('Imigracao dos 4 maiores paises da America do Sul para o Canada \n de 1980 a 2013') # titulo "geral pra os 4 graficos"

axs[0,0].plot(df.loc['Brasil',anos])
axs[0,0].set_title('Brasil')

axs[0,1].plot(df.loc['Colômbia',anos])
axs[0,1].set_title('Colômbia')

axs[1,0].plot(df.loc['Argentina',anos])
axs[1,0].set_title('Argentina')

axs[1,1].plot(df.loc['Peru',anos])
axs[1,1].set_title('Peru')

# ao invez de ajustar um a um criar um FOR para percorrer todos os graficos para fazer diversos ajustes
for ax in axs.flat:         #o flat faz o for percorrer todos os graficos da matriz
    ax.xaxis.set_major_locator(plt.MultipleLocator(5)) # setando os valores de anos de 5 em 5 para ficar mais legivel
    ax.set_xlabel('Ano')               # setando label em eixo x
    ax.set_ylabel('Imigrantes')        # setando label em eixo y

#criar duas varivaveis para definir os valores maximo e minimo que serão exibidos no eixo y
ymin=0
ymax=7000

#definir limites para todos os graficos e ajustar o eixo y para dar uma melhor visualização
for ax in axs.ravel(): #  o método ravel(), que consegue transformar um array bidimensional em unidimensional e fazer algumas aplicações
    ax.set_ylim(ymin,ymax) 

plt.show()