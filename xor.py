import base
import os
import random

from operator import xor

class XOREncryptor(base.Base):
	def __init__(self, tag, p1, p2):
		self.__tag__ = tag
		self.__getConfig__(p1, p2)
		self.__key__ = list(map(int, self.__key__.split(';')))

	@staticmethod
	def GenerateConfig(tag, p1, size):
		key = ';'.join([str(random.randint(0, 100000)) for i in range(size)])

		with open(f'./{p1}.key', 'w', encoding='utf-8') as file:
			file.write(f'{tag}\n')
			file.write(key)

	def Encrypt(self, path):
		self.__validTxt__(path)

		with open(path, 'r', encoding='utf-8') as file:
			inputText = ''.join(file.readlines())

		with open('.'.join(path.split('.')[:-1] + ['encrypt']), 'w', encoding='utf-8') as file:
			file.write(f'{self.__tag__}\n')
			for i, x in enumerate(inputText):
				file.write(chr(xor(ord(x), self.__key__[i % len(self.__key__)])))

	def Decrypt(self, path):
		self.__validEnc__(path)

		with open(path, 'r', encoding='utf-8') as file:
			if file.readline()[:-1] != self.__tag__:
				raise Exception('Данный файл зашифрован не шифром перестановки')
			inputText = ''.join(file.readlines())

		with open('.'.join(path.split('.')[:-1] + ['txt']), 'w', encoding='utf-8') as file:
			for i, x in enumerate(inputText):
				file.write(chr(xor(ord(x), self.__key__[i % len(self.__key__)])))
