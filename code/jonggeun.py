import cv2
import numpy as np
from PIL import Image
from pytesseract import *
import re
import pandas as pd

img = Image.open(r'C:\Users\82107\Desktop\ocr_test\ocr테스트이미지.jpg')
text = pytesseract.image_to_string(img,lang='kor')
size_table = re.split('\n',text)
matchers = ['사이즈(','어깨너비','가슴둘레','소매길이','총장']
size = [s for s in size_table if any(xs in s for xs in matchers)]

size2 = []
for i in range(len(size)):
    size2.append(size[i].split())
    
if '총장' and '소매길이' and '어깨너비' and '가슴둘레' not in size2[1][0] + size2[2][0]+size2[3][0]+size2[4][0]:
    pass
else:
    match = re.match(r"([가-힣]+)([(0-9].+)", size2[0][0], re.I)
    if match:
        items = match.groups()
    size2[0][0] = items[0]

    size3 = list(map(list, zip(*size2))) #리스트를 transpose하는 법
    #import numpy as np
    #np.array(a).T.tolist() - 똑같은 방법  -> array 변환 -> 전치 -> tolist
    df_size = pd.DataFrame(size3[1:], columns = size3[0])

size3=[]
for i in range(len(size2)):
    if len(size2[i]) == len(size2[0]):
        size3.append(size2[i])
    else:
        diff = len(size2[i]) - len(size2[0])
        size3.append(size2[i][diff:])

size4 = list(map(list, zip(*size3))) #리스트를 transpose하는 법

df_size = pd.DataFrame(size4[1:], columns = size4[0])

print(df_size)

with open(r'C:\Users\82107\Desktop\file\testtest', 'w') as file:
    print(df_size, file=file) #size 추출

cv2.waitKey(0)
cv2.destroyAllWindows()