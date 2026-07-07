import random
from datetime import datetime

from app.uwb.models import Measurement


class Simulator:

    def generate(self):

        return Measurement(

            tag_id=1,

            distances={

                1: round(random.uniform(2, 8), 2),

                2: round(random.uniform(2, 8), 2),

                3: round(random.uniform(2, 8), 2),

                4: round(random.uniform(2, 8), 2),

            },

            timestamp=datetime.now(),
        )