from django.forms import *
from django import forms
from TalkDoc.models import *

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ['sex', 'dob', 'address', 'medical_condition', 'alergy', 'blood_group', 'marital_status'
                , 'city', 'address', 'picture', 'first_name', 'last_name', 'cell_phone',
                  'services_offerd', 'speciality','user']

        def __init__(self, *args, **kwargs):
		super(UserProfileForm, self).__init__(*args, **kwargs)# Call to ModelForm constructor
                self.fields['dob'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['sex'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['medical_condition'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['alergy'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['blood_group'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['marital_status'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['city'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['address'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['picture'].widget.attrs.update({'style' : 'height: 33px;'})
                self.fields['first_name'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['last_name'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['cell_phone'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['speciality'].widget.attrs.update({'class': 'form-control pass_field'})
                self.fields['services_offerd'].widget.attrs.update({'class': 'form-control pass_field'})

class AvailabilitySettingsForm(ModelForm):
	class Meta:
		model = Availability
		fields = ['profile', 'start_date', 'end_date', 'start_time', 'end_time', 'is_saturday_off', 'is_sunday_off']

        def __init__(self, *args, **kwargs):
		super(AvailabilitySettingsForm, self).__init__(*args, **kwargs)# Call to ModelForm constructor
                self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
                self.fields['end_date'].widget.attrs.update({'class': 'form-control'})
                self.fields['start_time'].widget.attrs.update({'class': 'form-control'})
                self.fields['end_time'].widget.attrs.update({'class': 'form-control'})
