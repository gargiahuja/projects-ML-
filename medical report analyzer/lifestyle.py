def generate_full_suggestions(report):
    suggestions = {}

    if "HbA1c" in report:
        val = report["HbA1c"]
        if val > 6.5:
            suggestions["HbA1c"] = "High HbA1c indicates diabetes. Follow a low-carb diet, exercise daily, and monitor glucose."
        elif val > 5.7:
            suggestions["HbA1c"] = "Borderline HbA1c. Reduce sugar intake and increase physical activity."
        else:
            suggestions["HbA1c"] = "HbA1c is normal. Continue healthy eating and active lifestyle."

    if "Estimated Avg Glucose" in report:
        val = report["Estimated Avg Glucose"]
        if val > 126:
            suggestions["Estimated Avg Glucose"] = "Glucose levels are high. Control sugar and carbs in your diet."
        else:
            suggestions["Estimated Avg Glucose"] = "Glucose levels are normal."

    if "Fasting Glucose" in report:
        val = report["Fasting Glucose"]
        if val > 125:
            suggestions["Fasting Glucose"] = "Fasting glucose suggests diabetes. Limit refined carbs, exercise, and check regularly."
        elif val > 100:
            suggestions["Fasting Glucose"] = "Borderline fasting glucose. Control sugar intake and stay active."
        else:
            suggestions["Fasting Glucose"] = "Fasting glucose is normal."

    if "Total Bilirubin" in report:
        if report["Total Bilirubin"] > 1.2:
            suggestions["Total Bilirubin"] = "High bilirubin may suggest liver issues. Avoid alcohol, drink plenty of water, eat light foods."
        else:
            suggestions["Total Bilirubin"] = "Bilirubin is normal."

    if "Conjugated Bilirubin" in report:
        if report["Conjugated Bilirubin"] > 0.3:
            suggestions["Conjugated Bilirubin"] = "Elevated conjugated bilirubin may indicate liver or bile duct issues."
        else:
            suggestions["Conjugated Bilirubin"] = "Conjugated bilirubin is normal."

    if "Unconjugated Bilirubin" in report:
        if report["Unconjugated Bilirubin"] > 1.0:
            suggestions["Unconjugated Bilirubin"] = "High unconjugated bilirubin may indicate hemolysis or liver disorder."
        else:
            suggestions["Unconjugated Bilirubin"] = "Unconjugated bilirubin is normal."

    if "Total Proteins" in report:
        if report["Total Proteins"] < 6:
            suggestions["Total Proteins"] = "Low proteins. Improve protein intake (eggs, pulses, dairy)."
        elif report["Total Proteins"] > 8:
            suggestions["Total Proteins"] = "High proteins may indicate dehydration or inflammation."
        else:
            suggestions["Total Proteins"] = "Protein levels are normal."

    if "Albumin" in report:
        val = report["Albumin"]
        if val < 3.5:
            suggestions["Albumin"] = "Low albumin. Ensure adequate protein intake, check liver/kidney."
        elif val > 5:
            suggestions["Albumin"] = "High albumin may indicate dehydration."
        else:
            suggestions["Albumin"] = "Albumin is normal."

    if "Globulin" in report:
        val = report["Globulin"]
        if val < 2:
            suggestions["Globulin"] = "Low globulin. May suggest weak immunity."
        elif val > 3.5:
            suggestions["Globulin"] = "High globulin may indicate chronic inflammation."
        else:
            suggestions["Globulin"] = "Globulin is normal."

    if "A/G Ratio" in report:
        val = report["A/G Ratio"]
        if val < 1.0 or val > 2.2:
            suggestions["A/G Ratio"] = "Abnormal A/G ratio. Ensure balanced protein intake and check liver/kidney."
        else:
            suggestions["A/G Ratio"] = "A/G ratio is normal."

    # ---------- Iron Profile ----------
    if "Transferrin Saturation" in report:
        val = report["Transferrin Saturation"]
        if val < 20:
            suggestions["Transferrin Saturation"] = "Low saturation suggests iron deficiency. Eat iron-rich foods."
        elif val > 50:
            suggestions["Transferrin Saturation"] = "High saturation may indicate iron overload."
        else:
            suggestions["Transferrin Saturation"] = "Iron saturation is normal."

    if "Serum Iron" in report:
        if report["Serum Iron"] < 60:
            suggestions["Serum Iron"] = "Low serum iron. Eat iron-rich foods (spinach, beans, meat)."
        elif report["Serum Iron"] > 170:
            suggestions["Serum Iron"] = "High serum iron. Avoid iron supplements, check for overload."
        else:
            suggestions["Serum Iron"] = "Serum iron is normal."

    if "TIBC" in report:
        if report["TIBC"] > 450:
            suggestions["TIBC"] = "High TIBC may indicate iron deficiency."
        elif report["TIBC"] < 250:
            suggestions["TIBC"] = "Low TIBC may indicate chronic disease."
        else:
            suggestions["TIBC"] = "TIBC is normal."

    if "UIBC" in report:
        if report["UIBC"] > 350:
            suggestions["UIBC"] = "High UIBC suggests iron deficiency."
        else:
            suggestions["UIBC"] = "UIBC is normal."

    if "Total Cholesterol" in report:
        if report["Total Cholesterol"] > 200:
            suggestions["Total Cholesterol"] = "High cholesterol. Avoid fried foods, eat fiber-rich diet."
        else:
            suggestions["Total Cholesterol"] = "Cholesterol is normal."

    if "HDL" in report:
        if report["HDL"] < 40:
            suggestions["HDL"] = "Low HDL. Increase physical activity, eat nuts, olive oil, fatty fish."
        else:
            suggestions["HDL"] = "HDL is good."

    if "LDL" in report:
        if report["LDL"] > 130:
            suggestions["LDL"] = "High LDL. Reduce saturated fats, eat fiber-rich foods."
        else:
            suggestions["LDL"] = "LDL is normal."

    if "Triglycerides" in report:
        if report["Triglycerides"] > 150:
            suggestions["Triglycerides"] = "High triglycerides. Limit sugary foods, alcohol, and refined carbs."
        else:
            suggestions["Triglycerides"] = "Triglycerides are normal."

    if "VLDL" in report:
        if report["VLDL"] > 40:
            suggestions["VLDL"] = "High VLDL. Limit fats and sugars."
        else:
            suggestions["VLDL"] = "VLDL is normal."

    if "Non HDL Cholesterol" in report:
        if report["Non HDL Cholesterol"] > 160:
            suggestions["Non HDL Cholesterol"] = "High Non-HDL cholesterol. Improve diet and exercise."
        else:
            suggestions["Non HDL Cholesterol"] = "Non-HDL cholesterol is normal."

    if "LDL/HDL Ratio" in report:
        if report["LDL/HDL Ratio"] > 3.5:
            suggestions["LDL/HDL Ratio"] = "High LDL/HDL ratio increases heart risk. Improve lifestyle."
        else:
            suggestions["LDL/HDL Ratio"] = "LDL/HDL ratio is fine."

    if "Chol/HDL Ratio" in report:
        if report["Chol/HDL Ratio"] > 5:
            suggestions["Chol/HDL Ratio"] = "High Chol/HDL ratio. Heart disease risk. Improve diet and exercise."
        else:
            suggestions["Chol/HDL Ratio"] = "Chol/HDL ratio is normal."

    # ---------- Inflammation ----------
    if "CRP" in report:
        if report["CRP"] > 3:
            suggestions["CRP"] = "High CRP indicates inflammation. Follow anti-inflammatory diet, manage stress."
        else:
            suggestions["CRP"] = "CRP is normal."

    # ---------- Blood Counts ----------
    if "Hemoglobin" in report:
        if report["Hemoglobin"] < 12:
            suggestions["Hemoglobin"] = "Low hemoglobin. Eat iron-rich foods, vitamin B12, folate."
        else:
            suggestions["Hemoglobin"] = "Hemoglobin is normal."

    if "RBC" in report:
        if report["RBC"] < 4.5:
            suggestions["RBC"] = "Low RBC count may indicate anemia."
        elif report["RBC"] > 6:
            suggestions["RBC"] = "High RBC count may indicate dehydration or lung/heart issue."
        else:
            suggestions["RBC"] = "RBC count is normal."

    if "WBC" in report:
        if report["WBC"] > 11000:
            suggestions["WBC"] = "High WBC may indicate infection."
        elif report["WBC"] < 4000:
            suggestions["WBC"] = "Low WBC may indicate weak immunity."
        else:
            suggestions["WBC"] = "WBC count is normal."

    if "Platelets" in report:
        if report["Platelets"] < 150000:
            suggestions["Platelets"] = "Low platelets. Eat papaya, kiwi, vitamin C foods."
        elif report["Platelets"] > 450000:
            suggestions["Platelets"] = "High platelets may indicate inflammation."
        else:
            suggestions["Platelets"] = "Platelets are normal."

    if "ESR" in report:
        if report["ESR"] > 20:
            suggestions["ESR"] = "High ESR may indicate chronic inflammation."
        else:
            suggestions["ESR"] = "ESR is normal."

    if "TSH" in report:
        if report["TSH"] > 5:
            suggestions["TSH"] = "High TSH indicates hypothyroidism. Regular medication may be required."
        elif report["TSH"] < 0.5:
            suggestions["TSH"] = "Low TSH indicates hyperthyroidism."
        else:
            suggestions["TSH"] = "TSH is normal."

    if "T3" in report:
        if report["T3"] < 80:
            suggestions["T3"] = "Low T3 may suggest hypothyroidism."
        elif report["T3"] > 200:
            suggestions["T3"] = "High T3 may suggest hyperthyroidism."
        else:
            suggestions["T3"] = "T3 is normal."

    if "T4" in report:
        if report["T4"] < 5:
            suggestions["T4"] = "Low T4 may suggest hypothyroidism."
        elif report["T4"] > 12:
            suggestions["T4"] = "High T4 may suggest hyperthyroidism."
        else:
            suggestions["T4"] = "T4 is normal."

    if "Vitamin D" in report:
        if report["Vitamin D"] < 20:
            suggestions["Vitamin D"] = "Vitamin D deficiency. Get sunlight, consume dairy, supplements if needed."
        else:
            suggestions["Vitamin D"] = "Vitamin D is normal."

    if "Vitamin B12" in report:
        if report["Vitamin B12"] < 200:
            suggestions["Vitamin B12"] = "Low Vitamin B12. Eat eggs, dairy, meat, or supplements."
        else:
            suggestions["Vitamin B12"] = "Vitamin B12 is normal."

    if "Rheumatoid Factor" in report:
        if report["Rheumatoid Factor"] > 14:
            suggestions["Rheumatoid Factor"] = "High Rheumatoid Factor may indicate rheumatoid arthritis. Consult rheumatologist."
        else:
            suggestions["Rheumatoid Factor"] = "Rheumatoid Factor is normal."

    return suggestions