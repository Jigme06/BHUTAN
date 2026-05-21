class CulturalSite:

    def __init__(self,name:str,founded_year: int,location_dzongkhag: str):

        self.name =  name
        self.year = founded_year
        self.loc = location_dzongkhag

class Dzongkhag:
    def __init__(self,name:str,pop:int,for_cov:float):
        self.name = name
        self.population = pop
        self.forestCoverage = for_cov
        self.sites = []

    def add_site(self,site):
        if site not in self.sites:
            self.sites.append(site)