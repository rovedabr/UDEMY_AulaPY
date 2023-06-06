list1 = []
print(list1, type(list1))

#        0.....1......2.......3....4
#       -5....-4.....-3......-2...-1
list2 = [12, True, "Laranja", [], 1.2]
print(list2)
print(list2[2])
print(type(list2[2]))

list2[3] = [1,2,3]
print(list2)

list2[3] = "banana"
print(list2)

#CRUD

del (list2[1])
print(list2)



