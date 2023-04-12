from rest_framework import serializers
from user.models import UserModel


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
