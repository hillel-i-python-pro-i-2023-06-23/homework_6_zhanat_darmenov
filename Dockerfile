
FROM python:3.11

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y
RUN apt install curl


COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


COPY --chown=${USER} app/main.py main.py
COPY --chown=${USER} app/sqlite_manager.py sqlite_manager.py
COPY --chown=${USER} app/services services
COPY --chown=${USER} app/lorem_ipsum.txt lorem_ipsum.txt

USER ${USER}

ENTRYPOINT ["python", "main.py"]
