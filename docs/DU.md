# AC 2022/23 - Data Understanding

## Describe Data

The dataset consist on 8 relations: 
- relation account (4500 objects) - each record describes static characteristics of an account,
- relation client (5369 objects) - each record describes characteristics of a client,
- relation disposition (5369 objects) - each record relates together a client with an account i.e. this relation describes the rights of clients to operate accounts,
- relation permanent order (6471 objects) - each record describes characteristics of a payment order,
- relation transaction (1056320 objects) - each record describes one transaction on an account,
- relation loan (682 objects) - each record describes a loan granted for a given account,
- relation credit card (892 objects) - each record describes a credit card issued to an account,
- relation demographic data (77 objects) - each record describes demographic characteristics of a district.


### Account Relation
- account_id - identification of the account (categorical and nominal)
- district_id -	location of the branch (categorical and nominal)
- date - date of creating of the account in the form YYMMDD (object)
- frequency - frequency of issuance of statements (categorical and nominal)

The attribute Frequency it's composed by 3 options:
- "weekly issuance"
- "monthly issuance"
- "issuance after transaction"

### Client Relation
- client_id - client identifier (categorical and nominal)
- birth number - birthday and sex: the number is in the form YYMMDD for men, YYMM+50DD for women, where YYMMDD is the date of birth (object)
- district_id - address of the client (categorical and nominal)

### Disposition Relation
- disp_id - record identifier (categorical and nominal)
- client_id - identification of a client (categorical and nominal)
- account_id - identification of an account (categorical and nominal)
- type - type of disposition (owner/user): only owner can issue permanent orders and ask for a loan (categorical and nominal)

	 

### Credit Card Relation
- card_id - record identifier (categorical and nominal)
- disp_id - disposition to an account (categorical and nominal)
- type - type of card: possible values are "junior", "classic", "gold" (categorical and nominal)
- issued - issue date in the form YYMMDD (object)

The possible values for type card are:
- "junior"
- "classic"
- "gold"



### Transaction Relation

- trans_id - record identifier (categorical and nominal)
- account_id - account, the transation deals with (categorical and nominal)
- date - date of transaction	in the form YYMMDD (object)
- type : "credit" / "withdrawal" (+/- transaction)(categorical and nominal)
- operation - mode of transaction (categorical and nominal)
- amount - amount of money (numeric ratio)
- balance - balance after transaction (numeric ratio)
- k_symbol - characterization of the transaction (categorical and nominal)
- bank - bank of the partner each bank has unique two-letter code (categorical and nominal)
- account - account of the partner (categorical and nominal)

The possible values for operation are: 
- "credit in cash"
- "collection from another bank"
- "withdrawal in cash"
- "remittance to another bank"



### Loan

- loan_id - record identifier (categorical and nominal) 
- account_id - identification of the account (categorical and nominal)
- date - date when the loan was granted	in the form YYMMDD (object)
- amount - amount of money (numeric ratio)
- duration - duration of the loan (numeric ratio)
- payments - monthly payments (numeric ratio)
- status - status of paying off the loan (-1 means not payed, 1 means payed) (categorical and nominal)

The duration attribute's unit is months.

We saw that the payments, amount and duration attributes are related, having payments = amount / duration. This way, one of those should be discarded (payments?).


### District

- district_id - district code (categorical and nominal)
- district name (categorical and nominal)
- region (categorical and nominal)
- no. of inhabitants (numeric ratio)
- no. of municipalities with inhabitants < 499 (numeric ratio)
- no. of municipalities with inhabitants 500-1999 (numeric ratio)
- no. of municipalities with inhabitants 2000-9999 (numeric ratio)
- no. of municipalities with inhabitants >10000 (numeric ratio)
- no. of cities (numeric ratio)
- ratio of urban inhabitants (numeric ratio)
- average salary (numeric ratio)
- unemploymant rate '95 (numeric ratio)
- unemploymant rate '96 (numeric ratio)
- no. of enterpreneurs per 1000 inhabitants (numeric ratio)
- no. of commited crimes '95 (numeric ratio)
- no. of commited crimes '96 (numeric ratio)


## Verify Data Quality

## Diversity of statistical methods

## Complexity of statistical methods

## Interpretation of results of statistical methods

## Knowledge extraction from results of statistical methods

## Diversity of plots

## Complexity of plots

## Interpretation of plots

## Presentation

## Visual knowledge extraction

