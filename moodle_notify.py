import requests
import json
import os
from lotify.client import Client


def moodle_notify():
    lotify = Client()
    moodleToken = os.environ.get("MOODLE_TOKEN")
    lineToken = os.environ.get("LINE_TOKEN")
    url = f"{os.environ.get('MOODLE_URL','https://moodle.ntust.edu.tw/')}webservice/rest/server.php"
    params = {"moodlewsrestformat": "json",
              "wsfunction": "core_webservice_get_site_info", "wstoken": moodleToken}
    userId = requests.get(url, params).json()["userid"]
    params["wsfunction"] = "core_enrol_get_users_courses"
    params["userid"] = userId
    courses = requests.get(url, params).json()
    params["wsfunction"] = "core_course_get_contents"
    params.pop("userid")
    for course in courses:
        params["courseid"] = course["id"]
        courseContent = requests.get(url, params).json()
        if os.path.isfile(f"courses/{course['id']}.json"):
            with open(f"courses/{course['id']}.json", "r") as f:
                data = json.load(f)
                for i in range(len(data)):
                    modules = data[i]["modules"]
                    new_modules = courseContent[i]["modules"]
                    for module in new_modules:
                        if module not in modules:
                            lotify.send_message(
                                lineToken, f"{course['fullname']}\n{module['name']}\n add to moodle")
        if not os.path.exists("courses"):
            os.mkdir("courses")
        with open(f"courses/{course['id']}.json", "w") as f:
            json.dump(courseContent, f)
