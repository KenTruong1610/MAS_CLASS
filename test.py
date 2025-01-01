names = ["bob","mike","tom","mary"]
names = [n.upper() for n in names]
keys = ['Red','Blue','Green','Yellow']
values = [1,2,3,4]
a = zip(names, keys, values)
person, key, value = list(a)[0]
print(person, key, value)