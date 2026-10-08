class Soldat():
    def __init__(self, rank, name, surname, age, gender, perk, primary_slot, secondary_slot):
        self.rank = rank
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.perk = perk
        self.primary_weapon = primary_slot
        self.secondary_weapon = secondary_slot
        

    def soldat_pers_infos(self):
        print(f"{self.rank} {self.name} {self.surname}, Age: {self.age}, Gender: {self.gender}")

    def soldat_equip_infos(self):
        print(f"Perk: {self.perk}, Primary Slot: {self.primary_weapon}, Secondary Slot: {self.secondary_weapon}")
