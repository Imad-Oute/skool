import argparse
from uuid import uuid4

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

# Note: Broad Match Modifier (+keyword) is deprecated. 
# We use BROAD match instead.
CAMPAIGNS_DATA = [
    {
        "name": f"[RA] Senior - Mutuelle Santé - Call Only #{uuid4().hex[:8]}",
        "budget_micros": 25000000,
        "ad_groups": [
            {
                "name": "S1 : Changement de mutuelle",
                "keywords": [
                    {"text": "mutuelle santé senior", "match_type": "PHRASE"},
                    {"text": "changer de mutuelle après 60 ans", "match_type": "PHRASE"},
                    {"text": "comparateur mutuelle retraité", "match_type": "PHRASE"},
                    {"text": "meilleure mutuelle pour retraité", "match_type": "PHRASE"},
                    {"text": "mutuelle senior pas cher", "match_type": "PHRASE"},
                    {"text": "mutuelle complémentaire santé senior", "match_type": "PHRASE"},
                    {"text": "courtier mutuelle senior", "match_type": "BROAD"},
                    {"text": "simulation mutuelle retraité", "match_type": "BROAD"},
                ]
            },
            {
                "name": "S2 : Urgence soins / remboursements",
                "keywords": [
                    {"text": "mutuelle dentaire senior", "match_type": "PHRASE"},
                    {"text": "remboursement prothèse auditive mutuelle", "match_type": "PHRASE"},
                    {"text": "mutuelle optique senior", "match_type": "PHRASE"},
                    {"text": "reste à charge retraité mutuelle", "match_type": "PHRASE"},
                    {"text": "mutuelle 100% santé senior", "match_type": "PHRASE"},
                    {"text": "prise en charge auditive mutuelle", "match_type": "PHRASE"},
                    {"text": "mutuelle couronne dentaire remboursement", "match_type": "BROAD"},
                    {"text": "implant dentaire mutuelle senior", "match_type": "BROAD"},
                ]
            },
            {
                "name": "S3 : Hausse cotisation / résiliation Châtel",
                "keywords": [
                    {"text": "résiliation mutuelle hausse tarif", "match_type": "PHRASE"},
                    {"text": "mutuelle moins chère +60 ans", "match_type": "PHRASE"},
                    {"text": "loi Châtel résiliation mutuelle", "match_type": "PHRASE"},
                    {"text": "résilier mutuelle santé", "match_type": "PHRASE"},
                    {"text": "mutuelle trop chère retraite", "match_type": "PHRASE"},
                    {"text": "résilier mutuelle sans pénalité", "match_type": "BROAD"},
                ]
            }
        ],
        "ads": [
            {
                "headline_1": "Mutuelle Senior Devis Gratuit",
                "headline_2": "Courtier Indépendant 55+",
                "description": "Comparez les meilleures mutuelles adaptées à votre retraite. Appelez maintenant.",
                "business_name": "Rolland Assurances",
                "phone_number": "+33100000000",
                "country_code": "FR",
                "path_1": "mutuelle",
                "path_2": "senior",
                "verification_url": "https://rollandassurances.com/mutuelle-senior"
            },
            {
                "headline_1": "Votre Mutuelle Trop Chère ?",
                "headline_2": "Économisez Courtier Retraités",
                "description": "Hausse de tarif ? Notre courtier vous trouve une meilleure offre. Appelez-nous.",
                "business_name": "Rolland Assurances",
                "phone_number": "+33100000000",
                "country_code": "FR",
                "path_1": "mutuelle",
                "path_2": "senior",
                "verification_url": "https://rollandassurances.com/mutuelle-senior"
            }
        ],
        "negative_keywords": [
            "mutuelle animaux", "mutuelle étudiante", "mutuelle entreprise",
            "mutuelle collective", "mutuelle obligatoire salarié", "MAAF avis",
            "Axa tarif", "April contact", "Harmonie avis", "MGEN",
            "résiliation mutuelle modèle lettre", "formulaire résiliation",
            "lettre type", "gratuit"
        ]
    },
    {
        "name": f"[RA] BTP - Décennale - Call Only #{uuid4().hex[:8]}",
        "budget_micros": 25000000,
        "ad_groups": [
            {
                "name": "D1 : Urgence attestation",
                "keywords": [
                    {"text": "assurance décennale urgent", "match_type": "PHRASE"},
                    {"text": "assurance décennale immédiate", "match_type": "PHRASE"},
                    {"text": "attestation décennale rapide", "match_type": "PHRASE"},
                    {"text": "décennale en 24h", "match_type": "PHRASE"},
                    {"text": "assurance décennale express", "match_type": "PHRASE"},
                    {"text": "obtenir attestation décennale vite", "match_type": "BROAD"},
                ]
            },
            {
                "name": "D2 : Création / première décennale",
                "keywords": [
                    {"text": "assurance décennale artisan", "match_type": "PHRASE"},
                    {"text": "décennale auto entrepreneur bâtiment", "match_type": "PHRASE"},
                    {"text": "assurance décennale maçon", "match_type": "PHRASE"},
                    {"text": "décennale électricien", "match_type": "PHRASE"},
                    {"text": "décennale plombier", "match_type": "PHRASE"},
                    {"text": "décennale couvreur", "match_type": "PHRASE"},
                    {"text": "décennale carreleur", "match_type": "PHRASE"},
                    {"text": "assurance décennale peintre", "match_type": "PHRASE"},
                    {"text": "assurance décennale devis", "match_type": "PHRASE"},
                    {"text": "souscrire décennale artisan", "match_type": "BROAD"},
                    {"text": "assurance décennale nouveau artisan", "match_type": "BROAD"},
                ]
            },
            {
                "name": "D3 : Changement assureur / moins cher",
                "keywords": [
                    {"text": "changer assurance décennale", "match_type": "PHRASE"},
                    {"text": "assurance décennale moins chère", "match_type": "PHRASE"},
                    {"text": "résiliation décennale", "match_type": "PHRASE"},
                    {"text": "comparateur décennale professionnel", "match_type": "PHRASE"},
                    {"text": "assurance décennale pas cher artisan", "match_type": "PHRASE"},
                    {"text": "décennale meilleur prix courtier", "match_type": "BROAD"},
                ]
            },
            {
                "name": "D4 : Profils complexes / refusés ailleurs",
                "keywords": [
                    {"text": "assurance décennale refusée", "match_type": "PHRASE"},
                    {"text": "décennale sinistre antérieur", "match_type": "PHRASE"},
                    {"text": "assurance décennale artisan étranger", "match_type": "PHRASE"},
                    {"text": "décennale sans expérience", "match_type": "PHRASE"},
                    {"text": "assurance décennale tous risques", "match_type": "PHRASE"},
                    {"text": "décennale refus assureur solution", "match_type": "BROAD"},
                ]
            }
        ],
        "ads": [
            {
                "headline_1": "Décennale Attestation 24h",
                "headline_2": "Courtier BTP Expert Appelez",
                "description": "Besoin urgent d'une attestation décennale ? Devis rapide tous métiers.",
                "business_name": "Rolland Assurances",
                "phone_number": "+33100000000",
                "country_code": "FR",
                "path_1": "assurance",
                "path_2": "decennale",
                "verification_url": "https://rollandassurances.com/assurance-decennale"
            },
            {
                "headline_1": "Décennale Obligatoire Devis",
                "headline_2": "10+ Assureurs En 1 Appel",
                "description": "Loi Spinetta : obligation légale pour artisans. Notre courtier vous protège.",
                "business_name": "Rolland Assurances",
                "phone_number": "+33100000000",
                "country_code": "FR",
                "path_1": "assurance",
                "path_2": "decennale",
                "verification_url": "https://rollandassurances.com/assurance-decennale"
            }
        ],
        "negative_keywords": [
            "assurance décennale définition", "c'est quoi la décennale", "loi spinetta explication",
            "durée décennale", "décennale promoteur", "décennale maître d'ouvrage", "code des assurances",
            "jurisprudence décennale", "modèle contrat", "gratuit", "formation", "cours", "certification", "étude"
        ]
    }
]

