from sys import getsizeof
#try to create a tuple of even numbers with comrehension

values1 = (f"id {x*2}" for x in range(600000))
values2 = [f"id {x*2}" for x in range(600000)]

print(f"Gen size: {getsizeof(values1)}")
print(f"Lst size: {getsizeof(values2)}")


#for v in values:
#    print(v)
#    break
#print()


