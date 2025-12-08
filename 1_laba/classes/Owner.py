from uuid import uuid1


class Owner:
    def __init__(
        self,
        user_id: str = None,
        owns_flat_id: list[int] = None,
        reviews: list[int] = None,
    ):
        """
        id - uniq id
        user_id - id class User
        owns_flat_id - array of id class Addres
        reviews - array of id class Review
        """
        try:
            if not all(
                [
                    user_id is None or isinstance(user_id, str),
                    owns_flat_id is None or isinstance(owns_flat_id, list),
                    reviews is None or isinstance(reviews, list),
                ]
            ):
                raise TypeError
            self.id = str(uuid1())
            self.user_id = user_id
            self.owns_flat_id = owns_flat_id
            self.reviews = reviews
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            print("Error with init Owner")

    def update(self, flat_id: int = None, review: int = None) -> bool:
        result = True
        try:
            if not all(
                [
                    flat_id is None or isinstance(flat_id, int),
                    review is None or isinstance(review, int),
                ]
            ):
                raise TypeError
            if flat_id:
                self.owns_flat_id.append(flat_id)
            elif review:
                self.reviews.append(review)
            else:
                result = False
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            result = False
        return result

    def delete(self, flat_id: int = None):
        result = True
        try:
            if flat_id:
                self.owns_flat_id.remove(flat_id)
        except:
            result = False
        return result
