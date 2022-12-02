def findingAngle(hh,mm):
    hh=hh%12                          #24-hour notation
    h=(hh*360)//12+(mm*360)//(12*60)  #position of hour's hand
    m=(mm*360)//(60)                  #calculate angle differnce
    angle=abs(h-m)                    #consider the shorter angle and return it
    if angle>180:
        angle=360-angle
    return angle

if __name__== '__main__':             #clock angle problem
    hh=21
    mm=00

    print(findingAngle(hh,mm))