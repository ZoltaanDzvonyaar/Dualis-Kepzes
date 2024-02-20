uzenet="helloworld"
kulcs="abcdefgijkl"

def rejtjelez(uzenet,kulcs):
    rejtjelezett_u=""
    kulcs_karakter_indexe=0
    for karakter in uzenet:
        if karakter == " ":
            karakterkodja=26

        else:
            karakterkodja=ord(karakter) - ord("a") #a erteke 97, 0-25 tartomanyban marad.

        if kulcs_karakter_indexe>=len(kulcs):
            kulcs_karakter_indexe=0

        kulcs_karakterjeinek_kodja=ord(kulcs[kulcs_karakter_indexe]) - ord ("a")

        kulcs_karakter_indexe+=1

        uzenet_kulcs_kod=(karakterkodja + kulcs_karakterjeinek_kodja)%27
        if uzenet_kulcs_kod==26:
            rejtjelezett_u+=" "
        else:
            rejtjelezett_u+= chr(uzenet_kulcs_kod + ord("a")) #hozzaadva az a-hoz rendelt ASCII szamot visszater az uzenet_kulcs_kod az ASCII tablazatban levo betukhoz.
    return rejtjelezett_u

atirtuzenet=rejtjelez(uzenet,kulcs)
print(atirtuzenet)


def visszafejtes(atirtuzenet,kulcs):
    visszafejtettuzenet=""
    kulcs_karakter_indexe=0
    for karakter in atirtuzenet:
        if karakter == " ":
            karakterkodja=26

        else:
            karakterkodja = ord(karakter) - ord("a")

        if kulcs_karakter_indexe>=len(kulcs):
            kulcs_karakter_indexe = 0

        kulcs_karakterjeinek_kodja = ord(kulcs[kulcs_karakter_indexe]) - ord ("a")
        
        kulcs_karakter_indexe+=1
        

        uzenet_kulcs_kod_kulonbseg=(karakterkodja - kulcs_karakterjeinek_kodja)%27
        
        if uzenet_kulcs_kod_kulonbseg < 0:
            uzenet_kulcs_kod_kulonbseg += 27
        if uzenet_kulcs_kod_kulonbseg == 26:
            visszafejtettuzenet += " "
        else:
            visszafejtettuzenet += chr(uzenet_kulcs_kod_kulonbseg + ord("a") )
    return visszafejtettuzenet

visszairtuzenet=visszafejtes(atirtuzenet,kulcs)
print(visszairtuzenet)