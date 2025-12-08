from uuid import uuid1


class Property:

    def __init__(
        self,
        owner_id: str = None,
        address_id: str = None,
        property_type: str = None,  # apartment, house, room
        description: str = None,
        rooms: int = None,
        beds: int = None,
        bathrooms: int = None,
        area: float = None,
        amenities: list[str] = None,
    ):
        try:
            if not all(
                [
                    owner_id is None or isinstance(owner_id, str),
                    address_id is None or isinstance(address_id, str),
                    property_type is None or isinstance(property_type, str),
                    description is None or isinstance(description, str),
                    rooms is None or isinstance(rooms, int),
                    beds is None or isinstance(beds, int),
                    bathrooms is None or isinstance(bathrooms, int),
                    area is None or isinstance(area, (int, float)),
                    amenities is None or isinstance(amenities, list),
                ]
            ):
                raise TypeError
            self.id = str(uuid1())
            self.owner_id = owner_id
            self.address_id = address_id
            self.property_type = property_type
            self.description = description
            self.rooms = rooms
            self.beds = beds
            self.bathrooms = bathrooms
            self.area = area
            self.amenities = amenities
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            print("Error with init Property")

    def update(
        self,
        owner_id: str = None,
        address_id: str = None,
        property_type: str = None,
        description: str = None,
        rooms: int = None,
        beds: int = None,
        bathrooms: int = None,
        area: float = None,
        amenitie: str = None,
    ) -> bool:
        result = True
        try:
            if not all(
                [
                    owner_id is None or isinstance(owner_id, str),
                    address_id is None or isinstance(address_id, str),
                    property_type is None or isinstance(property_type, str),
                    description is None or isinstance(description, str),
                    rooms is None or isinstance(rooms, int),
                    beds is None or isinstance(beds, int),
                    bathrooms is None or isinstance(bathrooms, int),
                    area is None or isinstance(area, (int, float)),
                    amenitie is None or isinstance(amenitie, str),
                ]
            ):
                raise TypeError
            if owner_id:
                self.owner_id = owner_id
            elif address_id:
                self.address_id = address_id
            elif property_type:
                self.property_type = property_type
            elif description:
                self.description = description
            elif rooms:
                self.rooms = rooms
            elif beds:
                self.beds = beds
            elif bathrooms:
                self.bathrooms = bathrooms
            elif area:
                self.area = area
            elif amenitie:
                self.amenities.append(amenitie)
            else:
                result = False
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            result = False
        return result

    def delete(self, amenitie: str = None):
        result = True
        try:
            if amenitie:
                self.amenities.remove(amenitie)
            else:
                result = False
        except:
            result = False
        return result
