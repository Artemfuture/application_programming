from uuid import uuid1


class Review_user:

    def __init__(
        self,
        user_id_gave: str = None,
        user_id_whom: str = None,
        rating: int = None,
        comment: str = None,
    ):
        try:
            if not all(
                [
                    user_id_gave is None or isinstance(user_id_gave, str),
                    user_id_whom is None or isinstance(user_id_whom, str),
                    rating is None or isinstance(rating, int),
                    comment is None or isinstance(comment, str),
                ]
            ):
                raise TypeError
            self.id = str(uuid1())
            self.user_id_gave = user_id_gave
            self.user_id_whom = user_id_whom
            self.rating = rating
            self.comment = comment
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            print("Error with init Review_user")

    def update(
        self,
        user_id_gave: str = None,
        user_id_whom: str = None,
        rating: int = None,
        comment: str = None,
    ) -> bool:
        result = True
        try:
            if not all(
                [
                    user_id_gave is None or isinstance(user_id_gave, str),
                    user_id_whom is None or isinstance(user_id_whom, str),
                    rating is None or isinstance(rating, int),
                    comment is None or isinstance(comment, str),
                ]
            ):
                raise TypeError
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
