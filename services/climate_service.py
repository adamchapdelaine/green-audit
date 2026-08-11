
def get_company_analysis(company_name):
    mock_dict = {
            "company_name": company_name,
            "greenwashing_score": 63,
            "claims_vs_reality": [{"claim": "...", "reality": "..."}],
            "emissions_data": [{"year": 2023, "tonnage": 1200}, {"year": 2024, "tonnage": 1250}]
    }
    return mock_dict