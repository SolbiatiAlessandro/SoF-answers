import pandas as pd
import numpy as np
d={'0':['CAT','DOG','BIRD'],'1':[1,2,3],'2':[12,14,32], '3':[123,145,32], '4':[123,1456,32],'5':[123,14567,32]}
df = pd.DataFrame(d)

for i in [4, 3, 2, 1]:
    same_columns = df.iloc[:, i + 1] - df.iloc[:, i] == 0
    df.iloc[:,i+1][same_columns] = np.nan
import pdb;pdb.set_trace()
