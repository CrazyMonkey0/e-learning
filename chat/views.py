from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def course_chat_room(request, course_id):
    try:
        # Download a course with an ID that matches the ID of the course that the current user has joined.
        course = request.user.courses_joined.get(id=course_id)
    except:
        # The user is not a member of this course or the course does not exist.
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'course': course})
