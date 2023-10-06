FROM python:3.11
EXPOSE 5000
WORKDIR /app
COPY requrements.txt
RUN pip install -r requrements.txt
RUN pip install flask
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
