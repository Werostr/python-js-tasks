# dup = {5,'dupeczka','suczka', 66}

# dup.add('kutas')

def pupa(x):
    if x % 2 == 0:
        return True
    return False


lista = ['Tomasz',"Nie",'Chciałaś']
# superLista = list(filter(pupa,lista))
superLista2 = []

for x in lista:
    if pupa(len(x)):
        superLista2.append(x)
        
print(superLista2)
# nowaLista =[]

# for x in lista:
#     nowaLista.append(len(x))

# print(nowaLista)

# nowszaLista = [len(x) if len(x) > 4 else 'pizdeczka' for x in lista  ]
# print(nowszaLista)

# najnowszaLista = list(filter(len > 4,map(len,lista)))
# print(najnowszaLista)



# def niePupa(x):
#     return not pupa(x)

# print(pupa)

# lista = [4,7,2,8,6,3,5]

# nowe1 = [x for x in lista if pupa(x)]
# nowe3 = list(filter(pupa, lista))

# nowe2 = []
# for x in lista:
#     if pupa(x):
#         nowe2.append(x)

# print(nowe1)
# print(nowe2)
# print(nowe3)