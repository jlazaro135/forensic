dna = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

hair_color={"black":"CCAGCAATCGC", "brown":"GCCAGTGCCG", "blonde":"TTAGCTATCGC"}
facial_shape={"square":"GCCACGG", "round":"ACCACAA", "oval":"AGGCCTCA"}
eye_color = {"blue":"TTGTGGTGGC","green":"GGGAGGTGGC", "brown":"AAGTAGTGAC"}
gender={"female":"TGAAGGACCTTC", "male":"TGCAGGAACTTC"}
race={"white":"AAAACCTCA", "black":"CGACTACAG", "asian":"CGCGGGCCG"}


#color_pelo
if hair_color["black"] in dna:
    a = "pelo negro"

elif hair_color["brown"] in dna:
    a = "pelo marrón"

elif hair_color["blonde"] in dna:
    a = "pelo rubio"


#forma_cara
if facial_shape["square"] in dna:
    b = "cuadrada"

elif facial_shape["round"] in dna:
    b = "redonda"

elif facial_shape["oval"] in dna:
    b = "ovalada"

#color_ojos
if eye_color["blue"] in dna:
    c = "azules"
elif eye_color["green"] in dna:
    c = "verdes"
elif eye_color["brown"] in dna:
    c = "marrones"

#genero
if gender["male"] in dna:
    d = "masculino"
elif gender["female"] in dna:
    d = "femenino"

#Raza
if race["white"] in dna:
    e = "blanca"
elif race["black"] in dna:
    e = "negra"
elif race["asian"] in dna:
    e = "asiática"

print ("El sospechoso tiene el {0}, la cara {1}, color de ojos {2}, es de género {3} y corresponde a la raza {4}.".format(a.upper(),b.upper(),c.upper(),d.upper(),e.upper()))

ans = input("con estos datos, ya sabemos quién se ha zampado el helado. ¿Quieres saber quién ha sido?Y/N: ")

if ans.lower() == "y":
    if a == "pelo marrón" and b == "cuadrada" and c == "verdes" and d == "masculino" and e == "blanca":
        print ("el culpable es MIHA!!!")
    elif a == "pelo rubio" and b == "ovalada" and c == "azules" and d == "femenino" and e == "blanca":
        print ("la culpable es EVA!!!")
    elif a == "pelo marrón" and b == "ovalada" and c == "marrones" and d == "femenino" and e == "blanca":
        print ("la culpable es LARISA!!!")
    elif a == "pelo negro" and b == "ovalada" and c == "azules" and d == "masculino" and e == "blanca":
        print ("el culpable es MATEJ!!!")

else:
    print ("ok, bye!")