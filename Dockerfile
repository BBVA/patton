FROM cr0hn/python3.6-alpine-make:latest as python-base
COPY requirements.txt .
RUN apk update && apk upgrade && apk del openssl-dev && apk add postgresql-dev
RUN pip install -U -r requirements.txt

# Build clean image
FROM cr0hn/python3.6-alpine-gosu:latest
COPY --from=python-base /root/.cache /root/.cache
COPY --from=python-base requirements.txt .

# Copy binary dependencies
COPY --from=python-base /usr/lib/*xslt* /usr/lib/
COPY --from=python-base /usr/lib/libssl* /usr/lib/
COPY --from=python-base /usr/lib/libcrypto* /usr/lib/
COPY --from=python-base /usr/lib/libldap* /usr/lib/
COPY --from=python-base /usr/lib/liblber* /usr/lib/
COPY --from=python-base /usr/lib/*libxml* /usr/lib/
COPY --from=python-base /usr/lib/libsasl2* /usr/lib/
COPY --from=python-base /usr/lib/*libgcrypt* /usr/lib/
COPY --from=python-base /usr/lib/*libgpg-error* /usr/lib/
COPY --from=python-base /usr/lib/libpq* /usr/lib/

RUN pip install -U -r requirements.txt
RUN pip install patton-server
RUN rm -rf /root/.cache

ADD ./deploy/run_patton.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/run_patton.sh

ENTRYPOINT ["/usr/local/bin/run_patton.sh"]
