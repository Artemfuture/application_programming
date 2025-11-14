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

        self.id = str(uuid1())
        self.advertisment_id = advertisment_id
        self.addres_id = addres_id
        self.renter_id = renter_id
        self.rating = rating
        self.comment = comment

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
        except:
            result = False
        return result

    def delete(self, comment: str = None):
        result = True
        try:
            if comment:
                self.comment = None
        except:
            result = False
        return result
