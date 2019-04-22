FROM python:3.7-alpine as base

# Is this build from github, pypi, or the current checkout
ARG source=cwd

RUN case "$source" in \
	"github") \
	echo git+https://github.com/BBVA/patton-cli > /tmp/pip-source;; \
	"pypi") \
	echo patton-cli > /tmp/pip-source;; \
	"cwd") \
	echo /src > /tmp/pip-source;; \
	*) \
	echo Unknown source -- $source; exit 1;; \
esac


# git, and this COPY are only used in _some_ source modes. But since
# this is a two stage build it's simpler to include them here. They'll
# be omited from the final image
RUN apk add git
RUN mkdir /src
COPY . /src

# setup virtual end
RUN python3 -m pip install --user virtualenv
RUN python3 -m virtualenv /patton-cli

# Install! via whatever means chosen above
RUN /patton-cli/bin/pip install `cat  /tmp/pip-source`

FROM python:3.7-alpine
RUN apk update \
	&& apk upgrade \
	&& rm -r /var/cache/apk
COPY --from=base  /patton-cli  /patton-cli

ENTRYPOINT ["/patton-cli/bin/patton"]
CMD []
