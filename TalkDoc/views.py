from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
import simplejson as simplejson
from django.db.models import Count, Q
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from time import  time
from django.views.decorators.csrf import csrf_exempt
from dateutil.relativedelta import relativedelta
from TalkDoc.appointments import upload_appointment, send_email

from TalkDoc.forms import *

from TalkDoc.models import *
from login.models import *


#Home

@login_required
def home(request):
    try:
        user = UserExtended.objects.get(user=request.user)
    except UserExtended.DoesNotExist:
        messages.error(request, "User does not exist.")
    try:
        profile_obj = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile_obj = ''


    return render_to_response('talkdoc/home.html',
                              {
                                  'user': user,
                                  'profile_obj':profile_obj,
                                  'home': 1
                              },context_instance=RequestContext(request))



@login_required
def edit_profile(request):
    services_list = ''
    awards_list = ''
    membership_list = ''
    education_list = ''
    employment_list = ''
    practice_location_list = ''

    try:
        user = UserExtended.objects.get(user=request.user)
    except UserExtended.DoesNotExist:
        messages.error(request, "User does not exist.")
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = ''

    if request.method == 'POST':
        if user_profile:
            form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        else:
            form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            userProfile = form.save(commit=False)
            userProfile.user = request.user
            userProfile.save()
            form.save_m2m()

            user_profile = userProfile
            if user.user_type.user_type == 'Doctor':
                user_profile.profile_step = '2'
                user_profile.save()
    else:
        if user_profile:
            form = UserProfileForm(instance=user_profile)
            services_list = ServiceOffered.objects.filter(speciality=user_profile.speciality)
        else:
            form = UserProfileForm()
            print form
    city_list = City.objects.all()
    hospital_list = Hospital.objects.all()
    speciality_list = Speciality.objects.all()
    if user_profile:
        awards_list = AwardsRecognitions.objects.filter(profile=user_profile, date_deleted__isnull=True)
        membership_list = Membership.objects.filter(profile=user_profile, date_deleted__isnull=True)
        education_list = Education.objects.filter(profile=user_profile, date_deleted__isnull=True)
        employment_list = EmploymentHistory.objects.filter(profile=user_profile, date_deleted__isnull=True)
        practice_location_list = PracticeLocation.objects.filter(profile=user_profile, date_deleted__isnull=True)

    return render_to_response('talkdoc/editProfile.html',
                              {
                                  'profile': 1,
                                  'form': form,
                                  'user': user,
                                  'profile_obj': user_profile,
                                  'awards_list': awards_list,
                                  'membership_list': membership_list,
                                  'education_list': education_list,
                                  'employment_list': employment_list,
                                  'city_list': city_list,
                                  'speciality_list': speciality_list,
                                  'services_list': services_list,
                                  'practice_location_list': practice_location_list,
                                  'hospital_list': hospital_list
                              }, context_instance=RequestContext(request))


#User Profile
@login_required
def user_profile(request):
    try:
        user = UserExtended.objects.get(user=request.user)
    except UserExtended.DoesNotExist:
        messages.error(request, "User does not exist.")
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = ''

    return render_to_response('talkdoc/userProfile.html',
                              {
                                  'user': user,
                                  'profile': 1,
                                  'profile_obj': user_profile
                              }, context_instance=RequestContext(request))


