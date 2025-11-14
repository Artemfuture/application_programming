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

        self.id = str(uuid1())
        self.user_id = user_id
        self.owns_flat_id = owns_flat_id
        self.reviews = reviews

    def update(self, flat_id: int = None, review: int = None) -> bool:
        result = True
        try:
            if flat_id:
                self.owns_flat_id.append(flat_id)
            elif review:
                self.reviews.append(review)
            else:
                result = False
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
