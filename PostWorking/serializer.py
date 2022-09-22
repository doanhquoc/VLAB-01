from rest_framework import serializers
from .models import WorkInfor

class WorkInforSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkInfor
        fields = ['id','WorkName_text', 'Company_text', 'level', 'Description_text', 'LongTime', 'phone_number', 'photo',
                  'money']
