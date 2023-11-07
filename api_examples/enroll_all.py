import requests

username = 'bambi'
password = 'zaq1@WSX'

base_url = 'http://127.0.0.1:8000/api/'

# Download all courses
r = requests.get(f'{base_url}courses/')
courses = r.json()

available_courses = ' '.join(
    f"\nid: {course['id']}, title: {course['title']} " for course in courses)
print(f'Available courses: {available_courses}')


for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(
        f'{base_url}courses/{course_id}/enroll/', auth=(username, password))
    if r.status_code == 200:
        # Success
        print(f'Successfully enrolled in the course {course_title}')
