gram = {
	"S":["AA"],
	"A":["aA","b"]
}
start = "S"

non_terms = ["S'"]
for i in gram:
	non_terms.append(i)
gram["S'"]= [start]
# print(gram,non_terms)

Is = {}
Is[0] = {}
Is[0]["S'"] = ["."+gram["S'"][0]]
gt = 1

cnt = 0
while cnt<len(Is[0]):
	i = list(Is[0].keys())[cnt]
	for j in Is[0][i]:
		temp = j.replace(".","")
		if temp[0] in non_terms:
			Is[0][temp[0]] = gram[temp[0]]
			for k in range(len(Is[0][temp[0]])):
				Is[0][temp[0]][k] = "."+Is[0][temp[0]][k]
	cnt+=1


dots = {0:[]}
while True:
	for i in Is[0]:
		for j in Is[0][i]:
			try:
				dots[0].append(j[j.index(".")+1])
			except:
				pass
	for i in dots[0]:
		tempI = {}
		for j in Is[0]:
			for k in Is[0][j]:
				if ("."+i) in k:
					try:
						tempI[j] += [k.replace("."+i,i+".")]
					except:
						tempI[j] = [k.replace("."+i,i+".")]
		if tempI not in list(Is):
			Is[gt] = tempI
			gt+=1
	break

for i in Is:
	print(i,Is[i])