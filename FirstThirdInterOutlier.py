import numpy as np

print("Dhruvin Prajapati")
data = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25,
        25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
sort_data = np.sort(data)
sort_data

Q1 = np.percentile(data, 25, interpolation='midpoint')
Q3 = np.percentile(data, 75, interpolation='midpoint')
IQR = Q3 - Q1

low_lim = Q1 - 1.5 * IQR
up_lim = Q3 + 1.5 * IQR
outlier = []
for x in data:
    if ((x > up_lim) or (x < low_lim)):
        outlier.append(x)


print('Q1 25 percentile of the given data is : ', Q1)
print('Q3 75 percentile of the given data is : ', Q3)
print('IQR Interquartile range is :', IQR)
print('outlier in the dataset is :', outlier)
