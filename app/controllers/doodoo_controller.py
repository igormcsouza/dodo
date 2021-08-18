from flask import Blueprint, jsonify, request, Response, abort
from flask.app import Flask
from flask_jwt import jwt_required, current_identity

from app.models.doodoo import DooDoo


doodoo_controller = Blueprint('doodoo', __name__, url_prefix="/doodoo")


@doodoo_controller.route('/fetch', methods=["GET"])
@jwt_required()
def get_all_doodoos():

    doodoos = DooDoo.query.filter_by(user_id=current_identity.id).all()  # type: ignore # noqa

    return jsonify({
        "doodoos": [doodoo.to_dict() for doodoo in doodoos]
    })


@doodoo_controller.route('/add', methods=["POST"])
@jwt_required()
def add_new_doodoos():
    doodoo = request.form["doodoo"]
    DooDoo(doodoo, current_identity.id).save()  # type: ignore

    response = Response()
    response.status_code = 201
    return response


@doodoo_controller.route('/delete/<int:id>', methods=["DELETE"])
@jwt_required()
def delete_doodoo(id: int):
    doodoo = DooDoo.query.get(id)

    if doodoo.user_id == current_identity.id:  # type: ignore
        doodoo.delete()

        response = Response()
        response.status_code = 204
        return response

    else:
        return abort(400)


def init_app(app: Flask):
    app.register_blueprint(doodoo_controller)
