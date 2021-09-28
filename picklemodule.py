import pickle

#pickling a python object
data = ["audi","ferrari","suzuki","fortuner"]
file = "mydata.pkl"
fileop = open(file, 'wb')
pickle.dump(data, fileop)
fileop.close()

#depickling
file = "mydata.pkl"
fileop = open(file, 'rb')
print(pickle.loads(fileop))
fileop.close()