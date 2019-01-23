FROM restful-api:latest as build
WORKDIR /usr/src/app/grpc
RUN apk add --update  --no-cache libstdc++ libc6-compat openssh-client git gcc cython linux-headers make musl-dev python3-dev g++
ENV GRPC_PYTHON_VERSION 1.15.0
RUN pip install grpcio==${GRPC_PYTHON_VERSION} grpcio-tools==${GRPC_PYTHON_VERSION}


FROM python:3.6-alpine
COPY --from=build /usr/local/lib/python3.6/site-packages/ /usr/local/lib/python3.6/site-packages/
COPY --from=build /usr/src/app/restful /usr/src/app/restful
RUN apk add --update --no-cache libstdc++ libc6-compat
RUN mkdir -p /usr/src/app/grpc
WORKDIR /usr/src/app/grpc
COPY . /usr/src/app/grpc
ENV PYTHONPATH /usr/src/app/grpc:/usr/src/app/grpc:/usr/src/app/grpc/messages:/usr/src/app/restful
EXPOSE 50051

CMD [ "python", "./app.py" ]