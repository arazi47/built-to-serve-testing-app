FROM python:latest
RUN pip install -i https://test.pypi.org/simple/ built-to-serve-arazi47 --upgrade
WORKDIR /app
COPY . /app
EXPOSE 8000
CMD ["python", "main.py"]