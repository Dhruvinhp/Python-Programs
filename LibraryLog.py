import numpy as np
import matlablib as plt
import seaborn as sns
import pandas as pd

companies= pd.read_csv("C:\\Users\\HP\\Desktop\\log.csv")
x= companies.iloc[:,:-1].values
y= companies.iloc[:,4].values
companies.head()
