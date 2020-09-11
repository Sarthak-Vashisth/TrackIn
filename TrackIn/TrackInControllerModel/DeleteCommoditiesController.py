from django.contrib.auth.models import User, Group
from TrackInControllerModel.models import commodities_buy_sell_main
import logging
from django.contrib.auth.hashers import make_password
import datetime, time


class DeleteCommoditiesController():

    def handle_delete_commodities_request(self, request):
        permission_list = list()
        logger = logging.getLogger(__name__)
        try:
            print(request.data)
            logger.info(" In handle_delete_commodities_request method ")
            payload_request = request.data
            usr_name = request.userinfo['username']
            user_obj = User.objects.get(username=usr_name)
            deleted_by = request.userinfo['username'].username
            deleted_on = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            deleted_reference_id = request.userinfo['reference_id']
            for payload in payload_request:
                serial_id = payload['serial_id']
                commodity_entry = commodities_buy_sell_main.objects.get(serial_id=serial_id, user_id=user_obj.id)
                commodity_entry.record_status = 'Deleted'
                commodity_entry.deleted_by = deleted_by
                commodity_entry.deleted_on = deleted_on
                commodity_entry.deleted_reference_id = deleted_reference_id
                commodity_entry.save()
        except Exception as e:
            print(e)
            logger.error("Exception occured while deleting commodities data %s",e)
            raise
