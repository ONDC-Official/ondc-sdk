# ONDC SDK BUYER APP

A buyer app refers to any application that will help sellers interact with the buyers/ end consumers i.e., the demand side of any transaction, where the intent and transaction originate. These can include different types of applications including user experience (UX) based applications, voice assistants, chat-bots, etc. depicting the demand layer for the goods or services.

## User Manual

A detailed user manual for the buyer reference app is available [here](https://docs.google.com/document/d/1pGPZ0jwQH9AP0rdZXUcdv8B1QZudr86W3qjABsrlEso/edit)

## ONDC - API Contract for Retail (v1.2.0)
[Documentation](https://docs.google.com/document/d/1brvcltG_DagZ3kGr1ZZQk4hG4tze3zvcxmGV4NMTzr8/edit)

## Reference Buyer Web Application Feature List V1.2

| Feature                     | Sub Feature                                                                | Status                                            |
|-----------------------------|----------------------------------------------------------------------------|---------------------------------------------------|
| Incremental catalog refresh | Provider disabling                                                         | $${\color{green}Available}$$                      |
|                             | Store disabling                                                            | $${\color{green}Available}$$                      |
|                             | Store closed (known duration)                                              | $${\color{green}Available}$$                      |
|                             | Store closed (unknown duration)                                            | $${\color{green}Available}$$                      |
|                             | Item record changes                                                        | $${\color{green}Available}$$                      |
|                             | Offers                                                                     | $${\color{orange}In \space future \space scope}$$ |
| Full catalog refresh        | RET codes for L1 categories                                                | $${\color{green}Available}$$                      |
|                             | Catalog directly to BNP                                                    | $${\color{green}Available}$$                      |
|                             | Updated taxonomy (BPC, H&K, H&W)                                           | $${\color{green}Available}$$                      |
|                             | Store open / close / disable / enable                                      | $${\color{green}Available}$$                      |
|                             | Customization (input - selection)                                          | $${\color{green}Available}$$                      |
|                             | Customization (input - free text)                                          | $${\color{orange}In \space future \space scope}$$ |
|                             | Handling of make-to-order items display price having base price of 0       | $${\color{green}Available}$$                      |
|                             | Variants                                                                   | $${\color{green}Available}$$                      |
|                             | Custom Menu                                                                | $${\color{green}Available}$$                      |
|                             | Definition of ISN/MSN                                                      | $${\color{green}Available}$$                      |
|                             | Item availability schedule                                                 | $${\color{blue}Under \space Development}$$        |
| Order tracking              | Hyperlocal - using gps coordinates                                         | $${\color{green}Available}$$                      |
|                             | Hyperlocal & inter-city - using URL                                        | $${\color{orange}In \space future \space scope}$$ |
|                             | Live Order Tracking                                                        | $${\color{green}Available}$$                      |
| Order flow                  | Addition of quote type                                                     | $${\color{green}Available}$$                      |
|                             | Addition of updated /confirm, /on_confirm flow                             | $${\color{green}Available}$$                      |
|                             | Customization (input - selection: all pre-order APIs)                      | $${\color{green}Available}$$                      |
|                             | Customization (input - free text: all pre-order APIs)                      | $${\color{orange}In \space future \space scope}$$ |
|                             | Customization (input - selection: all post-order APIs)                     | $${\color{green}Available}$$                      |
|                             | Customization (input - free text: all post-order APIs)                     | $${\color{orange}In \space future \space scope}$$ |
|                             | Payment collection by SNP                                                  | $${\color{orange}In \space future \space scope}$$ |
|                             | Exchange of GST no between BNP & SNP                                       | $${\color{green}Available}$$                      |
|                             | PAN no for provider for verification of ISN / MSN                          | $${\color{green}Available}$$                      |
| Offers                      | Offer definition in catalog                                                | $${\color{orange}In \space future \space scope}$$ |
|                             | Applying offers during checkout                                            | $${\color{orange}In \space future \space scope}$$ |
|                             | Offer support in other pre-order APIs                                      | $${\color{orange}In \space future \space scope}$$ |
|                             | Offer support in other post-order APIs                                     | $${\color{orange}In \space future \space scope}$$ |
| Cancellation                | Updated cancel API (non-RTO)                                               | $${\color{green}Available}$$                      |
|                             | RTO flow for cancellation                                                  | $${\color{green}Available}$$                      |
|                             | Definition & communication of cancellation terms (fees, etc)               | $${\color{orange}In \space future \space scope}$$ |
|                             | Force cancellation (for fulfillment TAT breach)                            | $${\color{orange}In \space future \space scope}$$ |
|                             | Linking cancellation with IGM issue                                        | $${\color{orange}In \space future \space scope}$$ |
| Static terms                | Enabling static terms                                                      | $${\color{orange}In \space future \space scope}$$ |
| BNP + logistics             | Enabling logistics integration with BNP                                    | $${\color{orange}In \space future \space scope}$$ |
| Update API                  | Merchant part cancel                                                       | $${\color{green}Available}$$                      |
|                             | Return with pickup                                                         | $${\color{green}Available}$$                      |
|                             | Return with liquidation                                                    | $${\color{green}Available}$$                      |
|                             | Cancel return request                                                      | $${\color{green}Available}$$                      |
|                             | Linking return with IGM issue                                              | $${\color{orange}In \space future \space scope}$$ |
| Fulfillment                 | Enabling self-pickup                                                       | $${\color{green}Available}$$                      |
|                             | Enabling slotted delivery                                                  | $${\color{green}Available}$$                      |
|                             | Enabling additional fulfillment states - hyperlocal                        | $${\color{green}Available}$$                      |
|                             | Enabling additional fulfillment states - inter-city                        | $${\color{green}Available}$$                      |
|                             | Enabling authorization options                                             | $${\color{orange}In \space future \space scope}$$ |
|                             | Cascading discount, taxes on fulfillment from LSP                          | $${\color{orange}In \space future \space scope}$$ |
|                             | Payment on Delivery                                                        | $${\color{orange}In \space future \space scope}$$ |
|                             | Notification from LSP on fulfillment delay                                 | $${\color{orange}In \space future \space scope}$$ |
| Catalog (others)            | Polygon serviceability                                                     | $${\color{green}Available}$$                      |
|                             | Pincode serviceability                                                     | $${\color{orange}In \space future \space scope}$$ |
|                             | Distributed search by city                                                 | $${\color{orange}In \space future \space scope}$$ |
|                             | Back image for items                                                       | $${\color{green}Available}$$                      |
|                             | Minimum order value                                                        | $${\color{orange}In \space future \space scope}$$ |
|                             | Different store timings for delivery, pickup, order processing             | $${\color{orange}In \space future \space scope}$$ |
|                             | Provider credentials                                                       | $${\color{orange}In \space future \space scope}$$ |
|                             | Catalog download zip file link                                             | $${\color{orange}In \space future \space scope}$$ |
|                             | Communication from buyer NP to seller NP (catalog ingestion feedback, etc) | $${\color{orange}In \space future \space scope}$$ |
| Rating                      | rating, on_rating                                                          | $${\color{orange}In \space future \space scope}$$ |
| Others                      | /info, /on_info APIs                                                       | $${\color{orange}In \space future \space scope}$$ |
|                             | Off Network Logistics Option                                               | $${\color{orange}In \space future \space scope}$$ |
|                             | Option to select logistics delivery type                                   | $${\color{orange}In \space future \space scope}$$ |
| Personalisation             | Recommendation Engine                                                      | $${\color{blue}Under \space Development}$$        |
|                             | Festival calendar & configuring for different festivals                    | $${\color{blue}Under \space Development}$$        |
|                             | Bhashini Integration                                                       |  $${\color{blue}Under \space Development}$$       |
| Catalog Indexing            |                                                                            | $${\color{blue}Under \space Development}$$        |
| Configurable Theme          |                                                                            | $${\color{green}Available}$$                      |

## Working Group Members

| Name              | Role                      | Github Role | Github Username
| :---------------- | :------------------------ | :---------- | :-------------- 
| Navdeep Agarwal   | Backend Engineer & Devops | Maintainer  | @navdeep710
| Abhinandan Satpute| Backend Engineer          | Maintainer  | @wemo-abhinandan
| Aditya Patil      | Protocol Engineer         | Contributor | @adityapatil123
| Akshay Chavan     | Backend Engineer          | Contributor | @wemakshaychavan
| Mayur Jadhav      | Full Stack Engineer       | Contributor | @mj-jadhav
| Vaibhav           | Frontend Engineer         | Contributor | @vaibhav-wemo
| Rohaan Ansari     | Frontend Engineer         | Contributor | @RohaanAnsari
| Vishal            | Frontend Engineer         | Contributor | @vishal-wemotive
| Shalaka Patil     | Full Stack Engineer       | Contributor | @shalapatil
| Harsh Arya        | Frontend Engineer         | Contributor | @harsharya1405
| Punit Vajpeyi     | Mobile Developer          | Contributor | @Punit-Vajpeyi
| Abhijeet Singh    | Full Stack Engineer       | Contributor | @AbhijeetONDC
| Robin Chauhan     | Backend Engineer          | Contributor | @robin-chauhan1
| Sahil Sharma      | Backend Engineer          | Contributor | @sahilsharma9
| Abhishek Singh    | Frontend Engineer         | Contributor | @Abhi-ONDC


## Tech Stack

| Type         | Technologies                    |
| :----------- | :------------------------------ |
| **Client**   | React JS, Redux, Javascript     |
| **Server**   | Node JS, Express, Python, Nginx |
| **Database** | MongoDB                         |

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

Git repositories contain submodules that must be fetched. It requires HTTP-based URL by default in the `.gitmodules` file. Copy this into `.gitmodules` file

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
[submodule "biap-igm-node-js"]
	path = biap-igm-node-js
	url = https://github.com/ONDC-Official/biap-igm-node-js.git
[submodule "biap-bugzilla-service"]
	path = biap-bugzilla-service
	url = https://github.com/ONDC-Official/biap-bugzilla-service
[submodule "catalog-service"]
	path = catalog-service
	url = https://github.com/ONDC-Official/catalog-service
	branch = main
```

After that Run these commands

```bash
git submodule init
```

```bash
git submodule update
```

## Environment Variables

To get Environment Variables, Registration is required to access certain services.

**A. Payment gateway**

For the purpose of creating a reference buyer app, Juspay payment gateway has been used. However, participants who are going to leverage this buyer app may integrate with any payment gateway as per their requirement.

The below steps are considering Juspay’s payment gateway integration
Create an account with Juspay and obtain test account credentials.
Follow API integration details mentioned in https://developer.juspay.in/

Here are the detailed steps
Create the auth keys in the Juspay console - https://developer.juspay.in/docs/setup-juspay-account
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

### Generating the `.pem` File for Juspay Credentials

If you're unable to find the `.pem` file for Juspay credentials, follow these steps:

1. Go to [Juspay Security Settings](https://portal.juspay.in/settings/security).
2. Under the "RSA Keys" section, click the "Upload new RSA" button on the right.
3. Select the option "I don't have the RSA Keys, I want to auto-generate the keys."
4. This will download a file named `private.pem`. Rename this file to `juspay.pem`.
5. Set the environment variable `JUSPAY_SECRET_KEY_PATH` as:
   ```bash
   export JUSPAY_SECRET_KEY_PATH="/PATH/TO/juspay.pem"

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

copy the url to the clipboard and paste it into `BAP_URL` and `PROTOCOL_BASE_URL` in `.env-local`

**Note:** To access the web interface of ngrok one must sign-up to ngrok Refer to ngrok documentation.

**E. Bugzilla Setup**

For IGM ticket management, a bugzilla instance will be started as soon as all the containers are launched. Initially, it is not mandatory to mention a value for `BUGZILLA_API_KEY` but to use the instance post-setup, you will need to generate the API key and restart the container.

**_To generate the API Key and use Bugzilla_**:

- Once setup, visit the url: https://host-running-code/bugzilla/admin
- Login with username as "admin" and password as "password"
- Go to settings, and setup SMTP configuration. Visit [this link](https://bugzilla.readthedocs.io/en/latest/installing/essential-post-install-config.html) for more info.
- Once setup, generate the API key and it will be visible on the dashboard.
- Add the API KEY value to `BUGZILLA_API_KEY` in the .env variables and restart your bugzilla container.

**Note:** It is not mandatory to setup bugzilla and the buyer app **can** run without it, but for application issue/ticket management and to view all tickets generated across the portal, it is advised to setup bugzilla.

## Payload Submission To ONDC Staging Registry

Visit this [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSdz5-LLGX4m_pOQNFstoZQd5zhb68md_9zoX-dC8N8j2DABbA/viewform) and fill it out carefully.

In return you will get payload with additional data which will include ukId.

`BAP_UNIQUE_KEY_ID=` will be ukId which we will get after subscribing.

## Generate Payload For ONDC Registration

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

**Note**: `"created": "2023-03-30T15:27:45.123456Z"`
(The date format is OpenAPI date-time notation)

`BAP_PRIVATE_KEY=` This will be `SIGNING_PRIVATE_KEY` generated by the [utility](https://github.com/ONDC-Official/reference-implementations/tree/main/utilities/signing_and_verification).

`BAP_PUBLIC_KEY= `This will be `SIGNING_PRIVATE_KEY`

`BAP_UNIQUE_KEY_ID=` This will be ukId which we will get after subscribing.

`BAP_ID=` This will be the `HOSTED_DOMAIN `that you are sharing in the payload as the value of subscriber_id.

## To run all the services

````bash
Run docker-compose -f docker-compose-for-local.yaml --env-file .env-local up -d.```

````
