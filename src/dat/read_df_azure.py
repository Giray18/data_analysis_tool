import pandas as pd
from azure.storage.blob import BlobServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions
from datetime import datetime, timedelta, date
import dat


def create_account_sas(account_name: str, account_key: str):
    # Create an account SAS that's valid for one day
    start_time = datetime.utcnow()
    expiry_time = start_time + timedelta(days=1)

    # Define the SAS token permissions
    sas_permissions=AccountSasPermissions(read=True)

    # Define the SAS token resource types
    # For this example, we grant access to service-level APIs
    sas_resource_types=ResourceTypes(object=True)

    sas_token = generate_account_sas(
        account_name=account_name,
        account_key=account_key,
        resource_types=sas_resource_types,
        permission=sas_permissions,
        expiry=expiry_time,
        start=start_time
    )

    return sas_token



def df_read_azure_single_file(storage_account_name, account_key, blob_name, container_name, file_name = []):
    ''' Returns dataframe by reading defined dataset from defined source
    blob name == file name with full extension like "event.csv"'''

    # Creating service client var 
    blob_service_client = BlobServiceClient(account_url=f"https://{storage_account_name}.blob.core.windows.net"
                                            , credential=create_account_sas(storage_account_name,account_key))
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = container_client.get_blob_client(blob_name)
    
    # df = pd.read_csv(blob_client.download_blob())
    # blob_service_client.get_blob_to_path(container_name,blob_name,file_name)
    if "csv" in blob_name.split("."):
        blob_name = blob_name.split(".")
        # df = pd.read_csv(f"{file_name}")
        df = pd.read_csv(blob_client.download_blob())
    elif "parquet" or "pqt" in blob_name.split("."):
        blob_name = blob_name.split(".")
        df = pd.read_parquet(blob_client.download_blob())
    else:
        print("Unavailable file format")
    return df




# if __name__ == '__main__':
#     df_read_azure()