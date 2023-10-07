FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
