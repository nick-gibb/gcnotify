import csv
import logging
import os
import sys

from dotenv import load_dotenv, find_dotenv
from notifications_python_client.notifications import NotificationsAPIClient

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
load_dotenv(find_dotenv())

api_key = os.getenv("api_key")
template_id = os.getenv("template_id")

base_url = "https://api.notification.alpha.canada.ca"

notifications_client = NotificationsAPIClient(api_key, base_url)


def send_messages(send_list):
    logging.info(f'Sending {len(send_list)} emails.')
    for recipient in send_list:
        response = notifications_client.send_email_notification(
            email_address=recipient['email_address'],
            template_id=template_id,
            personalisation=recipient['personalisation']
        )
    logging.info(f'Emails sent.')


def prepare_inputs_from_csv(filepath):
    logging.info(f'Preparing inputs from {filepath}.')
    send_list = []
    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None)  # skip header
        for row in reader:
            send_list.append({
                'email_address': row[0],
                'personalisation': {
                    'firstname': row[1],
                    'date': row[2]
                }
            })
    logging.info('Inputs prepared.')
    return send_list


def main(argv):
    send_list = prepare_inputs_from_csv(argv[1])
    send_messages(send_list)


if __name__ == "__main__":
    main(sys.argv)
