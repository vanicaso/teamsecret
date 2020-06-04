from random import sample

miembros = {
    "Cliver": None,
    "Shiro": None,
    "Liz": None,
    "Issac": None,
    "Vani": None,
    "Walter": None
}

ini = 1
fin = 11

L = sample(range(ini, fin), len(miembros))

i = 0
for miembro in miembros:
    miembros[miembro] = L[i]
    i += 1

for miembro, ejer in miembros.items():
    print(miembro, " -----> ", ejer)
