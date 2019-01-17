#The Project is under development stage
import specs

class env_conditions:

    def elevation(height=0):
        # get height data from google maps
        return CAR_MASS*9.8*height

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