FROM python:3.6-alpine as build
WORKDIR /usr/src/app/restful
COPY requirements.txt /usr/src/app/restful
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

FROM python:3.6-alpine
COPY --from=build /usr/local/lib/python3.6/site-packages/ /usr/local/lib/python3.6/site-packages/
RUN mkdir -p /usr/src/app/restful
WORKDIR /usr/src/app/restful
COPY . /usr/src/app/restful
ENV PYTHONPATH /usr/src/app/restful
CMD ["python","application/app.py"]