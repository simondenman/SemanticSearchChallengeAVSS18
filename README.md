Semantic Search Challenge - AVSS 2018
=====================================

This repository contains code used for the AVSS 2018 Semantic Person Search Challenge. This constits of the code used to run the evaluation against ground truth for the two tasks, and is provided for other researchers to benchmark their approaches after the challenge.

It is very important that the data for the results follows the format outlined below. Participants are strongly encouraged to test their output generation for compatibiity prior to submission. This can be done by using some or all of the training as a make-shift evaluation set to simply test your output format.

Data Format
-----------
## Task 1 Data Format

## Task 2 Data Format

Task two consists of a number of sequences, named 'testing_subject_000', 'testing_subject_001', etc. Each sequence will generate it's own result file, which should be named '000.txt', '001.txt', etc; i.e. output files should be a text file that is simply the number of the test sequence. 

These files should be in csv format, with one line representing the results for a single frame of the sequence. The results should have five columns as follows:
1. The frame number
2. The x coordinate for the top left corner of the detected bounding box, i.e. the x coordinate of the left edge.
3. The y coordinate for the top left corner of the detected bounding box, i.e. the y coordinate of the top edge.
4. The x coordinate for the bottom right corner of the detected bounding box, i.e. the x coordinate of the right edge.
5. The y coordinate for the bottom right corner of the detected bounding box, i.e. the y coordinate of the bottom edge.

A portion of an example file is shown below.
```
frame,left,top,right,bottom
62,222,2,269,122
63,220,6,268,126
64,219,3,267,123
65,221,0,269,119
66,221,2,268,122
...

```
Please ensure to include the column headings in the first row of your output.

For these results files, you may have some frames which are either initialisation frames (i.e. not used for detection) or where your approach does not detect the target. You can handle these frames in one of two ways:
1. Don't include that frame in your results for. For example, considering the example frame above, if the system failed to detect the target for frame 63 the output file could be:
```
frame,left,top,right,bottom
62,222,2,269,122
64,219,3,267,123
65,221,0,269,119
66,221,2,268,122
...

```
2. Include the index and give the bounding box as an impossible/invalid location. For example, consider frame 63 as the failure frame again:
```
frame,left,top,right,bottom
62,222,2,269,122
63,-1,-1,-1,-1
64,219,3,267,123
65,221,0,269,119
66,221,2,268,122
...

```

Only frames which have ground truth annotation will be considered, so including initialisation frames in the results file with invalid locations will not impact results.