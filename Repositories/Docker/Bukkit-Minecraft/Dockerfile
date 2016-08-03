FROM buildpack-deps:trusty-scm

ENV MINECRAFT_URL http://dl.minecraft-statistic.net/files/spigot/spigot-1.10.2-R0.1-SNAPSHOT.jar?key=20oDho4MyNZziRQ5RBwygg&exp=1470248698

# Installiere Abhängigkeiten
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y openjdk-7-jre openjdk-7-jre perl screen


# Richte alles ein.
RUN sudo mkdir /home/Minecraft
WORKDIR /home/Minecraft
RUN  wget -q -O minecraft-server.jar ${MINECRAFT_URL} 

RUN touch start.sh 
RUN echo "#!/bin/sh&#13; BINDIR=$(dirname \"$(readlink -fn \"$0\")\")&#13; cd \"$BINDIR\"&#13; java -Xmx1024M -jar minecraft-server.jar" >> start.sh
EXPOSE 25565

CMD  bash start.sh
