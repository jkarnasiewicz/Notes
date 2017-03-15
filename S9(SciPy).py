# Numpy

np.show_config()
np.arange(3, 17, 3)
np.average([[1, 2, 3], [4, 5, 6], [7, 8, 9]], axis=1)
np.average([[1, 2, 3], [4, 5, 6]], weights=[1, 2, 3], axis=1)
np.dot([1, 3], [5, 7])

np.reshape([[1, 3, 5], [7, 9, 11]], [3, 2])
np.linalg.norm([1, 1, 1])


import numpy as np
# the core functionality of NumPy is the ndarray class, a multidimensional (n-dimensional) array
x = np.array([[1, 2, 3], [4, 5, 6]])
print("x:\n{}".format(x))










# Matplotlib

# Basic usage
import matplotlib.pyplot as plt
from matplotlib import style
style.use('bmh')
print(style.available)

plt.plot([1, 3, 5], [11, 33, 55])                                                   # line
plt.scatter([2, 7, 14], [-11, 3, 27], s=12, color='magenta', linewidths=5)          # dot
plt.show()



# 
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()



# Generate a sequence of numbers from -10 to 10 with 100 steps in between
x = np.linspace(-10, 10, 100)
# Create a second array using sine
y = np.sin(x)
# The plot function makes a line chart of one array against another
plt.plot(x, y, marker="x")
plt.show()


# 3D plot
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([1, 3, 5], [10, 20, 30], [11, 23, 35], c='magenta', marker='x')
plt.show()










# Pandas

from pandas import DataFrame as df
# create a simple dataset of people
data = {'Name': ["John", "Anna", "Peter", "Linda"],
        'Location' : ["New York", "Paris", "Berlin", "London"],
        'Age' : [24, 13, 53, 33]
}
data_pandas = df(data)
print(data_pandas)
# select all rows that have an age column greater than 30
print(data_pandas[data_pandas.Age > 30])










# Scikit-learn

# X - features, y - labels(possible outputs called classes)
# The individual items are called samples in machine learning, and their properties are called features
# The shape of the data array is the number of samples multiplied by the number of features
# dataset['data'].shape
import numpy as np
from sklearn.datasets import load_iris
iris_dataset = load_iris()
print(iris_dataset.keys(), iris_dataset['feature_names'], iris_dataset['target_names'], iris_dataset['data'].shape)



# training data and test data
# One part of the data is used to build our machine learning model, and is called the training data or training set
# The rest of the data will be used to assess how well the model works, this is called the test data
# We cannot use the data we used to build the model to evaluate it. This is because our model can always
# simply remember the whole training set

# train_test_split (shuffles the dataset and splits it)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)



# k-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)

# build the model using training set
knn.fit(X_train, y_train)

# making predictions
X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_new)

print("Predicted target name: {}".format(iris_dataset['target_names'][prediction]))



# model evaluation(oszacowanie)/compute the test set accuracy
# we can measure how well the model works by computing the accuracy(dokładność, trafność) on test_data(X_test)
accuracy = knn.score(X_test, y_test)
print("Test set score: {:.2f}".format(accuracy))










# Mean Shift
import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style
style.use("ggplot")

centers = [[1, 1, 1], [5, 5, 5], [3, 10, 10]]

X, _ = make_blobs(n_samples = 10, centers = centers, cluster_std = 1.5)

ms = MeanShift()
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

print(cluster_centers)
n_clusters_ = len(np.unique(labels))
print("Number of estimated clusters:", n_clusters_)

colors = 10*['r','g','b','c','k','y','m']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(X)):
    ax.scatter(X[i][0], X[i][1], c=colors[labels[i]], marker='o')

ax.scatter(cluster_centers[:,0],cluster_centers[:,1],
            marker="x",color='k', s=150, linewidths = 5, zorder=10)

plt.show()










# Machine Learning

# quandl / http://archive.ics.uci.edu/ml/datasets.html

# Supervised learning(we told/train machine what the classes of features are)
# Linear Regression(Regresja liniowa)(best fitting line)/Coefficient of determination(Współczynnik determinacji)
# Classification k-Nearest Neighbors(not scaling well)/Accuracy(dokładność/trafność)
# Classification Support Vector Machine(SVM)/Best separated hyperplane/Convex optimization problem/Kernels/RBF(Radial basic function)

