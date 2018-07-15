#
# File to load ground truth data for Task 2 of the Semantic Search challenge 
#
#	SD,	2018/06/16, 	Initial effort
#	SD, 2018/06/18		Flieshed it out
#

import xml.etree.ElementTree as ET
import os

#
# get the bounding box of a detection
#
def GetBoundingBox(fhs):
	bb = {}
	bb['left'] = min(fhs['hx'], fhs['rfx'], fhs['lfx'], fhs['rsx'], fhs['lsx'], fhs['rnx'], fhs['lnx'], fhs['rwx'], fhs['lwx'])
	bb['right'] = max(fhs['hx'], fhs['rfx'], fhs['lfx'], fhs['rsx'], fhs['lsx'], fhs['rnx'], fhs['lnx'], fhs['rwx'], fhs['lwx'])
	bb['top'] = min(fhs['hy'], fhs['rfy'], fhs['lfy'], fhs['rsy'], fhs['lsy'], fhs['rny'], fhs['lny'], fhs['rwy'], fhs['lwy'])
	bb['botom'] = max(fhs['hy'], fhs['rfy'], fhs['lfy'], fhs['rsy'], fhs['lsy'], fhs['rny'], fhs['lny'], fhs['rwy'], fhs['lwy'])

	return bb

#
# Load a sequence, i.e. one sequence with a query and the corresponding ground truth
# in actual fact we don't care about the query here as we're just doing the eval  
#
#	\param filename		the file to load, this file should be the XML file for a single sequence
#	\return 			loaded data, only the locations will be returned, as we don't really care
#						aobut the query here
#
def ParseSequence(filename):
	tree = ET.parse(filename)
	root = tree.getroot()

	sequence = []

	idx = 0
	for fhs in root.findall('fhs'):
		f = {}
		f['idx'] = idx
		f['filename'] = fhs.get('filename')
		f['gt'] = fhs.get('gt')
		if (f['gt'] == 'true'):
			f['hx'] = fhs.get('hx')
			f['hy'] = fhs.get('hy')
			f['rfx'] = fhs.get('rfx')
			f['rfy'] = fhs.get('rfy')
			f['lfx'] = fhs.get('lfx')
			f['lfy'] = fhs.get('lfy')
			f['rsx'] = fhs.get('rsx')
			f['rsy'] = fhs.get('rsy')
			f['lsx'] = fhs.get('lsx')
			f['lsy'] = fhs.get('lsy')
			f['rnx'] = fhs.get('rnx')
			f['rny'] = fhs.get('rny')
			f['lnx'] = fhs.get('lnx')
			f['lny'] = fhs.get('lny')
			f['rwx'] = fhs.get('rwx')
			f['rwy'] = fhs.get('rwy')
			f['lwx'] = fhs.get('lwx')
			f['lwy'] = fhs.get('lwy')

		sequence.append(f)
		idx = idx + 1

	return sequence


#
# Load the entire database. Will load the main file which will contain a list of 
# all other sequences, and will then load each sequence
#
#	\param mainfile		the main file for the database, this will contain full list of sequences and
#						some other stuff like height bounds etc that we don't care about here
#	\param path			path to the database, used to then load up all the other sequences, in the
#						likley rare event that the main file and sequences are located in different
#						locations
#	\returns			the databsae
#
def ParseDatabase(mainfile, path):
	tree = ET.parse(mainfile)
	root = tree.getroot()

	subjects = []

	for s in root.findall('Subject'):
 		subjects.append(ParseSequence(os.path.join(os.path.join(path, s.get('dir')), s.get('xml'))))

	return subjects