def avg(scores):
    assert len(scores) != 0, "The List is empty."
    return sum(scores)/len(scores)


List2 = [12, 45, 56, 32, 98]
print("The Average of List2:", avg(List2))

List1 = []
print("The Average of List1:", avg(List1))