#Main Search
@login_required
def main_search(request, u_type=None):
    user_list = []
    q_objs = []
    searched_users = ''
    try:
        user = UserExtended.objects.get(user=request.user)
    except UserExtended.DoesNotExist:
        messages.error(request, "User does not exist.")
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = ''

    user_list = get_user_list(u_type)
    specialities = Speciality.objects.all()
    services = ServiceOffered.objects.all()
    cities = City.objects.all()
    hospital_list = Hospital.objects.all()

    user_name = request.GET.get("user_name", None)
    specialilty = request.GET.get("specialilty", None)
    city = request.GET.get("city", None)
    hospital = request.GET.get("hospital", None)

    if user_name:
        q_objs.append(Q(first_name=user_name))
    if specialilty:
        q_objs.append(Q(speciality__id=specialilty))
    if city:
        q_objs.append(Q(city__id=city))

    hospital_users = ''
    if hospital:
        hospital_users = UserProfile.objects.filter(id__in=PracticeLocation.objects.filter(hospital__id=hospital).values('profile'))
    if q_objs:
        objs_list= UserProfile.objects.filter(*q_objs)
        searched_users = objs_list.filter(user__in=UserExtended.objects.filter(user_type__user_type=u_type).values('user'))
    else:
        objs_list= UserProfile.objects.filter()
        searched_users = objs_list.filter(user__in=UserExtended.objects.filter(user_type__user_type=u_type).values('user'))
    if hospital_users and searched_users:
        searched_users = searched_users.filter(id__in=hospital_users)
    elif hospital_users:
        searched_users = hospital_users

    return render_to_response('talkdoc/searchResults.html',
                              {
                                  'user': user,
                                  'user_type': u_type,
                                  'user_list': simplejson.dumps(user_list),
                                  'specialities': specialities,
                                  'services': services,
                                  'cities': cities,
                                  'searched_users': searched_users,
                                  'hospital_list': hospital_list,
                                  'profile_obj': user_profile,
                                  'search':1
                               }, context_instance=RequestContext(request))


#Main Search
@login_required
def patient_search(request, u_type=None):
    user_list = []
    q_objs = []
    searched_users = []
    searched_users_list = ''
    try:
        user = UserExtended.objects.get(user=request.user)
    except UserExtended.DoesNotExist:
        messages.error(request, "User does not exist.")
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = ''

    user_list = get_user_list(u_type)
    services = ServiceOffered.objects.all()

    user_name = request.GET.get("user_name", None)
    visitType = request.GET.get("visitType", None)
    visitDate = request.GET.get("visit_date", None)

    if user_name:
        q_objs.append(Q(appointment_by__first_name=user_name))
    if visitType:
        q_objs.append(Q(service_type=visitType))
    if visitDate:
        q_objs.append(Q(start_time__contains=datetime.strptime(visitDate, '%m/%d/%Y').date()))

    q_objs.append(Q(appointment_to=UserProfile.objects.get(user=request.user)))
    searched_users_list = AppointmentBooking.objects.filter(*q_objs)
    for app in searched_users_list:
        profile = UserProfile.objects.get(user=app.appointment_by)
        age = relativedelta(datetime.today().date(), profile.dob.date()).years
        visit_type = ServiceOffered.objects.get(id=app.service_type.id)
        searched_users.append({'profile': profile, 'age': age, 'visit_type': visit_type, 'visit_date': app.start_time,
                               'appointment_by': app.appointment_by.id, 'appt_id':app.id})
    return render_to_response('talkdoc/patientSearch.html',
                              {
                                  'user': user,
                                  'user_type': u_type,
                                  'user_list': simplejson.dumps(user_list),
                                  'services': services,
                                  'searched_users': searched_users,
                                  'profile_obj': user_profile,
                                  'search':1
                               }, context_instance=RequestContext(request))

#Availablility Settings
@login_required
def availability_settings(request, id=None):
    avail_id=0

    try:
        user = UserExtended.objects.get(user=request.user)
    except UserExtended.DoesNotExist:
        messages.error(request, "User does not exist.")

    try:
        profile_obj = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        pass

    if request.method == 'POST':
        try:
            obj = Availability.objects.get(id=id)
            form = AvailabilitySettingsForm(request.POST, request.FILES, instance=obj)
        except Availability.DoesNotExist:
            form = AvailabilitySettingsForm(request.POST, request.FILES)

        if form.is_valid():
            userProfile = form.save(commit=False)
            userProfile.profile = profile_obj
            userProfile.save()
            form = AvailabilitySettingsForm()
            messages.success(request, "Availablity Settings updated successfuly.")
    else:
        try:
            obj = Availability.objects.get(id=id)
            avail_id = obj.id
            form = AvailabilitySettingsForm(instance=obj)
        except Availability.DoesNotExist:
            form = AvailabilitySettingsForm()

    availability_list = Availability.objects.filter(profile=profile_obj, date_deleted__isnull=True)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render_to_response('talkdoc/availabilitySettings.html',
                              {
                                  'form': form,
                                  'user': user,
                                  'profile_obj': profile_obj,
                                  'availability_list': availability_list,
                                  'avail_id': avail_id,
                                  'practice': 1
                               }, context_instance=RequestContext(request))


