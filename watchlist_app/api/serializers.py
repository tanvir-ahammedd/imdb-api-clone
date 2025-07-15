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
    
    def create(self, validate_data):
        return Movie.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.description = validate_data.get('description', instance.description)
        instance.active = validate_data.get('active', instance.active)
        instance.save()
        return instance
        
