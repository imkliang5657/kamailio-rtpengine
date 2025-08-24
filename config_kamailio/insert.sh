mysql -e "INSERT INTO rtpengine (id, setid, url, weight, disabled, stamp) VALUES (NULL, '0', 'udp:10.0.5.7:2224', '1', '0', NOW());" kamailio
mysql -e "INSERT INTO rtpengine (id, setid, url, weight, disabled, stamp) VALUES (NULL, '1', 'udp:10.0.5.6:2223', '1', '0', NOW());" kamailio
mysql -e "INSERT INTO rtpengine (id, setid, url, weight, disabled, stamp) VALUES (NULL, '2', 'udp:114.35.197.224:12223', '1', '0', NOW());" kamailio
