import copy

di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
di_copy = copy.deepcopy(di)

di['four'][0] = "cztery"

print("Original dictionary: ", di)

print("Copied dictionary: ", di_copy)
