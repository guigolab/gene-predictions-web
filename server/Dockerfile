FROM guigolab/geneid:1.2 as geneid

FROM python:3.6-alpine

WORKDIR /soft

COPY ./soft/bin/* /soft/GeneID/geneid_1.2/bin/

COPY ./soft/param/* /soft/GeneID/geneid_1.2/

COPY --from=geneid /usr/local/bin/geneid /soft/GeneID/geneid_1.2/bin/

WORKDIR /server

ADD ./server /server

RUN apk --no-cache update
RUN apk --no-cache add gawk
RUN apk --no-cache add --virtual build-dependencies musl-dev linux-headers g++

RUN python -m pip install --upgrade pip

RUN apk --no-cache add ghostscript ghostscript-dev
RUN apk --no-cache add imagemagick

RUN pip install -r requirements.txt

RUN apk --no-cache del build-dependencies

ENV TAXDUMP_FILE="/server/taxdump.tar.gz"

RUN python -c "from ete3 import NCBITaxa; NCBITaxa(taxdump_file='${TAXDUMP_FILE}')"

CMD ["uwsgi", "app.ini"]