def create_campaign(client, customer_id, campaign_data):
    campaign_budget_service = client.get_service("CampaignBudgetService")
    campaign_service = client.get_service("CampaignService")
    
    # 1. Create a budget
    campaign_budget_operation = client.get_type("CampaignBudgetOperation")
    campaign_budget = campaign_budget_operation.create
    campaign_budget.name = f"Budget for {campaign_data['name']}"
    campaign_budget.delivery_method = client.enums.BudgetDeliveryMethodEnum.STANDARD
    campaign_budget.amount_micros = campaign_data["budget_micros"]

    budget_response = campaign_budget_service.mutate_campaign_budgets(
        customer_id=customer_id, operations=[campaign_budget_operation]
    )
    budget_resource_name = budget_response.results[0].resource_name
    print(f"Created campaign budget: {budget_resource_name}")

    # 2. Create a campaign
    campaign_operation = client.get_type("CampaignOperation")
    campaign = campaign_operation.create
    campaign.name = campaign_data["name"]
    campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
    campaign.status = client.enums.CampaignStatusEnum.PAUSED  # Created paused for safety
    campaign.manual_cpc.enhanced_cpc_enabled = False
    campaign.campaign_budget = budget_resource_name
    
    # Network settings: Target only Google Search
    campaign.network_settings.target_google_search = True
    campaign.network_settings.target_search_network = False
    campaign.network_settings.target_content_network = False
    campaign.network_settings.target_partner_search_network = False

    campaign_response = campaign_service.mutate_campaigns(
        customer_id=customer_id, operations=[campaign_operation]
    )
    campaign_resource_name = campaign_response.results[0].resource_name
    print(f"Created campaign: {campaign_resource_name}")

    # 3. Create negative keywords
    create_campaign_negative_keywords(client, customer_id, campaign_resource_name, campaign_data["negative_keywords"])

    for ad_group_data in campaign_data["ad_groups"]:
        ad_group_resource_name = create_ad_group(client, customer_id, campaign_resource_name, ad_group_data)
        create_keywords(client, customer_id, ad_group_resource_name, ad_group_data["keywords"])
        create_call_ads(client, customer_id, ad_group_resource_name, campaign_data["ads"])

