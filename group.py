
# may be useful when image processing
def groups_of_three(L: list[int]) ->list[list[int]]:
    new_list = []
    threes = []
    index = 0
    while index < len(L)-1:
        while len(threes) <= 2 and index < len(L):
            threes.append(L[index])
            index += 1
        new_list.append(threes)
        threes = []
    return new_list

# can also be done like this using a list comprehension

def groups_of_three2(l: list[int]) ->list[list[int]]:
    groups = [l[i:i+3] for i in range(0,len(l),3)]
    return groups