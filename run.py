from engine import KnowledgeEngine

engine = KnowledgeEngine("data.json")
engine.load_data()

print("🚀 Knowledge Engine successfully booted and loaded data!\n")

# 2. Test: Query a specific Dzongkhag's stats and nested sites
print("--- Test 1: Fetching Paro ---")
paro = engine.dict.get("Paro")
if paro:
    print(f"District: {paro.name}")
    print(f"Population: {paro.population:,}")
    print(f"Forest Cover: {paro.forestCoverage}%")
    print("Linked Cultural Sites:")
    for site in paro.sites:
        print(f"  * {site.name} ({site.type}) - Est. {site.year}")
else:
    print("Paro not found!")

print("\n" + "="*40 + "\n")

# 3. Test: Run a global cross-district query using your new method
print("--- Test 2: Global Search for 'Dzong' ---")
all_dzongs = engine.find_sites_by_type("Dzong")
print(f"Found {len(all_dzongs)} Dzongs across all districts:")
for dzong in all_dzongs:
    print(f"  * {dzong.name} (Located in: {dzong.loc})")