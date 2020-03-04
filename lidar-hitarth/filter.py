import numpy as np

class RangeFilter(object):


	def __init__(self, range_min, range_max):

		self.range_min = range_min
		self.range_max = range_max

	def update(self, lidar_data):

		filter_data = np.array(lidar_data)
		filter_data[filter_data<self.range_min] = self.range_min
		filter_data[filter_data>self.range_max] = self.range_max
		return list(filter_data)

class TemporalFilter(object):

	def __init__(self, D, N):


		self.D = D
		self.i = 0
		self.filter_data = np.zeros([D+1,N])

	def update(self, lidar_data):

		self.filter_data[1:,:] = self.filter_data[:-1,:]
		self.filter_data[0,:] = np.array(lidar_data)
		if (self.i < self.D):
			self.i = self.i + 1
			return list(np.median(self.filter_data[:self.i,:], axis=0))
		else:
			return list(np.median(self.filter_data, axis=0))
