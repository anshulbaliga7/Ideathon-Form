# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

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


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

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


class PortalMemberfive(models.Model):
    membernamefive = models.CharField(max_length=200, blank=True, null=True)
    memberfivecontactno = models.AutoField(primary_key=True)
    memberfiveemail = models.CharField(max_length=200, blank=True, null=True)
    memberfivedob = models.CharField(max_length=10)
    memberfivegender = models.CharField(max_length=200)
    memberfivedepartment = models.CharField(max_length=200, blank=True, null=True)
    memberfiverole = models.CharField(max_length=200, blank=True, null=True)
    memberfivecompetency = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_memberfive'


class PortalMemberfour(models.Model):
    membernamefour = models.CharField(max_length=200, blank=True, null=True)
    memberfourcontactno = models.AutoField(primary_key=True)
    memberfouremail = models.CharField(max_length=200, blank=True, null=True)
    memberfourdob = models.CharField(max_length=10)
    memberfourgender = models.CharField(max_length=200)
    memberfourdepartment = models.CharField(max_length=200, blank=True, null=True)
    memberfourrole = models.CharField(max_length=200, blank=True, null=True)
    memberfourcompetency = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_memberfour'


class PortalMemberone(models.Model):
    membernameone = models.CharField(max_length=200, blank=True, null=True)
    memberonecontactno = models.AutoField(primary_key=True)
    memberoneemail = models.CharField(max_length=200, blank=True, null=True)
    memberonedob = models.CharField(max_length=10)
    memberonegender = models.CharField(max_length=200)
    memberonedepartment = models.CharField(max_length=200, blank=True, null=True)
    memberonerole = models.CharField(max_length=200, blank=True, null=True)
    memberonecompetency = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_memberone'


class PortalMembersix(models.Model):
    membernamesix = models.CharField(max_length=200, blank=True, null=True)
    membersixcontactno = models.AutoField(primary_key=True)
    membersixemail = models.CharField(max_length=200, blank=True, null=True)
    membersixdob = models.CharField(max_length=10)
    membersixgender = models.CharField(max_length=200)
    membersixdepartment = models.CharField(max_length=200, blank=True, null=True)
    membersixrole = models.CharField(max_length=200, blank=True, null=True)
    membersixcompetency = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_membersix'


class PortalMemberthree(models.Model):
    membernamethree = models.CharField(max_length=200, blank=True, null=True)
    memberthreecontactno = models.AutoField(primary_key=True)
    memberthreeemail = models.CharField(max_length=200, blank=True, null=True)
    memberthreedob = models.CharField(max_length=10)
    memberthreegender = models.CharField(max_length=200)
    memberthreedepartment = models.CharField(max_length=200, blank=True, null=True)
    memberthreerole = models.CharField(max_length=200, blank=True, null=True)
    memberthreecompetency = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_memberthree'


class PortalMembertwo(models.Model):
    membernametwo = models.CharField(max_length=200, blank=True, null=True)
    membertwocontactno = models.AutoField(primary_key=True)
    membertwoemail = models.CharField(max_length=200, blank=True, null=True)
    membertwodob = models.CharField(max_length=10)
    membertwogender = models.CharField(max_length=200)
    membertwodepartment = models.CharField(max_length=200, blank=True, null=True)
    membertworole = models.CharField(max_length=200, blank=True, null=True)
    membertwocompetency = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_membertwo'


class PortalPersonalinfo(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    contactno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    dob = models.CharField(max_length=8)
    gender = models.CharField(max_length=200)
    department = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_personalinfo'


class PortalProject(models.Model):
    nameproj = models.CharField(max_length=2000, blank=True, null=True)
    painpoint = models.TextField(blank=True, null=True)
    solution = models.TextField(blank=True, null=True)
    innovation = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    customer = models.TextField(blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    businessmodel = models.TextField(blank=True, null=True)
    nameprojag = models.CharField(max_length=2000, blank=True, null=True)
    spec = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_project'


class PortalTeamdetails(models.Model):
    teamname = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_teamdetails'