def create_ad_group(client, customer_id, campaign_resource_name, ad_group_data):
    ad_group_service = client.get_service("AdGroupService")
    ad_group_operation = client.get_type("AdGroupOperation")
    ad_group = ad_group_operation.create
    ad_group.name = f"{ad_group_data['name']} #{uuid4().hex[:8]}"
    ad_group.status = client.enums.AdGroupStatusEnum.ENABLED
    ad_group.campaign = campaign_resource_name
    ad_group.type_ = client.enums.AdGroupTypeEnum.SEARCH_STANDARD
    ad_group.cpc_bid_micros = 5000000  # Default bid 5 EUR

    ad_group_response = ad_group_service.mutate_ad_groups(
        customer_id=customer_id, operations=[ad_group_operation]
    )
    resource_name = ad_group_response.results[0].resource_name
    print(f"Created ad group: {resource_name}")
    return resource_name

def create_keywords(client, customer_id, ad_group_resource_name, keywords):
    ad_group_criterion_service = client.get_service("AdGroupCriterionService")
    operations = []
    
    for kw in keywords:
        operation = client.get_type("AdGroupCriterionOperation")
        criterion = operation.create
        criterion.ad_group = ad_group_resource_name
        criterion.status = client.enums.AdGroupCriterionStatusEnum.ENABLED
        criterion.keyword.text = kw["text"]
        
        if kw["match_type"] == "PHRASE":
            criterion.keyword.match_type = client.enums.KeywordMatchTypeEnum.PHRASE
        elif kw["match_type"] == "BROAD":
            criterion.keyword.match_type = client.enums.KeywordMatchTypeEnum.BROAD
            
        operations.append(operation)

    if operations:
        response = ad_group_criterion_service.mutate_ad_group_criteria(
            customer_id=customer_id, operations=operations
        )
        print(f"Created {len(response.results)} keywords for Ad Group {ad_group_resource_name}.")

def create_call_ads(client, customer_id, ad_group_resource_name, ads_data):
    ad_group_ad_service = client.get_service("AdGroupAdService")
    operations = []

    for ad_data in ads_data:
        operation = client.get_type("AdGroupAdOperation")
        ad_group_ad = operation.create
        ad_group_ad.ad_group = ad_group_resource_name
        ad_group_ad.status = client.enums.AdGroupAdStatusEnum.ENABLED

        # Set call ad info
        ad_group_ad.ad.call_ad.headline_1 = ad_data["headline_1"]
        ad_group_ad.ad.call_ad.headline_2 = ad_data["headline_2"]
        ad_group_ad.ad.call_ad.description_1 = ad_data["description"]
        ad_group_ad.ad.call_ad.business_name = ad_data["business_name"]
        ad_group_ad.ad.call_ad.phone_number = ad_data["phone_number"]
        ad_group_ad.ad.call_ad.country_code = ad_data["country_code"]
        ad_group_ad.ad.call_ad.path_1 = ad_data["path_1"]
        ad_group_ad.ad.call_ad.path_2 = ad_data["path_2"]
        ad_group_ad.ad.call_ad.call_tracking_enabled = True
        
        # Append verification URL to the ad
        ad_group_ad.ad.final_urls.append(ad_data["verification_url"])
        
        operations.append(operation)

    if operations:
        response = ad_group_ad_service.mutate_ad_group_ads(
            customer_id=customer_id, operations=operations
        )
        print(f"Created {len(response.results)} Call Ads for Ad Group {ad_group_resource_name}.")

def create_campaign_negative_keywords(client, customer_id, campaign_resource_name, negative_keywords):
    campaign_criterion_service = client.get_service("CampaignCriterionService")
    operations = []

    for kw in negative_keywords:
        operation = client.get_type("CampaignCriterionOperation")
        criterion = operation.create
        criterion.campaign = campaign_resource_name
        criterion.negative = True
        criterion.keyword.text = kw
        criterion.keyword.match_type = client.enums.KeywordMatchTypeEnum.BROAD

        operations.append(operation)

    if operations:
        response = campaign_criterion_service.mutate_campaign_criteria(
            customer_id=customer_id, operations=operations
        )
        print(f"Created {len(response.results)} negative keywords for Campaign {campaign_resource_name}.")

def main(customer_id):
    try:
        # Client initialized using config from GOOGLE_ADS_CONFIGURATION_FILE_PATH or google-ads.yaml
        client = GoogleAdsClient.load_from_storage()
        print(f"Executing creation script for Customer ID: {customer_id}")
        
        for campaign_data in CAMPAIGNS_DATA:
            create_campaign(client, customer_id, campaign_data)
            
        print("\nNote: Campaigns are created in a PAUSED state.")
        print("Please review them in the Google Ads UI before enabling.")
        
    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f"GoogleAdsException Error: {error.message}")
    except Exception as e:
         print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Rolland Assurances Campaigns")
    parser.add_argument("-c", "--customer_id", type=str, required=True, help="The Google Ads customer ID without hyphens.")
    args = parser.parse_args()
    main(args.customer_id)
