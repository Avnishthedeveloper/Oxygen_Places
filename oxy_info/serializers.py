from rest_framework import serializers
from oxy_info.models import Place

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = ['id','Address','BusinessName','Person','Contact', 'VerifiedStatus', 'TimeStamp']