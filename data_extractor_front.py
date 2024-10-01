from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic

import os 

class DataExtractorView(QMainWindow):
	def __init__(self):
		super(DataExtractorView, self).__init__()
		uic.loadUi("./data_extractor_front.ui", self)
		self.show()