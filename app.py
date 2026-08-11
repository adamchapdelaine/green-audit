# Build out Mock API First

# write POST /api/analyze route
# Accept company name in JSON payload, return mock JSON data
# Return dict structure that includes:
    # company_name:string
    # greenwashing_score: (0-100)
    # claims_vs_reality: list of objects (e.g., claim vs. actual finding)
    # emissions_data: list of years and tonnage (frontend charts)

from flask import Flask, render_template, request, redirect, session
from services import climate_service

app = Flask(__name__)

@app.route("/api/analyze", methods=['POST'])

def analyze_company():
    data = request.get_json()
    return climate_service.get_company_analysis(data["company_name"])
    
if __name__ == "__main__":
    app.run(debug=True)