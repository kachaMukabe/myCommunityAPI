from api import app, db
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    graphql_sync,
    snake_case_fallback_resolvers,
    ObjectType,
)
from ariadne.explorer import ExplorerGraphiQL
from flask import request, jsonify
from api.mutations import resolve_create_event, resolve_login, resolve_signup

query = ObjectType("Query")

mutation = ObjectType("Mutation")
mutation.set_field("signup", resolve_signup)
mutation.set_field("login", resolve_login)
mutation.set_field("create_event", resolve_create_event)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

explorer_html = ExplorerGraphiQL().html(None)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)
    status_code = 200 if success else 400
    return jsonify(result), status_code
