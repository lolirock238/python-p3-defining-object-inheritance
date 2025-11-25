class Vehicle:
    """Parent class for all vehicles."""
    
    def __init__(self, wheel_size, wheel_number):
        """Initialize a vehicle with wheel size and number."""
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        """Make the vehicle go."""
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        """Fill up the vehicle's tank."""
        return "filling up!"