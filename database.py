import config
from azure.cosmos import CosmosClient, PartitionKey, exceptions
import json


URL = config.settings["url"]
ENDPOINT = config.settings["endpoint"]
MASTER_KEY = config.settings["master_key"]
CLIENT = CosmosClient(URL, MASTER_KEY)
DATABASE_NAME = config.settings["database_name"]
CONTAINER_NAME = config.settings["container_name"]

database = CLIENT.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)


def user_by_id(id):

    for user in container.query_items(
        query=f"SELECT * FROM container r WHERE r.id=@id",
        parameters=[{"name": "@id", "value": id}],
        enable_cross_partition_query=True,
    ):
        result = json.dumps(user, indent=True)
        return result


def user_by_userid(userId):
    for user in container.query_items(
        query=f"SELECT * FROM container r WHERE r.userId=@userId",
        parameters=[{"name": "@userId", "value": userId}],
        enable_cross_partition_query=True,
    ):
        result = json.dumps(user, indent=True)
        return result


def all_users():
    users = list(container.read_all_items())
    return json.dumps(users, indent=True)


def get_new_user(id, userId, firstName, lastName):
    user = {
        "id": id,
        "userId": userId,
        "firstName": firstName,
        "lastName": lastName,
    }

    return user


# def visAlle(self):
#     try:
#         self.cursor.execute("SELECT * FROM oppslag ORDER BY dato ASC")
#         result = self.cursor.fetchall()
#     except mysql.connector.Error as err:
#         print(err)
#     return result


# def visOppslag(self, id):
#     try:
#         self.cursor.execute("SELECT * FROM oppslag WHERE id=(%s)", (id,))
#         result = self.cursor.fetchone()
#     except mysql.connector.Error as err:
#         print(err)
#     return result


# def visAlleKategori(self):
#     try:
#         self.cursor.execute("SELECT * FROM kategori ORDER BY navn ASC")
#         result = self.cursor.fetchall()
#     except mysql.connector.Error as err:
#         print(err)
#     return result


# def visOppslagByKategori(self, kat_id):
#     try:
#         self.cursor.execute(
#             "SELECT id, tittel, ingress, dato from oppslag, kategori where oppslag.kategori = kategori.kat_id and kategori.kat_id = (%s)", (kat_id,))
#         result = self.cursor.fetchall()
#     except mysql.connector.Error as err:
#         print(err)
#     return result


# def create_database(client, database_name):
#     try:
#         database = client.create_database(id=database_name)
#         print(f'Database with id {database_name} was created.')
#         return database
#     except exceptions.CosmosResourceExistsError:
#         database = client.get_database_client(database_name)
#         print(f'A database with id {database_name} already exists')
#         return database


# def create_container(database_name, container_name):
#     try:
#         container = database_name.create_container(
#             id=container_name, partition_key=PartitionKey(path='/userId'))
#         print(f'Container with id {id} created')
#         return container
#     except exceptions.CosmosResourceExistsError:
#         container = database_name.get_container_client(container_name)
#         print(f'Container with id {id} already exists')
#         return container


# database = create_database(CLIENT, DATABASE_NAME)

# container = create_container(database, CONTAINER_NAME)
