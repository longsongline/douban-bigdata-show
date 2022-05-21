import pandas as pd
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.load('population.npz', allow_pickle=True)
# print(data.files)
# print(data['data'])
# print(data['feature_names'])
print(data['data'])
plt.rcParams['font.sans-serif'] = 'SimHei'
name = data['feature_names']
values = data['data']

def function(data):
    from mpl_toolkits.mplot3d import Axes3D

    #print(dims, types)
    flg=plt.figure()
    ax=Axes3D(flg)
    o = 0

    lei = ["nan","nv","cheng","nong"]
    for i in range(4):
        x = []
        y = []
        z = []
        for j in range(20):
            print(data['data'][j][0][:4])
            x.append(int(data['data'][j][0][:4]))
            y.append(int(data['data'][j][i + 2]))
            z.append(i)
        ax.scatter(x, z, y, label=lei[i])
    # for iris_type in types:
    #     o = o + 1
    #     tmp_data=iris_data[iris_data.species ==iris_type]
    #     x,y,z = tmp_data[dims['x']], tmp_data[dims['z']],tmp_data[dims['z']]
    #     x = y =z =[1+o,2+o,3+o,4+o,5+o]
    #     ax.scatter(x, y, z, label=o)
    # print(type(tmp_data[dims['z']]))
    ax.legend(loc='upper left')
    ax.set_zlabel('renshu')
    ax.set_xlabel('nianfen')
    ax.set_ylabel('leibie')

    plt.show()

if __name__ == '__main__':
    function(data)

