from rest_framework import serializers
from user.models import User, UserApply

class userApplySerializer():

    class Meta:
        model = UserApply
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    userapply = userApplySerializer()

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ["user_type",  "username", "password", "email", "fullname", "join_date", "userapply"]