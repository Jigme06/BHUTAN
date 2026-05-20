import json
from BHUTAN import Dzongkhag, CulturalSite

class KnowledgeEngine:
    def __init__(self,file_path : str):
        self.file = file_path
        self.dict = {}

    def load_data(self):
        with open(self.file,'r') as f:
            raw_data = json.load(f)

        
            for item in raw_data:
                if 'name' in item:
                    dis_obj = Dzongkhag(
                        name = item['name'],
                        pop = item['population'],
                        for_cov= item['forest_cover_pct']
                        )
                

                    raw_sites = item.get('cultural_sites',[])

                    for site in raw_sites:
                        site_obj = CulturalSite(
                                name = site['site_name'],
                                site_type = site['category'],
                                founded_year = site['year_established'],
                                location_dzongkhag = dis_obj.name
                                )
                        dis_obj.add_site(site_obj)

                    self.dict[dis_obj.name] = dis_obj

                else:
                    print(f'Warning: Skipping {item}')

    def find_sites_by_type(self, site_type: str):
        matching_sites = []
        for dzongkhag_obj in self.dict.values():
            for site in dzongkhag_obj.sites:
                if site.type.lower() == site_type.lower():
                    matching_sites.append(site)
        return matching_sites

            





