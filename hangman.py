import random
def citire_fisier(x):
    fisier = open("cuvinte_de_verificat.txt","r", encoding="utf-8-sig")
    linii = fisier.readlines()
    linia_curenta = linii[x]
    cuvinte = linia_curenta.split(";")
    return cuvinte



def cele_mai_des_intalnite_litere_1(cuvant , cuvant_de_gasit):
    cele_mai_des_intalnite_litere = ("ierla").upper()
    top_litera = random.choice(cele_mai_des_intalnite_litere)
    lista_temporara = []
    incercari = 0
    count = 0
    cuvant_ghicit = ''
    cuvant_flag = ''
    while sorted(cuvant_flag) != sorted(cele_mai_des_intalnite_litere):
        top_litera = random.choice(cele_mai_des_intalnite_litere)
        if top_litera not in cuvant_flag:
            cuvant_flag += top_litera
            if top_litera not in cuvant:
                incercari += 1
                for i in range(0, len(cuvant_de_gasit)):
                    if top_litera == cuvant_de_gasit[i]:
                        cuvant[i] = cuvant_de_gasit[i]

    for i in range(0 , len(cuvant_de_gasit)):
        if cuvant[i] == cuvant_de_gasit[i]:
            count += 1
    for i in range(0, len(cuvant_de_gasit)):
        lista_temporara += cuvant[i]
    for litere in lista_temporara:
        cuvant_ghicit += litere
    return cuvant_ghicit , incercari ,count




def cele_mai_des_intalnite_litere_2(cuvant ,cuvant_de_gasit ,incercari):

    cele_mai_des_intalnite_litere = ('outnc').upper()
    cuvant_flag = ''
    count = 0
    cuvant_ghicit = ''
    while sorted(cuvant_flag) != sorted(cele_mai_des_intalnite_litere):
        top_litera = random.choice(cele_mai_des_intalnite_litere)
        if top_litera not in cuvant_flag:
            cuvant_flag += top_litera
            if top_litera not in cuvant:
                incercari += 1
                for i in range(0, len(cuvant_de_gasit)):
                    if top_litera == cuvant_de_gasit[i]:
                        cuvant[i] = cuvant_de_gasit[i]
    for i in range(0 , len(cuvant_de_gasit)):
        if cuvant[i] == cuvant_de_gasit[i]:
            count += 1

    for litere in cuvant:
        cuvant_ghicit += litere
    return cuvant_ghicit, incercari ,count

def cele_mai_des_intalnite_litere_3(cuvant,cuvant_de_gasit, incercari):
    cele_mai_des_intalnite_litere = ('smdpg').upper()
    cuvant_flag = ''
    cuvant_ghicit = ''
    count = 0
    while sorted(cuvant_flag) != sorted(cele_mai_des_intalnite_litere):
        top_litera = random.choice(cele_mai_des_intalnite_litere)
        if top_litera not in cuvant_flag:
            cuvant_flag += top_litera
            if top_litera not in cuvant:
                incercari += 1
                for i in range(0, len(cuvant_de_gasit)):
                    if top_litera == cuvant_de_gasit[i]:
                        cuvant[i] = cuvant_de_gasit[i]

    for i in range(0, len(cuvant_de_gasit)):
        if cuvant[i] == cuvant_de_gasit[i]:
            count += 1


    for litere in cuvant:
        cuvant_ghicit += litere
    return cuvant_ghicit, incercari ,count

def cele_mai_des_intalnite_litere_4(cuvant , cuvant_de_gasit , incercari):
    cele_mai_des_intalnite_litere = ('țăș').upper()
    cuvant_flag = ''
    cuvant_ghicit = ''
    while sorted(cuvant_flag) != sorted(cele_mai_des_intalnite_litere):
        top_litera = random.choice(cele_mai_des_intalnite_litere)
        if top_litera not in cuvant_flag:
            cuvant_flag += top_litera
            if top_litera not in cuvant:
                incercari += 1
                for i in range(0, len(cuvant_de_gasit)):
                    if top_litera == cuvant_de_gasit[i]:
                        cuvant[i] = cuvant_de_gasit[i]

    for litere in cuvant:
        cuvant_ghicit += litere
    return cuvant_ghicit, incercari


def cele_mai_intalnite_litere_5(cuvant , cuvant_de_gasit, incercari):
    cele_mai_des_intalnite_litere = ('bfzvh').upper()
    cuvant_flag = ''
    cuvant_ghicit = ''
    while sorted(cuvant_flag) != sorted(cele_mai_des_intalnite_litere):
        top_litera = random.choice(cele_mai_des_intalnite_litere)
        if top_litera not in cuvant_flag:
            cuvant_flag += top_litera
            if top_litera not in cuvant:
                incercari += 1
                for i in range(0, len(cuvant_de_gasit)):
                    if top_litera == cuvant_de_gasit[i]:
                        cuvant[i] = cuvant_de_gasit[i]

    for litere in cuvant:
        cuvant_ghicit += litere
    return cuvant_ghicit, incercari

