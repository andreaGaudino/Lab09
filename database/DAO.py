from database.DB_connect import DBConnect
from model.airport import Airport
from model.volo import Volo


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllFlights(distance):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT origin_airport_id, destination_airport_id, distance
                    from flights
                    where distance <= %s
                    order by distance"""

        cursor.execute(query, (distance,))

        for row in cursor:
            result.append(Volo(row["origin_airport_id"], row["destination_airport_id"], row["distance"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT *
                    from airports
                        """

        cursor.execute(query)

        for row in cursor:
            result.append(Airport(row["id"], row["iata_code"], row["airport"], row["city"],row["state"], row["country"], row["latitude"], row["longitude"], row["timezone_offset"]))
        cursor.close()
        conn.close()
        return result