from rest_framework import serializers
from watchlist.models import Movie, Review, StreamPlatform, WatchList


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ("watchlist",)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"
        # depth = 1


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="movie-details"
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    len_names = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ["id", "name", "description"]
        # exclude = ["active"]

    def get_len_names(self, instance):
        return len(instance.name)

    def validate(self, instance):
        if instance["name"] == instance["description"]:
            raise serializers.ValidationError(
                "Title and description should be different!"
            )
        else:
            return instance

    def validate_name(self, instance):
        if len(instance) < 2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return instance


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance

#     def validate(self, instance):
#         if instance["name"] == instance["description"]:
#             raise serializers.ValidationError(
#                 "Title and description should be different!"
#             )
#         else:
#             return instance

#     # def validate_name(self, instance):
#     #     if len(instance) < 2:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     else:
#     #         return instance
