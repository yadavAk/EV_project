#The Project is under development stage
import specs


class vehicle:
    
    def charging():
        pass

    def discharing():
        pass

    def default():
        # includes average rolling resistance and aerodynamic drag
        # here while calculating aerodynamic drag wind speed is assumed to be zero with respect to ground
        # aerodynamic drag depends on front area of car in this case
        return 0

    def complete_stop_regen():
        # This will give loss of power in complete stopping of car with regenerative braking
        return 0   #constant depends on car model
    def complete_stop_non_regen():
        # This will give loss of power in complete stopping of car with instant breaking
        return 0    # constant depends on car model

