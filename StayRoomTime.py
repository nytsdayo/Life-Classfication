from tensorflow import keras
from tensorflow.keras.preprocessing.image import array_to_img, img_to_array, load_img, ImageDataGenerator
import numpy as np
import os
model = keras.models.load_model("Models\使用するモデル名")
datagen = ImageDataGenerator(rescale=1./255)
directory='Data/TodayDate/' #TodayDateば今日の日付をyyyymmddで入力する
dirlist = os.listdir(directory)
dirlist=sorted(dirlist)
list_time=[]
for filename in dirlist:
  if filename.endswith(".jpg") or filename.endswith(".png"):

    filepath = os.path.join(directory,filename)
    print(filepath)
    img = load_img(filepath, target_size=(128, 128))  # モデルの入力サイズに合わせる
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # バッチの次元を追加

    # ImageDataGeneratorで前処理
    img_array = datagen.standardize(img_array)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)
    #推論値の表示
    print(predicted_class)
    list_time.append([predicted_class,filename])

last = -10
for i in range(len(list_time)-1):
  if list_time[i][0]!=list_time[i+1][0]:
    #if i-last<=5:
    #  continue
    last=i
    if list_time[i][0]==0:
      print("外出：",)
    else:
      print("帰宅：")
    print(list_time[i][1][8:-6])