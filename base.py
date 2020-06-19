import os

class Base:
	def __init__(self, tag, p1, p2):
		self.__tag__ = tag
		self.__key__ = '1'

	def Encrypt(self):
		pass
	
	def Decrypt(self):
		pass

	def __isKey__(self, p):
		return p.split('.')[-1] == 'key'

	def __isAlph__(self, p):
		return p.split('.')[-1] == 'alph'

	def __isTxt__(self, p):
		return p.split('.')[-1] == 'txt'

	def __isEnc__(self, p):
		return p.split('.')[-1] == 'encrypt'

	def __validTxt__(self, p):
		if not self.__isTxt__(p):
			raise Exception('Это не текстовый файл')

		if not os.path.exists(p):
			raise Exception('Текстового файла не существует')

	def __validEnc__(self, p): 
		if not self.__isEnc__(p):
			raise Exception('Это не зашифрованный файл')

		if not os.path.exists(p):
			raise Exception('Текстового файла не существует')

	def __getConfig__(self, p1, p2):
		if not self.__isAlph__(p1):
			raise Exception('Файл алфавита недействительный')

		if not self.__isKey__(p2):
			raise Exception('Файл ключа недействительный')

		if not os.path.exists(p1):
			raise Exception('Файла алфавита не существует')

		with open(p1, 'r', encoding='utf-8') as file:
				self.__alp__ = ''.join(file.readlines())

		if not os.path.exists(p2):
			raise Exception('Файла ключа не существует')

		with open(p2, 'r', encoding='utf-8') as file:
			if file.readline()[:-1] != self.__tag__:
				raise Exception('Данный ключ используется не для данного типа шифрования')

			self.__key__ = file.readline()

	def SetKey(self, key):
		self.__key__ = key

	def GetKey(self):
		return self.__key__

	def SetAlph(self, alph):
		self.__alp__ = alph

	def GetAlph(self):
		return self.__alp__
