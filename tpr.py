from scipy.spatial.distance import mahalanobis as mlnbs_dist

import numpy as np
import sys

class NNMDetector:
    def __init__(self, train_data):
        print "td", train_data
        sys.stdout.flush()
        self.train_data = train_data
        self.cov_mat = np.cov(np.transpose(train_data))

    def anomaly_score(self, test_vector):
        print self.cov_mat
        sys.stdout.flush()
        mlnbs_dists = []
        for timing_vector in self.train_data:
            mlnbs_dists.append(mlnbs_dist(timing_vector, test_vector, self.cov_mat))

        return min(mlnbs_dists)