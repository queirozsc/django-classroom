import requests
from allauth.account.signals import user_logged_in
from allauth.socialaccount.models import SocialToken
from django.dispatch import receiver
from courses.models import Course


@receiver(user_logged_in)
def retrieve_google_classroom_data(request, user, **kwargs):
    """After login, retrieve Google Classroom data"""
    # get the user's authorization token
    token = SocialToken.objects.filter(account__user=user, account__provider='google')
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
