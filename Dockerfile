FROM python:3-onbuild
WORKDIR /usr/src/app
COPY . .
CMD [ "python3", "-u", "./Redfin/main.py" ]