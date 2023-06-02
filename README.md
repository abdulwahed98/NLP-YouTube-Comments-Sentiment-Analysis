# NLP-YouTube-Comments-Sentiment-Analysis
# Build + Deploy a Sentiment Analysis Model(on Heroku using flask) to classify YouTube comments into Positive, Neutral & Negative
An end-to-end toolkit on building a sentiment prediction model with a Jupyer notebook and deploying model on Heroku using flask. Our use case here is review classification of YouTube comments on Samsung Galaxy S23 Ultra into positive, neutral & negative and suggest moddifications to the product to improve brand image of Samsung. I have scraped comments using youtube_comment_scraper_python library by bot-studio.

## Deployed model on Heroku
[Sentiment Analysis ISI Chennai 2023](https://sentiment-analysis-isi-chennai.herokuapp.com/) 

## I suggest the following modifications to ”Sumsung Galaxy S23 Ultra” developing team based on the negative cooments recieved
• To include expandable memory card slot for upcoming version.
• To use the better processor for upcoming version.
• To include more features than previous model for upcoming
model.

## How the model works!
![](https://github.com/skillcate/sentiment_analysis_with_sklearn_pipeline/blob/main/readme/model-functionality.gif)

## Step by step Implementation:
• Scraping comments on Samsung Galaxy S23 Ultra's official film available on YouTube using Python 
• Labelling data as positive or negative based on polarity scores
• Transforming data: Using lemmatization module; converting alphabets to lower case; removing new lines, punctuations, special characters, stop words; tokenization 
• Encoding: Labels to numerical form; comments to vectors using TfidfVectorizer 
• Balancing the dataset 
• Machine Learning model: Splitting the data into train and test set, feeding the data to Support Vector Classifier 
• Model pipeline: Creating a pipeline which passes the data first into TfidfVectorizer and then to SVClassifier 
• Model evaluation using accuracy score 
• Saving the model pipeline as pickle file 
• Making index.html and flask app(app.py) 
• Committing the files to Github 
• Creating an app on Heroku and connecting it to Github repository 
• Model deployment on Heroku

## Steps to run on Windows for local Deployment

* Prerequisites: [Python 3.9](https://www.python.org/downloads/) (ensure Python is added to [PATH](https://medium.com/co-learning-lounge/how-to-download-install-python-on-windows-2021-44a707994013)) + [Git](https://www.markdownguide.org/basic-syntax/) Client
* Open GIT CMD >> navigate to working directory >> Clone this Github Repo

      git clone https://github.com/abdulwahed98/NLP-YouTube-Comments-Sentiment-Analysis.git  
* Open Windows Powershell >> navigate to new working directory (cloned repo folder)
* Create a virtual environment
  * install virtual environment
 
        pip install virtualenv
        
  * create virtual environment by the name ENV
        
        virtualenv ENV
        
  * activate ENV

        .\ENV\Scripts\activate
        
* Install project dependencies

      pip install -r .\requirements.txt
      
* Run the project

      python app.py
      
* Look for the local host address on Powershell screen, something like: 127.0.0.1:5000 >> Type it on your Web Browser >> Project shall load
* Try out your Amazon Alexa test reviews and look for results
* To close >> Go back to Powershell & type `ctrl+c` >> Deactivate Virtual Environment ENV

      deactivate


### Steps to run on Mac for local Deployment

* Prerequisites: [Python 3.9](https://www.python.org/downloads/)
* Open Terminal >> navigate to working directory >> Clone this Github Repo

      git clone https://github.com/abdulwahed98/NLP-YouTube-Comments-Sentiment-Analysis.git  
* Navigate to new working directory (cloned repo folder)
* Create a virtual environment
  * install virtual environment

        pip install virtualenv
        
  * create virtual environment by the name ENV
  
        virtualenv ENV  
  * activate ENV
        
        source ENV/bin/activate
* Install project dependencies

      pip install -r requirements.txt  
* Run the project

      python app.py
      
* Look for the local host address on Terminal screen, something like: 127.0.0.1:5000 >> Type it on your Web Browser >> Project shall load
* Try out your Amazon Alexa test reviews and look for results
* To close >> Go back to Terminal & type `ctrl+c` >> Deactivate Virtual Environment ENV

      deactivate
