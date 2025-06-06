FROM python:3.9

WORKDIR /app

# Install Flask
RUN pip install flask

COPY app.py .

EXPOSE 5000

CMD ["python", "-u", "/app/app.py"]

