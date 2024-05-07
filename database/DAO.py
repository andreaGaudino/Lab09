from database.DB_connect import DBConnect
from model.airport import Airport
from model.volo import Volo


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllFlights():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT origin_airport_id, destination_airport_id, distance
                    from flights
                    """

        cursor.execute(query)

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
            result.append(Airport(row["ID"], row["IATA_CODE"], row["AIRPORT"], row["CITY"],row["STATE"], row["COUNTRY"], row["LATITUDE"], row["LONGITUDE"], row["TIMEZONE_OFFSET"]))
        cursor.close()
        conn.close()
        return result