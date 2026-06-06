"""
A permutation can be specified by an array P, where P[i] represents the location of the element
at i in the permutation. A permutation can be applied to an array to reorder the array.
Given an array A of n elements and a permutation P, apply P to A.
elements of programming interview python
"""
array = ["a", "b", "c", "d"]
permutation = [2,0,1,3]

def permute_array(array, permutation):
        elem_current_index = 0
        temp = None
        while True:
            if permutation[elem_current_index] == -1:
                i = 0
                while permutation[i] == -1 and i < len(permutation) - 1:
                        i += 1
                if i == len(permutation) -1 and permutation[i] == -1:
                      break
                else:
                    elem_current_index = i 
            permutation_position = permutation[elem_current_index]
            array[elem_current_index], array[permutation_position] = array[permutation_position], array[elem_current_index]
            permutation[elem_current_index] = -1
            elem_current_index = permutation[permutation_position]

permute_array(array, permutation)

# we can also go left to right and applying the cycle only if the current position is the leftmost position in the cycle.
# Testing whether the current position is the leftmost position entails traversing the cycle once more, which increases the run time to O(n**2).