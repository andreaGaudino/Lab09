from dataclasses import dataclass


@dataclass
class Volo:
    _origin_airport_id : int
    _destination_airport_id : int
    _distance : int

    @property
    def origin_airport_id(self):
        return self._origin_airport_id
    @property
    def destination_airport_id(self):
        return self._destination_airport_id

    @property
    def distance(self):
        return self._distance
