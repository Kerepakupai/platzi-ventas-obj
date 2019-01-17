import csv

from clients.models import Client as ClientModel


class Client:

    def __init__(self, table):
        self.table = table

    def create_client(self, client):
        with open(self.table, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=ClientModel.schema())
            writer.writerow(client.to_dic())
