# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy entrypoint.sh
# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# install system dependencies
RUN apt-get update && apt-get install -y netcat curl ftp

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# install eutils
RUN sh -c "$(curl -fsSL https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh)"
ENV PATH="$PATH:$HOME/edirect"
# RUN ftp 'ftp://ftp.ncbi.nlm.nih.gov/geo/README.txt' -a -i -o 'ncbi_eutils_ftp_readme.txt'
# RUN curl 'ftp://ftp.ncbi.nlm.nih.gov/geo/datasets/GDSnnn/GDS999/soft/GDS999.soft.gz' -o 'GDS999.soft.gz'
# RUN gunzip 'GDS999.soft.gz'

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME
# brute force download GDS999.soft.gz
RUN $APP_HOME/staticfiles/get_soft_file.py
# change to the app user
USER app

# run entrypoint.prod.sh
# ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]

# # copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
