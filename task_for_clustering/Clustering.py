from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


data = pd.read_csv('/home/admin1/Downloads/machine_learning/task_for_clustering/datasets/Datasets/Radius-Queries.csv', header = None)


print(data.info())

print(data.head())

print(data.describe())

print(data.shape)

data.columns = ['X_coordinate', 'Y_coordinate', 'Radius']

print(data.head())

fig, ax = plt.subplots(figsize = (10, 5))
data.hist(ax = ax)
plt.show()


cor = data.corr()
ax = sb.heatmap(cor, annot = True)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)


# we can see that all the columns have very low correlation with each other but out of that column Radius has the least correlation

# Dropping the column Radius
data.drop(['Radius'], axis = 1, inplace = True)

#Taking only few samples of data for clustering
train_radius_queries = data.sample(frac = 0.2, random_state = 0)

print(train_radius_queries.shape)


# Clustering the crimes based on x coordinate, y coordinate and radius of the loaction to investigate number of crime incidents, the total arrests and the average beat of the disc region for the Radius Queries dataset 

# Applying Kmeans on the Radius-Queries dataset

wcss = [ ]
for i in range(1, 11):
    km = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    km.fit(train_radius_queries.values)
    wcss.append(km.inertia_)


fig, ax = plt.subplots(figsize = (10, 5))
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method', fontsize = 20)
plt.xlabel('No. of Clusters')
plt.ylabel('wcss')
plt.show()

km = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_means = km.fit_predict(train_radius_queries.values)


print(y_means)


# Visualising the Clusters


fig, ax = plt.subplots(figsize = (10, 8))

plt.scatter(train_radius_queries.values[y_means == 0, 0], train_radius_queries.values[y_means == 0,1], s = 100, c = 'red', label = 'Cluster 1')

plt.scatter(train_radius_queries.values[y_means == 1, 0], train_radius_queries.values[y_means == 1,1], s = 100, c = 'blue', label = 'Cluster 2')

plt.scatter(train_radius_queries.values[y_means == 2, 0], train_radius_queries.values[y_means == 2,1], s = 100, c = 'green', label = 'Cluster 3')

plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], s = 200, c = 'yellow', label = 'Centroid')

plt.legend()

plt.title('Clusters of crime', size = 20)

plt.xlabel('x coordinate ')

plt.ylabel('y coordinate')

plt.show()


# Applying Hierarchical Clustering on Radius Queries Dataset

fig, ax = plt.subplots(figsize = (20,8))
dendrogram(linkage(train_radius_queries,'ward'))
plt.show()


hc = AgglomerativeClustering(n_clusters = 2, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(train_radius_queries.values)


print(y_hc)


# # Radius Queries Count Dataset

df = pd.read_csv('/home/admin1/Downloads/machine_learning/task_for_clustering/datasets/Datasets/Radius-Queries-Count.csv',header = None)



print(df.head())


print(df.describe())


print(df.shape)


df.columns = ['X_coordinate', 'Y_coordinate', 'Radius', 'Count']


print(df.head())


print(df.info())


fig, ax = plt.subplots(figsize = (10, 5))
df.hist(ax = ax)
plt.show()


fig, ax = plt.subplots(figsize = (10, 5))
cor = df.corr()
ax = sb.heatmap(cor, annot = True)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)
plt.show()


# Clustering the crimes based on x coordinate, y coordinate, radius of the location and number of crime incidents  
# Applying Kmeans Clustering on Radius Queries Count Dataset

wcss = [ ]
for i in range(1, 11):
    km = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    km.fit(df.values)
    wcss.append(km.inertia_)


fig, ax = plt.subplots(figsize = (10, 5))
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method', fontsize = 20)
plt.xlabel('No. of Clusters')
plt.ylabel('wcss')
plt.show()


km_df = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_means_df = km_df.fit_predict(df.values)

print(y_means_df)

# Applying Hierarchical Clustering on Radius Queries Count Dataset

fig, ax = plt.subplots(figsize = (20,8))
dendrogram(linkage(df,'ward'))
plt.show()

hc_df = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
y_hc_df = hc_df.fit_predict(df.values)


# Clustering the crimes based on x, y coordinate, number of crime incidents, x range, y range, sum of arrests

# Range Queries Aggregates Dataset

dt = pd.read_csv('/home/admin1/Downloads/machine_learning/task_for_clustering/datasets/Datasets/Range-Queries-Aggregates.csv')

print(dt.head())

print(dt.info())

print(dt.shape)

dt.columns = ['ID', 'X_coordinate', 'Y_coordinate',  'X_range', 'Y_range', 'Count', 'SUM', 'AVG']

print(dt.head())

print(len(dt['ID'].unique()))

dt.drop(['ID','AVG',], axis = 1, inplace = True)


fig, ax = plt.subplots(figsize = (15, 8))
dt.hist(ax = ax)
plt.show()

fig, ax = plt.subplots(figsize = (10, 5))
cor = dt.corr()
ax = sb.heatmap(cor, annot = True)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)
plt.show()

#Taking only few samples of data to apply clustering
sample = dt.sample(frac = 0.05, random_state = 0)


print(sample.shape)


# Applying Kmeans Clustering on Range Queries Aggregates

wcss = [ ]
for i in range(1, 11):
    km = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    km.fit(sample.values)
    wcss.append(km.inertia_)


fig, ax = plt.subplots(figsize = (10, 5))
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method', fontsize = 20)
plt.xlabel('No. of Clusters')loaction
plt.ylabel('wcss')
plt.show()


km_sample = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_means_sample = km_sample.fit_predict(sample.values)

print(y_means_sample)


# Applying Hierarchical Clustering on Range Queries Aggregates
fig, ax = plt.subplots(figsize = (20,8))
dendrogram(linkage(sample,'ward'))
plt.show()


hc_sample = AgglomerativeClustering(n_clusters = 2, affinity = 'euclidean', linkage = 'ward')
y_hc_sample = hc_sample.fit_predict(sample.values)


print(y_hc_sample)
