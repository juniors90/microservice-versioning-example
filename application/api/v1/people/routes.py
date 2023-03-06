from typing import Dict, List, Tuple

from flask import abort, make_response

from application.api.v1.schemas.people import PEOPLE_SCHEMA, PERSON_SCHEMA
from application.core.database import db
from application.models.person import Person


def create(person: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_person = PERSON_SCHEMA.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return PERSON_SCHEMA.dump(new_person), 201
    else:
        abort(
            406,
            f"Person with last name {lname} already exists",
        )


def delete(lname: str) -> str:
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {lname} not found")


def read_all() -> List[Dict[str, str]]:
    people = Person.query.all()
    return PEOPLE_SCHEMA.dump(people)


def read_one(lname: str) -> Dict[str, str]:
    person = Person.query.filter(Person.lname == lname).one_or_none()
    if person is not None:
        return PERSON_SCHEMA.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")


def update(lname: str, person: Dict[str, str]) -> Dict[str, str]:
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        update_person = PERSON_SCHEMA.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return PERSON_SCHEMA.dump(existing_person), 201
    else:
        abort(404, f"Person with last name {lname} not found")