# Unsupervised learning
# Clustering K-Means (Flat)/ we want k-clusters/groups
# Clustering Mean Shift (Hierarchical)/ machine/model try to figure the amount of clusters / radius and weighted mean

# Deep learning Neural networks / TensorFlow / TFLearn(higher-level API for TensorFlow)
'''
input > weight > hidden layer 1 (activation function) > weight > hidden layer 2 (activation function) > weight > output layer

comapre output to intended output > cost function(cross entropy)
optimization function (optimizer) > minimize cost (AdamOptimizer.....SGD, AdaGrad)

backpropagation

feed forward + backpropagation = epoch/one cycle
'''

# Recurrent Neural Network(RNN) with LSTM (Long Short Term Memory) (remember or feed output recurrently in to nodes)
# Convolutional Neural Networks / input => (Convolution => Pooling) Hidden Layer => Fully Connected => Output










# ===========================
matplotlib.rc('font', family='Helvetica')
matplotlib.rcParams['svg.fonttype'] = 'none'
pylab.rc('text', usetex=True)
pylab.rc('text.latex',unicode=True)
pylab.rc('text.latex',preamble='\usepackage[T1]{polski}')


# ===========================
@login_required
def draw_file(request):
    file_id = request.GET.getlist('id', None)
    exp_id = request.GET.get('exp_id', None)
    extension = str(request.GET.get('extension', None))
    print(type(extension))
    if(len(file_id) != 1):
        messages.info(request, _('Please check one file to draw.'))
        return redirect('management', exp_id=exp_id)
    else:
        import matplotlib
        matplotlib.use('Agg')
        matplotlib.rc('font', family='DejaVu Sans')
        import matplotlib.pyplot as plt
        plt.style.use('bmh')
        obj = get_object_or_404(SpinLabFile, pk=file_id[0])
        obj_type = obj.experiment_type
        fig = plt.figure()
        plt.xlabel(_('Wavelenght/nm'), fontsize=18)
        plt.ylabel(_('Counts/$10^6$'), fontsize=18)
        plt.title(obj.name+' : '+obj.get_experiment_type_display())
        file_content = obj.file_txt.read()
        file_con_list = file_content.splitlines()
        output = StringIO.StringIO()
        date = datetime.now()
        date_string = '{}/{}/{}'.format(date.day, date.month, date.year)
        if(obj_type in ['EmF', 'ExF', 'DTF']):
            empty_index = file_con_list.index('')+1
            data_x = []
            data_y = []
            for line in file_con_list[empty_index:]:
                row = line.split(',')
                try:
                    data_x.append(row[0])
                    data_y.append(row[1])
                except IndexError:
                    pass
            y = 0.875
            if(obj_type == 'EmF'):
                fields = obj.get_fields_for_emission_file
            elif(obj_type == 'ExF'):
                fields = obj.get_fields_for_excitation_file
            else:
                fields = obj.get_fields_for_decay_time_file
            for i in fields():
                text = u'{} - {}'.format(i[0], i[1])
                a = plt.figtext(0.91, y, text)
                y = y - 0.025
            ax = fig.add_subplot(111)
            ax.plot(data_x, data_y, label=obj.name)
            # d = ax.legend(loc='upper left', bbox_to_anchor=(1, 1),
            #               ncol=1, fancybox=True, shadow=True)
            plt.figtext(1.125, 0, date_string)
            print(ax.get_position().width)
            fig.savefig(output, format=extension,
                        bbox_inches='tight')
                        # bbox_extra_artists=(d, a))
        else:
            label_row = file_con_list[file_con_list.index('')+1]
            label_list = label_row.split(',')[1:-1]
            count_of_sample = len(label_list)
            start_index = file_con_list[2:].index('')+3
            y = 0.875
            if(obj_type == 'EmMF'):
                fields = obj.get_fields_for_emission_map_file()
            else:
                fields = obj.get_fields_for_decay_time_map_file()
            for i in fields:
                text = u'{} - {}'.format(i[0], i[1])
                a = plt.figtext(0.91, y, text)
                y = y - 0.025
            for i in range(count_of_sample):
                data_x = []
                data_y = []
                for line in file_con_list[start_index:]:
                    row = line.split(',')
                    try:
                        data_x.append(row[0])
                        data_y.append(row[i+1])
                    except IndexError:
                        pass
                ax = fig.add_subplot(111)
                ax.plot(data_x, data_y)
            plt.figtext(1.125, 0, date_string)
            fig.savefig(output, format=extension, bbox_inches='tight')
    plt.clf()
    plt.close()
    response = HttpResponse(mimetype='application/force-download')
    response['Content-Disposition'] = ('attachment; filename={}'
                                       .format(obj.name+'.'+str(extension)))
    response.write(output.getvalue())
    return response


