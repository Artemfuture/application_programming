from datetime import date
from uuid import uuid1


class Advertisment:

    def __init__(
        self,
        address_id: str = None,
        owner_id: str = None,
        price_for_night: float = None,
        start_date: date = None,
        end_date: date = None,
        property_id: str = None,
        review_ids: list[str] = None,
        status: str = "pending",  # pending, confirmed, canceled, completed
    ):
        """
        id - uniq id
        """
        try:
            if not all(
                [
                    address_id is None or isinstance(address_id, str),
                    owner_id is None or isinstance(owner_id, str),
                    price_for_night is None
                    or isinstance(price_for_night, (int, float)),
                    start_date is None or isinstance(start_date, date),
                    end_date is None or isinstance(end_date, date),
                    property_id is None or isinstance(property_id, str),
                    review_ids is None or isinstance(review_ids, list),
                    status is None or isinstance(status, str),
                ]
            ):
                raise TypeError
            self.id = str(uuid1())
            self.address_id = address_id
            self.owner_id = owner_id
            self.price_for_night = price_for_night
            self.start_date = start_date
            self.end_date = end_date
            self.property_id = property_id
            self.review_ids = review_ids
            self.status = status
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            print("Error with init Adverstisment")

    def update(
        self,
        address_id: str = None,
        owner_id: str = None,
        price_for_night: float = None,
        start_date: date = None,
        end_date: date = None,
        property_id: str = None,
        review_id: str = None,
        status: str = None,
    ) -> bool:
        result = True
        try:
            if not all(
                [
                    address_id is None or isinstance(address_id, str),
                    owner_id is None or isinstance(owner_id, str),
                    price_for_night is None
                    or isinstance(price_for_night, (int, float)),
                    start_date is None or isinstance(start_date, date),
                    end_date is None or isinstance(end_date, date),
                    property_id is None or isinstance(property_id, str),
                    review_id is None or isinstance(review_id, str),
                    status is None or isinstance(status, str),
                ]
            ):
                raise TypeError
            if address_id:
                self.address_id = address_id
            elif owner_id:
                self.owner_id = owner_id
            elif price_for_night:
                self.price_for_night = price_for_night
            elif start_date:
                self.start_date = start_date
            elif end_date:
                self.end_date = end_date
            elif property_id:
                self.property_id = property_id
            elif review_id:
                self.review_ids.append(review_id)
            elif status:
                self.status = status
            else:
                result = False
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            result = False
        return result

    def delete(self):
        result = True
        return result
