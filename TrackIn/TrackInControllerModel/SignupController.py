from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User, Group
from TrackInControllerModel.models import user_profile
import logging
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.hashers import make_password
import datetime, time


class SignupUserController(APIView):

    def handle_signup_request(self, request):
        permission_list = list()
        logger = logging.getLogger(__name__)
        try:
            request_data = request.data
            user_name = request_data['username']
            pwd = make_password(request_data['password'])
            email = request_data['email']
            phone_no = request_data['phone_no']
            first_name = request_data['first_name']
            last_name = request_data['last_name']
            created_by = request_data['username']
            created_on = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            user_details = User(username=user_name, password=pwd, email=email, first_name=first_name, last_name=last_name)
            user_details.save()
            phone = user_profile(user_id = user_details.id, phone_no = phone_no, created_by=created_by,created_on=created_on)
            phone.save()
            logger.info("User Data Saved Successfully")
        except Exception as e:
            print(e)
            logger.error("Exception occured while saving user data %s",e)
            raise
