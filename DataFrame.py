import pandas as pd

data = {'Name':['Dhruvin', 'Hiren','Parth', 'Mohit'],
        'Age':[20,27,25,34],
        'Address':['Ahmedabad','Surat','Bangaluru','Chennai']}
df = pd.DataFrame(data)
print(df)