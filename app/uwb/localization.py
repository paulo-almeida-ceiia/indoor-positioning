from app.uwb.models import Measurement


class LocalizationEngine:

    def calculate(self, measurement: Measurement):

        return {

            "tag_id": measurement.tag_id,

            "x": measurement.distances[1],

            "y": measurement.distances[2],

            "z": 1.5,
        }