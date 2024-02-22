from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


def main(param_dict):
    try:
        client = Cloudant.iam(
            account_name=param_dict["7422baae-6c44-4421-b623-3f102f8da609-bluemix"],
            api_key=param_dict["ewGwrRie9LjB-kT6jEzJRtpMn14CaWzytHztRmFWHt1v"],
            connect=True,
        )
        print(f"Databases: {client.all_dbs()}")
    except CloudantException as cloudant_exception:
        print("unable to connect")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {"dbs": client.all_dbs()}
