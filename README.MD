git# Credit Card Analysis with Azure Document Intelligence

This project uses the **Azure Document Intelligence** service to analyze credit card images and extract relevant information such as card number, cardholder name, expiration date, and card type.

## Functionality

The `analyze_credit_card` function analyzes a credit card document using the Azure API, extracting the following relevant data:

- Card Number
- Cardholder Name
- Expiration Date
- Card Type (Mastercard, Visa, Amex, etc.)

## Requirements

- Python 3.x
- Azure SDK for Python (`azure-ai-documentintelligence` package)
- Azure Configuration (API keys and endpoint)
- `re` library for regular expression processing