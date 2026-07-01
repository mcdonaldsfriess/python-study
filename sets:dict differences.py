colors = {"red", "blue", "green"} # set of color, no duplicates/no defined order

s = {1, 2, 3} # set with 3 elements
s = set() #empty set
s = set([1, 2, 2, 3]) # from a list -> {1, 2, 3}, dupes dropped

empty = {} # empty dict, not a set
empty_set = set() # empty dict, not a set

s = {1, 2, 3}
s.add(4) # add 4 to set, {1, 2, 3, 4}
s.discard(10) # no error, even though 10 isnt in set
s.remove(10) # KeyError: 10, since 10 isnt in set
3 in s # True, 3 is in set
len(s) # 4, count of elements in set(size)


a = {1, 2, 3}
b = {3, 4, 5}

a | b # union -> {1, 2, 3, 4, 5}
a & b # intersection -> {3}
a - b # difference -> {1, 2}
a ^ b # symmetric difference -> {1, 2, 4, 5}, elements in either a or b but not both





# set elements and dict keys must be hashable, meaning they must be immutable.

{1, 2, 3} # valid set
{(1, 2), (3, 4)} # valid set of tuples, tuples are immutable
{[1, 2], [3, 4]} # TypeError: unhashable type: 'list', lists are mutable





# set vs dict

# set: unordered collection of unique elements
# dict: insertion-ordered collection of key-value pairs

# set operations
s = {1, 2, 3}
s.add(4)
s.discard(10)
s.remove(10)

# dict operations
d = {"a": 1, "b": 2}
d["c"] = 3
d.pop("a")
d.get("b")