import pickle

class Char:
    name = "undefined"

    def __init__(self):
        #self.race = race
        self.exp = 0
        self.lvl = 1
        self.str = str
        self.int = int
        #self.dex = dex
        #self.con = con
        #self.spd = spd
        #self.hp = (con + str) / 2
        #self.current_hp = self.hp
        #self.mp_bonus = mp_bonus
        #self.mp = (int * mp_bonus)
        #self.current_mp = self.mp

    def save(self):
        with open("save.pk1", "wb") as fp:
            pickle.dump(self, fp, protocol=pickle.HIGHEST_PROTOCOL)

def load():
    with open('save.pk1', 'rb') as fp:
        return pickle.load(fp) # no idea what to put here 
                                        # or if it should be in the Char class or not

