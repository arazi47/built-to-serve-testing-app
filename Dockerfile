FROM python:latest
# Pull the package from test pypi repo and its deps (if any) from the main pypi repo
RUN pip install -i https://test.pypi.org/simple/ ws2g --extra-index-url=https://pypi.org/simple/
WORKDIR /app
COPY . /app
EXPOSE 8000
CMD ["python", "main.py"]