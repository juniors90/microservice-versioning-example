from application import ma
from application.core.database import db
from application.models.note import Note


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True


NOTE_SCHEMA = NoteSchema()
NOTES_SCHEMA = NoteSchema(many=True)
