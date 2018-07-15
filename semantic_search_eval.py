#
# Main file to control everything
#
#	SD, 2018/07/15		Initial effort
#

import csv
import os

import task_2.eval as eval
import task_2.ground_truth as gt
import task_2.results as results

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
	subjects = gt.ParseDatabase(database_main_file, database_path)

	# load results
	user_data = results.ParseResults(results_path, num_sequences)

	# do eval
	eval_results = eval.EvaluateDataset(subjects, user_data)
	# and get the metrics, use IoU = 0.4, so just leave this as default
	sequence_results, metrics = eval.GenerateMetrics(eval_results)

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
