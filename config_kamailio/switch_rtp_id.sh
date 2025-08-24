
NAME=$1
kamctl db exec "UPDATE location 
SET mos_avg_pv = @tmp := mos_avg_pv, 
    mos_avg_pv = mos_avg_pv2,       
    mos_avg_pv2 = @tmp,  
    rtp_id = @tmp_rtp := rtp_id,
    rtp_id = rtp_id2,
    rtp_id2 = @tmp_rtp   
WHERE username = $NAME;"
