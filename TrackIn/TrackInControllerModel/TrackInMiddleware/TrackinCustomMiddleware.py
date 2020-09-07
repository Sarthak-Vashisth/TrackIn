from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User, Group, Permission
import json
import datetime, time
import logging
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.db import connection

class TrackinMiddleware(MiddlewareMixin):

    def generate_ref_id(self,):
        try:
            sql_str = "select generate_ref_id()"
            # print("sql_str from generate_ref_id : {}".format(sql_str))
            cur = connection.cursor()
            cur.execute(sql_str)
            ref_id = cur.fetchone()
            # print("Generated Ref Id ::: ", ref_id)
            cur.close()
            return ref_id[0]
        except Exception as e:
            raise e

    def process_request(self, request):
        logger = logging.getLogger(__name__)
        logger.info("INSIDE process_request METHOD OF TrackinMiddleware.")
        # print("In middleware")
        # print(dir(request))
        # print(request.META.get('HTTP_AUTHORIZATION'))
        if '/signup/' in request.path or '/login/' in request.path:  # request.path.startswith('/login/'):
            return None
        elif 'HTTP_AUTHORIZATION' in request.META and request.META['HTTP_AUTHORIZATION'] != '' and request.META[
            'HTTP_AUTHORIZATION'] != None:
            userinfodict = {}
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            print(" token :LLL ",token)
            data = {'token': token}
            try:
                logger.info('Request Path: %s', request.get_full_path)
                valid_data = VerifyJSONWebTokenSerializer().validate(data)
                # print(valid_data)
                user = valid_data['user']
                user_id = User.objects.filter(username=user).values('id')[0]['id']
                all_groups = Group.objects.filter(user=user)
                reference_id = self.generate_ref_id()
                print("reference_id ::: ",reference_id)
                request.userinfo = userinfodict
                request.userinfo['username'] = user
                request.userinfo['group'] = all_groups
                request.userinfo['reference_id'] = reference_id
                get_data = dict(request.GET)
                post_data = dict(request.POST)

                # insert_req = {
                #     "request_api_url": request.path,
                #     "request_method": request.method,
                #     "request_user_info": user,
                #     "request_get_info": get_data,
                #     "request_post_info": post_data,
                #     "reference_id": reference_id,
                #     "request_date": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                # }
                # insert_api_obj = api_call_log(**insert_req)
                # insert_api_obj.save()
            except ValidationError as e:
                status_dict = {}
                status_dict["level"] = "Token Validation"
                status_dict["status_text"] = "Token Validation Failed.Invalid Token."
                response = Response(status=status.HTTP_401_UNAUTHORIZED, data=status_dict)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Headers"] = "*"
                response.renderer_context = {}
                return response
            except Exception as e:
                raise e
