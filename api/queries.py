from api import db
from api.models import CommunityEvent
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def resolve_events(_, info):
    return CommunityEvent.query.all()


@jwt_required()
def resolve_event(_, info, id):
    return CommunityEvent.query.filter_by(id=id).first()
