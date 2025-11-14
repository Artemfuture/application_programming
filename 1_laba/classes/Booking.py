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

        self.id = str(uuid1())
        self.advertisement_id = advertisement_id
        self.renter_id = renter_id
        self.payment_id = payment_id
        self.date_start = date_start
        self.date_end = date_end
        self.status = status

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
        except:
            result = False
        return result

    def delete(self):  
        result = True
        return result
