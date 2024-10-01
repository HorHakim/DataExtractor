from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic
import json

import os 

class DataExtractorView(QMainWindow):
	def __init__(self):
		super(DataExtractorView, self).__init__()
		uic.loadUi("./data_extractor_front.ui", self)
		self.show()


	def browse_file(self):
		document_path, _ = QFileDialog.getOpenFileName(self, "Selectionnez une facture")
		return document_path

	def show_output_information(self, document_json):

		document_dict = json.loads(document_json)
		ouput_message = []
		
		for key, value in document_dict.items():
			ouput_message.append(f"{key} : {value}")

		self.output_text.setPlainText("\n".join(ouput_message))