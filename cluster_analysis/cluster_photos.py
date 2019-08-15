import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

photo_prefix = 'g:/My Drive/Photo_Backup/' #windows
#photo_prefix = '/g/My\ Drive/Photo_Backup/' #unix

res_enc = np.load(photo_prefix+'photo_enc_resnet50.npy')
photo_path = np.load(photo_prefix+'photo_path.npy')
print(photo_path)

df_path = pd.DataFrame({'path':photo_path})
df_enc = pd.DataFrame(data=res_enc)

print(df_path)
print(df_enc)

km4 = KMeans(n_clusters=4)
photo_pred4 = km4.fit_predict(df_enc)
print('Cluster %d - Inertia %f' % (4,km4.inertia_))

df_path_vec = df_path.merge(df_enc, left_index=True, right_index=True)
print(df_path_vec)
print(photo_pred4)

df_photo_pred = pd.DataFrame(photo_pred4)
print(df_photo_pred)

df_path_pred = df_path_vec.merge(df_photo_pred, left_index=True, right_index=True)
print(df_path_pred)

df_path_pred.to_csv('kmeans4_resnet50_res.csv')
