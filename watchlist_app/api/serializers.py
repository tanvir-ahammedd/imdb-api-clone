from rest_framework import serializers
from watchlist_app.models import Movie

# with Modelserializer
# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = "__all__"

# without Modelserializer -> serializer
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    active = serializers.BooleanField()
