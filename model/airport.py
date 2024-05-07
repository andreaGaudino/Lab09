from dataclasses import dataclass

@dataclass
class Airport:
    _id : int
    _iata_code : str
    _airport : str
    _city : str
    _state : str
    _country : str
    _latitude : float
    _longitude : float
    _timezone_offset : float
