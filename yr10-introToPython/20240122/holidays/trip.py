class Trip:
    def __init__(self, family_name, destination, no_passengers):
        self.family_name = family_name
        self.destination = destination
        self.no_passengers = no_passengers
    def generate_string(self):
        return f"Family name: {self.family_name} / Destination: {self.destination} / Number of Passengers: {self.no_passengers}"
    def change_family_name(self, name):
        self.family_name = name
    def change_destination(self, destination):
        self.destination = destination
    def change_passengers(self, passengers):
        self.no_passengers = passengers
    def generate_from_file(self, file_line):
        details = file_line.split("/")
