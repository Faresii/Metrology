import pandas as pd
import math as m


#filename = "C:\Project with Alexey\Metrology\11.xlsx"

P = 0.95
W = {'U': 0}
n = 20

data = pd.read_excel('C:/ProjectWithAlexey/Metrology/3_laba/11.xlsx', skiprows=2, index_col=0)
data_mean = pd.DataFrame(data.mean()).T.round(1)
data_mean.index = ['mean']
print(data_mean)
#data.loc['mean'] = data_mean
# data.loc['Ua'] = data.std() / m.sqrt(n)
# data.loc['Ub'] = 0

# data.loc['Ub']['U, В'] = W['U'] / m.sqrt(3)
# for i in range(1, 8):
#   data.loc['Ub']['U, В.' + str(i)] = W['U'] / m.sqrt(3)

# data.loc['Ub']['h, %'] = (W['U'] / m.sqrt(3)) * 100
# for i in range(1, 8):
#   data.loc['Ub']['h, %.' + str(i)] = (W['U'] / m.sqrt(3)) * 100

# data.loc['Uc'] = (data.loc['Ua'] ** 2 + data.loc['Ub'] ** 2) ** (1 / 2)


# k = 2
# data.loc['U'] = k * data.loc['Uc']


# for i in range(len(data.columns)):
#   index = data.columns[i]
#   tmp_series = data[index]
#   print(f"U for {data.columns[i]}:\n {tmp_series['mean']},\t{tmp_series['U']},\t{P}\n")