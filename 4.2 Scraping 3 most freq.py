"""
A script that reads a file from the web and 
returns the three most frequent words in the file

IMPORTANT: you have to do the mandatory self-study for Lec 4 first
"""

# 1. Import some useful libraries
import re
from nltk.corpus import stopwords
import requests
from operator import itemgetter

#  2. Define the main function

#  input: url of the website to be parsed 
# output: three most frequent words
def run(url): 
    
    # keep the frequency of each word in the file
    freq={}
    
    # import the NLTK stopword dictionary
    # feel free to look online for what stopwords are; don't worry if
    # you're not sure, as we will cover them in lecture 6
    stopLex= set(stopwords.words('english'))
    
    # keep track of whether the file was successfully parsed
    success=False
    
    # try 5 times
    for i in range(5): # try 5 times
        try:           
            #use the browser to access the url 
            response=requests.get(url,headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })              
            # if an error does not occur, set success 
            success=True             
            # we got the file, break the loop
            break        
        except:
            # if we got an exception, the attempt to get the response failed
            print ('failed attempt',i)
     
    # all five attempts failed, return  None
    if not success:
        return None
    
    # if we successfully read the file, let's grab the three most frequent words
    # read in the text from the file
    text=response.text
    # split the text into sentences 
    sentences=text.split('.')
	
    # for each sentence
    for sentence in sentences:
        # lower case everything and strip leading and trailing whitespace
        sentence=sentence.lower().strip() 
        # replace all non-letter characters  with a space
        sentence=re.sub('[^a-z]',' ',sentence) 
		# split to get the words in the sentence 
        words=sentence.split(' ') 
        
        # for each word in the sentence 
        for word in words:
            # ignore empty words and stopwords 
            if word=='' or word in stopLex:
                continue 
            # update the frequency of the word 
            else: 
                # if word     in dict, return the correspnding value
                # if word not in dict, return 0
                freq[word]=freq.get(word,0)+1 
            
    # sort the dictionary by value, in descending order 
    sortedByValue=sorted(freq.items(),key=itemgetter(1),reverse=True)
    
    # return the top 3 terms and their frequencies 
    return sortedByValue[0:3]

#  3. What happens if the script is run as the main program
#     (if it is imported, code block below is ignored)
if __name__=='__main__':
    print(run('http://www.apostolos-filippas.com/teaching/bill.txt'))
	

	
