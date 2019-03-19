# Simple code to upload/download files to/from OneDrive.
# Reference: https://github.com/OneDrive/onedrive-sdk-python/tree/master/examples
# For more functions, follow the link above

# pip install onedrivesdk

from __future__ import unicode_literals

import onedrivesdk
from onedrivesdk.helpers import GetAuthCodeServer
import os


def main():

    # authentiicate
    redirect_uri = "http://localhost:8080/"
    client_secret = "BqaTYqI0XI7wDKcnJ5i3MvLwGcVsaMVM"

    client = onedrivesdk.get_default_client(client_id='00000000481695BB',
                                            scopes=['wl.signin',
                                                    'wl.offline_access',
                                                    'onedrive.readwrite'])
    auth_url = client.auth_provider.get_auth_url(redirect_uri)

    
    code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
    client.auth_provider.authenticate(code, redirect_uri, client_secret)

    while True:
        print("")
        items = client.item(id="root").children.get()
        count = 0
        # print items in root directory
        for count, item in enumerate(items):
            print("{} {}".format(count+1, item.name if item.folder is None else "/"+item.name))
        
        selected = input("Enter an item id to download, or enter U to upload, or enter Q to quit: ")
        
        if selected == 'Q':
            exit()

        elif selected == 'U':
            try:
                upload(client, "root")
                print("Successfully uploaded.")
            except Exception as e:
                print(e)

        else:
            selected = int(selected)
            if items[selected-1].folder is None:
                try: 
                    download(client, items[selected-1].id, items[selected-1].name)
                    print("Successfully downloaded.")
                except Exception as e:
                    print(e)
            else:
                print("Error: Can't download a folder.")


def download(client, item_id, item_name):
    # download the item to the current working directory
    download_path = os.getcwd() + '/' + item_name
    client.item(id=item_id).download(download_path)

def upload(client, item_id):
    # upload an item in the current working directory to OneDrive root directory
    item_name = input("Enter file name with extension: ")
    upload_path = os.getcwd() + '/' + item_name
    client.item(id=item_id).children[item_name].upload(upload_path)


if __name__ == '__main__':
    main()