#View Profile
@login_required
def view_profile(request, id=None, appt_by=None, appt_id=None):
    try:
        user = UserExtended.objects.get(user=request.user)
    except UserExtended.DoesNotExist:
        messages.error(request, "User does not exist.")

    try:
        searched_by = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        pass

    try:
        profile_obj = UserProfile.objects.get(id=id)
    except UserProfile.DoesNotExist:
        pass

    try:
        searched_user = UserExtended.objects.get(user=profile_obj.user)
    except UserExtended.DoesNotExist:
        messages.error(request, "User does not exist.")
    return render_to_response('talkdoc/viewProfile.html',
                              {
                                  'user': user,
                                  'profile_obj': profile_obj,
                                  'searched_by': searched_by,
                                  'searched_to': searched_user,
                                  'search':1,
                                  'appt_by': appt_by,
                                  'appt_id': appt_id
                               }, context_instance=RequestContext(request))


#Delete Settings
@login_required
def delete_settings(request, id):
    print id
    try:
        obj = Availability.objects.get(id=id, date_deleted__isnull=True)
        obj.date_deleted = datetime.today()
        obj.save()
    except Availability.DoesNotExist:
        messages.success(request, "Tool does not exist.")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Booking
@login_required
def book_now(request, app_by=None, app_to=None, appt_id=None):
    profile_obj = ''
    user = ''
    searched_user = []

    try:
        user = UserExtended.objects.get(user=request.user)
    except UserExtended.DoesNotExist:
        pass
    try:
        profile_obj = UserProfile.objects.get(id=app_to)
    except UserProfile.DoesNotExist:
        pass

    visit_types = ServiceOffered.objects.all()
    if request.method == 'POST':
        date = request.POST.get("selected_date", None)
        visitType = request.POST.get("visitType", None)
        selected_time = request.POST.get("availableslots", None)

        start_date = str(date)+' ' + str(selected_time)
        try:
            service_obj = ServiceAvailability.objects.get(service__id=int(visitType), profile__id=app_to)
        except ServiceAvailability.DoesNotExist:
            pass
        if service_obj:
            counter = 0
            email_address = []
            current_start = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
            appt_start = current_start
            while counter < int(service_obj.get_duration_display())/15:
                obj = AppointmentBooking()
                obj.appointment_by = User.objects.get(id=app_by)
                obj.appointment_to = profile_obj
                obj.service_type = service_obj.service
                obj.start_time = current_start
                obj.end_time = current_start+timedelta(minutes=15)
                obj.save()

                current_start += timedelta(minutes=15)
                counter += 1

                if request.user.email not in email_address:
                    email_address.append(request.user.email)
                if profile_obj.user.email not in email_address:
                    email_address.append(profile_obj.user.email)
            appt_end = current_start
            upload_appointment(email_address, appt_start, appt_end)
            messages.success(request, "Appointment successfully created.")
        else:
            messages.warining(request, "Doctor is not available for this service.")
    else:
        if user.user_type.user_type == 'Doctor':
            profile = UserProfile.objects.get(user=app_by)
            age = relativedelta(datetime.today().date(), profile.dob.date()).years
            appointment = AppointmentBooking.objects.get(id=appt_id)
            searched_user.append({'profile': profile, 'age': age, 'visit_type': appointment.service_type.service_name})
    return render_to_response('talkdoc/bookNow.html',
                              {
                                  'user': user,
                                  'visit_types': visit_types,
                                  'profile_obj': profile_obj,
                                  'appt_by': app_by,
                                  'appt_to': app_to,
                                  'searched_user': searched_user,
                                  'appt_id':appt_id
                              },   context_instance=RequestContext(request))

