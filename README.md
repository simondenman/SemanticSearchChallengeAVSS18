Semantic Search Challenge - AVSS 2018
=====================================

This repository contains code used for the AVSS 2018 (https://avss2018.org/) Semantic Person Search Challenge (https://semanticsbsearch.wordpress.com/). This constits of the code used to run the evaluation against ground truth for the two tasks, and is provided for other researchers to benchmark their approaches after the challenge.

It is very important that the data for the results follows the format outlined below. Participants are strongly encouraged to test their output generation for compatibiity prior to submission. This can be done by using some or all of the training as a make-shift evaluation set to simply test your output format.

Workshop Materials
-----------

The presentations by the organisers, and the summary paper, are avaialble in the workshop directory.

Please note that if you use the database for either task we ask that you cite the summary paper (also in the workshop directory):

```
@inproceedings{halsteadAVSS2018Challenge2,
  title={Semantic Person Retrieval in Surveillance Using Soft Biometrics: AVSS 2018 Challenge II},
  author={Halstead, Michael and Denman, Simon and Fookes, Clinton and Tian, YingLi and Nixon, Mark},
  booktitle={2018 IEEE International Conference on Advanced Video and Signal Based Surveillance},
  pages={},
  year={2018}
}
```

Data Format
-----------
## Task 1 Data Format

Task one consists of a set of images and a set of queries, with the task being to determine which query matches which image. As such, for any given query the retuned result should be a list of images ordered from best to worst match, in a similar manner to a person re-identification task. For the evaluation a single text file in csv format should be supplied. 

For each row of the csv file, the first entry should be the query number (this corresponds to the ```query_id``` attribute in each ```<Person>``` tag in the XML file that contain the queries). After this should follow the list of images in order of best to worst match. Participants should use the full image name, including the extension.

A sample CSV file is shown below. In this example we have limited the id's to 10 for simplicity, in your CSV file we expect you to include a total of 196 ranks and 196 id's for the full evaluation.
```
query_id,1,2,3,4,5,6,7,8,9,10
0,A_0001_01_001.png,A_0001_01_083.png,A_0001_03_126.png,A_0001_05_051.png,A_0002_01_021.png,A_0002_04_011.png,A_0002_08_051.png,A_0003_03_131.png,A_0003_04_026.png,A_0003_08_091.png
1,A_0001_01_083.png,A_0001_03_126.png,A_0001_05_051.png,A_0002_01_021.png,A_0002_04_011.png,A_0002_08_051.png,A_0003_03_131.png,A_0003_04_026.png,A_0003_08_091.png,A_0001_01_001.png
2,A_0001_01_001.png,A_0001_05_051.png,A_0002_01_021.png,A_0002_04_011.png,A_0001_01_083.png,A_0001_03_126.png,A_0002_08_051.png,A_0003_03_131.png,A_0003_04_026.png,A_0003_08_091.png
3,A_0001_05_051.png,A_0002_01_021.png,A_0001_01_001.png,A_0001_01_083.png,A_0001_03_126.png,A_0002_04_011.png,A_0002_08_051.png,A_0003_03_131.png,A_0003_04_026.png,A_0003_08_091.png
4,A_0001_05_051.png,A_0002_01_021.png,A_0001_01_001.png,A_0001_01_083.png,A_0001_03_126.png,A_0002_04_011.png,A_0002_08_051.png,A_0003_03_131.png,A_0003_04_026.png,A_0003_08_091.png
5,A_0002_04_011.png,A_0002_08_051.png,A_0003_03_131.png,A_0003_04_026.png,A_0003_08_091.png,A_0001_01_001.png,A_0001_01_083.png,A_0001_03_126.png,A_0001_05_051.png,A_0002_01_021.png
6,A_0002_04_011.png,A_0002_08_051.png,A_0003_03_131.png,A_0003_04_026.png,A_0003_08_091.png,A_0001_01_001.png,A_0001_01_083.png,A_0001_03_126.png,A_0001_05_051.png,A_0002_01_021.png
7,A_0001_03_126.png,A_0001_05_051.png,A_0002_01_021.png,A_0002_04_011.png,A_0002_08_051.png,A_0003_03_131.png,A_0003_04_026.png,A_0003_08_091.png,A_0001_01_001.png,A_0001_01_083.png
8,A_0001_05_051.png,A_0002_01_021.png,A_0002_04_011.png,A_0002_08_051.png,A_0003_03_131.png,A_0003_04_026.png,A_0001_01_001.png,A_0001_01_083.png,A_0001_03_126.png,A_0003_08_091.png
9,A_0003_03_131.png,A_0003_04_026.png,A_0003_08_091.png,A_0001_01_001.png,A_0001_01_083.png,A_0001_03_126.png,A_0001_05_051.png,A_0002_01_021.png,A_0002_04_011.png,A_0002_08_051.png
```
Please ensure that the column headings are also included in your output file. This can be seen in the first row of the CSV document, where we indicate the query_id, then the associated ranks, 1,2,...,10. In the full case this would be 1,...,196. 

If for any reason you do not evaluate one or more queries, or don't return matches past a given rank, simply use a blank entry, i.e. as in the following case where only the best five images are returned for the first query, and the second query isn't attempted:
```
query_id,1,2,3,4,5,6,7,8,9,10
0,A_0001_01_001.png,A_0001_01_083.png,A_0001_03_126.png,A_0001_05_051.png,A_0002_01_021.png,,,,,
1,,,,,,,,,,
```

### Testing Your Output Format

If you wish to verify that your code is outputting data in the correct format, the ```sample_data``` directory (in task_1) contains an XML for a small test set (using the first 10 queries from the training data) and the corresponding ground truth file that you may use. To use these, for each of the 10 queries in Test.xml compare to the 10 images listed in GT.xml; and output the results in the format described above.

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
