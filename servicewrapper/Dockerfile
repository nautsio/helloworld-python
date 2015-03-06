FROM cargonauts/helloworld-python
RUN apt-get update && apt-get -y install curl

ADD servicewrapper.sh /
ENTRYPOINT ["/servicewrapper.sh"]
