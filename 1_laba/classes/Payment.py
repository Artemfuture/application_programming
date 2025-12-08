from uuid import uuid1


class Payment:

    def __init__(
        self,
        booking_id: str = None,
        amount: float = None,
        status: str = "unpaid",  # unpaid, paid, refunded
    ):
        try:
            if not all(
                [
                    booking_id is None or isinstance(booking_id, str),
                    amount is None or isinstance(amount, (int, float)),
                    status is None or isinstance(status, str),
                ]
            ):
                raise TypeError
            self.id = str(uuid1())
            self.booking_id = booking_id
            self.amount = amount
            self.status = status
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            print("Error with init Payment")

    def update(
        self, booking_id: str = None, amount: float = None, status: str = None
    ) -> bool:
        result = True
        try:
            if not all(
                [
                    booking_id is None or isinstance(booking_id, str),
                    amount is None or isinstance(amount, (int, float)),
                    status is None or isinstance(status, str),
                ]
            ):
                raise TypeError
            if booking_id:
                self.booking_id = booking_id
            elif amount:
                self.amount = amount
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
