import math

__author__ = "Keezy Silencer"
"""
 Calculates the distance from one point on earth to the other 
"""


class CalculateDistance:
    _radius_of_earth = 6371e8  # in metres

    def distance(self, location_data, destination_data):
        """
        Calculates the distance between two points on a map using Haversine Formula
        :param location_data: Dict containing the longitude and latitude
        :param destination_data:  Dict containing the longitude and latitude
        :return: distance between two points in latitude in metres
        """
        distance_data = dict()
        # convert decimal degrees to radians
        location_data['longitude'], location_data['latitude'] = map(math.radians, [location_data['longitude'],
                                                                                   location_data['latitude']])
        destination_data['longitude'], destination_data['latitude'] = map(math.radians, [destination_data['longitude'],
                                                                                         destination_data['latitude']])
        # haversine formula
        distance_data["longitude"] = destination_data['longitude'] - location_data['longitude']
        distance_data['latitude'] = destination_data['latitude'] - location_data['latitude']
        a = math.sin(distance_data['latitude'] / 2) ** 2 + math.cos(location_data['latitude']) * math.cos(
            destination_data['latitude']) * math.sin(distance_data["longitude"] / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))

        return c * self._radius_of_earth

    def nearby_location(self, location_data, destination_data):
        """
        Calculates nearby locations within a [radius]
        :param location_data:     Dict containing the longitude and latitude
        :param destination_data:  Dict containing the longitude and latitude
        :return: Bool True when location is within radius and false otherwise
        """
        radius = 2000  # 2km
        if self.distance(location_data, destination_data) <= radius:
            return True
        else:
            return False
