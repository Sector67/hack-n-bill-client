#!/usr/bin/python

import requests
import json

class SectorAdmin:

    def GetAuthorizedUsers(waste, nodeId):
        response = requests.get('http://www.drupal.sector67.org/temp_service.php?action=users_for_machine&machine_id={0}'.format(nodeId))
        data = json.loads(response.text)
        return data
