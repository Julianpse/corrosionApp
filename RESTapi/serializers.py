from rest_framework import serializers
from .models import Companies


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('company_name', 'street_address', 'city', 'state', 'zip_code', 'tel_num','logo_location','primary_color','secondary_color')

