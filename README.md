A. Train CNNs to predict contours of the LV. 
0. change the SETTINGS.py data directories, and download the sunny-brook data set, the train, valid, and test data set.
####Part A.
1. go to CNN_A, 
2. run >> bash run_train.sh
	a) it preprocess the image data for the cnn net to train
	b) it trains many version of the model with different parameters
	c) it predicts the contours for train cases
	d) extracts the sex-age inforamtion
if there are additional cases that you need to make predictions, just run the run_test.sh script:
3. run >> bash run_test.sh 
	a) predicts the contours for test cases
	b) extracts the sex-age inforamtion for test cases

####part B. 
run >>python train.py
it will run these step in CNN_B

###TRAIN: Combine all the processed results that contains the area of the contours, build train model based on the know volume result, and predict for the unknows
run >> ./train_pred.py 
#use case 1-700 to train the fitting models
#read all the results from CNN_A/output and CNN_B/output
#train the following models:
	a) sex-age model
	b) largest-slice model
	c) 4-channel model
	d) CNN_B
	e) CNN_A
	d) CNN_A method2
	f) combination model to combine all the previous models

### About data:
Directory manual_data includes all the hand labeled images and the contours, they are combined with the sunnybrook data to train the CNN network.

## About hardware we used:
CNN_A: GTX 970
CNN_B: GTX 980Ti

## About software:
python2.7.6