#Get Time Slots
@login_required
def get_time_slots(request):
    date = request.POST.get("selected_date", None)
    doc_id = request.POST.get("doc_id", None)
    visitType = request.POST.get("visitType", None)
    if request.is_ajax():
        date_obj = datetime.strptime(str(date), '%Y-%m-%d')

        try:
            availability_time = Availability.objects.get(profile__id=doc_id, end_date__gte=date_obj, start_date__lte=date_obj)
        except Availability.DoesNotExist:
            availability_time = ''

        service_obj = ''
        slots = []

        if availability_time.is_saturday_off and date_obj.strftime("%A") == 'Saturday':
            json_stuff = simplejson.dumps({'slots': slots})
            return HttpResponse(json_stuff, content_type="application/json")
        if availability_time.is_sunday_off and date_obj.strftime("%A") == 'Sunday':
            json_stuff = simplejson.dumps({'slots': slots})
            return HttpResponse(json_stuff, content_type="application/json")

        try:
            service_obj = ServiceAvailability.objects.get(service__id=int(visitType), profile__id=doc_id)
        except ServiceAvailability.DoesNotExist:
            pass

        t_start = str(date)+' ' + str(availability_time.start_time)
        t_end = str(date)+' '+ str(availability_time.end_time)

        start = datetime.strptime(t_start, '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(t_end, '%Y-%m-%d %H:%M:%S')
        temp_end = datetime.strptime(t_start, '%Y-%m-%d %H:%M:%S')+ timedelta(minutes=int(service_obj.get_duration_display()))

        while start < end:
            is_booked = AppointmentBooking.objects.filter(appointment_to__id=doc_id, start_time__gte=start,
                                                           end_time__lte=temp_end)
            if is_booked:
                start += timedelta(minutes=15)
                temp_end += timedelta(minutes=15)
            else:
                if not start + timedelta(minutes=int(service_obj.get_duration_display())) > end:
                    slots.append(str(start.time()))
                start += timedelta(minutes=int(service_obj.get_duration_display()))
                temp_end += timedelta(minutes=int(service_obj.get_duration_display()))
                # temp = start+timedelta(minutes=15)
                # slots.append({'start':start,'end':temp})


        # index = 1
        # i=0
        # dolt = []
        # temmm= ''
        # for x in slots:
        #     if x['end']==slots[index]['start']:
        #         print x['start'],'>>>>>>>>>>>>>>>>>>>>>>>>>>>',x['end']
        #         i+=1
        #         if int(service_obj.get_duration_display())==30:
        #             if i == 2:
        #                 print temp,'...........................',i
        #                 dolt.append(temp)
        #                 i=0
        #                 temp=''
        #             else:
        #                 temp = x['start']
        #     index+=1
        json_stuff = simplejson.dumps({"slots": slots})
        return HttpResponse(json_stuff, content_type="application/json")


#Services Settings
@login_required
def services_settings(request, id=None):
    service_id = 0
    service = ''

    try:
        user = UserExtended.objects.get(user=request.user)
    except UserExtended.DoesNotExist:
        messages.error(request, "User does not exist.")

    try:
        profile_obj = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        pass

    if request.method == 'POST':
        duration = request.POST.get('duration', None)
        try:
            obj = ServiceAvailability.objects.get(id=id)
            obj.duration = duration
            obj.save()
        except ServiceAvailability.DoesNotExist:
            pass

    else:
        for s in profile_obj.services_offerd.all():
            try:
                obj = ServiceAvailability.objects.get(service=s, profile=profile_obj)
            except ServiceAvailability.DoesNotExist:
                obj = ServiceAvailability()
                obj.service = ServiceOffered.objects.get(id=s.id)
                obj.profile = profile_obj
                obj.save()

    services_list = ServiceAvailability.objects.filter(profile=profile_obj, date_deleted__isnull=True)

    return render_to_response('talkdoc/servicesSetting.html',
                              {
                                  'user': user,
                                  'profile_obj': profile_obj,
                                  'services_list': services_list,
                                  'practice': 1
                                }, context_instance=RequestContext(request))


# Profile Next Step
@login_required
def show_next_step(request, profile_id, step):

    try:
        profile_obj = UserProfile.objects.get(id=profile_id)
        profile_obj.profile_step = step
        profile_obj.save()
    except UserProfile.DoesNotExist:
        pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Add New Award
@login_required
def add_award_item(request, id=None):
    try:
        profile_obj = UserProfile.objects.get(id=id)
    except UserProfile.DoesNotExist:
        pass

    obj = AwardsRecognitions()
    obj.profile = profile_obj
    obj.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Submit New Award
@login_required
def submit_award_item(request, id= None):
    if request.method == 'POST':
        award = request.POST.get('award', None)
        year = request.POST.get('year', None)
        institute = request.POST.get('institute', None)

        try:
            obj = AwardsRecognitions.objects.get(id=id)
        except AwardsRecognitions.DoesNotExist:
            obj = ''

        if obj:
            obj.award_recognitions = award
            obj.year_of_award = year
            obj.awarding_institute = institute
            obj.save()

    messages.success(request, "Award & Recognition added successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Delete Award
@login_required
def delete_award_item(request, id=None):

    try:
        obj = AwardsRecognitions.objects.get(id=id)
        obj.date_deleted = datetime.today()
        obj.save()
    except AwardsRecognitions.DoesNotExist:
        pass

    messages.success(request, "Award & Recognition deleted successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Add Membership
def add_membership_item(request, profile_id=None):
    try:
        profile_obj = UserProfile.objects.get(id=profile_id)
    except UserProfile.DoesNotExist:
        pass

    obj = Membership()
    obj.profile = profile_obj
    obj.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

#Submit New Membership
@login_required
def submit_membership_item(request, id=None):
    if request.method == 'POST':
        membership = request.POST.get('membership', None)

        try:
            obj = Membership.objects.get(id=id)
        except Membership.DoesNotExist:
            obj = ''

        if obj:
            obj.membership = membership
            obj.save()

    messages.success(request, "Membership added successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Delete Membership
@login_required
def delete_membership_item(request, id=None):

    try:
        obj = Membership.objects.get(id=id)
        obj.date_deleted = datetime.today()
        obj.save()
    except Membership.DoesNotExist:
        pass

    messages.success(request, "Membership deleted successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Add Education
def add_education_item(request, profile_id=None):
    try:
        profile_obj = UserProfile.objects.get(id=profile_id)
    except UserProfile.DoesNotExist:
        pass

    obj = Education()
    obj.profile = profile_obj
    obj.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

#Submit New Education
@login_required
def submit_education_item(request, id=None):
    if request.method == 'POST':
        degree = request.POST.get('degree', None)
        start = request.POST.get('start', None)
        end = request.POST.get('end', None)
        institute = request.POST.get('institute', None)
        grade = request.POST.get('grade', None)

        try:
            obj = Education.objects.get(id=id)
        except Education.DoesNotExist:
            obj = ''
        if obj:
            obj.degree = degree
            obj.start_date = datetime.strptime(start, '%m/%d/%Y')
            obj.end_date = datetime.strptime(end, '%m/%d/%Y')
            obj.institute_board = institute
            obj.grade = grade
            obj.save()

    messages.success(request, "Education added successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Delete Education
@login_required
def delete_education_item(request, id=None):

    try:
        obj = Education.objects.get(id=id)
        obj.date_deleted = datetime.today()
        obj.save()
    except Education.DoesNotExist:
        pass

    messages.success(request, "Education deleted successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Add Employment History
def add_employment_item(request, profile_id=None):
    try:
        profile_obj = UserProfile.objects.get(id=profile_id)
    except UserProfile.DoesNotExist:
        pass

    obj = EmploymentHistory()
    obj.profile = profile_obj
    obj.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

#Submit New Employment History
@login_required
def submit_employment_item(request, id=None):
    if request.method == 'POST':
        designation = request.POST.get('designation', None)
        employer = request.POST.get('employer', None)
        start = request.POST.get('start', None)
        end = request.POST.get('end', None)
        country = request.POST.get('country', None)
        city = request.POST.get('city', None)
        if not designation:
            messages.warning(request, "Please enter Designation.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if not employer:
            messages.warning(request, "Please enter Employer.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if not start:
            messages.warning(request, "Please enter Start Date.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if not end:
            messages.warning(request, "Please enter End Date.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        try:
            obj = EmploymentHistory.objects.get(id=id)
        except EmploymentHistory.DoesNotExist:
            obj = ''
        try:
            city_obj = City.objects.get(id=int(city))
        except City.DoesNotExist:
            messages.error(request, "City does not exist.")

        if obj:
            obj.designation = designation
            obj.employer_name = employer
            obj.start_date = datetime.strptime(start, '%m/%d/%Y')
            obj.end_date = datetime.strptime(end, '%m/%d/%Y')
            obj.country = country
            obj.city = city_obj
            obj.save()

    messages.success(request, "Employment history added successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Delete Employment History
@login_required
def delete_employment_item(request, id=None):

    try:
        obj = EmploymentHistory.objects.get(id=id)
        obj.date_deleted = datetime.today()
        obj.save()
    except EmploymentHistory.DoesNotExist:
        pass

    messages.success(request, "Employment history deleted successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Add Practice Location
@login_required
def add_location_item(request, profile_id=None):
    try:
        profile_obj = UserProfile.objects.get(id=profile_id)
    except PracticeLocation.DoesNotExist:
        pass

    obj = PracticeLocation()
    obj.profile = profile_obj
    obj.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

#Submit New Practice Location
@login_required
def submit_location_item(request, id=None):
    if request.method == 'POST':
        location = request.POST.get('location', None)
        flatplotnumber = request.POST.get('flatplotnumber', None)
        streetnumber = request.POST.get('streetnumber', None)
        area = request.POST.get('area', None)
        country = request.POST.get('country', None)
        city = request.POST.get('city', None)
        hospital = request.POST.get('hospital', None)
        if not location:
            messages.warning(request, "Please enter Location.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if not flatplotnumber:
            messages.warning(request, "Please enter Flat Number.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if not streetnumber:
            messages.warning(request, "Please enter Street Number.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if not area:
            messages.warning(request, "Please enter End Area.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        try:
            obj = PracticeLocation.objects.get(id=id)
        except PracticeLocation.DoesNotExist:
            obj = ''
        try:
            city_obj = City.objects.get(id=int(city))
        except City.DoesNotExist:
            pass
        try:
            hospital_obj = Hospital.objects.get(id=int(hospital))
        except Hospital.DoesNotExist:
            pass

        if obj:
            obj.location = location
            obj.flat_plot_number = flatplotnumber
            obj.street_number = streetnumber
            obj.area = area
            obj.country = country
            obj.city = city_obj
            obj.hospital = hospital_obj
            obj.save()

    messages.success(request, "Practice Location added successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Delete Practice Location
@login_required
def delete_location_item(request, id=None):

    try:
        obj = PracticeLocation.objects.get(id=id)
        obj.date_deleted = datetime.today()
        obj.save()
    except PracticeLocation.DoesNotExist:
        pass

    messages.success(request, "Practice Location deleted successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Get Services by Speciality
@login_required
def get_services_by_speciality(request):
    service_list = []
    speciality_id = request.POST.get("selected_id", None)
    services = ServiceOffered.objects.filter(speciality__id=int(speciality_id))
    for obj in services:
        service_list.append({'key': obj.id, 'value': obj.service_name})

    json_stuff = simplejson.dumps({'service_list':service_list})
    return HttpResponse(json_stuff, content_type="application/json")


#Add Speciality & Services
def add_speciality_services(request, profile_id=None):
    speciality = request.POST.get("speciality", None)
    services = request.POST.getlist("services", None)

    try:
        profile_obj = UserProfile.objects.get(id=profile_id)
    except UserProfile.DoesNotExist:
        pass

    for obj in services:
        profile_obj.speciality = Speciality.objects.get(id=int(speciality))
        profile_obj.services_offerd.add(ServiceOffered.objects.get(id=int(obj)))
        profile_obj.save()

    messages.success(request, "Speciality & Services added successfully")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

#Appointment & Review
@login_required
def appointments_reviews(request):
    appointments_list = ''
    try:
        user = UserExtended.objects.get(user=request.user)
    except UserExtended.DoesNotExist:
        user = ''
    try:
        profile_obj = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile_obj = ''

    if user.user_type.user_type == 'Doctor':
        approved_appointments = AppointmentBooking.objects.filter(appointment_to=profile_obj, approved=True, date_deleted__isnull=True)
        appointments = AppointmentBooking.objects.filter(appointment_to=profile_obj, approved=False, date_deleted__isnull=True)
        appointments_list = fill_appointment_list(appointments)
    else:
        approved_appointments = AppointmentBooking.objects.filter(appointment_by=request.user, approved=True, date_deleted__isnull=True)

    approved_appointments_list = fill_appointment_list(approved_appointments)
    return render_to_response('talkdoc/appointments_reviews.html',
                              {
                                  'user': user,
                                  'profile_obj': profile_obj,
                                  'appointment_review': 1,
                                  'appointments': appointments_list,
                                  'approved_appointments': approved_appointments_list
                              }, context_instance=RequestContext(request))


#Approve Appointment
@login_required
def approve_appointment(request, appt_id, service_id):
    try:
        service = ServiceAvailability.objects.get(service__id=service_id)
    except ServiceOffered.DoesNotExist:
        pass

    try:
        appointment = AppointmentBooking.objects.get(id=appt_id)
        appointment.approved = True
        appointment.save()
    except AppointmentBooking.DoesNotExist:
        pass

    for i in range(1, int(service.get_duration_display())/15):

        try:
            app = AppointmentBooking.objects.get(start_time=appointment.start_time+timedelta(minutes=15))
            app.approved = True
            app.save()
        except AppointmentBooking.DoestNotExist:
            pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#Decline Appointment
@login_required
def decline_appointment(request, appt_id, service_id):
    if request.method == 'POST':
        try:
            service = ServiceAvailability.objects.get(service__id=service_id)
        except ServiceOffered.DoesNotExist:
            pass

        try:
            appointment = AppointmentBooking.objects.get(id=appt_id)
            appointment.date_deleted = datetime.now()
            appointment.save()
        except AppointmentBooking.DoesNotExist:
            pass

        for i in range(1, int(service.get_duration_display())/15):

            try:
                app = AppointmentBooking.objects.get(start_time=appointment.start_time+timedelta(minutes=15))
                app.date_deleted = datetime.now()
                app.save()
            except AppointmentBooking.DoestNotExist:
                pass
        if appointment:
            msg = request.POST.get('declineMsg','')
            user = User.objects.get(id=appointment.appointment_by.id)
            send_email(user.first_name, user.email, msg)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))








#Private Methods
#Get User List
def get_user_list(u_type):
    user_list = []

    users = UserExtended.objects.filter(user_type__user_type=u_type)

    for u in users:
        try:
            obj = UserProfile.objects.get(user=u.user)
            if obj.first_name not in user_list:
                user_list.append(str(obj.first_name))
        except UserProfile.DoesNotExist:
            pass

    return user_list

#Get Duration
def get_duration(duration):
    if duration == '1':
        return 15
    elif duration == '2':
        return 30
    elif duration == '3':
        return 45
    else:
        return 60

#Fill Appointment List
def fill_appointment_list(appointments):
    appointments_list = []
    app_obj = ''
    if len(appointments) == 1:
        index = 0
    else:
        index = 1

    for app in appointments:
        if len(appointments) == index:
            index -=1
        if app.end_time == appointments[index].start_time and app.appointment_by == appointments[index].appointment_by \
                and app.service_type == appointments[index].service_type:
            if not app_obj:
                app_obj = app
            continue
        if not app_obj:
            app_obj = app

        appointments_list.append({'appointment':app_obj})
        index +=1
        app_obj = ''
    return appointments_list