nums = [3, 1, 2] 
mixed = [1, "hi", 3.14, True]
empty = []

nums[0] # first
nums[-1] # last
nums[-2] # second to last
nums[1:3] # from index 1 to 2 (not including index 3)
nums[:2] # from the beginning to index 1 (not including index 2)
nums[1:] # from index 1 to the end
nums[:] # copy the entire list
nums[::-1] # reverse the list
nums[::2] # every other element
nums[1::2] # every other element starting from index 1

nums.append(4) # add 4 to the end of the list
nums.insert(1, 5) # insert 5 at index 1

lst = nums.pop() # remove and return the last element (4)
lst = nums.pop(1) # remove and return the element at index 1 (5)
nums.remove(2) # remove the first occurrence of 2
nums.clear() # remove all elements from the list

nums.sort() # sort the list in place
nums.sort(reverse=True) # sort the list in reverse order
new = sorted(nums) # return a new sorted list

#nums = nums.sort() #Wrong! nums.sort() returns None, so nums will be set to None
nums.sort() # Correct way to sort the list in place