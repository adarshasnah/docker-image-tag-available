FROM python:3.8-alpine
ADD . /docker-image-tag-available
WORKDIR /docker-image-tag-available
RUN python /docker-image-tag-available/setup.py install
CMD docker-image-tag-available