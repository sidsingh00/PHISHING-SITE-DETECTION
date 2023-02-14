hey this is phishing site detection 
Today's growing phishing websites pose significant threats due to their extremely undetectable risk. They anticipate internet users to mistake them as genuine ones in order to reveal user information and privacy, such as login ids, passwords, credit card numbers, etc. without notice. This paper proposes a new approach to solve the anti-phishing problem. The new features of this approach can be represented by URL character sequence without phishing prior knowledge, various hyperlink information, and textual content of the webpage, which are combined and fed to train the XGBoost classifier. One of the major contributions of this paper is the selection of different new features, which are capable enough to detect 0-h attacks, and these features do not depend on any third-party services. In particular, we extract character level Term Frequency-Inverse Document Frequency (TF-IDF) features from noisy parts of HTML and plaintext of the given webpage. Moreover, our proposed hyperlink features determine the relationship between the content and the URL of a webpage. Due to the absence of publicly available large phishing data sets, we needed to create our own data set with 60,252 webpages to validate the proposed solution. This data contains 32,972 benign webpages and 27,280 phishing webpages. For evaluations, the performance of each category of the proposed feature set is evaluated, and various classification algorithms are employed. From the empirical results, it was observed that the proposed individual features are valuable for phishing detection. However, the integration of all the features improves the detection of phishing sites with significant accuracy. The proposed approach achieved an accuracy of 96.76% with only 1.39% false-positive rate on our dataset, and an accuracy of 98.48% with 2.09% false-positive rate on benchmark dataset, which outperforms the existing baseline approaches.

Phishing is a form of cybercrime in which a target is contacted via email, telephone, or text message by an attacker disguising as a reputable entity or person. The attacker then lures individuals to counterfeit websites to trick recipients into providing sensitive data.

Objective of the work
A phishing website is a common social engineering method that mimics trustful uniform resource locators (URLs) and webpages. The objective of this project is to train machine learning models and deep neural nets on the dataset created to predict phishing websites.

