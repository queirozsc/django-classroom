import requests
# from allauth.account.signals import user_logged_in
from allauth.socialaccount.signals import social_account_updated
from allauth.socialaccount.models import SocialToken
from django.dispatch import receiver
from accounts.models import User
from courses.models import Course


# @receiver(user_logged_in)
@receiver(social_account_updated)
def retrieve_google_classroom_data(request, sociallogin, **kwargs):
# def retrieve_google_classroom_data(request, user, **kwargs):
    """ After a user successfully authenticates via a social provider, but before the login is fully processed,
    retrieve Google Classroom data"""
    # updates user's extra data
    user = User.objects.get(pk=request.user.id)
    user.name = sociallogin.account.extra_data['name']
    user.avatar = sociallogin.account.extra_data['picture']
    user.save()

    # get the user's authorization token
    token = SocialToken.objects.filter(account__user=request.user, account__provider='google')

    # save courses' data
    url = 'https://classroom.googleapis.com/v1/courses/'
    print(url)
    headers = {
        'content-type': 'application/json',
    }
    response = requests.get(
        url,
        params={'access_token': token[0].token},
        headers=headers)
    courses = response.json()['courses']
    Course.objects.filter(teacher=user).delete()
    for course in courses:
        Course.objects.create(
            id=course['id'],
            teacher=user,
            name=course['name'],
            section=course['section'],
            state=course['courseState'],
            link=course['alternateLink'],
            teachers_email=course['teacherGroupEmail'],
            course_email=course['courseGroupEmail'],
            created_at=course['creationTime'],
            updated_at=course['updateTime']
        )
