#Kamailio Base image
FROM miller112321507/kamailio:3.0
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
COPY insert.sh /etc/kamailio/insert.sh
COPY add_col.sh /etc/kamailio/add_col.sh
COPY add_usr.sh /etc/kamailio/add_usr.sh
COPY update_mos.sh /etc/kamailio/update_mos.sh
COPY update_usr.sh /etc/kamailio/update_usr.sh
COPY select_usr.sh /etc/kamailio/select_usr.sh
COPY test.sh /etc/kamailio/test.sh
COPY search.sh  /etc/kamailio/search.sh
COPY counter.sh /etc/kamailio/counter.sh
COPY switch.sh  /etc/kamailio/switch.sh
COPY true.sh /etc/kamailio/true.sh
COPY sip_message.txt /etc/kamailio/sip_message.txt
COPY extract_sip_body.sh  /etc/kamailio/extract_sip_body.sh
COPY rtpcmd.py rtpcmd.py 
#COPY calist.pem /etc/pki/CA/catlist.pem
#COPY kamailio1_cert.pem /home/certificate/kamailio_cert.pem
#COPY privkey.pem /home/certificate/privkey.pem
#Adding executing permissions
RUN chmod +x /etc/kamailio/switch.sh
RUN chmod +x /etc/kamailio/true.sh
RUN chmod 077 /etc/kamailio/sip_message.txt
RUN chmod +x /etc/kamailio/startup.sh
RUN chmod +x /etc/kamailio/insert.sh
RUN chmod +x /etc/kamailio/test.sh
RUN chmod +x /etc/kamailio/search.sh
RUN chmod +x /etc/kamailio/add_col.sh
RUN chmod +x /etc/kamailio/add_usr.sh
RUN chmod +x /etc/kamailio/update_mos.sh
RUN chmod +x /etc/kamailio/update_usr.sh
RUN chmod 777 /etc/kamailio/counter.sh
RUN chmod +x /etc/kamailio/extract_sip_body.sh
#Initial command when starting up the container
ENTRYPOINT ["/etc/kamailio/startup.sh"]
