FROM python:3.11-slim

RUN  apt-get update && apt-get install -y libxml2-dev libxmlsec1-dev libxmlsec1-openssl

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install Zango

COPY . .

ENV PYTHONUNBUFFERED=1 
   
# EXPOSE 8000

# # CMD ["gunicorn", "-b", "0.0.0.0:8000", "IssueTrackerApplication.wsgi:application"]
# CMD ["python","manage.py","runserver","0.0.0.0:8000"]
