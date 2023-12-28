import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('C:/ProjectWithAlexey/Metrology/3_laba/metrology/11.xlsx', skiprows=2, index_col=0)
df = pd.DataFrame(data,
                                            #Параметры импульса, при подключении коротким кабелем
                                                #500                                    #100
                     columns=['U, В','h, %', 'τ, нс', 'τф, нс', 'τс, нс', 'U, В','h, %', 'τ, нс', 'τф, нс', 'τс, нс', 
                             'U, В','h, %', 'τ, нс', 'τф, нс', 'τс, нс',  'U, В','h, %', 'τ, нс', 'τф, нс', 'τс, нс',
                                                #50                                        #20
                                                
                                            #Параметры импульса, при ограничении полосы пропускания осциллографа
                                                #500                                    #100                                            
                             'U, В','h, %', 'τ, нс', 'τф, нс', 'τс, нс', 'U, В','h, %', 'τ, нс', 'τф, нс', 'τс, нс', 
                             'U, В','h, %', 'τ, нс', 'τф, нс', 'τс, нс',  'U, В','h, %', 'τ, нс', 'τф, нс', 'τс, нс'])
                                                #50                                        #20
                                                
data1 = data
P = 0.95
n = 20
AgCri = 0 # agreement criterion - критерий согласия

X_max = 0

# print(data)

# print(data.mean())

AgCri = ( 1 / (n*data.std(ddof=0)) ) * (data - data.mean())

# print('\nКритерий согласия')
# print(AgCri)


def GetIndex():
    for i in data:
        data[0][i].loc(f'{i}')
    return data

def IdentifyingMisses(): #Выявление промахов для критерия согласия
    X_max = data.max()
    data_mean = data.mean()
    
    # for i in data :
    #     if X_max[i] > data_mean[i] : data[i].drop()
    print(X_max)
    return X_max

def main():
    print('Выявление промахов')
    IdentifyingMisses()

def AllGraphs():
    k = 0
    for i in data:
        
        ax = plt.subplot(7, 7, k+1)
        sns_plot = sns.distplot(data[i], norm_hist=True, label=None, rug=True)
        k +=1
    
    fig = sns_plot.get_figure()
    plt.show()
    
if __name__ == '__main__' :
    main()
    
    AllGraphs()
