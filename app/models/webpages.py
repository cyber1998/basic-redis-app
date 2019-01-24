from sqlalchemy.exc import ProgrammingError

from app.models import db, BaseModel


# Inheriting the BaseModel
class Webpage(BaseModel):
    __tablename__ = 'webpages'  # Setting a custom table name

    url = db.Column(db.String(), nullable=False)
    words = db.Column(db.Integer)
    title = db.Column(db.String(150))

    def __init__(self, payload):

        try:
            for key, value in payload.items():
                setattr(self, key, value)
        except ProgrammingError as e:
            db.rollback()
            raise ProgrammingError

    def get_details(self):
        data = {
            'id': self.id_,
            'url': self.url,
            'words': self.words,
            'title': self.title
        }
        return data

    @staticmethod
    def get_all_details():

        # Result set to store all results
        result_set = []

        # Iterating through all available web pages stored in the db
        # and appending the result of the get_details function of each
        # individual object and storing it into the result set

        webpages = Webpage.query.all()
        for webpage in webpages:
            result_set.append(webpage.get_details())

        return result_set
