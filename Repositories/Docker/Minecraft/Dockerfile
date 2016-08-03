FROM buildpack-deps:trusty-scm

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-7-jre
RUN mkdir /home/Minecraft
WORKDIR /home/Minecraft


EXPOSE 25000

CMD java -Xmx1024M -Xms1024M -jar minecraft_server.1.10.2.jar nogui

