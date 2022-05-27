class Student:
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
# Allow change of names
    def changeName(self, newName):
        self.name = newName
        print('Student\'s name is updated as', newName)
# Allow change of age
    def changeAge(self, newAge):
        self.age = newAge
        print('Student\'s age is updated as', newAge) 
# Allow addition of new tracks
    def addTrack(self, newTrack):
        updatedTrack = self.tracks
        updatedTrack.append(newTrack)
        print('Student\'s track is updated as', updatedTrack)
        
# Return students current score
    def getScore(self):
        print('Student\'s current score is', self.score)         



Bob = Student("Bob", 26, ["FE","BE"], 20.90)

#Test initial stdout
print(Bob.name, Bob.age, Bob.tracks, Bob.score)


# Expected methods
Bob.changeName("Peter")
Bob.changeAge(34)
Bob.addTrack("UI/UX")
Bob.getScore()
  
