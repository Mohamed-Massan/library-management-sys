class Groupe():
    def __init__(self) -> None:
        self.gr = dict()
    def ajouter(self, et):
        self.gr[et.nce] = et 
    def trouver(self, nce):
        if nce in self.gr:
            return self.gr[nce]
        return None
        
        
        
    

class Etudient(object):
    __statut = 'National'
    def __init__(self,nce,nom):
        self.__nce = nce
        self.__nom = nom
        self.books = dict()
    
    def get_statut(self):
        return self.__statut
    def set_status(self,new_statut):
        self.__statut = new_statut
    statut = property(get_statut,set_status)
    
    def get_nce(self):
        return self.__nce
    def set_nce(self,new_nce):
        if new_nce < -1:
            raise Exception("nce doit erte greater than 0")
        self.__nce = new_nce
    nce = property(get_nce,set_nce)

    def get_nom(self):
        return self.__nom
    def set_nom(self,new_nom):
        self.__nom = new_nom
    nom = property(get_nom,set_nom)
    
    def __eq__(self, __o: object):
        if (__o == None):
            return False
        return self.nce == __o   
    def emprunter(self, lv):
        if len(self.books) == 2:
            return 'vous navez pas le droit demprunter plus dun 2 livres'
        if lv.code in self.books:
            return 'vous possedez deja se livre'
        if lv.ndex == 0:
            return 'se live ne pas disponible'
        lv.ndex -= 1
        self.books[lv.code] = lv
        return 'le livre a ete emprunter'

    def rendre(self, lv):
        if not lv.code in self.books:
            return 'le livre a rendre vous ne possede pas'
        lv.ndex += 1
        l = self.books.pop(lv.code)
        return l.__str__() + 'a ete rendu'
        
    def __str__(self):
        ch = """
Etudient info
-------------
NCE:    {}
Nom:    {}
Status: {}
""".format(self.nce, self.nom, self.statut)
        for lv in self.books.values():
            if lv != None:
                ch += " " + lv.__str__()
        return ch