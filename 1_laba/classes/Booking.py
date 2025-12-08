from datetime import date
from uuid import uuid1


class Booking:

    def __init__(
        self,
        advertisement_id: str = None,
        renter_id: str = None,
        payment_id: str = None,
        date_start: date = None,
        date_end: date = None,
        status: str = None,
    ):
        try:
            if not all(
                [
                    advertisement_id is None or isinstance(advertisement_id, str),
                    renter_id is None or isinstance(renter_id, str),
                    payment_id is None or isinstance(payment_id, str),
                    date_start is None or isinstance(date_start, date),
                    date_end is None or isinstance(date_end, date),
                    status is None or isinstance(status, str),
                ]
            ):
                raise TypeError
            self.id = str(uuid1())
            self.advertisement_id = advertisement_id
            self.renter_id = renter_id
            self.payment_id = payment_id
            self.date_start = date_start
            self.date_end = date_end
            self.status = status
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            print("Error with init Booking")

    def update(
        self,
        advertisement_id: str = None,
        renter_id: str = None,
        payment_id: str = None,
        date_start: date = None,
        date_end: date = None,
        status: str = None,
    ) -> bool:
        result = True
        try:
            if not all(
                [
                    advertisement_id is None or isinstance(advertisement_id, str),
                    renter_id is None or isinstance(renter_id, str),
                    payment_id is None or isinstance(payment_id, str),
                    date_start is None or isinstance(date_start, date),
                    date_end is None or isinstance(date_end, date),
                    status is None or isinstance(status, str),
                ]
            ):
                raise TypeError
            if advertisement_id:
                self.advertisement_id = advertisement_id
            elif renter_id:
                self.renter_id = renter_id
            elif payment_id:
                self.payment_id = payment_id
            elif date_start:
                self.date_start = date_start
            elif date_end:
                self.date_end = date_end
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
