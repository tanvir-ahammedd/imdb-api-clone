from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class WatchlistSerializer(serializers.ModelSerializer): 
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchlistSerializer(many=True, read_only=True)
    # this will show now what i have defined in __str__ field
    # as i am returning the name, it will show the name
    # watchlist = serializers.StringRelatedField(many=True) 
    # this is for showing primary key
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # this is for hyperlink
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-details'
    )
    class Meta:
        model = StreamPlatform
        fields = "__all__"
    