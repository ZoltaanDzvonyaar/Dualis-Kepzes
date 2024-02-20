uzenet="helloworld"
kulcs="abcdefgjikl"

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

        
