FROM buildpack-deps:trusty-scm

ENV MINECRAFT_URL https://s3.amazonaws.com/Minecraft.Download/versions/1.10.2/minecraft_server.1.10.2.jar


RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-7-jre && \
    wget -q -O minecraft-server.jar ${MINECRAFT_URL} 


EXPOSE 25565

CMD ls
CMD java -Xmx1024M -Xms1024M -jar minecraft-server.jar nogui

