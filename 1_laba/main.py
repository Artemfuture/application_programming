from classes import *
from manager import Manager
from datetime import date


info = Manager(json_path="test.json", xml_path="test.xml")
user_own = User(
    name="Pety",
    email="pety@gmail.com",
    phone_number=777777777,
    passport=4444444444,
    user_type="owner",
)
user_renter = User(
    name="Vasy",
    email="vasy@gmail.com",
    phone_number=8888888888,
    passport=3333333333,
    user_type="renter",
)
addres = Address(
    country="Russia",
    city="Moscow",
    street="Pervay",
    house=1,
    building="c2",
    entrance=3,
    floor=4,
    flat_number=765,
    postal_code="123456",
    latitude=1.4556,
    longitude=54.6344,
)
own = Owner(user_id=user_own.id, owns_flat_id=[addres.id])
property = Property(
    owner_id=own.id,
    address_id=addres.id,
    property_type="appartment",
    description="super room in the center of city",
    rooms=1,
    beds=1,
    bathrooms=1,
    area=10.0,
    amenities=["wi-fi", "window", "parking"],
)
advertisment = Advertisment(
    address_id=addres.id,
    owner_id=own.id,
    price_for_night=1.2,
    start_date=date(2025, 11, 11),
    end_date=date(2025, 11, 13),
    property_id=property.id,
    status="completed",
)
review_house = Review_house(
    advertisment_id=advertisment.id,
    addres_id=addres.id,
    renter_id=user_renter.id,
    rating=5,
    comment="super flat",
)
advertisment.update(review_id=review_house.id)
cards = Cards(user_id=user_renter.id, number=1234556678, date="06/32", csv=123)
renter = Renter(user_id=user_renter.id, reviewings=[review_house.id], cards=[cards.id])
booking = Booking(
    advertisement_id=advertisment.id,
    renter_id=user_renter.id,
    date_start=date(2025, 11, 11),
    date_end=date(2025, 11, 13),
    status="proggres",
)
renter.update(booking=booking.id)
payment = Payment(booking_id=booking.id, amount=1234)
booking.update(payment_id=payment.id)
review_user = Review_user(
    user_id_gave=user_own.id, user_id_whom=user_renter.id, rating=2, comment="rude man"
)


info.add(user_own)
info.add(user_renter)
info.add(addres)
info.add(own)
info.add(property)
info.add(advertisment)
info.add(review_house)
info.add(cards)
info.add(renter)
info.add(booking)
info.add(payment)
info.add(review_user)

info.save_json()
info.save_xml()
data = info.load_json()
info.data = data
info.save_json()
