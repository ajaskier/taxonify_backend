from flask import current_app as app, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from aquascope.webserver.data_access.conversions import group_id_to_container_name
import aquascope.webserver.data_access.storage.blob as blob
from aquascope.webserver.schema.sas import SasSchema
from aquascope.webserver.schema.custom_schema import FormattedValidationError


class Sas(Resource):
    @jwt_required
    def get(self):
        schema = SasSchema()
        try:
            args = schema.load(request.args)
        except FormattedValidationError as e:
            return e.formatted_messages, 400

        group_id = args['destination']
        container_name = group_id_to_container_name(group_id)
        storage_client = app.config['storage_client']
        sas_token = blob.generate_container_download_sas(storage_client, container_name)
        return dict(token=sas_token)
