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

imag_arr_M = imag_arr.mean(axis=1)      #얼굴평균 픽셀값
imag_arr_Mrs = imag_arr_M.reshape(5600, 1)
imag_M = imag_arr_M.reshape(80,70)      #이미지의 원래 배열로 변환

pil_image=Image.fromarray(imag_M)       #얼굴평균 이미지화 하기
# pil_image.show()        #얼굴평균 출력

Mean_arr = []           #얼굴평균 픽셀값 (400, 5600)으로 배열하기
for i in range(400):
    N = imag_arr_Mrs
    Mean_arr.append(N)


Mean_arr_A = np.array(Mean_arr).reshape(400, 5600)
Mean_arr_AT = Mean_arr_A.T

#차이벡터
A = imag_arr-Mean_arr_AT

Cov_matrix1 = (np.matmul(A.T, A))/5599
Cov_matrix2 = np.cov(A.T)

#고유값, 고유벡터, eige_face 생성
eigenvalue, eigenvector = np.linalg.eig(Cov_matrix2)
eig_face = np.matmul(A, eigenvector)

## eigenface 이미지 저장
# a = 0
# for i in range (400):
#     example = eig_face[:, i]
#     example = example.reshape(80,70)
#     eig_face_t_imag =Image.fromarray(example.astype(np.uint8), "L")
#     eig_face_t_imag.save('/Users/junsangwon/Desktop/eig_face5/{a}.jpeg'.format(a=a))
#     a += 1
