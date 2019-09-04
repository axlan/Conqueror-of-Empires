
# Gameplay Summery

* You are the intelligence cheif for a nation at war and need to assign resources toward espianage and reconisance and make decisions based on the gathered intelligence.

* Gathered intelligence can either be imprecise, or intetionally misleading.

* Random generated enemy movements

* Predetermined maps, need to complete a compaign, no save scumming. 

# Decisions

* Setting
* Civilian collateral damage?
* Name "Enemy Uknown Unknown", Fog of War
* Have commanders with different AI controlling troops

# Execution

1. XXX Start with "Conqueror of Empires" codebase
2. XXX Create menu for first mission
    1. XXX Text screen to give back story
    2. XXX Menu to choose to spend money on intelligence
    3. View map overlayed with intelligence
    4. Deploy troops
    5. Battle
    6. Results
3. Refactor
    1. Move into new repo
    2. Seperate UI into it's own repo
    3. Wrap the control logic so that it can be reused for multiple levels
    4. Add back in an initial menu with load / save
    5. Move level descriptions and scripts to assets
