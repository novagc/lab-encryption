import base
import os
import random

class PermutationsEncryptor(base.Base):
	def __init__(self, tag, p1, p2):
		self.__tag__ = tag
		self.__getConfig__(p1, p2)
		self.__key__ = list(map(int, self.__key__.split(';')))

	@staticmethod
	def GenerateConfig(tag, p1, p2, size):
		with open(f'./{p1}.alph', 'w', encoding='utf-8') as file:
			file.write('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.!?;:\'" \n\t')
		
		key = list(map(str, range(size)))
		random.shuffle(key)
		key = ';'.join(key)

		with open(f'./{p2}.key', 'w', encoding='utf-8') as file:
			file.write(f'{tag}\n')
			file.write(key)

	def Encrypt(self, path):
		self.__validTxt__(path)

		with open(path, 'r', encoding='utf-8') as file:
			inputText = [x for x in ''.join(file.readlines())]

		blockSize = len(self.__key__)
		textSize = len(inputText)
		
		dif = (textSize) % blockSize

		if dif != 0:
			for i in range(blockSize - dif):
				inputText += [self.__alp__[random.randint(0, len(self.__alp__) - 1)]]

			textSize = len(inputText)

		with open('.'.join(path.split('.')[:-1] + ['encrypt']), 'w', encoding='utf-8') as file:
			file.write(f'{self.__tag__}\n')
			file.write(f'{blockSize - dif}\n')

			for i in range(textSize // blockSize):
				string = inputText[i * blockSize: i * blockSize + blockSize]

				for j in range(blockSize):
					file.write(string[self.__key__[j]])

	def Decrypt(self, path):
		self.__validEnc__(path)

		with open(path, 'r', encoding='utf-8') as file:
			if file.readline()[:-1] != self.__tag__:
				raise Exception('Данный файл зашифрован не шифром перестановки')

			dif = int(file.readline()[:-1])
			inputText = [x for x in ''.join(file.readlines())]

		block = [[x, i] for i, x in enumerate(self.__key__)]
		block.sort(key=lambda x: x[0])

		blockSize = len(self.__key__)
		textSize = len(inputText)

		temp = [''] * textSize

		with open('.'.join(path.split('.')[:-1] + ['txt']), 'w', encoding='utf-8') as file:
			for i in range(textSize // blockSize):
				string = inputText[i * blockSize: i * blockSize + blockSize]
				for j in range(blockSize):
					temp[i * blockSize + j] = string[block[j][1]]
			file.write(''.join(temp[:-1 * dif]))
			
