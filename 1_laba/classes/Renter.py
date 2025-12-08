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
        try:
            if not all(
                [
                    user_id is None or isinstance(user_id, str),
                    reviewings is None or isinstance(reviewings, list),
                    curent_booking is None or isinstance(curent_booking, list),
                    cards is None or isinstance(cards, list),
                ]
            ):
                raise TypeError
            self.id = str(uuid1())
            self.user_id = user_id
            self.reviewings = reviewings
            self.curent_booking = curent_booking
            self.cards = cards
        except TypeError:
            print("Error: something wrong with types")
            return False
        except:
            print("Error with init Renter")

    def update(self, review: str = None, booking: str = None, card: str = None) -> bool:
        result = True
        try:
            if not all(
                [
                    review is None or isinstance(review, str),
                    booking is None or isinstance(booking, str),
                    card is None or isinstance(card, str),
                ]
            ):
                raise TypeError
            if review:
                self.reviewings.append(review)
            elif booking:
                self.curent_booking.append(booking)
            elif card:
                self.cards.append(card)
            else:
                result = False
        except TypeError:
            print("Error: something wrong with types")
            return False
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
