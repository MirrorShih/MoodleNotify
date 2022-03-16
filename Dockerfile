FROM centos:centos7

WORKDIR /etc/moodlenotify

# Install python
RUN yum install python3 -y

# Copy python scripts
COPY . /etc/moodlenotify

# Install python packages
RUN pip3 install -r requirements.txt

# Environment Variables
# ENV MOODLE_TOEKN=(Your MOODLE_TOKEN)
# ENV LINE_TOKEN=(Your LINE_TOKEN)
# ENV MOODLE_URL=(Your MOODLE_URL)
# ENV NOTIFY_TIME=(TIME)

ENTRYPOINT python3 clock.py
