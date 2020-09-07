from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User, Group
from TrackInControllerModel.Common import masterconf
from TrackInControllerModel.SigninController import SigninController
import logging
from django.contrib.auth.hashers import check_password


class LoginUser(APIView):
    authentication_classes = ()
    # # parser_class = (MultiPartParser, FormParser,)
    # # renderer_classes = (JSONRenderer,)
    permission_classes = ()

    def validate_login_request(self, request_data):

        logger = logging.getLogger(__name__)
        params = masterconf.login
        logger.info("Input params receiving for Login: %s", request_data)
        logger.info("params from validate_login_request: %s", params)
        status_flag = False
        for param in params:
            if param not in request_data.keys():
                status_flag = False
                break
            else:
                status_flag = True
        logger.info("Returned status flag from validate_login_request: %s", status_flag)
        return status_flag

    def post(self, request, format=None):
        print(request.data)
        logger = logging.getLogger(__name__)
        try:
            check_if_valid = self.validate_login_request(request.data)
            if check_if_valid:
                print(request.data)
                check_if_exists = User.objects.filter(username=request.data['username'])
                if check_if_exists:
                    user_db_pwd = User.objects.get(username=request.data['username'])
                    check_pwd = check_password(request.data['password'], user_db_pwd.password)
                    #check_credentials = User.objects.filter(username=request.data['username'], password=request.data['password'])
                    if check_pwd:
                        login_cntrl_obj = SigninController()
                        return_dict = login_cntrl_obj.handle_login_request(request)
                        return Response(status=status.HTTP_200_OK, data=return_dict)
                    else:
                        wrong_credentials = {
                            "status_code": 'E102',
                            "status_description": masterconf.error_codes['E102']
                        }
                        return Response(status=status.HTTP_400_BAD_REQUEST, data=wrong_credentials)
                else:
                    user_exists = {
                        "status_code": 'E100',
                        "status_description": masterconf.error_codes['E100']
                    }
                    return Response(status=status.HTTP_400_BAD_REQUEST, data=user_exists)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error("Exception occured while signup %s", e)
            exception_msg_bundle = {
                "status_code": "X100",
                "status_description": masterconf.error_codes['X100']
            }
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=exception_msg_bundle)