FROM debian:stable

RUN apt update && apt -y install debsecan
COPY ./stdin2debsecan /usr/local/bin/

ENTRYPOINT /usr/local/bin/stdin2debsecan
