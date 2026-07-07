import time

from app.db.database import SessionLocal

from app.services.position_service import save_position
from app.uwb.gateway import UWBGateway
from app.uwb.localization import LocalizationEngine

gateway = UWBGateway()
engine = LocalizationEngine()


def run():

    print("Pipeline started!")

    db = SessionLocal()

    while True:

        measurement = gateway.receive()

        print("Received measurement:")
        print(measurement)

        position = engine.calculate(measurement)

        print("Calculated position:")
        print(position)

        save_position(
            db=db,
            tag_id=position["tag_id"],
            x=position["x"],
            y=position["y"],
            z=position["z"],
        )

        print("Saved to database\n")

        time.sleep(1)
