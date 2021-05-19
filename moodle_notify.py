import requests
import datetime
import time
import os
from lotify.client import Client


def moodle_notify():
    lotify = Client()
    moodleToken = os.environ.get("MOODLE_TOKEN")
    lineToken = os.environ.get("LINE_TOKEN")
    url = f"{os.environ.get('MOODLE_URL','https://moodle.ntust.edu.tw/')}webservice/rest/server.php"
    currentTime = int(time.time())
    dayTime = 86400
    GMT8 = 28800
    params = {"moodlewsrestformat": "json",
              "wsfunction": "core_webservice_get_site_info", "wstoken": moodleToken}
    userId = requests.get(url, params).json()["userid"]
    params["wsfunction"] = "core_enrol_get_users_courses"
    params["userid"] = userId
    courses = requests.get(url, params).json()
    params["wsfunction"] = "core_course_get_contents"
    params.pop("userid")
    typeParams = {"moodlewsrestformat": "json", "wstoken": moodleToken}
    for course in courses:
        params["courseid"] = course["id"]
        courseContent = requests.get(url, params).json()
        for i in courseContent:
            modules = i["modules"]
            for module in modules:
                if module.get("contents") == None:
                    continue
                for content in module["contents"]:
                    if int(content["timemodified"]) >= currentTime-dayTime:
                        lotify.send_message(
                            lineToken, f"{course['fullname']}\n{content['filename']}\nUpdate on moodle")
        # assignments notify
        typeParams["wsfunction"] = "mod_assign_get_assignments"
        typeParams["courseids[0]"] = course["id"]
        assignments = requests.get(url, typeParams).json()[
            "courses"][0]["assignments"]
        for assingment in assignments:
            if int(assingment["timemodified"]) >= currentTime-dayTime:
                dueDate = datetime.datetime.utcfromtimestamp(
                    int(assingment['duedate'])+GMT8).strftime('%Y-%m-%d %H:%M:%S')
                lotify.send_message(
                    lineToken, f"{course['fullname']}\n{assingment['name']}\nDue: {dueDate}\nUpdate on moodle")
        # quiz notify
        typeParams["wsfunction"] = "mod_quiz_get_quizzes_by_courses"
        quizzes = requests.get(url, typeParams).json()["quizzes"]
        for quiz in quizzes:
            if int(quiz["timeclose"]) >= currentTime-dayTime:
                closeTime = datetime.datetime.utcfromtimestamp(
                    int(assingment['timeclose'])+GMT8).strftime('%Y-%m-%d %H:%M:%S')
                lotify.send_message(
                    lineToken, f"{course['fullname']}\n{quiz['name']}\nClose time: {closeTime}\nUpdate on moodle")


if __name__ == "__main__":
    moodle_notify()
