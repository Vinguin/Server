docker_container:
	docker build -t ts3 . 

docker_run:
	docker run -it \
	--name ts3 \
	-d \
	-p 9987:9987/udp -p 30033:30033 -p 10011:10011 \
	-v /root/Data/TS3/logs:/home/ts3/teamspeak3-server_linux_amd64/logs \
	-v /root/Data/TS3/files:/home/ts3/teamspeak3-server_linux_amd64/files \
	-v /root/Data/TS3/query_ip_blacklist.txt:/home/ts3/teamspeak3-server_linux_amd64/query_ip_blacklist.txt \
   	-v /root/Data/TS3/query_ip_whitelist.txt:/home/ts3/teamspeak3-server_linux_amd64/query_ip_whitelist.txt \
   	-v /root/Data/TS3/ts3server.ini:/home/ts3/teamspeak3-server_linux_amd64/ts3server.ini  \
	-v /root/Data/TS3/ts3server.sqlitedb:/home/ts3/teamspeak3-server_linux_amd64/ts3server.sqlitedb  \
	ts3

hello:
	echo "hallo hallo"
