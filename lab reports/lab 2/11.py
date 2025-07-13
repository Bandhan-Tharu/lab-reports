# 11. Given a list of numbers with duplicates, use a set to remove the duplicates. Then,
# convert it back to a sorted list and display the result.
num=[12,1,1,1,2,3,4,5,5,5,6,6,7]
num=set(num)
num=list(num)
num.sort()
print(num)
