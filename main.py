import os
import caesar
import permutations
import xor

cTag = 'c'
pTag = 'p'
xTag = 'x'

def PrintGenerateDialog():
	os.system('cls||clear')
	com = input('Выберите вид шифрования, для которого генерировать конфиг:\n\t1) Замена\n\t2) Перестановка\n\t3) Гаммирование\n')

	if com == '1':
		caesar.CaesarEncryptor.GenerateConfig(
			cTag, 
			input('Имя файла алфавита: '), 
			input('Имя файла ключа: '),
			int(input('Ключ (смещение): '))
			)
	elif com == '2':
		permutations.PermutationsEncryptor.GenerateConfig(
			pTag,
			input('Имя файла алфавита: '),
			input('Имя файла ключа: '),
			int(input('Размер блока перестановки: '))
		)
	else:
		xor.XOREncryptor.GenerateConfig(
			xTag,
			input('Имя файла ключа: '),
			int(input('Размер гамма-последовательности: '))
		)


def PrintEDDialog():
	os.system('cls||clear')
	com = input('Выберите вид шифрования:\n\t1) Зашифровать\n\t2) Расшифровать\n')#input('Выберите вид шифрования:\n\t1) Замена\n\t2) Перестановка\n\t3) Гаммирование\n')
	if com == '1':
		PrintEDialog()
	else:
		PrintDDialog()


def PrintEDialog():
	os.system('cls||clear')
	com = input('Выберите вид шифрования:\n\t1) Замена\n\t2) Перестановка\n\t3) Гаммирование\n')
	if com == '1':
		enc = caesar.CaesarEncryptor(
			cTag, 
			input('Путь до файла алфавита: '),
			input('Путь до файла ключа: ')
			)
		enc.Encrypt(input('Путь до текстового файла: '))
	elif com == '2':
		enc = permutations.PermutationsEncryptor(
				pTag,
				input('Путь до файла алфавита: '),
				input('Путь до файла ключа: ')
			)
		enc.Encrypt(input('Путь до текстового файла: '))
	else:
		enc = xor.XOREncryptor(
				xTag,
				input('Путь до файла алфавита: '),
				input('Путь до файла ключа: ')
			)
		enc.Encrypt(input('Путь до текстового файла: '))


def PrintDDialog():
	os.system('cls||clear')
	com = input('Выберите вид шифрования:\n\t1) Замена\n\t2) Перестановка\n\t3) Гаммирование\n')
	if com == '1':
		enc = caesar.CaesarEncryptor(
				cTag,
				input('Путь до файла алфавита: '),
				input('Путь до файла ключа: ')
			)
		enc.Decrypt(input('Путь до зашифрованного файла: '))
	elif com == '2':
		enc = permutations.PermutationsEncryptor(
				pTag,
				input('Путь до файла алфавита: '),
				input('Путь до файла ключа: ')
			)
		enc.Decrypt(input('Путь до зашифрованного файла: '))
	else:
		enc = xor.XOREncryptor(
				xTag,
				input('Путь до файла алфавита: '),
				input('Путь до файла ключа: ')
			)
		enc.Decrypt(input('Путь до зашифрованного файла: '))


def PrintMain():
	os.system('cls||clear')
	com = input('Главное меню:\n\t1) Зашифровать/Расшифровать\n\t2) Сгенерировать ключ\n')

	if com == '1':
		PrintEDDialog()
	else:
		PrintGenerateDialog()

try:
	PrintMain()
except Exception as e:
	print(e)