# ===========================
ab = AnnotationBbox(imagebox, xy,
                    xybox=(120., -80.),
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0.5
                    )

ab = AnnotationBbox(imagebox, xy,
                    xybox=(120., -80.),
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0.5,
                    arrowprops=dict(arrowstyle="->",
                                    connectionstyle="angle,angleA=0,angleB=90,rad=3")
                    )


# ===========================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig = plt.figure()
plt.xlabel('X.....')
plt.ylabel('Y.....')
plt.title('Title')
a = plt.figtext(0.91, 0.550, 'isasdasdasdwerwerw')
b = plt.figtext(0.91, 0.525, 'forqweqwrwerwer')
c = plt.figtext(0.91, 0.5, 'foowerwerwerwer')
ax = fig.add_subplot(111)
ax.plot([100, 500, 1000], [10, 20, 300], label='$y = x')
ax = fig.add_subplot(111)
ax.plot([100, 500, 1000], [50, 100, 150], label='$y = x')
ax = fig.add_subplot(111)
ax.plot([100, 500, 1000], [500, 750, 1000], label='$y = x')
ax.text(0.5, 0.5, 'right top',
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)
d = ax.legend(loc='upper left', bbox_to_anchor=(1, 1),
          ncol=1, fancybox=True, shadow=True)
fig.savefig('test.svg', bbox_inches='tight', bbox_extra_artists=(d, a, b, c))


# ===========================
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, prop={'size': 6},
           borderaxespad=0.)
plt.legend(prop={'size': 6}, borderaxespad=0.)


# ===========================
plt.yscale('log', nonposy='clip/mask')





# Anchored Box
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredOffsetbox, TextArea, DrawingArea, HPacker

fig=plt.figure(1, figsize=(3,3))
ax = plt.subplot(111)

box1 = TextArea(" Test : ", textprops=dict(color="k"))

box2 = DrawingArea(60, 20, 0, 0)
el1 = Ellipse((10, 10), width=16, height=5, angle=30, fc="r")
el2 = Ellipse((30, 10), width=16, height=5, angle=170, fc="g") 
el3 = Ellipse((50, 10), width=16, height=5, angle=230, fc="b") 
box2.add_artist(el1)
box2.add_artist(el2)
box2.add_artist(el3)


box = HPacker(children=[box1, box2],
              align="center",
              pad=0, sep=5)

anchored_box = AnchoredOffsetbox(loc=3,
                                 child=box, pad=0.,
                                 frameon=True,
                                 bbox_to_anchor=(0., 1.02),
                                 bbox_transform=ax.transAxes,
                                 borderpad=0.,
                                 )


ax.add_artist(anchored_box)

fig.subplots_adjust(top=0.8)
plt.show()






# This illustrates placing images directly in the figure, with no axes
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


fig = plt.figure()
Z = np.arange(10000.0)
Z.shape = 100,100
Z[:,50:] = 1.

im1 = plt.figimage(Z, xo=50, yo=0, cmap=cm.jet, origin='lower')
im2 = plt.figimage(Z, xo=100, yo=100, alpha=.8, cmap=cm.jet, origin='lower')

plt.show()

# ===============================

# styles = ['bmh', 'classic', 'dark_background', 'fivethirtyeight', 'ggplot', 'grayscale',
#  'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark',
#  'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
#  'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn']

# plt.figure(figsize=(15, 10), dpi=300)
# plt.savefig(f, format=self.extension, facecolor=(0.95, 0.95, 0.95))
# df = pd.DataFrame(data=np.array(list(zip(r, y)), dtype='int64'), columns=['X', 'Y'])

# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radiuses
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
