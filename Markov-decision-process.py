def solveMDP(probs, mR, s1Reward, s4Reward):
    error=0.00001
    S3Qup=0
    S3Qdown=0
    S2Qup=0
    S2Qdown=0
    pres3u=1
    pres3d=1
    pres2u=1
    pres2d=1
    x=0
    while(pres3u>error or pres3d>error or pres2u>error or pres2d>error):
        pres3u = S3Qup 
        pres3d = S3Qdown
        pres2u = S2Qup
        pres2d = S2Qdown

        S3Qup   = (probs[0]*(s4Reward+mR+max(0,0)))+((round(1-probs[0],1))*(mR+max(S2Qup,S2Qdown)))
        pres3u=abs(pres3u-S3Qup)
        
        S3Qdown = (probs[1]*(mR+max(S2Qup,S2Qdown)))+((round(1-probs[1],1))*(mR+s4Reward + max(0,0)))
        pres3d=abs(pres3d-S3Qdown)
        
        S2Qup   = (probs[0]*(mR+max(S3Qdown,S3Qup)))+((round(1-probs[0],1))*(mR+s1Reward+max(0,0)))
        pres2u = abs(pres2u-S2Qup)
        
        S2Qdown = (probs[1]*(mR+s1Reward+max(0,0)))+((round(1-probs[1],1))*(mR+max(S3Qup,S3Qdown)))
        pres2d=abs(pres2d-S2Qdown)

        if(pres3u<error and pres3d<error and pres2u<error and pres2d<error):
            return [round(S2Qup,6),round(S2Qdown,6),round(S3Qup,6),round(S3Qdown,6)]