def cele_mai_intalnite_litere_6(cuvant , cuvant_de_gasit, incercari):
    cele_mai_des_intalnite_litere = ('jîâ').upper()
    cuvant_flag = ''
    cuvant_ghicit = ''
    while sorted(cuvant_flag) != sorted(cele_mai_des_intalnite_litere):
        top_litera = random.choice(cele_mai_des_intalnite_litere)
        if top_litera not in cuvant_flag:
            cuvant_flag += top_litera
            if top_litera not in cuvant:
                incercari += 1
                for i in range(0, len(cuvant_de_gasit)):
                    if top_litera == cuvant_de_gasit[i]:
                        cuvant[i] = cuvant_de_gasit[i]

    for litere in cuvant:
        cuvant_ghicit += litere
    return cuvant_ghicit, incercari

def cele_mai_intalnite_litere_7(cuvant , cuvant_de_gasit, incercari):
    cele_mai_des_intalnite_litere = ('xk').upper()
    cuvant_flag = ''
    cuvant_ghicit = ''
    while sorted(cuvant_flag) != sorted(cele_mai_des_intalnite_litere):
        top_litera = random.choice(cele_mai_des_intalnite_litere)
        if top_litera not in cuvant_flag:
            cuvant_flag += top_litera
            if top_litera not in cuvant:
                incercari += 1
                for i in range(0, len(cuvant_de_gasit)):
                    if top_litera == cuvant_de_gasit[i]:
                        cuvant[i] = cuvant_de_gasit[i]

    for litere in cuvant:
        cuvant_ghicit += litere
    return cuvant_ghicit, incercari



def pozitia_liniei(x):
    x += 1
    return x


def main():
    y = -1
    procent = 8/10
    count_final = 0
    total_numar_incercari = 0
    for i in range(0,100):
        cuvant_ghicit = ''
        x = pozitia_liniei(y)
        y = x
        c = citire_fisier(x)[1]
        cuvant = list(c)
        cuvant_de_gasit = citire_fisier(x)[2]
        cuvant_de_gasit = cuvant_de_gasit.rstrip('\n')
        count_final = cele_mai_des_intalnite_litere_1(cuvant, cuvant_de_gasit)[2]
        if count_final >= len(cuvant_de_gasit) * procent:
            print(cuvant)
            cuvant_ghicit = cuvant_de_gasit
        cuvant_ghicit += cele_mai_des_intalnite_litere_1(cuvant, cuvant_de_gasit)[0]
        numarul_incercarilor = 0
        numarul_incercarilor += cele_mai_des_intalnite_litere_1(cuvant, cuvant_de_gasit)[1]

        if cuvant_ghicit != cuvant_de_gasit:
            numarul_incercarilor = cele_mai_des_intalnite_litere_2(cuvant, cuvant_de_gasit, numarul_incercarilor)[1]
            cuvant_ghicit = ''
            cuvant_ghicit = cele_mai_des_intalnite_litere_2(cuvant , cuvant_de_gasit ,numarul_incercarilor)[0]
            count_final = cele_mai_des_intalnite_litere_2(cuvant , cuvant_de_gasit , numarul_incercarilor)[2]
            if count_final >= len(cuvant_de_gasit) * procent:
                print(cuvant)
                cuvant_ghicit = cuvant_de_gasit

            if cuvant_ghicit != cuvant_de_gasit:
                numarul_incercarilor = cele_mai_des_intalnite_litere_3(cuvant, cuvant_de_gasit, numarul_incercarilor)[1]
                cuvant_ghicit = ''
                cuvant_ghicit += cele_mai_des_intalnite_litere_3(cuvant, cuvant_de_gasit, numarul_incercarilor)[0]
                count_final = cele_mai_des_intalnite_litere_3(cuvant, cuvant_de_gasit, numarul_incercarilor)[2]
                if count_final >= len(cuvant_de_gasit) * procent:
                    print(cuvant)
                    cuvant_ghicit = cuvant_de_gasit

                if cuvant_ghicit != cuvant_de_gasit:
                    cuvant_ghicit = ''
                    numarul_incercarilor = cele_mai_des_intalnite_litere_4(cuvant, cuvant_de_gasit, numarul_incercarilor)[1]
                    cuvant_ghicit += cele_mai_des_intalnite_litere_4(cuvant, cuvant_de_gasit, numarul_incercarilor)[0]

                    if cuvant_ghicit != cuvant_de_gasit:
                        numarul_incercarilor = cele_mai_intalnite_litere_5(cuvant, cuvant_de_gasit, numarul_incercarilor)[1]
                        cuvant_ghicit = ''
                        cuvant_ghicit += cele_mai_intalnite_litere_5(cuvant, cuvant_de_gasit, numarul_incercarilor)[0]

                        if cuvant_ghicit != cuvant_de_gasit:
                            numarul_incercarilor = cele_mai_intalnite_litere_6(cuvant, cuvant_de_gasit, numarul_incercarilor)[1]
                            cuvant_ghicit = ''
                            cuvant_ghicit += cele_mai_intalnite_litere_6(cuvant, cuvant_de_gasit, numarul_incercarilor)[0]

                            if cuvant_ghicit != cuvant_de_gasit:
                                numarul_incercarilor = cele_mai_intalnite_litere_5(cuvant, cuvant_de_gasit, numarul_incercarilor)[1]
                                cuvant_ghicit = ''
                                cuvant_ghicit += cele_mai_intalnite_litere_7(cuvant, cuvant_de_gasit, numarul_incercarilor)[0]

        total_numar_incercari += numarul_incercarilor
        print(cuvant_ghicit , total_numar_incercari)

if __name__ == '__main__':
    main()
