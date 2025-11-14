from uuid import uuid1


class Payment:

    def __init__(
        self,
        booking_id: str = None,
        amount: float = None,
        status: str = "unpaid",  # unpaid, paid, refunded
    ):

        self.id = str(uuid1())
        self.booking_id = booking_id
        self.amount = amount
        self.status = status

    def update(
        self, booking_id: str = None, amount: float = None, status: str = None
    ) -> bool:
        result = True
        try:
            if booking_id:
                self.booking_id = booking_id
            elif amount:
                self.amount = amount
            elif status:
                self.status = status
            else:
                result = False
        except:
            result = False
        return result

    def delete(self):
        result = True
        return result
