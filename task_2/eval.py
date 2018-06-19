#
# File to do the actual evaluation, will compare a ground truth data to a set of results
# and output some info on how well it worked
#
#	SD, 2018/06/18		Initial effort
#

def Intersection(box_a, box_b):
	intersection = {}
	intersection['left'] = min(box_a['left'], box_b['left'])
	intersection['top'] = min(box_a['top'], box_b['top'])
	intersection['bottom'] = max(box_a['bottom'], box_b['bottom'])
	intersection['right'] = max(box_a['right'], box_b['right'])

def Area(box):
	if((box['left'] > box['right']) | (box['top'] > box['bottom'])):
		return 0
	else:	
		return (box['right'] - box['left'] + 1)*(box['bottom'] - box['top'] + 1)

def IoU(box_a, box_b):
	intsect = Area(Intersection(box_a, box_b))
	return (intsect/(Area(box_a) + Area(box_b) - intersect))