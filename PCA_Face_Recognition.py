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

#첫 번째 이미지 저장,
imag_f = Image.open('/Users/junsangwon/Downloads/archive/' + file_list[0])
imag_arr = mk_ar(imag_f)
#모든 얼굴 이미지 한 행렬
for i in range(len(file_list)):
    imag_ = Image.open('/Users/junsangwon/Downloads/archive/' + file_list[i])
    imag_arr_A = mk_ar(imag_)
    imag_arr = np.concatenate((imag_arr, imag_arr_A), axis=1)

imag_arr = np.delete(imag_arr, 0, axis=1)       #중복된 첫 열 제거(수정필요)

imag_arr_M = imag_arr.mean(axis=1)      #얼굴평균
imag_arr_Mrs = imag_arr_M.reshape(5600, 1)
imag_M = imag_arr_M.reshape(80,70)      #픽셀

pil_image=Image.fromarray(imag_M)       #얼굴평균 이미지화 하기
# pil_image.show()        #얼굴평균 출력
