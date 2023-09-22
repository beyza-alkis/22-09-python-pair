class ogretmen:
    
    def __init__(self, name:str, classroom:str):
        self.name = name
        self.classroom= classroom

    def change_teacher_name(self, name:str):
        self.name = name
    
    def change_classroom(self, classroom:str):
        self.classroom = classroom
    