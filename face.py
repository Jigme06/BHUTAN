from engine import KnowledgeEngine

def run_dashboard():
    engine = KnowledgeEngine("data.json")
    
    engine.load_data()
    
    print("--- ENGINE ONLINE ---")

    online = True

    while online:
        print (
            " 0: Search Sites by Type"
            " 1: Shut Down Engine"
            )
        
        user_choice = input('Enter Choice:')

        if user_choice == "0":
            print("\n KUZUZANGPO Searching Sites....") 

            site_type = input('What type of site are you looking for today?:' \
            '\n 1: Dzongs' 
            '\n 2: Monasteries and Other Neys')
    
            if site_type == "1":
                results = engine.find_sites_by_type("Dzong") 
                
                print("\n--- Found Sites ---")
                for site in results:
                    print(f"- {site.name} (Located in {site.loc})")
            elif site_type == "2":
                results = engine.find_sites_by_type("Monastery") 
                print("\n--- Found Monasteries & Neys ---")
                for site in results:
                    print(f"- {site.name} (Located in {site.loc})")

            else:
                print("\n !!! INVALID CHOICE")


        elif user_choice == "1":
            print("\n Shutting Down Engine. Tashi Delek")
            online = False
        else:
            print("\n !!! Invalid Choice !!!")


if __name__ == "__main__":
    run_dashboard()
       