import json
from BHUTAN import CulturalSite
import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

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

    def fetch_wikipedia_summary(self, site_name: str):
        headers = {
            'User-Agent': 'BhutanCulturalEngine/1.0'
        }
        
        search_url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={site_name}&limit=1&format=json&origin=*"
        
        try:
            search_response = requests.get(search_url, headers=headers, timeout=10)
            search_data = search_response.json()
            
            if len(search_data) > 1 and len(search_data[1]) > 0:
                official_title = search_data[1][0]
                
                summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{official_title.replace(' ', '_')}"
                summary_response = requests.get(summary_url, headers=headers, timeout=10)
                
                if summary_response.status_code == 200:
                    return summary_response.json().get('extract', 'No description found.')
                else:
                    return f"Summary error: Received status {summary_response.status_code}"
            else:
                return "No matching page found on Wikipedia."
            
        except Exception as e:
            return f"Error connecting to Wikipedia: {str(e)}"

    def get_stats(self,indicator):
        url = f"https://api.worldbank.org/v2/country/BT/indicator/{indicator}?format=json&per_page=5"
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
            data = response.json()
            
            if len(data) > 1 and data[1]:
                for entry in data[1]:
                    if entry.get('value') is not None:
                        return entry['value'], entry['date']
            
            return None, "No Data Found"
            
        except Exception as e:
            return None, str(e)
        
    def get_coordinates(self,loc:str):
        if loc == "Singye Dzong":
            return (27.9724, 91.2991)
        elif loc == "Membartsho":
            return (27.5403, 90.8128)
        else:
            api_key = os.getenv("GEO_API_KEY")

            url = f"https://api.geoapify.com/v1/geocode/search?text={loc},+Bhutan&apiKey={api_key}"

            response = requests.get(url)
            data = response.json()

            result = data['features'][0]
            coords = result['geometry']['coordinates']
            return (coords[1],coords[0])









            





