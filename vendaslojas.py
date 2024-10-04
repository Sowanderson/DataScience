import pandas as pd
import matplotlib.pyplot as plt


lojas = ['A', 'B', 'C', 'D']
vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}

df = pd.DataFrame(vendas_2022, index=lojas)

cores = []
for lojas in lojas:
    if lojas=='A':
        cores.append('green')
    elif lojas =='B':
        cores.append('yellow')
    elif lojas =='C':
        cores.append('blue')
    else:
       cores.append('brown')
print (cores)
# Criar a figura e os subplots
fig,axs = plt.subplots(2,2, figsize=(10,6))
# ax.bar(vendas_2022.lojas,vendas_2022[''])
fig.subplots_adjust(hspace=0.5,wspace=0.3) #ajusta o espaçamento entre os graficos em valores decimais onde 0.5 significa que o espaçamento será de 50% da altura/largura da figura.
                                           # wspace controla o espaçamento horizontal e hspace controla o espaçamento vertical
fig.suptitle('Compilado das Vendas das lojas no ano de 2022') # titulo "geral pra os 4 graficos"
"""
axss0,0].plot(df.loc['A'])
axs[0,0].set_title('Loja A')

axs[0,1].plot(df.loc['B'])
axs[0,1].set_title('Loja B')

axs[1,0].plot(df.loc['C'])
axs[1,0].set_title('Loja C')

axs[1,1].plot(df.loc['D'])
axs[1,1].set_title('Loja D')
"""
# ao invez de ajustar um a um criar um FOR para percorrer todos os graficos para fazer diversos ajustes
for i, ax in enumerate(axs.flat):        #o flat faz o for percorrer todos os graficos da matriz
    ax.plot(df.loc[df.index[i]], color=cores[i], lw=3)
    print(df.loc[df.index[i]])
    ax.set_title(f'Vendas na loja {df.index[i]}', loc='left', fontsize=16)
    ax.set_xlabel('Mes')           # setando label em eixo x
    ax.set_ylabel('Vendas')        # setando label em eixo y
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(labelsize=12)
    ax.grid(color='lightgrey')

#criar duas varivaveis para definir os valores maximo e minimo que serão exibidos no eixo y
ymin=0
ymax=500

0#definir limites para todos os graficos e ajustar o eixo y para dar uma melhor visualização
for ax in axs.ravel(): #  o método ravel(), que consegue transformar um array bidimensional em unidimensional e fazer algumas aplicações
    ax.set_ylim(ymin,ymax) 

# fig.savefig('dadoslojas.png', transparent=False,dpi=500, bbox_inches='tight')
plt.show()

