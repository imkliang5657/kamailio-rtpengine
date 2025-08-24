FROM project/kamailio1:latest

#Copy the config file onto the Filesystem of the Docker instance
#COPY kamailio.cfg /etc/kamailio/
#COPY tls.cfg /etc/kamailio/
#COPY kamailio /etc/default/kamailio
#COPY logrotate/50-default.conf /etc/rsyslog.d/50-default.conf
COPY startup.sh /etc/kamailio/startup.sh
RUN chmod +x /etc/kamailio/startup.sh
#Initial command when starting up the container
ENTRYPOINT ["/etc/kamailio/startup.sh"]
