from django.contrib.auth.models import User, Group
from TrackInControllerModel.models import user_profile
import logging
from rest_framework_jwt.settings import api_settings



class SigninController():

    def handle_login_request(self, request):
        logger = logging.getLogger(__name__)
        try:
            return_dict = {}
            user_name = request.data['username']
            pwd = request.data['password']
            usr_db = User.objects.filter(username__iexact=user_name).first()
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # upto return 64 line no
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(usr_db)
            print(payload)
            jwt_token = jwt_encode_handler(payload)
            return_dict['access_token'] = jwt_token
            return_dict['username'] = user_name
            return return_dict
        except Exception as e:
            logger.error("Exception occured while saving user data %s", e)
            raise