# ONDC SDK BUYER APP

A buyer app refers to any application that will help sellers interact with the buyers/ end consumers i.e., the demand side of any transaction, where the intent and transaction originate. These can include different types of applications including user experience (UX) based applications, voice assistants, chat-bots, etc. depicting the demand layer for the goods or services.

## Documentation

[Documentation](https://docs.google.com/document/d/1pGPZ0jwQH9AP0rdZXUcdv8B1QZudr86W3qjABsrlEso/edit)

## Tech Stack

|  Type |       Technologies               |
| :-------- |:-------------------------------- |
| **Client**     | React JS, Redux, Javascript
| **Server**     | Node JS, Express, Python, Nginx |
| **Database**     | MongoDB |

ONDC's buyer app uses a modern technical stack for web, mobile, and server-side development. The client layer of the web application is built using React JS v17, while the mobile app is built using React Native 18. Node JS v16 is used for server-side development, and Python v3.7 is used for the protocol layer.

The app's data is stored in a MongoDB database. Overall, this tech stack enables ONDC to develop scalable and performant applications for their buyers, focusing on flexibility and efficiency.

This repo is ONDC Buyer App is developed with microservice architecture
which contains
 - protocol layer(python)
 - client API layer (node js)
 - front app(react) being served via nginx
 - ancillary API (python) - flask apis for utilities like mapmyindia, knowlarity
composed together with docker-compose.yaml

## For Whom

- wants to refer the buyer app 
- wants the same setup to be available in their infra
- pick any component of it and use separately

## Installation

Clone the Buyer App ONDC SDK repository

```bash
  git clone https://github.com/ONDC-Official/ondc-sdk.git
```

Git repositories contain submodules that must be fetched. It requires HTTP-based URL by default in the ```.gitmodules``` file. Copy this into ```.gitmodules```  file

```bash
[submodule "biap-app-ui-front"]
    path = biap-app-ui-front
    url = https://github.com/ONDC-Official/biap-app-ui-front.git
[submodule "ondc-mmi-service"]
    path = ondc-mmi-service
    url = https://github.com/ONDC-Official/mmi-service-template.git
[submodule "biap-client-node-js"]
    path = biap-client-node-js
    url = https://github.com/ONDC-Official/biap-client-node-js.git
[submodule "py-ondc-protocol"]
    path = py-ondc-protocol
    url = https://github.com/ONDC-Official/py-protocol-layer.git
```

After that Run these commands

```bash
git submodule init

```

```bash
git submodule update
```



## Environment Variables
To get Environment Variables, Registeration is required to access certain services.


**A. Payment gateway**

For the purpose of creating a reference buyer app, Juspay payment gateway has been used. However, participants who are going to leverage this buyer app may integrate with any payment gateway as per their requirement. 

The below steps are considering Juspay’s payment gateway integration
Create an account with Juspay and obtain test account credentials. 
Follow API integration details mentioned in https://developer.juspay.in/

Here are the detailed steps 
Create the auth keys in the Juspay console -  https://developer.juspay.in/docs/setup-juspay-account
Setup keys in buyer client .env file
	After obtaining the Juspay credentials from the console, the user needs to set keys in the buyer client app as mentioned below,

```bash
JUSPAY_SECRET_KEY_PATH= “/PATH/JUSTPAY_CREDS_FILE.pem”
JUSPAY_BASE_URL=https://sandbox.juspay.in
JUSPAY_MERCHANT_ID= “MERCHANT_ID”
JUSPAY_API_KEY= “ACCESS_KEY”
JUSPAY_WEBHOOK_USERNAME= “USER_NAME”
JUSPAY_WEBHOOK_PASSWORD= “PASSWORD”
```

Setup Jus pay in the Mobile app
Setup Jus pay in Web app
```bash
REACT_APP_JUSTPAY_CLIENT_AND_MERCHANT_KEY="MERCHANT_ID"
REACT_APP_MERCHANT_KEY_ID=”MERCHANT_ID”
REACT_APP_PAYMENT_SDK_ENV=”ENVIRONMENT”
REACT_APP_PAYMENT_SERVICE_URL=”PAYMENT_SERVICE_URL”

```



**B. Map My India (MMI)**

For location based information, integration with MMI has been used. MMI has been used as follows - 
Get detailed address information by typing in search query
Get list of addresses for a given PIN code
Get state and city by PIN code
Get Latitude and longitude of the provided address 

MMI API that have been used are as follows - 
https://outpost.mapmyindia.com/api
https://atlas.mapmyindia.com/api/places/search/json
https://explore.mappls.com
https://apis.mapmyindia.com/advancedmaps/v1
https://atlas.mappls.com/api/places/geocode

```bash
MMI Configuration in the white labeled buyer app
MMI_CLIENT_SECRET=”MMI_SERVICE”
MMI_CLIENT_ID=”MMI_CLIENT_ID”
MMI_ADVANCE_API_KEY=”MMI_ADVANCE_API_KEY”
```


**C. Firebase Authentication**

Create the application under firebase console
Once the application is created, visit the application and click on authentication tab
Enable the following sign methods in the authentication sign-in method tab
Email/Password
Google
In project settings create different projects supported for various platforms like Android, iOS and web, (this will help in downloading the config files, required for authentication)


##### Client Env 

```bash
FIREBASE_ADMIN_SERVICE_ACCOUNT=”/path/firebase-service-account.json”
```
Web
```bash
REACT_APP_FIREBASE_API_KEY=”API_KEY”
REACT_APP_FIREBASE_AUTH_DOMAIN=”www.example.com”
REACT_APP_GOOGLE_API_KEY=”GOOGLE_API_KEY” // 
```

**D. Ngrok installation**

A ngrok instance is required to be running locally so you can publish yourself to the internet.

```bash
brew install --cask ngrok
```

```bash
ngrok http 5555
```

copy the url to the clipboard and paste it into ``` BAP_URL ``` and ```PROTOCOL_BASE_URL``` in ```.env-local```


**Note:** To access the web interface of ngrok one must sign-up to ngrok Refer to ngrok documentation.

 

## Generate Payload For ONDC Registeration

```bash

{
    "country": "IND",
    "city": "*",
    "type": "BAP",
    "subscriber_id": "YOUR_HOSTED_DOMAIN",
    "subscriber_url": "YOUR_HOSTED_DOMAIN",
    "domain": "nic2004:52110",
    "signing_public_key": "SIGNING_PUBLIC_KEY",
    "encr_public_key": "CRYPTO_PUBLICKEY",
    "created": "2023-03-30T15:27:45.123456Z"
    "valid_from": "2023-03-30T15:27:45.123456Z",
    "valid_until": "2033-03-30T15:27:45.123456Z",
    "updated": "2023-03-30T15:27:45.123456Z"
}

```

**Note**: ```"created": "2023-03-30T15:27:45.123456Z"```
(The date format is OpenAPI date-time notation)




```BAP_PRIVATE_KEY=``` This will be ```SIGNING_PRIVATE_KEY``` generated by the [utility](https://github.com/ONDC-Official/reference-implementations/tree/main/utilities/signing_and_verification).

```BAP_PUBLIC_KEY= ```This will be ```SIGNING_PRIVATE_KEY```

```BAP_UNIQUE_KEY_ID=```  This will be ukId which we will get after subscribing.

```BAP_ID=``` This will be the ```HOSTED_DOMAIN ```that you are sharing in the payload as the value of subscriber_id.


## Payload Submission To ONDC Staging Registery

Visit this [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdz5-LLGX4m_pOQNFstoZQd5zhb68md_9zoX-dC8N8j2DABbA/viewform) and fill it out carefully.


In return you will get payload with additional data which will include ukId.

```BAP_UNIQUE_KEY_ID=``` will be ukId which we will get after subscribing.

## To run all the services

```bash
Run docker-compose -f docker-compose-for-local.yaml --env-file .env-local up -d.```


