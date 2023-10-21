from api import db
from api.models import CommunityEvent, AssistanceRequest
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def resolve_events(_, info):
    return CommunityEvent.query.all()


@jwt_required()
def resolve_event(_, info, id):
    return CommunityEvent.query.get(id)


@jwt_required()
def resolve_assistance_requests(_, info):
    return AssistanceRequest.query.all()


@jwt_required()
def resolve_assistance_request(_, info, id):
    return AssistanceRequest.query.get(id)
