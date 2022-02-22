# **Preprocess module**


## **LowerCase(text: str) → str**
### **Description**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Converts letters in given text to lowercase.

### **Parameters**

***text:*** *str*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text to preprocess.

### **Returns**

***preprocessedText:*** *str* 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lowercase text.
___
## **RemoveHashtags(text: str) → str**
### **Description**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Removes hashtags from given tweet text.

### **Parameters**

***text:*** *str*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text to preprocess.

### **Returns**

***preprocessedText:*** *str* 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text with no hashtags.
___
## **RemoveMentions(text: str) → str**
### **Description**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Removes mentions from given tweet text.

### **Parameters**

***text:*** *str*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text to preprocess.

### **Returns**

***preprocessedText:*** *str* 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text with no mentions.
___
## **RemovePunctuation(text: str) → str**
### **Description**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Removes non text characters from given tweet text.

### **Parameters**

***text:*** *str*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text to preprocess.

### **Returns**

***preprocessedText:*** *str* 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text with no non tex characters.
___
## **Lemmatize(text: str) → str**
### **Description**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lemmatizes polish text from given tweet.

### **Parameters**

***text:*** *str*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text to preprocess.

### **Returns**

***lemmatizedText:*** *str* 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lemmatized text.
___
## **RemoveStopWords(text: str) → str**
### **Description**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Removes stopwords.

### **Parameters**

***text:*** *str*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text to preprocess.

### **Returns**

***preprocessedText:*** *str* 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Text with no stopwords.
___