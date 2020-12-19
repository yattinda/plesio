def uptoblob(filepath):
    import os, uuid, sys
    from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

    try:
        blob_service_client = BlockBlobService(
            account_name='',
            account_key='')

        print("#######################")
        container_name = 'takeface'
        blob_service_client.create_container(container_name)
        blob_service_client.set_container_acl(
            container_name, public_access=PublicAccess.Container)

        ## TODO: def namerule
        local_name = ""
        fullpath = os.path.join()
        blob_service_client.create_blob_from_path(
            container_name, local_name, fullpath)

        ## TODO: delete local local_path
        ## TODO: after roop, delete container
    except Exception as ex:
        print('Exception:')
        print(ex)
