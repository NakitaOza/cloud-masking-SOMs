#Training the SOM
# The susi package needs to be installed. It can be found in https://pypi.org/project/susi/

import susi 
from data_preprocessing import X_train
import pickle
#n_iter_unsupervised: number of iterations
#n_rows: rows of the SOM grid
#n_columns: columns of the SOM grid

som = susi.SOMClustering(n_iter_unsupervised=1000000, n_rows=20, n_columns=15)
som.fit(X_train)

#export the trained SOM 
with open('SOM_trained.p', 'wb') as outfile:
    pickle.dump(som, outfile)

#load the trained SOM
with open('SOM_trained.p', 'rb') as infile:
   som = pickle.load(infile)


