def drawGrid(canvas, fill="gray"):
	width = int(canvas['width'])
	height = int(canvas['height'])

	distance = 10
	nx = width / distance
	ny = height / distance

	ys = range(distance, height, distance)
	xs = range(distance, width, distance)
	# draw vertical lines (from top to bottom)
	for x in xs:
		y0 = 0
		y1 = height
		if x % (5 * distance) == 0:
			canvas.create_line(x, y0, x, y1, fill=fill)
			canvas.create_text(x + 15, 10, text="{0}".format(x), fill=fill)
		else:
			canvas.create_line(x, y0, x, y1, dash=(1, 3), fill=fill)

	# draw horizontal lines (from left to right)
	for y in ys:
		x0 = 0
		x1 = width
		if y % (5 * distance) == 0:
			canvas.create_line(x0, y, x1, y, fill=fill)
			canvas.create_text(x0 + 15, y - 7, text="{0}".format(y), fill=fill)
		else:
			canvas.create_line(x0, y, x1, y, dash=(1, 3), fill=fill)


def tkCoor(x0, y0, width, height):
	"""Tkinter using top left and bottom right point as coordinate. It is fairly difficult use.
	So here using different coordinate
		(x0, y0) is the center point.
		width is the radium in x axis
		height is the radium in y axis
	"""
	return x0 - width, y0 - width, x0 + width, y0 + height