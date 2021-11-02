from rest_framework import serializers
from .models import categories, product


class categoriesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = categories
        fields = '__all__'


class productSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = product
        fields = '__all__'
