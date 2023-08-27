class Electronic_Device:
    pass

class Pocket_Gadgets(Electronic_Device):
    camera=1
    def show(self):
        return f"It has {self.camera} no. of cameras"

class Phones(Pocket_Gadgets):
    camera=4
    def show(self):
        return f"It has {self.camera} no. of cameras"