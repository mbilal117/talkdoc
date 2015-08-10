from django.db import models
from django.contrib.auth.models import User

from base.models import TimeStampAwareModel

# User Type
class UserType(TimeStampAwareModel):
    user_type = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user_type

#Speciality
class Speciality(models.Model):
    speciality_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.speciality_name

#Service Offered
class ServiceOffered(models.Model):
    service_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    speciality = models.ForeignKey(Speciality)

    def __unicode__(self):
        return self.service_name

#City
class City(models.Model):
    city_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.city_name

#Hospital
class Hospital(TimeStampAwareModel):
    hospital_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.hospital_name

#User Profile
class UserProfile(TimeStampAwareModel):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )

    MARITAL_STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
    )

    PROFILE_STEP = (
        ('1', 'step1'),
        ('2', 'step2'),
        ('3', 'step3'),
        ('4', 'step4'),
        ('5', 'complete'),
    )

    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    cell_phone = models.CharField(max_length=13, default='')
    user = models.ForeignKey(User, null=True, blank=True)
    dob = models.DateTimeField(null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SEX)
    medical_condition = models.CharField(max_length=100, null=True, blank=True)
    alergy = models.CharField(max_length=50, null=True, blank=True)
    picture = models.FileField(max_length=200, upload_to="TalkDoc/Files", null=True, blank=True, default="")
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP, null=True, blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS, null=True, blank=True)
    city = models.ForeignKey(City)
    address = models.CharField(max_length=100, null=True, blank=True)
    speciality = models.ForeignKey(Speciality, null=True, blank=True)
    services_offerd = models.ManyToManyField(ServiceOffered, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    profile_step = models.CharField(max_length=2, choices=PROFILE_STEP, default='1', null=True, blank=True)

    def __unicode__(self):
        return "%s-%s" % (self.first_name, self.last_name)

#Availability
class Availability(TimeStampAwareModel):
    # WEEK_DAYS = (
    #     ('1', 'Sunday'),
    #     ('2', 'Monday'),
    #     ('3', 'Tuesday'),
    #     ('4', 'Wednesday'),
    #     ('5', 'Thursday'),
    #     ('6', 'Friday'),
    #     ('7', 'Saturday'),
    # )

    DURATION = (
        ('1', '15'),
        ('2', '30'),
        ('3', '45'),
        ('4', '60'),
    )

    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    # service = models.ForeignKey(ServiceOffered)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # day = models.CharField(max_length=10, choices=WEEK_DAYS)
    # duration = models.CharField(max_length=10, choices=DURATION)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    is_saturday_off = models.BooleanField(default=False)
    is_sunday_off = models.BooleanField(default=False)

    def __unicode__(self):
        return self.profile.first_name

#Availability
class ServiceAvailability(TimeStampAwareModel):
    DURATION = (
        ('1', '15'),
        ('2', '30'),
        ('3', '45'),
        ('4', '60'),
    )

    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    service = models.ForeignKey(ServiceOffered, null=True, blank=True)
    duration = models.CharField(max_length=10, choices=DURATION)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.service.service_name

#Booking
class AppointmentBooking(TimeStampAwareModel):
    appointment_by = models.ForeignKey(User, related_name='Patient')
    appointment_to = models.ForeignKey(UserProfile, related_name='Doctor')
    service_type = models.ForeignKey(ServiceOffered)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __unicode__(self):
        return self.appointment_by.first_name

#Awards & Recognitions
class AwardsRecognitions(TimeStampAwareModel):
    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    award_recognitions = models.CharField(max_length=100, null=True, blank=True)
    year_of_award = models.CharField(max_length=10, null=True, blank=True)
    awarding_institute = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s-%s" % (self.profile.first_name, self.award_recognitions)

#Mebmership & Affiliations
class Membership(TimeStampAwareModel):
    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    membership = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s-%s" % (self.profile.first_name, self.membership)

#Mebmership & Affiliations
class Education(TimeStampAwareModel):
    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    institute_board = models.CharField(max_length=100, null=True, blank=True)
    grade = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s-%s" % (self.profile.first_name, self.degree)

#Employment History
class EmploymentHistory(TimeStampAwareModel):
    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    employer_name = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s-%s-%s" % (self.profile.first_name, self.designation, self.employer_name)

#Employment History
class PracticeLocation(TimeStampAwareModel):
    profile = models.ForeignKey(UserProfile, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    flat_plot_number = models.CharField(max_length=100, null=True, blank=True)
    street_number = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    hospital = models.ForeignKey(Hospital,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s-%s" % (self.profile.first_name, self.location)
