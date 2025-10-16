FROM python:3.9-slim-buster
WORKDIR /app
COPY main.py /app
RUN pip install flask

EXPOSE 5000
ENV FLASK_APP=main.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]