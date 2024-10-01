from data_extractor_front import DataExtractorView


 
class DataExtractorController:
	def __init__(self):
		self.frontend = DataExtractorView()
		self.connect_widgets()


	def connect_widgets(self):
		self.frontend.browse_button.clicked.connect(self.run_process)


	def run_process(self):
		"""
		1) Dans le front elle va afficher le QFileDialog # Done
		2) Reccupère de chemin de l'image
		3) Elle envoie le chemin de l'image au backend
		4) Le backend utilise l'api pour recevoir le json
		5) On envoie le json au frontend pour l'affichage
		"""
		document_name = self.frontend.browse_file()
		print(document_name)