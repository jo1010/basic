def function(data, new_value):
    if isinstance(data, list):
        data.append(new_value)
    elif isinstance(data, set):
        data.add(new_value)
    elif isinstance(data, str):
        if isinstance(new_value, str):
            data += new_value
    return data


print(function([1, 2 , 3], 4))