import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

def downsample_1d(arr, scale=2):
    newarr = []
    for i in range(int(len(arr)/scale)):
        # newarr.append((arr[i]+arr[i+1])/2)
        ind = i*scale

        sum = 0
        for j in range(scale):
            sum+=arr[ind+j]
        sum = sum/scale
        newarr.append(sum)
    return newarr
    

def round_arr(arr):
    arr2 = arr
    for i in range(len(arr)):
        arr2[i] = int(round(arr[i]))
    return(arr2)


def distribution(mean, stdev, integer=False, samples=10, sample_depth=1000):
    tail = np.random.normal(mean, stdev, int(sample_depth*samples/2))
    tail = selection_sort(tail)

    curve = tail.tolist()
    for i in range(len(tail)):
        curve.append(tail[-i])
    
    for i in range(len(curve)-1):
        curve[i] = curve[i]

    # return curve
    if(integer):
        return round_arr(downsample_1d(curve, scale=sample_depth))
    else:
        return downsample_1d(curve, scale=sample_depth)

def mid_distribution(arr):
    if(len(arr)%2==0):
        mid = len(arr)/2

        m = (arr[int(round(mid))] + arr[int(round(mid))+1]/2)
        return(m/2)
    else:
        return(arr[len(arr)/2])
