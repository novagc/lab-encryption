import base
import os
import random

class CaesarEncryptor(base.Base):
	def __init__(self, tag, p1, p2):
		self.__tag__ = tag
		self.__getConfig__(p1, p2)
		self.__key__ = int(self.__key__)

	@staticmethod
	def GenerateConfig(tag, p1, p2, key):
		with open(f'./{p1}.alph', 'w', encoding='utf-8') as file:
			file.write('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.!?;:\'" \n\t')

		with open(f'./{p2}.key', 'w', encoding='utf-8') as file:
			file.write(f'{tag}\n')
			file.write(str(key))

	def Encrypt(self, path):
		self.__validTxt__(path)

		with open(path, 'r', encoding='utf-8') as file:
			inputText = ''.join(file.readlines())
		
		with open('.'.join(path.split('.')[:-1] + ['encrypt']), 'w', encoding='utf-8') as file:
			file.write(f'{self.__tag__}\n')
			for x in inputText:
				file.write(self.__alp__[(self.__alp__.index(x) + self.__key__) % len(self.__alp__)])
	
	def Decrypt(self, path):
		self.__validEnc__(path)

		with open(path, 'r', encoding='utf-8') as file:
			if file.readline()[:-1] != self.__tag__:
				raise Exception('Данный файл зашифрован не шифром цезаря')

			inputText = ''.join(file.readlines())
		with open('.'.join(path.split('.')[:-1] + ['txt']), 'w', encoding='utf-8') as file:
			for x in inputText:
				file.write(
					self.__alp__[(self.__alp__.index(x) - self.__key__) % len(self.__alp__)])
