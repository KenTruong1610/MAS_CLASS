names = ["bob","mike","tom","mary"]
names = [n.upper() for n in names]
keys = ['Red','Blue','Green','Yellow']
values = [1,2,3,4]
out = {}
for i in range(len(keys)):
	out[keys[i]] = values[i]
names, key, value = list(a)[0]