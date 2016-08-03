FROM java:8

RUN wget http://goo.gl/IHP6Qw -O selenium-server-standalone-2.53.0.jar

 
EXPOSE 4444 

ENTRYPOINT java -jar selenium-server-standalone-2.53.0.jar \
    -Djava.security.egd=file:///dev/urandom switch

