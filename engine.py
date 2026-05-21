import json
from BHUTAN import CulturalSite
import requests

class KnowledgeEngine:
    def __init__(self,file_path : str):
        self.file = file_path
        self.sites = []

    def load_data(self):
        with open(self.file,'r') as f:
            raw_data = json.load(f)

        
            for item in raw_data:
                if 'name' in item and 'build_date' in item and 'location' in item:
                    site_obj = CulturalSite(
                        name = item['name'],
                        founded_year = item['build_date'],
                        location_dzongkhag = item['location']
                    )
                    self.sites.append(site_obj)
                else:
                    print(f'Warning: Skipping incomplete item {item}')

    




            





