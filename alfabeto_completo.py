import numpy as np

alfabeto_completo =['A','A','A','A','A','A','A','A','A','A','A','A','A','A',
			'B','B','B',
			'C','C','C','C','C','C',
			'D','D','D',
			'E','E','E','E','E','E','E','E','E','E','E',
			'F','F','F',
			'G','G',
			'H','H',
			'I','I','I','I','I','I','I','I','I','I','I','I',
			'L','L','L','L','L',
			'M','M','M','M','M',
			'N','N','N','N','N',
			'O','O','O','O','O','O','O','O','O','O','O','O','O','O','O',
			'P','P','P',
			'Q',
			'R','R','R','R','R','R',
			'S','S','S','S','S','S',
			'T','T','T','T','T','T',
			'U','U','U','U','U',
			'V','V','V',
			'Z','Z',
			'J','J']

filename = 'alfabeto.npy'
np.save(filename,alfabeto_completo)
