#SETS ARE AN UNORDERED COLLECTION OF UNQUIE ELEMENTS
#use ful when you ned to eliminate duplictaes for perfromence


numbers = [1,2,2,3,4,4,5]
unique_numbers = set(numbers) #super useful
print(unique_numbers)


nums1 = {1,2,3,4,5}
nums2 = {4,5,6,7,8}

#useful union
print(nums1 | nums2)
all_nums = list(nums1 | nums2)
print(all_nums)


#intersections
print(nums1 & nums2)

#difference
print(nums1 - nums2)

#symm
print(nums1 ^ nums2)
