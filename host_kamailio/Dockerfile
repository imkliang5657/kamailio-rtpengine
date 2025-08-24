#Kamailio Base image
FROM project/kamailio1:latest
#Configuration files
#COPY kamailio-simple.cfg /etc/kamailio/kamailio-simple.cfg
#Configuration files using websocket
COPY kamailio.cfg /etc/kamailio/kamailio.cfg
COPY kamailio-modules.cfg /etc/kamailio/kamailio-modules.cfg
COPY kamailio-address.cfg /etc/kamailio/kamailio-address.cfg
COPY kamailio /etc/default/kamailio
COPY logrotate/50-default.conf /etc/rsyslog.d/50-default.conf
COPY startup.sh /etc/kamailio/startup.sh
COPY kamctlrc /etc/kamailio/kamctlrc
#COPY calist.pem /etc/pki/CA/catlist.pem
#COPY kamailio1_cert.pem /home/certificate/kamailio_cert.pem
#COPY privkey.pem /home/certificate/privkey.pem
#Adding executing permissions
RUN chmod +x /etc/kamailio/startup.sh

#Initial command when starting up the container
ENTRYPOINT ["/etc/kamailio/startup.sh"]
