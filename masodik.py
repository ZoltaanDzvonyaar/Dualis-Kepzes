u1="curiosity killed the cat"
u2="early bird catches the worm"
words=[]

with open("words.txt", "r") as forrasfajl:
    for sorbeolvas in forrasfajl:
        szavak = sorbeolvas.strip().split()
        egylistaba = " ".join(szavak)
        words.append(egylistaba)


def kulcskeres(u1, u2):
    visszafejtettuzenet=[]
    visszafejtettuzenettemp=[]
    kulcs_karakter_indexe=0
    lehetsegeskulcs=[]
    valtozo=26
    index=0
    templist=[]
    for karakter in u1[index]:

        if karakter == " ":
            karakterkodja=26

        else:
            karakterkodja = ord(karakter) - ord("a")

        for i in range(0, valtozo):

            uzenet_kulcs_kod_kulonbseg=(karakterkodja - i)%27

            if uzenet_kulcs_kod_kulonbseg < 0:
                uzenet_kulcs_kod_kulonbseg += 27
            if uzenet_kulcs_kod_kulonbseg == 26:
                visszafejtettuzenet += " "
            else:
                visszafejtettuzenettemp = chr(uzenet_kulcs_kod_kulonbseg + ord("a") )
                def keres_szot(visszafejtettuzenettemp, words):
                    talalatok = []
                    for szo in words:
                        for betu0 in szo:
                            fg=0
                            if visszafejtettuzenettemp[fg]==szo[fg]:
                                talalatok.append(szo)
                                fg+=1
                            if szo in talalatok:
                                break

                    return talalatok
                y=keres_szot(visszafejtettuzenettemp, words)
                #print(y)
                templist.append(visszafejtettuzenettemp)
    #print(templist)
    #(len(y))

    for z in range(1, len(templist)):           
        #print(o)
        for o in range(0, len(y)):
            for p in range(1, len(y[o])):


                if y[o][p]==templist[z]:print(y[o]):
                    print(y[o])
    return  lehetsegeskulcs

x=kulcskeres(u1, words)
print(x)