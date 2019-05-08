import django_filters
from custom_auth.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'email': ['exact'],
            'date_of_birth': ['exact', 'year__gt', 'year__lt'],
        }
