import time
import random
import datetime

loadingtime = random.randint(3,5)

foutmelding = random.randint(100,800)

database = {"new york": '''New York is de grootste stad van de Verenigde Staten van Amerika. Dankzij de leidinggevende en invloedrijke rol in handel, financiën, media, public relations, kunst, mode en educatie geldt zij als een van de belangrijkste wereldsteden.
''', "amsterdam": "Amsterdam, de Nederlandse hoofdstad, staat bekend om het artistieke erfgoed, het uitgebreide grachtennetwerk en de smalle gevelhuizen, een erfenis uit de Gouden Eeuw. In het Museumkwartier bevinden zich het Van Gogh Museum, het Rijksmuseum met werken van Rembrandt en Vermeer, en het Stedelijk Museum met moderne kunst. Fietsen is onlosmakelijk verbonden met het karakter van de stad en er zijn veel fietspaden.", "istanbul": '''Istanboel of Istanbul is een stad in het Europese en Aziatische deel van Turkije en was de hoofdstad van het Ottomaanse Rijk. Daarvoor was ze onder de naam Constantinopel hoofdstad van het Byzantijnse Rijk. De stad is oorspronkelijk gesticht door Griekse kolonisten in 667 v.Chr. en werd door hen Byzantion genoemd.''', "parijs": '''Parijs is de hoofdstad en regeringszetel van Frankrijk. De stad wordt doorsneden door de rivier de Seine. Parijs zelf telde in 2014 ongeveer 2,22 miljoen inwoners, daarbij de banlieues niet meegerekend. In 2014 woonden er in de hele agglomeratie meer dan 10 miljoen mensen. Parijs ligt in de regio Île-de-France.''', "rome": '''Rome is de hoofdstad van Italië en het bestuurlijk centrum van de regio Lazio en de Città Metropolitana di Roma Capitale. De stad heeft ca. 2,8 miljoen inwoners, het inwonertal van de metropoolregio bedraagt 3,7 miljoen. Het is de grootste stad van Italië.''', "berlijn": '''Berlijn is de hoofdstad van Duitsland en als stadstaat een deelstaat van dat land. Met 3.437.916 inwoners is Berlijn tevens de grootste stad van het land en na Londen de grootste stad in de EU. De stad ligt in het noordoosten van Duitsland, aan de rivier de Spree.'''}

def keuze_stad():
    print('''
Over welke stad wil je informatie uitlezen kies uit:
New York
Amsterdam
Istanbul
Parijs
Rome
Berlijn
Uw keuze: ''')
    

def main():
  opdracht()
    
def menu():
    print('''************ MAIN MENU **************
************ ''' + str(datetime.datetime.now()) + ''' ************''')
    #time.sleep(1)
    
def opdracht():
    """Hier komt de code"""
    gebruiker = input("Voer je leerlingnummer in: ")
    klas = input("Voer je klas in: ")
    keuze = input('''
Wil je de landen database inlezen?
Typ "Ja" of "Nee" voor uw gewenste keuze: ''')

    
    keuze = keuze.lower()
    print(keuze)
    if keuze == "ja" or "Ja":
        datetime.datetime.now()
        datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
        keuze_stad()
        jouw_keuze = input()
        jouw_keuze = jouw_keuze.lower()
        
        f = open("inputlog.txt", "a")
        f.write("input van gebruiker: " + jouw_keuze + " " + str(datetime.datetime.now()) + " ingestuurd door: " + gebruiker + " klas: " + klas + "\n")
        f.close()
        if jouw_keuze in database:
            print()
            time.sleep(0.1)
            for i in reversed(range(0, loadingtime)):
              time.sleep(1)
              print("Loading Database... " + "%s\r" %i, end="")
            print(database[jouw_keuze])
        else:
          print("Incorrecte syntax zoek op de hulppagina op: Error " + str(foutmelding))
          print()
        
    elif keuze == "nee" or "Nee":
        print()
        print("Bedankt voor het bezoeken van de database!")
      
    
menu()
main()




