import numpy as np


def de_aliasing(v):
    """
    De-aliased a 2D vector (part of the 2D x time)
    """
    K=np.shape(v)[0]*3/2 # 'cause our non-linear time is quadratic
    a=int((K-np.shape(v)[0])/2)+1
    v_pad=np.pad(v, ((a,a),(a,a)), 'constant')

    return v_pad


v=np.array([[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]])

print(de_aliasing(v))