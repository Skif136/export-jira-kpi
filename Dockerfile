FROM python:3.6
ADD . /app
WORKDIR /app
RUN apt-get update && apt-get -y install ncat && apt-get -y install cron && pip install -r requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN (crontab -l ; echo "0 */6 * * * python main.py ") | crontab
EXPOSE 5050
CMD ncat -lk -p 5050 -e header.sh
