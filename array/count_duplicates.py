input = [1,3,4,5,2,1,2,1,1,1,3,3,2,2,2,4,4,4,4,5,5,5,5,5]

def count_duplicates(arr):
    count_dict = {}
    for num in arr:
        if count_dict.get(num):
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict
print(count_duplicates(input))
