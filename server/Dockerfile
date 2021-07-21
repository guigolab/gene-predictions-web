FROM python:3.6

EXPOSE 5000

EXPOSE 8000

RUN python -m pip install --upgrade pip

RUN mkdir /server

WORKDIR /server

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY . .

ENV TAXDUMP_FILE="./services/taxdump.tar.gz"
RUN python -c "from ete3 import NCBITaxa; NCBITaxa(taxdump_file='${TAXDUMP_FILE}')"

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
