FROM python:3-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache --virtual .build-deps \
          alpine-sdk make gcc python3-dev python-dev libxslt-dev libxml2-dev libc-dev libffi-dev zlib-dev py-pip postgresql-dev

RUN pip install patton-server==1.0.2

ADD ./deploy/run_patton.sh /usr/local/bin/
ADD ./deploy/wait-for-it.sh /usr/local/bin/
ADD ./deploy/make_cron_task.sh /usr/local/bin/
ADD ./deploy/update_vulns.sh /usr/local/bin/

RUN apk del .build-deps && \
    apk add bash apk-cron libxslt libpq && \
    rm -rf /root/.cache /var/cache/apk/* && \
    chmod +x /usr/local/bin/*.sh

ENTRYPOINT ["/usr/local/bin/run_patton.sh"]
