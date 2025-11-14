from uuid import uuid1


class User:
    def __init__(
        self,
        name: str = None,
        email: str = None,
        phone_number: int = None,
        passport: int = None,
        user_type: str = None,
    ):
        """
        id - uniq id
        user_type - owner,renter,guest
        """

        self.id = str(uuid1())
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.passport = passport
        self.user_type = user_type

    def update(
        self,
        name: str = None,
        email: str = None,
        phone_number: int = None,
        passport: int = None,
        user_type: str = None,
    ) -> bool:
        result = True
        try:
            if name:
                self.name = name
            elif email:
                self.email = email
            elif phone_number:
                self.phone_number = phone_number
            elif passport:
                self.passport = passport
            elif user_type:
                self.user_type = user_type
            else:
                result = False
        except:
            result = False
        return result

    def delete(self):
        result = True
        return result
