from api import db
from api.models import User, CommunityEvent, AssistanceRequest
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


def resolve_signup(_, info, username, password):
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def resolve_login(_, info, username, password):
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token, "user": user}

    return None


@jwt_required()
def resolve_create_event(_, info, input):
    current_user_id = get_jwt_identity()

    user = User.query.get(current_user_id)

    if user:
        new_event = CommunityEvent(
            title=input["title"],
            description=input.get("description"),
            location=input.get("location"),
            date=input.get("date"),
            time=input.get("time"),
            organizer_id=user.id,
        )

        db.session.add(new_event)
        db.session.commit()
        return new_event

    return None


def resolve_create_assistance_request(_, info, input):
    new_request = AssistanceRequest(
        description=input["description"],
        assistance_type=input["assistance_type"],
        user_id=1,  # Replace with the actual user ID
    )

    db.session.add(new_request)
    db.session.commit()
    return new_request


def resolve_update_assistance_request(_, info, id, input):
    request = AssistanceRequest.query.get(id)

    if request:
        request.description = input["description"]
        request.assistance_type = input["assistance_type"]
        db.session.commit()
        return request

    return None
