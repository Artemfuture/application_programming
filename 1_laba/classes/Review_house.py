from uuid import uuid1


class Review_house:
    def __init__(
        self,
        advertisment_id: str = None,
        addres_id: str = None,
        renter_id: str = None,
        rating: int = None,
        comment: str = None,
    ):
        """
        id - uniq id
        """
        try:
            if not all(
                [
                    advertisment_id is None or isinstance(advertisment_id, str),
                    addres_id is None or isinstance(addres_id, str),
                    renter_id is None or isinstance(renter_id, str),
                    rating is None or isinstance(rating, int),
                    comment is None or isinstance(comment, str),
                ]
            ):
                raise TypeError
            self.id = str(uuid1())
            self.advertisment_id = advertisment_id
            self.addres_id = addres_id
            self.renter_id = renter_id
            self.rating = rating
            self.comment = comment
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            print("Error with init Adverstisment")

    def update(
        self,
        advertisment_id: str = None,
        addres_id: str = None,
        renter_id: str = None,
        rating: int = None,
        comment: str = None,
    ) -> bool:
        result = True
        try:
            if not all(
                [
                    advertisment_id is None or isinstance(advertisment_id, str),
                    addres_id is None or isinstance(addres_id, str),
                    renter_id is None or isinstance(renter_id, str),
                    rating is None or isinstance(rating, int),
                    comment is None or isinstance(comment, str),
                ]
            ):
                raise TypeError
            if advertisment_id:
                self.advertisment_id = advertisment_id
            elif addres_id:
                self.addres_id = addres_id
            elif renter_id:
                self.renter_id = renter_id
            elif rating:
                self.rating = rating
            elif comment:
                self.comment = comment
            else:
                result = False
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            result = False
        return result

    def delete(self, comment: str = None):
        result = True
        try:
            if comment:
                self.comment = comment
        except:
            result = False
        return result
