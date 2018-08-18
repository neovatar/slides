FROM ubuntu:latest
RUN apt-get update && apt-get -y install procps python3 dumb-init
COPY fork.py /root/
CMD ["python3","/root/fork.py"]
