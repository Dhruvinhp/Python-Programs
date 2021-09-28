import numpy as np
from itertools import combinations, groupby
from collections import Counter

# Sample data
orders = np.array([[1, 'apple'],
[1, 'egg'],
[1, 'milk'],
[2, 'egg'],
[2, 'milk']], dtype=object)


def get_item_pairs(order_item):
    for order_id, order_object in groupby(orders, lambda x: x[0]):
        item_list = [item[1] for item in order_object]

        for item_pair in combinations(item_list, 2):
            yield item_pair

print("Hiren Jadvani")
print("Item Sets In Pair :",Counter(get_item_pairs(orders)))