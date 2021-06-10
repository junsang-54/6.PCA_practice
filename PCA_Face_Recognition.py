import os
import numpy as np
from PIL import Image

#파일 불러오기
path_dir = '/Users/junsangwon/Downloads/archive'
file_list = os.listdir(path_dir)

#이미지파일 배열(n,1)로 변환한기
def mk_ar(a):
    np_array = np.array(a)
    len_np_array = np_array.shape[0]*np_array.shape[1]
    np_array_res = np.array(a).reshape(len_np_array, 1)
    return np_array_res
