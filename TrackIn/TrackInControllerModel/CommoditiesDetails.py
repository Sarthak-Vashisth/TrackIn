from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User, Group
from TrackInControllerModel.models import user_profile, commodities_buy_sell_main, commodity_main
import logging

class CommoditiesDetailsController():

    def handle_commodities_details_req(self, request):
        logger = logging.getLogger(__name__)
        try:
            print(request.data)
            logger.info(" In handle_commodities_details_req method ")
            usr_name = request.userinfo['username']
            user_obj = User.objects.get(username=usr_name)
            print(" user_obj ",user_obj.id)
            result = list(commodities_buy_sell_main.objects.filter(user_id = user_obj.id).values())
            print(" result ::: ",result)
            return result
        except Exception as e:
            raise

    def handle_commodities_list_req(self, request):
        logger = logging.getLogger(__name__)
        try:
            print(request.data)
            logger.info(" In handle_commodities_details_req method ")
            usr_name = request.userinfo['username']
            user_obj = User.objects.get(username=usr_name)
            print(" user_obj ",user_obj.id)
            result = list(commodity_main.objects.all().values())
            print(" result ::: ",result)
            return result
        except Exception as e:
            raise