import graphics as gr

def matryoshka(n):
	if n == 1:
		print('Матрёшечка')
	else:
		print('Верх матрёшки n = ', n)
		matryoshka(n-1)
		print('Низ матрёшки n = ', n)


window = gr.GraphWin('Russian game', 600, 600)

def fractal_rectangle():
	pass



matryoshka(5)
