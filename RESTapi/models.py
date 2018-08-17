# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Basin(models.Model):
    basin_name = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey('Companies', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basin'


class Companies(models.Model):
    company_name = models.CharField(max_length=50, blank=True, null=True)
    street_address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    tel_num = models.CharField(max_length=12, blank=True, null=True)
    logo_location = models.CharField(max_length=100, blank=True, null=True)
    primary_color = models.CharField(max_length=15, blank=True, null=True)
    secondary_color = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Facility(models.Model):
    facility_name = models.CharField(max_length=100, blank=True, null=True)
    basin = models.ForeignKey(Basin, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility'


class FixedEquipment(models.Model):
    equipment_name = models.CharField(max_length=100, blank=True, null=True)
    facility = models.ForeignKey(Facility, models.DO_NOTHING, blank=True, null=True)
    equipment_type = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    commision_date = models.DateField(blank=True, null=True)
    initial_thickness = models.FloatField(blank=True, null=True)
    min_req_thickness = models.FloatField(blank=True, null=True)
    documents_loc = models.CharField(max_length=100, blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    pressure = models.FloatField(blank=True, null=True)
    outside_diameter = models.FloatField(blank=True, null=True)
    nom_wall_thickness = models.FloatField(blank=True, null=True)
    corrosion_allowance = models.FloatField(blank=True, null=True)
    stress_at_temp = models.FloatField(blank=True, null=True)
    long_efficiency = models.FloatField(blank=True, null=True)
    undertolerance_allowance = models.FloatField(blank=True, null=True)
    weld_joint_red_factor = models.FloatField(blank=True, null=True)
    y_coefficient = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fixed_equipment'


class Measurements(models.Model):
    tml = models.ForeignKey('TmlInfo', models.DO_NOTHING, blank=True, null=True)
    measurement = models.FloatField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    insert_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'measurements'


class TmlInfo(models.Model):
    tml_name = models.CharField(max_length=100, blank=True, null=True)
    fixed_eqp = models.ForeignKey(FixedEquipment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tml_info'


class Users(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True)
    basin = models.ForeignKey(Basin, models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
