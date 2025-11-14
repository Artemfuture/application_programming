from uuid import uuid1


class Cards:
    def __init__(
        self,
        user_id: str = None,
        number: int = None,
        date: str = None, 
        csv: int = None
    ):

        self.id = str(uuid1())
        self.user_id = user_id
        self.number = number
        self.date = date
        self.csv = csv

    def update(self,number: int = None,
        date: str = None, 
        csv: int = None) -> bool:
        result = True
        try:
            if number:
                self.number = number
            elif date:
                self.date = date
            elif csv:
                self.csv = csv
            else:
                result = False
        except:
            result = False
        return result

    def delete(self): 
        result = True
        return result
