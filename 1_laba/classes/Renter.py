from uuid import uuid1


class Renter:

    def __init__(
        self,
        user_id: str = None,
        reviewings: list[str] = None,
        curent_booking: list[str] = None,
        cards: list[str] = None,
    ):
        """
        reviewings - array of id class Review
        curent_booking - array of id class Booking
        cards - array of id class Cards
        """
        self.id = str(uuid1())
        self.user_id = user_id
        self.reviewings = reviewings
        self.curent_booking = curent_booking
        self.cards = cards

    def update(self, review: str = None, booking: str = None, card: str = None) -> bool:
        result = True
        try:
            if review:
                self.reviewings.append(review)
            elif booking:
                self.curent_booking.append(booking)
            elif card:
                self.cards.append(card)
            else:
                result = False
        except:
            result = False
        return result

    def delete(self, review: str = None, booking: str = None, card: str = None):
        result = True
        try:
            if review:
                self.reviewings.remove(review)
            elif booking:
                self.curent_booking.remove(booking)
            elif card:
                self.cards.remove(card)
            else:
                result = False
        except:
            result = False
        return result
