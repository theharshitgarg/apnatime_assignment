from rest_framework import serializers

from custom_auth.models import User
# class Meta:
#         model = UploadedDoc
#         fields = ("id", "uploaded_on", "storage_path", "status")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "first_name", "last_name", "date_of_birth",
            "preferred_language"
        ]
