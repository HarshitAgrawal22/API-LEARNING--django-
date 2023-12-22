#create serializers
from rest_framework import serializers
from apis.models import company, employee
class company_serializers(serializers.HyperlinkedModelSerializer):
    # TODO model serializers give us the advantage to create the meta class 
    id=serializers.ReadOnlyField()
    class Meta:
        model=company# defining the model for which we have created the api
        fields="__all__" # the fields we are going to use in it
        
class employee_serializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=employee
        fields="__all__"