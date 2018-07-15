#
# Main file to control everything
#
#	SD, 2018/07/15		Initial effort
#

import task_2.eval as eval
import task_2.ground_truth as gt
import task_2.results as results

def RunEval_Task2(database_path, database_main_file, results_path, num_sequences, output_path):
	# load ground truth
	subjects = gt.ParseDatabase(database_main_file, database_path)

	# load results
	user_data = results.ParseResults(results_path, num_sequences)

	# do eval
	eval_results = eval.EvaluateDataset(subjects, user_data)
	# and get the metrics, use IoU = 0.4, so just leave this as default
	metrics = eval.GenerateMetrics(eval_results)