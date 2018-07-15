#
# File to do the actual evaluation, will compare a ground truth data to a set of results
# and output some info on how well it worked
#
#	SD, 2018/06/18		Initial effort
#	SD, 2018/06/19		more coding
#	SD, 2018/06/19		still going, I haven't had much time, added some comments too
#	2D, 2018/07/15		finally got back to this, added a missing return
#

import results
import ground_truth

#
# get the intersection between two bounding boxes. I'm sure that somewhere in python there's a box object
# and all the associated stuff, but the wifi is crap and it's easy to write somethign to do it
#	\param box_a	the first bounding box
#	\param box_b	the second bounding box
#	\return 		the intersection of box_a and box_b, note that this function will not test is this is a
#					valid box or not (i.e left <= right, top <= bottom), so something else should do that
#
def Intersection(box_a, box_b):
	intersection = {}
	intersection['left'] = min(box_a['left'], box_b['left'])
	intersection['top'] = min(box_a['top'], box_b['top'])
	intersection['bottom'] = max(box_a['bottom'], box_b['bottom'])
	intersection['right'] = max(box_a['right'], box_b['right'])

#
# get the area of a box
#	\param box 		the bounding box to look at
#	\return 		area of the box, i.e., width*height
#
def Area(box):
	if((box['left'] > box['right']) | (box['top'] > box['bottom'])):
		return 0
	else:	
		return (box['right'] - box['left'] + 1)*(box['bottom'] - box['top'] + 1)

#
# get the intersection over union between the two boxes
#	\param box_a	the first bounding box
#	\param box_b	the second bounding box
#	\return 		the intersection over union of the two boxes
#
def IoU(box_a, box_b):
	intsect = Area(Intersection(box_a, box_b))
	return (intsect/(Area(box_a) + Area(box_b) - intersect))

#
# evaluate a sequence, i.e compare the ground truth to the results from a single sequence
#	\param gt_sequence 			the gt_sequence to compare
#	\param results_sequence		the results we are comparing to
#	\return						a list of dictionaries, each dict is a frame index and an iou
#
def EvaluateSequence(gt_sequence, results_sequence):
	frame_results = []

	for gt in gt_sequence:
		if gt['gt'] == 'true':
			r = results.GetResultsForFrame(results_sequence, gt['idx'])
			if (r is not None):
				frame_results.append({'frame' : gt['idx'], 'IoU': IoU(r, ground_truth.GetBoundingBox(gt))})

	return frame_results

#
# Evaluate a whole dataaset, basically, run EvaluateSequence over all sequences
#	\param gt_sequences 		the ground truth sequences 
#	\param results_sequence 	the results sequences
#	\return 					a list of sequence results, i.e. a list of what's retruned by EvaluateSequence 
#
def EvaluateDataset(gt_sequences, results_sequence):
	results = []
	for gt, res in zip(gt_sequences, results_sequence):
		results.append(EvaluateSequence(gt, res))

	return results

#
# Get some metrics for a sequence, compute somethings like the average IoU, number of frames above
# a threshoold, and whatever else I decide to add
#	\param sequence 		sequence to get metrics for
#	\param iou_thresh 		the minimum IoU that we need to consider a 'match'
#	\returm 				a dictionary, that has the average IoU for the seqeunce, the percentage of frames above
#							the IoU threshold, and the number of observations
#
def MetricsForSequence(sequence, iou_thresh = 0.4):
	average_iou = 0
	iou_above_thresh = 0
	for s in sequence:
		average_iou += s['IoU']
		if (s['IoU'] >= iou_thresh):
			iou_above_thresh += 1

	return {'average_IoU' : average_iou/len(sequence), 'percentage_above_thresh' : iou_above_thresh / len(sequence), 'observations' : len(sequence)}

#
# Get metrics for the entire dataset, will compute metrics per sequence and overall metrics
# 	\param results 			the full set of results to evaluate
#	\param iou_thresh 		the minimum IoU that we need to consider a 'match'
#	\returns				a list of sequence results (see MetricsForSequence) and a dictionary (same entires as sequence results)
#							that captures the overall metrics
#
def GenerateMetrics(results, iou_thresh = 0.4):
	sequence_results = []
	overall_metrics = {}
	overall_metrics['average_iou'] = 0
	overall_metrics['percentage_above_thresh'] = 0
	overall_metrics['observations'] = 0

	for r in results:
		sr = MetricsForSequence(r, iou_thresh)
		overall_metrics['average_iou'] += sr['average_iou']*sr['observations']
		overall_metrics['percentage_above_thresh'] += sr['percentage_above_thresh']*sr['observations']
		overall_metrics['observations'] += sr['observations']
		sequence_results.append(sr)

	overall_metrics['average_iou'] /= overall_metrics['observations']
	overall_metrics['percentage_above_thresh'] /= overall_metrics['observations']

	return sequence_results, overall_metrics
