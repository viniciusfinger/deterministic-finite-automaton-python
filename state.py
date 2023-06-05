class State:
    def __init__(self, id, is_initial = False, is_final = False) -> None:
        self.id = id
        self.is_initial = is_initial
        self.is_final = is_final
    
    def __str__(self) -> str:
        return "Estado: {}, Inicial: {}, Final: {}".format(self.id, self.is_initial, self.is_final)
    