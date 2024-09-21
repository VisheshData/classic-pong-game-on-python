from turtle import Screen

screen=Screen()

class Mode():
    def __init__(self):
        self.mode_input='C'
        
    def choose_mode(self):
        self.mode_input= screen.textinput("Choose", "Against computer(press 'C') or Against player(press'V')")
        return self.mode_input.lower()

        

