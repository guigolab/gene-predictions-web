# FROM guigolab/geneid:1.4.5 as geneid

FROM python:3.6-stretch

# WORKDIR /soft

# COPY ./soft/bin/* /soft/GeneID/bin/

# COPY --from=geneid /usr/local/bin/geneid /soft/GeneID/bin/

# RUN chmod u+x  /soft/GeneID/bin/

WORKDIR /server

ADD ./server /server

# RUN apt-get update -qq && apt-get install -y \
#     gawk \
#     ghostscript \
#     libgs-dev \
#     imagemagick

# RUN apk --no-cache update
# RUN apk --no-cache add gawk
# RUN apk --no-cache add --virtual build-dependencies musl-dev linux-headers g++

RUN python -m pip install --upgrade pip

# RUN apk --no-cache add ghostscript ghostscript-dev
# RUN apk --no-cache add imagemagick

RUN pip install -r requirements.txt

# RUN apk --no-cache del build-dependencies

CMD ["uwsgi", "app.ini"]





