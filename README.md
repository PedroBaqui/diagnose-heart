This is the code that generates the 1st place solution to the second Annual Data science bowl competition. https://www.kaggle.com/c/second-annual-data-science-bowl

#### A. Download and prepare data  
Change the directories in SETTINGS.py to your settings, and download the sunny-brook data set, the train, valid, and test data set. Append the rows from validate.csv to train.csv and rename it as train_valid.csv

The directory manual_data/ includes all the hand labeled images and the contours, they are combined with the sunnybrook data to train the CNN networks.

### B. Train CNNs to predict the contours of the LV   

##### Part A

1. run >> bash CNN_A/run_train.sh  
	a) it preprocesses the image data for the CNN net to train.  
	b) it trains many version of the CNN models with different parameters. To save time, you can simply just run versions 3 and 6 and get a slightly worse result.
	c) it loads the trained CNN models and predicts the contours for all cases.  
	d) it extracts the sex-age inforamtion for later use to build sex-age based default model.   
If there are additional cases that you need to make predictions, just run the run_test.sh script:  
2. run >> bash CNN_A/run_test.sh  
	a) predicts the contours for test cases.   
	b) extracts the sex-age inforamtion for test cases.  

##### Part B 

run >>python train.py  
it runs similar steps for CNN_B

### C. Calculate the volumes
Combine (average) all the processed results that contains the area of the contours, calculate the volumes for each case, and fit simple models based on the train dataset to correct systematic errors, and predict for the unknowns.   

run >> ./train_pred.py   
It uses case 1-700 to fit the following simple models, and generates the final submission file.  
	a) sex-age model  
	b) largest-slice model  
	c) 4-channel model   
	d) CNN_B  
	e) CNN_A  
	d) CNN_A method2  
	f) average model to combine all the previous models

#### About hardware we used:  
CNN_A: GTX 970  
CNN_B: GTX 980Ti  

#### About software:  
python2.7.6  
CNN_A: cv2.__version__ = 3.1.0   
CNN_B: cv2.__version__ = 2.4.12  
