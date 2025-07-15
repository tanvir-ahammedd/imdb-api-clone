from rest_framework import serializers
from watchlist_app.models import Movie

# without Modelserializer
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#custom validator
def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short")
    return value
    

# with Modelserializer -> serializer
class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = "__all__"
        
    def get_len_name(self, object):
        return len(object.name)
    
    def create(self, validate_data):
        return Movie.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.description = validate_data.get('description', instance.description)
        instance.active = validate_data.get('active', instance.active)
        instance.save()
        return instance
    
    #object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should not be same")
        return data
    
    #field level validation
    #format: validate_(name of that field)
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value
