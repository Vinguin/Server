FROM ubuntu:16.04


ENV TS3_UID 1000
ENV TS3_DL http://dl.4players.de/ts/releases/3.0.12.4/teamspeak3-server_linux_amd64-3.0.12.4.tar.bz2

RUN apt update && \
    apt-get install -y \
    wget bzip2


RUN useradd -M --uid ${TS3_UID} ts3 && \
    wget -q -O teamspeak3-server_linux_amd64.tar.bz2  ${TS3_DL} && \
    tar -xvf teamspeak3-server_linux_amd64.tar.bz2  && \
    rm teamspeak3-server_linux_amd64.tar.bz2 && \
    mkdir /home/ts3 && \
    mv teamspeak3-server_linux_amd64 /home/ts3 && \
    cd /home/ts3/teamspeak3-server_linux_amd64 && \
    mkdir files  logs && \
    touch query_ip_blacklist.txt query_ip_whitelist.txt  ts3server.ini  ts3server.sqlitedb
 

#Expose the Standard TS3 port, for files, for serverquery
EXPOSE 9987/udp 30033 10011

ENTRYPOINT ["/home/ts3/teamspeak3-server_linux_amd64/ts3server_minimal_runscript.sh"]

