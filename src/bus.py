class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passenger = []
    
    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passenger)
    
    def pick_up(self, person):
        self.passenger.append(person)
    
    def drop_off(self, person):
        self.passenger.remove(person)

    def empty(self):
        self.passenger.clear()

    def pick_up_from_stop(self, bus_stop):
        # self.pick_up(bus_stop.queue)
        for person in bus_stop.queue:
            self.passenger.append(person)
        bus_stop.clear()