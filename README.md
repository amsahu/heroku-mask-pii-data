# Heroku-mask-pii-data

**App link:** https://mask-pii-data.herokuapp.com/

Follow the description given in the website to get the results.
Since it is deployed as demo, it has some limitations to take care of.

### Abstract

* Aim was to create a solution to automate PII data discovery and masking for tabular datasets.
* Why we created this: There are multiple options available for data discovery and masking, but most of them uses column metadata and regex to find the patterns. This method is not helpful for irregular entities like addresses. It’s very difficult to define address using just regex and column metadata. So to overcome this problem and also reduce the cost, we needed to come up this solution.



### Solution Architecture

<img src="https://user-images.githubusercontent.com/60923910/132125427-557e2ab3-c0e9-48f9-b505-e66c9d2875a9.png" width="700">



### AI Model

<img src="https://user-images.githubusercontent.com/60923910/132125442-f9897aaa-e5dd-4479-a500-19b6d1b954a4.png" width="700">


### AI Model - Metrics

<img src="https://user-images.githubusercontent.com/60923910/132125456-e236eac4-b282-4a76-b37a-7c64e68ac195.png" width="700">


### Achievements

* Created a working Flask app using Python to completely automate the data discovery and masking process with intelligence.
* Achieved an NER model using spacy with very low error rate.
* All the components are in Python and created in modular approach.
* Created from open source components, so will reduce the implementation cost for customer and will attract more customers.
* Deployed the demo in heroku.
* App Link: https://mask-pii-data.herokuapp.com/
