from uuid import uuid1


class Review_user:

    def __init__(
        self,
        user_id_gave: str = None,
        user_id_whom: str = None,
        rating: int = None,
        comment: str = None,
    ):

        self.id = str(uuid1())
        self.user_id_gave = user_id_gave
        self.user_id_whom = user_id_whom
        self.rating = rating
        self.comment = comment

    def update(
        self,
        user_id_gave: str = None,
        user_id_whom: str = None,
        rating: int = None,
        comment: str = None,
    ) -> bool:
        result = True
        try:
            if user_id_gave:
                self.user_id_gave = user_id_gave
            elif user_id_whom:
                self.user_id_whom = user_id_whom
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
