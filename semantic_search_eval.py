#
# Main file to control everything
#
#	SD, 2018/07/15		Initial effort
#	SD, 2018/07/26		Add Task 1
#

import csv
import os

import task_2.eval as t2_eval
import task_2.ground_truth as t2_gt
import task_2.results as t2_results

import task_1.eval as t1_eval
import task_1.ground_truth as t1_gt
import task_1.results as t1_results

#
# Task 1
#
# 	\param groundtruth_file		The xml file with the ground truth (use 'sample_data/GT.xml' for the sanity check)
# 	\param results_file		This is the results .txt file (use 'sample_data/results_1.txt' or 'sample_daata/results_2.txt' or your own txt file for the sanity check)
#	\param output_path 		MAH - Not in use (20180730)
# 	\param prefix			MAH - Not in use (20180730)	
def RunEval_Task1(groundtruth_file, results_file, output_path = '.', prefix = ''):
	# load in the ground truth from the xml
	gt = t1_gt.ParseGroundTruth(groundtruth_file)

	# load in the results data from the txt file - CSV
	user_data = t1_results.load_results(results_file)

	# calculate the desired results.
	results = t1_eval.Evaluate(user_data, gt)
	cmc = t1_eval.GetCMC(results)

	# in future the results will be output to a text file.
	return results, cmc

#
# Function to run the eval for task 2. Will load database and results, compute metrics, and dump results to
# a file
#	\param database_path		path to the database
#	\param database_main_file	main file for the datbase
#	\parma results_path			where the results files are located
#	\param num_sequences		number of test sequences, used to guide loading of the results
#	\param output_path			path to write outputs to
#	\param prefix				prefix to append to metrics that are written
#
def RunEval_Task2(database_path, database_main_file, results_path, num_sequences, output_path = '.', prefix = ''):
	# load ground truth
	subjects = t2_gt.ParseDatabase(database_main_file, database_path)

	# load results
	user_data = t2_results.ParseResults(results_path, num_sequences)

	# do eval
	eval_results = t2_eval.EvaluateDataset(subjects, user_data)
	# and get the metrics, use IoU = 0.4, so just leave this as default
	sequence_results, metrics = t2_eval.GenerateMetrics(eval_results)

	keys_sequence = sequence_results[0].keys()
	keys_metrics = metrics.keys()
	print(metrics)

	with open(os.path.join(output_path, prefix + 'sequence_results.txt'), 'wb') as csv_out:
		dict_writer = csv.DictWriter(csv_out, keys_sequence)
		dict_writer.writeheader()
		dict_writer.writerows(sequence_results)

	with open(os.path.join(output_path, prefix + 'overall.txt'), 'wb') as csv_out:
		dict_writer = csv.DictWriter(csv_out, keys_metrics)
		dict_writer.writeheader()
		dict_writer.writerow(metrics)
