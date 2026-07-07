from app.uwb.simulator import Simulator


class UWBGateway:

    def __init__(self):

        self.simulator = Simulator()

    def receive(self):

        return self.simulator.generate()