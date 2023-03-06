from flask import abort, make_response

from application.api.v2.schemas.note import NOTE_SCHEMA
from application.core.database import db
from application.models.note import Note
from application.models.person import Person


def create(note):
    person_id = note.get("person_id")
    person = Person.query.filter(Person.id == person_id).one_or_none()

    if person:
        new_note = NOTE_SCHEMA.load(note, session=db.session)
        person.notes.append(new_note)
        db.session.commit()
        return NOTE_SCHEMA.dump(new_note), 201
    else:
        abort(404, f"Person not found for ID: {person_id}")


def delete(note_id):
    existing_note = Note.query.filter(Note.id == note_id).one_or_none()

    if existing_note:
        db.session.delete(existing_note)
        db.session.commit()
        return make_response(f"{note_id} successfully deleted", 204)
    else:
        abort(404, f"Note with ID {note_id} not found")


def read_one(note_id):
    note = Note.query.filter(Note.id == note_id).one_or_none()

    if note is not None:
        return NOTE_SCHEMA.dump(note)
    else:
        abort(404, f"Note with ID {note_id} not found")


def update(note_id, note):
    existing_note = Note.query.filter(Note.id == note_id).one_or_none()

    if existing_note:
        update_note = NOTE_SCHEMA.load(note, session=db.session)
        existing_note.content = update_note.content
        db.session.merge(existing_note)
        db.session.commit()
        return NOTE_SCHEMA.dump(existing_note), 201
    else:
        abort(404, f"Note with ID {note_id} not found")
