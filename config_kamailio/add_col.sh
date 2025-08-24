 kamctl db exec "ALTER TABLE rtpengine  
ADD mos_avg_pv FLOAT Default NULL,
ADD mos_min_pv FLOAT Default NULL,
ADD mos_max_pv FLOAT Default NULL,
ADD mos_average_jitter_pv FLOAT Default NULL,
ADD mos_average_roundtrip_pv FLOAT Default NULL, 
ADD mos_average_packetloss_pv FLOAT Default NULL,
ADD mos_average_samples_pv INT Default NULL,
ADD mos_max_jitter_pv  FLOAT Default NULL ,
ADD mos_max_roundtrip_pv  FLOAT Default NULL, 
ADD mos_max_packetloss_pv  FLOAT Default NULL, 
ADD mos_min_jitter_pv  FLOAT Default NULL ,
ADD mos_min_roundtrip_pv  FLOAT Default NULL ,
ADD mos_min_packetloss_pv FLOAT Default NULL ;"
