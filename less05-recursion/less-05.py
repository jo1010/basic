a = [4, 5, 6, 3, 2]

def iter_rec(array, index=0):
    if index < len(array):
        print(array[index])
        index += 1
        iter_rec(array, index)


iter_rec(a)