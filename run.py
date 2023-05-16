def run(media_folder, extension_folder, app):
	"""
	Run extension speech_train
	Parameters
	----------
	media_folder: path to media folder to save files
	extension_folder: path to extension folder where run.py file
	app

	Returns
	-------

	"""
	import os
	import sys
	import time
	sys.path.insert(0, extension_folder)

	import random
	import torch
	import yaml
	import glob
	import json
	from time import gmtime, strftime
	from flask_cors import cross_origin
	from flask import request
	from tacotron2.train import main as tacotron2
	from waveglow.train import main as waveglow

	sys.path.pop(0)

	save_train_voice_folder = os.path.join(media_folder, 'user_trained_voice')
	if not os.path.exists(save_train_voice_folder):
		os.makedirs(save_train_voice_folder)

	def current_time(format: str = None):
		if format:
			return strftime(format, gmtime())
		return strftime("%Y%m%d%H%M%S", gmtime())

	def clear_memory():
		app.config['models'] = []
		torch.cuda.empty_cache()
		time.sleep(10)
		torch.cuda.empty_cache()
		return {"status": 200}

	@app.route('/change_processor', methods=["POST"])
	@cross_origin()
	def change_processor():
		current_processor = os.environ.get('WUNJO_TORCH_DEVICE', "cpu")
		if app.config['SYSNTHESIZE_STATUS'].get("status_code") == 200:
			if current_processor == "cpu":
				os.environ['WUNJO_TORCH_DEVICE'] = 'cuda'
				return {"current_processor": 'cuda'}
			else:
				os.environ['WUNJO_TORCH_DEVICE'] = 'cpu'
				return {"current_processor": 'cpu'}
		return {"current_processor": current_processor}

	# :TODO install modules
	# :TODO if modules exist when this method add
	@staticmethod
	def tacotron2_train(hparams_path):
		tacotron2(hparams_path=hparams_path)
		return

	@staticmethod
	def waveglow_train(json_config):
		waveglow(json_config=json_config)
		return

	@app.route('/tacotron2/', methods=["POST"])
	@cross_origin()
	def tacotron2_run():
		if app.config['SYSNTHESIZE_STATUS']["status_code"] != 200:
			return {"status_code": 200}

		clear_memory()

		request_list = request.get_json()
		app.config['SYSNTHESIZE_STATUS'] = {"status_code": 400, "message": "Происходит обучение модели Tacotron2"}

		checkpoint_file = request_list.get("checkpoint")
		audio_path = request_list.get("audio_path")
		mark_file = request_list.get("mark_path")
		charset = request_list.get("language")
		train_split = int(request_list.get("train_split"))
		tacotron2_config = request_list.get("config")
		tacotron2_config = yaml.safe_load(tacotron2_config)

		if checkpoint_file:
			if not os.path.isfile(checkpoint_file):
				# User set path to checkpoint file but this doesn't exist
				app.config['SYSNTHESIZE_STATUS'] = {"status_code": 200, "message": "Не найден checkpoint файл"}
				return {"status_code": 200}
		else:
			checkpoint_file = None

		if not audio_path or not mark_file:
			# User not set paths
			app.config['SYSNTHESIZE_STATUS'] = {"status_code": 200,
												"message": "Директория аудио или путь к разметке не установлены"}
			return {"status_code": 200}

		if not os.path.isdir(audio_path) or not os.path.isfile(mark_file):
			# Audio path is not path or mark is not file
			app.config['SYSNTHESIZE_STATUS'] = {"status_code": 200, "message": "Директория аудио не найдена или не найден файл разметки"}
			return {"status_code": 200}

		dir_time = current_time()
		train_folder = os.path.join(save_train_voice_folder, dir_time)

		if not os.path.exists(train_folder):
			os.makedirs(train_folder)

		with open(mark_file, "r", encoding="utf-8") as file:
			mark_lines = file.readlines()
		random.shuffle(mark_lines)  # random shuffle list

		len_mark_lines = len(mark_lines)
		train_size = int(len_mark_lines * (train_split / 100))

		mark_test = mark_lines[train_size:]
		validation_files = os.path.join(train_folder, "mark_test.txt")
		with open(validation_files, "w") as file:
			file.writelines(mark_test)  # because elements has \n

		mark_train = mark_lines[:train_size]
		training_files = os.path.join(train_folder, "mark_train.txt")
		with open(training_files, "w") as file:
			file.writelines(mark_train)  # because elements has \n

		# todo set absolute path
		tacotron2_config["audios_path"] = audio_path
		tacotron2_config["training_files"] = training_files
		tacotron2_config["validation_files"] = validation_files
		tacotron2_config["output_dir"] = train_folder
		tacotron2_config["charset"] = charset
		tacotron2_config["checkpoint"] = checkpoint_file

		new_yaml_path = os.path.join(train_folder, "config")
		if not os.path.exists(new_yaml_path):
			os.makedirs(new_yaml_path)

		new_yaml_file_path = os.path.join(new_yaml_path, "hparams.yaml")
		with open(new_yaml_file_path, "w") as file:
			yaml.dump(tacotron2_config, file)

		# delete tts models from memory
		app.config['models'] = {}
		torch.cuda.empty_cache()
		# start train
		try:
			tacotron2_train(hparams_path=new_yaml_file_path)
		except:
			app.config['SYSNTHESIZE_STATUS'] = {"status_code": 200, "message": "Недостаточно памяти графического процессора. Увеличьте размер памяти"}
			return {"status_code": 400}

		app.config['SYSNTHESIZE_STATUS'] = {"status_code": 200, "message": ""}

		return {"status_code": 200}

	@app.route('/waveglow/', methods=["POST"])
	@cross_origin()
	def waveglow_run():
		if app.config['SYSNTHESIZE_STATUS']["status_code"] != 200:
			return {"status_code": 200}

		clear_memory()

		request_list = request.get_json()
		app.config['SYSNTHESIZE_STATUS'] = {"status_code": 400, "message": "Происходит обучение модели Waveglow"}
		audio_path = request_list.get("audio_path")
		train_split = int(request_list.get("train_split"))

		if not audio_path:
			# User not set paths
			app.config['SYSNTHESIZE_STATUS'] = {"status_code": 200, "message": "Директория аудио не установлена"}
			return {"status_code": 200}

		if not os.path.isdir(audio_path):
			# Audio path is not path or mark is not file
			app.config['SYSNTHESIZE_STATUS'] = {"status_code": 200, "message": "Директория аудио не найдена или не найден файл разметки"}
			return {"status_code": 200}

		audio_list = glob.glob(os.path.join(audio_path, "*.wav"))
		len_audio_list = len(audio_list)
		train_size = int(len_audio_list * (train_split / 100))

		dir_time = current_time()
		train_folder = os.path.join(save_train_voice_folder, dir_time)

		if not os.path.exists(train_folder):
			os.makedirs(train_folder)

		random.shuffle(audio_list)  # random shuffle list

		mark_test = audio_list[train_size:]
		validation_files = os.path.join(train_folder, "test_file.txt")
		with open(validation_files, "w") as file:
			for item in mark_test:
				file.write(item + "\n")

		mark_train = audio_list[:train_size]
		training_files = os.path.join(train_folder, "train_file.txt")
		with open(training_files, "w") as file:
			for item in mark_train:
				file.write(item + "\n")

		waveglow_config = request_list.get("config")
		waveglow_config = json.loads(waveglow_config)

		waveglow_config["train_config"]["output_directory"] = train_folder
		waveglow_config["data_config"]["training_files"] = training_files

		new_json_path = os.path.join(train_folder, "config")
		if not os.path.exists(new_json_path):
			os.makedirs(new_json_path)

		new_json_file_path = os.path.join(new_json_path, "config.json")
		with open(new_json_file_path, "w") as file:
			json.dump(waveglow_config, file)

		# delete tts models from memory
		app.config['models'] = {}
		torch.cuda.empty_cache()
		# start train
		try:
			waveglow_train(json_config=new_json_file_path)
		except:
			app.config['SYSNTHESIZE_STATUS'] = {"status_code": 200, "message": "Недостаточно памяти графического процессора. Увеличьте размер памяти"}
			return {"status_code": 400}

		app.config['SYSNTHESIZE_STATUS'] = {"status_code": 200, "message": ""}

		return {"status_code": 200}

	sys.path.pop(0)
