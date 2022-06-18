FROM ubuntu:20.04
RUN apt update -y
RUN apt upgrade -y
RUN mkdir /codes/
COPY ./app/ /codes/app/
COPY ./nginx/ /codes/nginx/
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get install -y python3-pip python3-dev
RUN apt install nginx -y
RUN pip install -r /codes/app/requirement.txt
COPY entrypoint.sh entrypoint.sh
EXPOSE 5000
EXPOSE 81
ENTRYPOINT [ "sh", "entrypoint.sh"]