from rest_framework import serializers
import django_filters
from .models import Companies
from .models import Basin
from .models import Facility
from .models import FixedEquipment
from .models import TmlInfo
from .models import Measurements
from .models import Users


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('company_name', 'street_address', 'city', 'state', 'zip_code', 'tel_num','logo_location','primary_color','secondary_color')

class BasinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basin
        fields = ('basin_name','company')

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('facility_name','basin')

class FixedEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedEquipment
        fields = ('equipment_name','facility', 'equipment_type',\
        'material', 'commision_date', 'initial_thickness',\
        'min_req_thickness', 'documents_loc', 'temperature',\
        'pressure', 'outside_diameter', 'nom_wall_thickness',\
        'corrosion_allowance','stress_at_temp','long_efficiency',\
        'undertolerance_allowance','weld_joint_red_factor','y_coefficient')

class TMLinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TmlInfo
        fields = ('tml_name','fixed_eqp')

class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ('tml','measurement', 'user', 'insert_timestamp')

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name','last_name', 'user_type', 'company',\
        'basin', 'email','phone')
