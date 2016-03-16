This is the code that generates the 1st place solution to the second Annual Data science bowl competition. https://www.kaggle.com/c/second-annual-data-science-bowl

#### download and prepare data.  
Change the SETTINGS.py data directories, and download the sunny-brook data set, the train, valid, and test data set. Appended the rows from validate.csv to train.csv and name is as train_valid.csv

### A. Train CNNs to predict the contours of the LV.   

##### Part A.
1. run >> bash CNN_A/run_train.sh  
	a) it preprocesses the image data for the CNN net to train  
	b) it trains many version of the CNN model with different parameters  
	c) it loads the train CNN model and predicts the contours for all cases  
	d) extracts the sex-age inforamtion for later use to build sex-age based default model

if there are additional cases that you need to make predictions, just run the run_test.sh script:  
2. run >> bash CNN_A/run_test.sh  
	a) predicts the contours for test cases   
	b) extracts the sex-age inforamtion for test cases  

##### part B. 

run >>python train.py  
it will run similar steps in CNN_B

### B. Calculate the volumes
Combine (average) all the processed results that contains the area of the contours, calculate the volumes for each case, and fit simple models based on the known volume to correct systematic errors, and predict for the unknowns.   
run >> ./train_pred.py  
It uses case 1-700 to train the fitting models, reads all the results from CNN_A/output and CNN_B/output, trains the following models:  
	a) sex-age model  
	b) largest-slice model  
	c) 4-channel model   
	d) CNN_B  
	e) CNN_A  
	d) CNN_A method2  
	f) combination model to combine all the previous models

### About data:  
Directory manual_data includes all the hand labeled images and the contours, they are combined with the sunnybrook data to train the CNN network.

### About hardware we used:  
CNN_A: GTX 970  
CNN_B: GTX 980Ti  

### About software:  
python2.7.6
