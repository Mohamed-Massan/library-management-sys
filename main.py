from etudient import *
from livre import Books, Livre
from emprunt import Emprunt

def gestion_etudients(g):
    touch = ['a','r','f']
    c = '1'
    while c !='f':
        try:
            print("'A' pour ajouter un etudient\n'R' pour rechercher un etudient\n'F' Fermer")
            c = input('Faite votre choix: ')
            if c == 'a':
                nce = int(input("enter le NCE du nouveau etudient: "))
                e = g.trouver(nce)
                if e != None:
                    raise Exception("Letudient deja existe!")
                nom = input("enter le nom: ")
                if isinstance(nom, str):
                    raise Exception('dakhal issm machi ar9am al9erd')
                g.ajouter(Etudient(nce,nom))
                print("letudient a ete ajouetr avec succes!")
            if c == 'r':
                nce = int(input("entrer le NCE detudient a rechercher: "))
                e = g.trouver(nce)
                if e == None:
                    raise Exception('letudient nexist pas!')
                print(e)
            if c == 'f':
                print('Fin de programme')

            if not c in touch:
                print('Touch incorrect !')
        except Exception as err:
            print(err)


def gestion_livre(b):
    touch = [1,2,3]
    c = "k"
    while c != 3:
        try:
            print("1 pour ajouter un livre")
            print("2 pour chercher un livre")
            print("3 fermer")
            c = int(input("faites votre choix: "))
            if c == 1:
                code = int(input("Enter le code: "))
                e = b.trouver(code)
                if e != None:
                    raise Exception("le livre deja existe ")
                title = input("entre le nom de livre: ")
                ndex = int(input("ente le nombre d'exemplaire: "))
                b.ajouter(Livre(code,title,ndex))
                print("Livre a ete ajouetr avec succes!")
                
            if c == 2:
                code = int(input("entrer le code de livre a rechercher: "))
                e = b.trouver(code)
                if e == None:
                    raise Exception('livre nexist pas!')
                print('\n',e, '\n')
            if c == 3:
                print("fin de programme!")
            if not c in touch:
                print('Touch incorrect !')
                
        except Exception as err:
            print(err)
def gestion_emprunt(biblio):
    pass
        
touch = [1,2,3,4]
c = 'p'
biblio = Emprunt(Groupe(),Books())
while c != 4:
    try:
        print('1 Gestion detudients')
        print('2 Gestion Des livres')
        print('3 Gestion Des epmprunte')
        print('4 quiet lapplication')
        c = int(input("Faite votre choix: "))
        if c == 1:
            gestion_etudients(biblio.g)
        if c == 2:
            gestion_livre(biblio.b)
        if c == 3:
            gestion_emprunt(biblio)
        if c == 4:
            print("Fin de programme")
        if not c in touch:
            print("Touch incorrect")
    except Exception as err:
        print(err)
