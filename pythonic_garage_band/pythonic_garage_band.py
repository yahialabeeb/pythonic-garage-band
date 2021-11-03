class Band:
    instances = []
    def __init__(self, name, members: list):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        listy = []
        for member in self.members: 
            listy.append(member.play_solo())
        return listy


    @classmethod
    def to_list(cls):
        return cls.instances

        

class Musician:
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"{self.job} instance. Name = {self.name}"


class Guitarist(Musician):

    def __init__(self, name):
        self.name = name
        self.job = "Guitarist"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self.job = "Bassist"
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self.job = "Drummer"
    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"