FROM python:alpine
WORKDIR /home/data
COPY ./ ./
CMD ["python" ,"assignment3.py"]