Disadvantages/Limitations in the existing system
First limitation is that the textual features of our phishing detection approach depend on the English language. This may cause an error in generating efficient classification results when the suspicious webpage includes language other than English. About half (60.5%) of the websites use English as a text language44. The second limitation is that despite the proposed approach uses URL based features, our approach may fail to identify the phishing websites in case when the phishers use the embedded objects (i.e., JavaScript, images, Flash, etc.) to obscure the textual content and HTML coding
from the anti-phishing solutions. Based on our experiments, we noticed that legitimate pages usually contain rich textual content features, and high amount of hyperlinks (At least one hyperlink in the HTML source code). Hence, the next limitation of this approach is that it is not sufficiently capable of detecting attached malware because our approach does not read and process content from the web page`s external files, whether they are cross-domain or not.


Proposed System
Our approach extracts and analyzes different features of suspected webpages for effective identification of large-scale phishing offenses. 
For improving the detection accuracy of phishing webpages, we have proposed features. 
Our proposed features determine the relationship between the URL of the webpage and the webpage content. 
The main purpose of the project is to detect the fake or phishing websites who are trying to get access to the sensitive data or by creating the fake websites and trying to get access of the user personal credentials.
We are using machine learning algorithms to to detect the phishing websites and safeguard the sensitive data. 


Hardware and Software Used

Software Requirement 

Coding languages: Python (3.9), HTML5, CSS, JavaScript frameworks
Libraries required: Python libraries like- Numpy, Pandas, BeautifulSoup, OpenCV, Matplotlib, etc


Hardware Requirement

OS: Windows 7, Windows 8, Windows 10, Windows 11
RAM required: Minimum 16GB

Overall Architected Diagram 
<img width="436" alt="Screenshot 2023-02-14 at 11 58 39 PM" src="https://user-images.githubusercontent.com/124824485/218825604-1cf6e9ae-ea9f-45a3-a552-87fae501d91c.png">

System Design and implementation 
Module 1 – Scikit Learn – Sklearn Module

scikit-learn (formerly scikits.learn and also known as sklearn) is a free software machine learning library for the Python programming language.[3] It features various classification, regression and clustering algorithms including support-vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy. Scikit-learn is a NumFOCUS fiscally sponsored project.
scikit-learn is largely written in Python and uses NumPy extensively for high-performance linear algebra and array operations. Furthermore, some core algorithms are written in Cython to improve performance. Support vector machines are implemented by a Cython wrapper around LIBSVM; logistic regression and linear support vector machines by a similar wrapper around LIBLINEAR. In such cases, extending these methods with Python may not be possible.
scikit-learn integrates well with many other Python libraries, such as Matplotlib and plotly for plotting, NumPy for array vectorization, Pandas dataframes, SciPy, and many more.

Module 2 – Random Forest Classifer

class sklearn.ensemble.RandomForestClassifier(n_estimators=100, *, criterion='gini', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='sqrt', max_leaf_nodes=None, min_impurity_decrease=0.0, bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0, warm_start=False, class_weight=None, ccp_alpha=0.0, max_samples=None)
A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree

Module 3 – Numpy Module

NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy was created in 2005 by Travis Oliphant. It is an open-source project and you can use it freely.
NumPy stands for Numerical Python.
In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
Arrays are very frequently used in data science, where speed and resources are very important.

Module 4 – Pandas Module

Pandas is an open source library in Python. It provides ready to use high-performance data structures and data analysis tools.
Pandas module runs on top of NumPy and it is popularly used for data science and data analytics.
NumPy is a low-level data structure that supports multi-dimensional arrays and a wide range of mathematical array operations. Pandas has a higher-level interface. It also provides streamlined alignment of tabular data and powerful time series functionality.
DataFrame is the key data structure in Pandas. It allows us to store and manipulate tabular data as a 2-D data structure.
Pandas provides a rich feature-set on the DataFrame. For example, data alignment, data statistics, slicing, grouping, merging, concatenating data, etc.

Module 5 – OS Module

It is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
You first need to import the os module to interact with the underlying operating system. So, import it using the import os statement before using its functions.

Module 6 – Requests Module

The requests module allows you to send HTTP requests using Python.
The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

Module 7 – Flask Framework
Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.
It does have many cool features like url routing, template engine. It is a WSGI web app framework.
A Web Application Framework or a simply a Web Framework represents a collection of libraries and modules that enable web application developers to write applications without worrying about low-level details such as protocol, thread management, and so on.

Conclusion 

Phishing website attacks are a massive challenge for researchers, and they continue to show a rising trend in recent years. Blacklist/whitelist techniques are the traditional way to alleviate such threats. However, these methods fail to detect non-blacklisted phishing websites (i.e., 0-day attacks). As an improvement, machine learning techniques are being used to increase detection efficiency and reduce the misclassification ratio. However, some of them extract features from third-party services, search engines, website traffic, etc., which are complicated and difficult to access. In this paper, we propose a machine learning-based approach which can speedily and precisely detect phishing websites using URL and HTML features of the given webpage. The proposed approach is a completely client-side solution and does not rely on any third-party services. It uses URL character sequence features without expert intervention, and hyperlink specific features that determine the relationship between the content and the URL of a webpage. Moreover, our approach extracts TF-IDF character level features from the plaintext and noisy part of the given webpage's HTML.
A new dataset is constructed to measure the performance of the phishing detection approach, and various classification algorithms are employed. Furthermore, the performance of each category of the proposed feature set is also evaluated. According to the empirical and comparison results from the implemented classification algorithms, the XGBoost classifier with integration of all kinds of features provides the best performance. It acquired 1.39% false-positive rate and 96.76% of overall detection accuracy on our dataset. An accuracy of 98.48% with a 2.09% false-positive rate on a benchmark dataset.
