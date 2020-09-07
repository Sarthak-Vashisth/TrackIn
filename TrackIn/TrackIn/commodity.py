from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User, Group
from TrackInControllerModel.Common import masterconf
from TrackInControllerModel.CommoditiesDetails import CommoditiesDetailsController
import logging

class GetCommoditiesList(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    # # parser_class = (MultiPartParser, FormParser,)
    # # renderer_classes = (JSONRenderer,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format = None):
        logger = logging.getLogger(__name__)
        try:
            get_commodities_obj = CommoditiesDetailsController()
            return_obj = get_commodities_obj.handle_commodities_list_req(request)
            return Response(status=status.HTTP_200_OK, data=return_obj)
        except Exception as e:
            logger.error("Exception occured while signup %s", e)
            exception_msg_bundle = {
                "status_code": "X100",
                "status_description": masterconf.error_codes['X100']
            }
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=exception_msg_bundle)

class GetCommoditiesDetails(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    # # parser_class = (MultiPartParser, FormParser,)
    # # renderer_classes = (JSONRenderer,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format = None):
        logger = logging.getLogger(__name__)
        try:
            get_commodities_obj = CommoditiesDetailsController()
            return_obj = get_commodities_obj.handle_commodities_details_req(request)
            return Response(status=status.HTTP_200_OK, data=return_obj)
        except Exception as e:
            logger.error("Exception occured while signup %s", e)
            exception_msg_bundle = {
                "status_code": "X100",
                "status_description": masterconf.error_codes['X100']
            }
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=exception_msg_bundle)
