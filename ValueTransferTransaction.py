import requests
import json
import csv
import time

# Reference
# Klaytn Wallet API - https://refs.klaytnapi.com/ko/wallet/latest



# 1 klay = 10^18 peb
# https://ko.docs.klaytn.com/klaytn/design/klaytn-native-coin-klay
KLAY = 0.02
PEB = int(10**18 * KLAY)
HEX_PEB = hex(PEB)


# POST - Sending KLAY
url = "https://wallet-api.klaytnapi.com/v2/tx/value"


# CSV
file = open("wallet_list_sample.csv", 'r')
reader = csv.reader(file)
students = [line for line in reader]


# log
log = open("log", 'w+')
failed = []
counter = 1


for student in students:
    time.sleep(3)
    name, wallet = student[0], student[1]

    headers = {
        "x-chain-id": "1001",
        "Authorization": "AUTHORIZATION"
    }
    body = {
        "from": "SENDER_WALLET_ADDRESS",
        "value": "PED_VALUE",
        "to": wallet,
        "submit": True
    }
    # API Call
    response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))

    # executed log
    executed = str(counter) + ". " + name + ", " + str(response.content) + "\n\n\n"
    print(str(counter) + ": " + str(response.status_code))
    log.write(executed)

    counter += 1
    # failed to transfer klay
    if response.status_code == 400:
        failed.append(name)


# Result
print("\nTotal: " + str(counter - 1))
print(failed)
log.close()


