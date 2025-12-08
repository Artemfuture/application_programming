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
        try:
            if not all(
                [
                    name is None or isinstance(name, str),
                    email is None or isinstance(email, str),
                    phone_number is None or isinstance(phone_number, int),
                    passport is None or isinstance(passport, int),
                    user_type is None or isinstance(user_type, str),
                ]
            ):
                raise TypeError
            self.id = str(uuid1())
            self.name = name
            self.email = email
            self.phone_number = phone_number
            self.passport = passport
            self.user_type = user_type
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            print("Error with init Property")

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
            if not all(
                [
                    name is None or isinstance(name, str),
                    email is None or isinstance(email, str),
                    phone_number is None or isinstance(phone_number, int),
                    passport is None or isinstance(passport, int),
                    user_type is None or isinstance(user_type, str),
                ]
            ):
                raise TypeError
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
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            result = False
        return result

    def delete(self):
        result = True
        return result
