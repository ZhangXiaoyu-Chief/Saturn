from rest_framework import serializers
from books.models import Publisher, Author


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=60)
    state_province = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=50)
    website = serializers.URLField()

    def create(self, validated_data):
        return Publisher.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.city = validated_data.get("city", instance.city)
        instance.state_province = validated_data.get("state_province", instance.state_province)
        instance.country = validated_data.get("country", instance.country)
        instance.website = validated_data.get("website", instance.website)
        instance.save()

        return instance


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=40)
    email = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.save()

        return instance
