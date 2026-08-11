# Built out Mock API First

# write POST /api/analyze route
# Accept company name in JSON payload, return mock JSON data
# Return dict structure that includes:
    # company_name:string
    # greenwashing_score: (0-100)
    # claims_vs_reality: list of objects (e.g., claim vs. actual finding)
    # emissions_data: list of years ans tonnage (frontend charts)

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route("/api/analyze", methods=['POST'])

def analyze_company():
    request.get_json(company_name)
    mock_dict = {
        "company_name": "Boeing",
        "greenwashing_score": 63,
        "claims_vs_reality": list,
        "emissions_data": 1
    }