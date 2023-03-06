from marshmallow_sqlalchemy import fields

from application import ma
from application.api.v1.schemas.note import NoteSchema
from application.core.database import db
from application.models.person import Person


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    notes = fields.Nested(NoteSchema, many=True)


PERSON_SCHEMA = PersonSchema()
PEOPLE_SCHEMA = PersonSchema(many=True)
