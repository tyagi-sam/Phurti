from rest_framework import serializers
from .models import categories, product


class categoriesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = categories
        fields = '__all__'


class productSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = product
        fields = '__all__'

    def get_category(self, obj):
        return obj.category.title

