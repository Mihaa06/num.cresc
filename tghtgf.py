sir=[21,1,6,32,1,9,9,6,6,5,64,46,46]
vec_frev=[0]*100
lista_sort=[]
for ch in sir:
    vec_frev[ch] += 1
for i in range(0,len(vec_frev)):
    for nr in range(0,vec_frev[i]):
        lista_sort.append(i)
print(vec_frev)
print(lista_sort)

