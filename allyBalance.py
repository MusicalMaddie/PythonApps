import requests
import json

# replace with your API key
api_key = 'your-api-key'

# replace with your account ID
account_id = 'your-account-id'

# make the HTTP request
response = requests.get(f'https://api.ally.com/v1/accounts/{account_id}',
                        headers={'Authorization': f'Bearer {api_key}'})

# parse the response and extract the balance
data = json.loads(response.text)
balance_cents = data['balance']
balance_dollars = balance_cents / 100

# display the balance in dollars
print(f'Your account balance is ${balance_dollars:.2f}')
