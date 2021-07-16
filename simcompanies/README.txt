
in static/js/Building/Building.tsx...
const administrationCostWithExecsImpact = administrationOverhead ? getAdministrationOverheadWithExecsImpact(administrationOverhead, skillCOO) : 1;
    const wages = (buildingConstant && building && administrationOverhead) ? buildingConstant.wages*building.size*administrationCostWithExecsImpact : null;


Go to resource page
https://www.simcompanies.com/encyclopedia/resource/3/
In Chrome Devtools
  Sources
  static/js/Utils/Utils.tsx

const profitPerUnit = (
  salesModifier,
  price,
  quality,
  marketSaturation,
  retailModeling,
  administrationOverhead,
  storeBaseSalary
) => {
  return price - (storeBaseSalary * administrationOverhead)/unitsSoldAnHour(salesModifier, price, quality, marketSaturation, retailModeling);
};

    # storeBaseSalary is dict key "storeBaseSalary"
    # also check "retailable: True"
    # administrationOverhead is the same for all resources
    # ie, perhaps in the core User data
    # ../Redux/Actions/UserActions
    # api_v2_players_administration_overhead
    # https://www.simcompanies.com/api/v2/players/me/administration-overhead/
