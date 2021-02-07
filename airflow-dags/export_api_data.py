import requests
import datetime
import json

from constant import Constant
from read_config import Config

config , stage = Config.config , Config.stage

def export_data_to_json():
    try:
        start_date = config.get(stage, Constant.START_DATE)
        end_date = str(datetime.datetime.now().date())
        url = config.get(stage, Constant.API_URL)
        url=url.format(start_date,end_date)
        print(url)
        response = requests.get(url)
        response= response.json()
        with open(Constant.JSON_OUTPUT_FILE, 'w') as outfile:
            json.dump(response, outfile)
    except requests.exceptions.HTTPError as errh:
        raise(errh)
    except requests.exceptions.ConnectionError as errc:
        raise(errc)
    except requests.exceptions.Timeout as errt:
        raise(errt)
    except requests.exceptions.RequestException as err:
        raise(err)