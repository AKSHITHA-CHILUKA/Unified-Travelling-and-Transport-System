# RideSharing.py

class RideShare:
    def __init__(self):
        self.rides = []

    def add_ride(self, origin, destination, driver, capacity):
        ride = {
            "origin": origin,
            "destination": destination,
            "driver": driver,
            "capacity": capacity,
            "passengers": []
        }
        self.rides.append(ride)
        return ride

    def join_ride(self, ride_id, passenger):
        for ride in self.rides:
            if ride_id == id(ride) and len(ride["passengers"]) < ride["capacity"]:
                ride["passengers"].append(passenger)
                return True
        return False

if __name__ == "__main__":
    ride_share = RideShare()
    ride1 = ride_share.add_ride("Location A", "Location B", "Driver 1", 4)
    ride2 = ride_share.add_ride("Location C", "Location D", "Driver 2", 3)
    ride_share.join_ride(id(ride1), "Passenger 1")
    ride_share.join_ride(id(ride1), "Passenger 2")
    print(ride_share.rides)
