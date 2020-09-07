from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User, Group
from TrackInControllerModel.Common import masterconf
from TrackInControllerModel.CreateCommodities import CreateCommoditiesController
import logging


class CreateCommodities(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    # # parser_class = (MultiPartParser, FormParser,)
    # # renderer_classes = (JSONRenderer,)
    permission_classes = (IsAuthenticated,)

    def validate_create_commodity_request(self, request_data):

        logger = logging.getLogger(__name__)
        params = masterconf.create_commodity
        logger.info("Input params receiving for create commodity API: %s", request_data)
        logger.info("params from validate_create_commodity_request: %s", params)
        status_flag = False
        for param in params:
            if param not in request_data[0].keys():
                status_flag = False
                break
            else:
                status_flag = True
        logger.info("Returned status flag from validate_create_commodity_request: %s", status_flag)
        return status_flag

    def post(self, request, format = None):
        logger = logging.getLogger(__name__)
        try:
            check_if_valid = self.validate_create_commodity_request(request.data)
            if check_if_valid:
                get_commodities_obj = CreateCommoditiesController()
                get_commodities_obj.handle_create_commodities_req(request)
                success_status = {
                    "status_code" : "S102",
                    "status_desc" : masterconf.success_codes['S102']
                }
                return Response(status=status.HTTP_200_OK, data=success_status)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("Exception occured while creating commodity entries %s", e)
            exception_msg_bundle = {
                "status_code": "X101",
                "status_description": masterconf.error_codes['X101']
            }
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=exception_msg_bundle)
