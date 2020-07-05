FROM python:3.8.2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV TESTENV='{"TESTA":1,"TESTB":2,"TESTXYZ":54}'

COPY src/ /usr/src/app
RUN [ "python", "/usr/src/app/make_env.py" ]
CMD [ "python", "/usr/src/app/hello.py" ]
