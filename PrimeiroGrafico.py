import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/wanderson/workplace/datascience/imigrantes_canada.csv')
df.set_index('País',inplace=True) 
anos=list(map(str,range(1980,2014)))

df_comparacao = df.loc[['Brasil', 'Argentina'], anos].T
df_comparacao = df_comparacao
df_comparacao.head()
plt.plot(df_comparacao['Brasil'],label = 'Brasil')
plt.plot(df_comparacao['Argentina'],label ='Argentina')
plt.title('Imigração do Brasil e Argentina para o Canadá')
plt.xlabel('Ano')
plt.ylabel('Número de imigrantes')
plt.xticks(['1980', '1986', '1990', '1995', '2000', '2005', '2010'])
plt.legend()
plt.show()