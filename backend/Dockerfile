FROM python:3.10.12-slim


ADD requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

CMD ["python3", "-u", "app.py"]