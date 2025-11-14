import json
import xml.etree.ElementTree as ET
from datetime import datetime
import inspect
from xml.dom import minidom
from classes import *

class Manager:
    def __init__(self, json_path, xml_path):
        self.json_path = json_path
        self.xml_path = xml_path
        self.data = []

    def add(self, obj):
        self.data.append(obj)

    def update(self, obj, **kwargs) -> bool:

        result = obj.update(**kwargs)
        self.save_xml()
        self.save_json()
        return result

    def delete(self, obj, **kwargs) -> bool:
        result = obj.delete(**kwargs)
        self.save_xml()
        self.save_json()
        return result

    def save_json(self):
        data = json.dumps(
            [{i.__class__.__name__: i.__dict__} for i in self.data],
            indent=4,
            default=str,
        )
        with open(self.json_path, "w", encoding="utf-8") as f:
            f.write(data)

    def save_xml(self) -> None:
        root = ET.Element("note")
        for classes in self.data:
            cl = classes.__class__.__name__
            if cl == "User":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "name").text = classes.name
                ET.SubElement(pe, "email").text = classes.email
                ET.SubElement(pe, "phone_number").text = str(classes.phone_number)
                ET.SubElement(pe, "passport").text = str(classes.passport)
                ET.SubElement(pe, "user_type").text = classes.user_type
            elif cl == "Address":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "country").text = classes.country
                ET.SubElement(pe, "city").text = classes.city
                ET.SubElement(pe, "street").text = classes.street
                ET.SubElement(pe, "house").text = str(classes.house)
                ET.SubElement(pe, "building").text = classes.building
                ET.SubElement(pe, "entrance").text = str(classes.entrance)
                ET.SubElement(pe, "floor").text = str(classes.floor)
                ET.SubElement(pe, "flat_number").text = str(classes.flat_number)
                ET.SubElement(pe, "postal_code").text = classes.postal_code
                ET.SubElement(pe, "latitude").text = str(classes.latitude)
                ET.SubElement(pe, "longitude").text = str(classes.longitude)
            elif cl == "Owner":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "user_id").text = classes.user_id
                if classes.owns_flat_id:
                    flat = ET.SubElement(pe, "owns_flat_id")
                    for i in classes.owns_flat_id:
                        ET.SubElement(flat, "flat").text = str(i)
                if classes.reviews:
                    review = ET.SubElement(pe, "reviews")
                    for i in classes.reviews:
                        ET.SubElement(review, "review").text = str(i)
            elif cl == "Property":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "owner_id").text = classes.owner_id
                ET.SubElement(pe, "address_id").text = classes.address_id
                ET.SubElement(pe, "property_type").text = classes.property_type
                ET.SubElement(pe, "description").text = classes.description
                ET.SubElement(pe, "rooms").text = str(classes.rooms)
                ET.SubElement(pe, "beds").text = str(classes.beds)
                ET.SubElement(pe, "bathrooms").text = str(classes.bathrooms)
                ET.SubElement(pe, "area").text = str(classes.area)
                if classes.amenities:
                    am = ET.SubElement(pe, "amenities")
                    for i in classes.amenities:
                        ET.SubElement(am, "amentity").text = i
            elif cl == "Advertisment":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "address_id").text = classes.address_id
                ET.SubElement(pe, "owner_id").text = classes.owner_id
                ET.SubElement(pe, "price_for_night").text = str(classes.price_for_night)
                ET.SubElement(pe, "start_date").text = str(classes.start_date)
                ET.SubElement(pe, "end_date").text = str(classes.end_date)
                ET.SubElement(pe, "property_id").text = classes.property_id
                if classes.review_ids:
                    review = ET.SubElement(pe, "review_ids")
                    for i in classes.review_ids:
                        ET.SubElement(review, "review").text = i
                ET.SubElement(pe, "status").text = classes.status
            elif cl == "Review_house":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "advertisment_id").text = classes.advertisment_id
                ET.SubElement(pe, "addres_id").text = classes.addres_id
                ET.SubElement(pe, "renter_id").text = classes.renter_id
                ET.SubElement(pe, "rating").text = str(classes.rating)
                ET.SubElement(pe, "comment").text = classes.comment
            elif cl == "Cards":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "user_id").text = classes.user_id
                ET.SubElement(pe, "number").text = str(classes.number)
                ET.SubElement(pe, "date").text = classes.date
                ET.SubElement(pe, "csv").text = str(classes.csv)
            elif cl == "Renter":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "user_id").text = classes.user_id
                if classes.reviewings:
                    review = ET.SubElement(pe, "reviewings")
                    for i in classes.reviewings:
                        ET.SubElement(review, "review").text = i
                if classes.curent_booking:
                    booking = ET.SubElement(pe, "curent_bookings")
                    for i in classes.curent_booking:
                        ET.SubElement(booking, "booking").text = i
                if classes.cards:
                    card = ET.SubElement(pe, "cards")
                    for i in classes.cards:
                        ET.SubElement(card, "card").text = i
            elif cl == "Booking":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "advertisement_id").text = classes.advertisement_id
                ET.SubElement(pe, "renter_id").text = classes.renter_id
                ET.SubElement(pe, "payment_id").text = classes.payment_id
                ET.SubElement(pe, "date_start").text = str(classes.date_start)
                ET.SubElement(pe, "date_end").text = str(classes.date_end)
                ET.SubElement(pe, "status").text = classes.status
            elif cl == "Payment":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "booking_id").text = classes.booking_id
                ET.SubElement(pe, "amount").text = str(classes.amount)
                ET.SubElement(pe, "status").text = classes.status
            elif cl == "Review_user":
                pe = ET.SubElement(root, cl, attrib={"id": classes.id})
                ET.SubElement(pe, "user_id_gave").text = classes.user_id_gave
                ET.SubElement(pe, "user_id_whom").text = classes.user_id_whom
                ET.SubElement(pe, "rating").text = str(classes.rating)
                ET.SubElement(pe, "comment").text = classes.comment

        rough_string = ET.tostring(root, "utf-8")
        reparsed = minidom.parseString(rough_string)
        root = reparsed.toprettyxml(indent="    ")
        with open(self.xml_path, "w", encoding="utf-8") as file:
            file.write(root)

    def load_json(self):
        result = []
        with open(self.json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        for item in data:
            if "Address" in item:
                tmp = {k: v for k, v in item["Address"].items() if k not in "id"}
                result.append(Address(**tmp))
            elif "Owner" in item:
                tmp = {k: v for k, v in item["Owner"].items() if k not in "id"}
                result.append(Owner(**tmp))
            elif "Advertisment" in item:
                tmp = {k: v for k, v in item["Advertisment"].items() if k not in "id"}
                tmp["end_date"] = datetime.strptime(tmp["end_date"], "%Y-%m-%d").date()
                tmp["start_date"] = datetime.strptime(
                    tmp["start_date"], "%Y-%m-%d"
                ).date()
                result.append(Advertisment(**tmp))
            elif "Booking" in item:
                tmp = {k: v for k, v in item["Booking"].items() if k not in "id"}
                tmp["date_start"] = datetime.strptime(
                    tmp["date_start"], "%Y-%m-%d"
                ).date()
                tmp["date_end"] = datetime.strptime(tmp["date_end"], "%Y-%m-%d").date()
                result.append(Booking(**tmp))
            elif "Cards" in item:
                tmp = {k: v for k, v in item["Cards"].items() if k not in "id"}
                result.append(Cards(**tmp))
            elif "Payment" in item:
                tmp = {k: v for k, v in item["Payment"].items() if k not in "id"}
                result.append(Payment(**tmp))
            elif "Property" in item:
                tmp = {k: v for k, v in item["Property"].items() if k not in "id"}
                result.append(Property(**tmp))
            elif "Renter" in item:
                tmp = {k: v for k, v in item["Renter"].items() if k not in "id"}
                result.append(Renter(**tmp))
            elif "Review_house" in item:
                tmp = {k: v for k, v in item["Review_house"].items() if k not in "id"}
                result.append(Review_house(**tmp))
            elif "Review_user" in item:
                tmp = {k: v for k, v in item["Review_user"].items() if k not in "id"}
                result.append(Review_user(**tmp))
            elif "User" in item:
                tmp = {k: v for k, v in item["User"].items() if k not in "id"}
                result.append(User(**tmp))
        return result

    def load_xml(self):
        result = []
        tree = ET.parse(self.xml_path)
        root = tree.getroot()
        class_map = {
            "Address": Address,
            "Payment": Payment,
            "Owner": Owner,
            "Advertisment": Advertisment,
            "Booking": Booking,
            "Cards": Cards,
            "Property": Property,
            "Renter": Renter,
            "Review_house": Review_house,
            "Review_user": Review_user,
            "User": User,
        }
        for obj in root:
            class_name = obj.tag
            if class_name in class_map:
                types = {
                    name: param.annotation
                    for name, param in inspect.signature(
                        class_map[class_name]().__init__
                    ).parameters.items()
                }
                data = {child.tag: child.text for child in obj}
                cls = class_map[class_name]
                for child in obj:
                    if types[child.tag] is type(int()):
                        data[child.tag] = int(data[child.tag])
                    elif types[child.tag] is type(float()):
                        data[child.tag] = float(data[child.tag])
                    if child.tag == "amenities" and obj.tag == "Property":
                        data[child.tag] = [i.text for i in child]
                    elif child.tag == "owns_flat_id" and obj.tag == "Owner":
                        data[child.tag] = [i.text for i in child]
                    elif child.tag == "reviews" and obj.tag == "Owner":
                        data[child.tag] = [i.text for i in child]
                    elif child.tag == "review_ids" and obj.tag == "Advertisment":
                        data[child.tag] = [i.text for i in child]
                    elif child.tag == "reviewings" and obj.tag == "Renter":
                        data[child.tag] = [i.text for i in child]
                    elif child.tag == "curent_bookings" and obj.tag == "Renter":
                        data[child.tag] = [i.text for i in child]
                    elif child.tag == "cards" and obj.tag == "Renter":
                        data[child.tag] = [i.text for i in child]
                    elif child.tag == "date_start" and obj.tag == "Booking":
                        data[child.tag] = datetime.strptime(
                            data[child.tag], "%Y-%m-%d"
                        ).date()
                    elif child.tag == "date_end" and obj.tag == "Booking":
                        data[child.tag] = datetime.strptime(
                            data[child.tag], "%Y-%m-%d"
                        ).date()
                    elif child.tag == "end_date" and obj.tag == "Advertisment":
                        data[child.tag] = datetime.strptime(
                            data[child.tag], "%Y-%m-%d"
                        ).date()
                    elif child.tag == "start_date" and obj.tag == "Advertisment":
                        data[child.tag] = datetime.strptime(
                            data[child.tag], "%Y-%m-%d"
                        ).date()
                obj = cls(**data)
                result.append(obj)

        return result
