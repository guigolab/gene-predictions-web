FROM guigolab/geneid:1.2 as geneid

FROM python:3.6-stretch

WORKDIR /soft

COPY ./soft/bin/* /soft/GeneID/geneid_1.2/bin/

COPY ./soft/param/* /soft/GeneID/geneid_1.2/

COPY --from=geneid /usr/local/bin/geneid /soft/GeneID/geneid_1.2/bin/

WORKDIR /server

ADD . /server

RUN apt-get update -y
RUN apt-get -y install gawk;

RUN python -m pip install --upgrade pip

RUN apt-get install -y ghostscript libgs-dev
RUN apt-get install -y libmagickwand-dev imagemagick --fix-missing

RUN pip install -r ./server/requirements.txt

# ENV TAXDUMP_FILE="./server/services/taxdump.tar.gz"

# RUN python -c "from ete3 import NCBITaxa; NCBITaxa(taxdump_file='${TAXDUMP_FILE}')"

CMD ["uwsgi", "app.ini"]





