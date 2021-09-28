from collections import Counter

print("Dhruvin Prajapati")
Dataset=[13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33,33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
print(Dataset)
def my_mean(sample):
    return sum(sample) / len(sample)
print("Mean: ",my_mean(Dataset))

def my_median(sample):
     n = len(sample)
     index = n // 2
     if n % 2:
         return sorted(sample)[index]
         return sum(sorted(sample)[index - 1:index + 1]) / 2
print("Median: ",my_median(Dataset))

def my_mode(sample):
    c = Counter(sample)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
print("Mode: ",my_mode(Dataset))


m = (max(Dataset) + min(Dataset))/2
print("MidRange: "+ str(m))