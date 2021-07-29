FROM guigolab/geneid:1.2 as geneid

FROM python:3.6-stretch

WORKDIR /server

ADD . /server

# RUN python -m pip install --upgrade pip

COPY --from=geneid /usr/local/bin/geneid /geneid-software

RUN pip install -r requirements.txt
# COPY requirements.txt requirements.txt

# RUN python -m pip install -r requirements.txt

# ENV TAXDUMP_FILE="./services/taxdump.tar.gz"
# RUN python -c "from ete3 import NCBITaxa; NCBITaxa(taxdump_file='${TAXDUMP_FILE}')"

CMD ["uwsgi", "app.ini"]





