print("Hello! This is simulation code")

#Car specifications
CAR_FRONT_AREA = 0
CAR_BACK_AREA = 0
CAR_MASS = 0


SEG_LEN = 0

def default():
    # includes average rolling resistance and aerodynamic drag
    # here while calculating aerodynamic drag wind speed is assumed to be zero with respect to ground
    # aerodynamic drag depends on front area of car in this case
    return 0

def elevation():
    # get height data from google maps
    return CAR_MASS*9.8*height

def complete_stop_regen():
    # This will give loss of power in complete stopping of car with regenerative braking
    return 0   #constant depends on car model
def complete_stop_non_regen():
    # This will give loss of power in complete stopping of car with instant breaking
    return 0    # constant depends on car model


class env_conditions:
    def wind():
        # get the data wind velocity from wether related website
        return 0

    def temperature():
        # get the outside temperature data from sensor
        return 0

    def day_night():
        # headlights
        return 0

    def rain():
        # will affect rolling resistance coffecient
        # may need to turn on the wipers
        return 0

    def driver_behaviour():
        # ML algos
        return 0



