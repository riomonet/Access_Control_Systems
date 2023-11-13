import xml.etree.ElementTree as ET
import requests

def open ():

    params = {
        'cmd': 'relay',
        'GetAll': ''
    }

    set_params = {
        'cmd': 'relay',
        'Vehicle': 0
    }

    res = requests.get('http://192.168.1.191/UHCapi.xml', params=params)
    cur_root = ET.fromstring(res.content)

    cur_state = cur_root.getchildren()[0].text

    if cur_state == 'On':
        set_params['Vehicle'] = 0
    else:
        set_params['Vehicle'] = 1

    set_state = requests.get('http://192.168.1.191/UHCapi.xml', params=set_params)
    new_root = ET.fromstring(set_state.content)
    new_state = new_root.getchildren()[0].text
    return {'Vehicle_Relay': new_state}


def open_pedestrian ():

    params = {
        'cmd': 'relay',
        'GetAll': ''
    }

    set_params = {
        'cmd': 'relay',
        'Pedestrian': 0
    }

    res = requests.get('http://192.168.1.191/UHCapi.xml', params=params)
    cur_root = ET.fromstring(res.content)

    cur_state = cur_root.getchildren()[1].text

    if cur_state == 'On':
        set_params['Pedestrian'] = 0
    else:
        set_params['Pedestrian'] = 1

    set_state = requests.get('http://192.168.1.191/UHCapi.xml', params=set_params)
    new_root = ET.fromstring(set_state.content)
    new_state = new_root.getchildren()[0].text
    return {'Pedestrian_Relay': new_state}
