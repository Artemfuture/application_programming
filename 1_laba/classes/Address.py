from uuid import uuid1


class Address:
    def __init__(
        self,
        country: str = None,
        city: str = None,
        street: str = None,
        house: int = None,
        building: str = None,
        entrance: int = None,
        floor: int = None,
        flat_number: int = None,
        postal_code: str = None,
        latitude: float = None,
        longitude: float = None,
    ):
        self.id = str(uuid1())
        self.country = country
        self.city = city
        self.street = street
        self.house = house
        self.building = building
        self.entrance = entrance
        self.floor = floor
        self.flat_number = flat_number
        self.postal_code = postal_code
        self.latitude = latitude
        self.longitude = longitude

    def update(
        self,
        country: str = None,
        city: str = None,
        street: str = None,
        house: int = None,
        building: str = None,
        entrance: int = None,
        floor: int = None,
        flat_number: int = None,
        postal_code: str = None,
        latitude: float = None,
        longitude: float = None,
    ) -> bool:
        result = True
        try:
            if country:
                self.country = country
            elif city:
                self.city = city
            elif street:
                self.street = street
            elif house:
                self.house = house
            elif building:
                self.building = building
            elif entrance:
                self.entrance = entrance
            elif floor:
                self.floor = floor
            elif flat_number:
                self.flat_number = flat_number
            elif postal_code:
                self.postal_code = postal_code
            elif latitude:
                self.latitude = latitude
            elif longitude:
                self.longitude = longitude
            else:
                result = False
        except:
            result = False
        return result

    def delete(self):
        result = True
        return result
