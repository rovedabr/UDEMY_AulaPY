list_a = [1,2,3]
list_b = [4,5,6]

list_c = list_a + list_b
print(list_c)
list_a.extend(list_b) #altera a própria lista a juntando os dados da lista b
print(list_a)

name = 'Pedro'
other_name = name
print(other_name)

#alterando dados do "other_name"
other_name = 'Maria'
print(name)
print(other_name)

#--------------------------------------------

new_list_a = ['Maria', 1, 2, 3, 1.2, True]
print(new_list_a)

new_list_b = new_list_a.copy()
print(new_list_b)

new_list_b[0] = 'Pedro'
print(new_list_b)

#--------------------------------------------
list_c = ['Maria', 'Ana', 'Pedro', 1, 1.2, True]

for name in list_c:
  print(name, type(name))

names = ["Maria", "João", "Pedro"] #lista
name1, name2, name3 = names
print(name2)

names2 = "Maria", "João", "Pedro" #tupla
names3 = tuple(names)