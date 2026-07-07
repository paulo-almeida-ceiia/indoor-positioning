from app.uwb.gateway import UWBGateway

gateway = UWBGateway()

measurement = gateway.receive()

print(measurement)
