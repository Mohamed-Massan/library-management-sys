class Books():
    def __init__(self) -> None:
        self.bk = dict()
    def ajouter(self,lv):
        self.bk[lv.code] = lv
    def trouver(self, code):
        if code in self.bk:
            return self.bk[code]
        
class Livre():
    def __init__(self, code, title, ndex):
        self.__code = code
        self.__title = title
        self.__ndex = ndex
    def get_code(self):
        return self.__code
    def get_title(self):
        return self.__title
    def get_ndex(self):
        return self.__ndex
    def set_code(self,new_code):
        self.__code = new_code
    def set_title(self,new_title):
        self.__title = new_title
    def set_ndex(self,new_ndex):
        self.__ndex = new_ndex
    code = property(get_code,set_code)
    title = property(get_title,set_title)
    ndex = property(get_ndex,set_ndex)
    
    
    def __str__(self):
        return  "Books info --> Code: {} Title: {} Ndex: {}".format(self.code, self.title, self.ndex)