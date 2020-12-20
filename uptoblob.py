def uptoblob(container_name, filepath, filenum):
    import os, uuid, sys
    from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

    try:
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        #container_name = 'takeface'
        # blob_service_client.create_container(container_name)
        # blob_service_client.set_container_acl(
        #     container_name, public_access=PublicAccess.Container)

        ## TODO: def namerule
        local_name = "{}.jpg".format(filenum)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_name)

        with open(filepath, "rb") as data:
            blob_client.upload_blob(data)

        os.remove(filepath)

        ## TODO: delete local local_path
        ## TODO: after roop, delete container
    except Exception as ex:
        print('Exception:')
        print(ex)
