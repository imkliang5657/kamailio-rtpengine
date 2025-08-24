kamctl db exec "ALTER TABLE subscriber  
ADD rtp_id   INT Default NULL,
ADD counter   INT Default NULL,
ADD mos_avg_pv FLOAT Default NULL,
ADD mos_average_roundtrip_pv FLOAT Default NULL,
ADD rtp_id2   INT Default NULL,
ADD mos_avg_pv2 FLOAT Default NULL,
ADD mos_average_roundtrip_pv2 FLOAT Default NULL;"
