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
import datetime, time

class CreateCommoditiesController():

    def handle_create_commodities_req(self, request):
        logger = logging.getLogger(__name__)
        try:
            request_data = request.data
            db_list = []
            print(" request_data ::::",request_data)
            logger.info(" In handle_create_commodities_req method ")
            created_by = request.userinfo['username'].username
            created_on = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            created_reference_id = request.userinfo['reference_id']
            user_obj = User.objects.get(username=created_by)
            user_id = user_obj.id
            # commodity_queryset = commodity_main.objects.filter(commodity_name=request_data['commodity_name'], record_status='Active').values()
            # print("commodity_id ::: ",list(commodity_queryset)[0]['commodity_id'])
            for record in request_data:
                record['user_id'] = user_id
                record['created_by'] = created_by
                record['created_on'] = created_on
                record['created_reference_id'] = created_reference_id
                record['record_status'] = 'Active'
                db_list.append(record)
            # commodity_id = record['commodity_id']
            # buy_sell_date = record['buy_sell_date']
            # commodity_name = record['commodity_name']
            # buy_or_sell = record['buy_or_sell']
            # price = record['price']
            # result = commodities_buy_sell_main(user_id=user_id, commodity_id=commodity_id, commodity_name=commodity_name, buy_or_sell=buy_or_sell, price=price, buy_sell_date=buy_sell_date, created_by=created_by, created_on=created_on, created_reference_id=created_reference_id)
            # result.save()
            commodities_buy_sell_main.objects.bulk_create([commodities_buy_sell_main(**rec) for rec in db_list])
        except Exception as e:
            raise