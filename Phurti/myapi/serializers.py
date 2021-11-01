from rest_framework import serializers
from .models import categories

class categoriesSerializer(serializers.HyperlinkedModelSerializer):
    # prod = serializers.SerializerMethodField()

    class Meta:
        model = categories
        fields = '__all__'

    # def get_prod(self, obj):
    #     return obj.prod.title