def transpose_array(array):
    return [r for r in zip(*array)]

def print_array(array):
    for row in array:
        print("".join(row))

def array_to_string(array):
    s = ""
    for row in array:
        s += "".join(row)+"\n"
    return s

def flip_array_vertically(array):
    return array[::-1]
def flip_array_horizontally(array):
    new_array = []
    for row in array:
        new_array.append(row[::-1])
    return new_array