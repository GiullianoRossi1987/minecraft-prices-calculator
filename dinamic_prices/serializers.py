from rest_framework import serializers
from .models import Sell

#class SellSerializer(serializers.Serializer):
#	"""
#	Serializes the data using the Rest API framework
#	"""
#	cd = models.IntegerField(primary_key=True)
#	item = models.TextField()
#	qtd = models.IntegerField()
#	value = models.DecimalField(max_digits=10, decimal_places=2)
#	datetime_sell = models.DateTimeField(auto_now_add=True, blank=True)
#
#	def create(self, validated_data):
#		"""
#		Create and return a new Sell log with the validated data
#		"""
#		return Sell.objects.create(**validated_data)

class SellSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Sell
		fields = ['cd', 'item', 'qtd', 'value', 'datetime_sell']



	
