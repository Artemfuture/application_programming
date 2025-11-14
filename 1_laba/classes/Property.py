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
