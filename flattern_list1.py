def flatten_list(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened


input_list = [1, [2, 3, [4, [5, 6], 7]], 8, 9, [[10]]]

output_list = flatten_list(input_list)
print(output_list)
