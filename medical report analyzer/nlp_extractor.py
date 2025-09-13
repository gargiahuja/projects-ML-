import re
def extract_value(text, pattern):
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        value_str = match.group(1).strip()

        value_str = value_str.replace(',', '').replace(' ', '')

        if re.fullmatch(r"[-+]?\d*\.\d+|\d+", value_str):
            return float(value_str)
    
    return None


def extract_params(text):
    return {
        # DIABETES
        "HbA1c": extract_value(text, r"HBA1C\s*[=:\s]*([\d.]+)"),
        "Estimated Avg Glucose": extract_value(text, r"ESTIMATED AVG\.? GLUCOSE\s*([\d.]+)"),
        "Fasting Glucose": extract_value(text, r"Plasma Glucose Fasting\s*([\d.]+)"),
        
        # LIVER FUNCTION
        "Total Bilirubin": extract_value(text, r"TOTAL BILIRUBIN\s*([\d.]+)"),
        "Conjugated Bilirubin": extract_value(text, r"CONJUGATED.*?Bilirubin.*?([\d.]+)"),
        "Unconjugated Bilirubin": extract_value(text, r"UNCONJUGATED.*?Bilirubin.*?([\d.]+)"),
        "Total Proteins": extract_value(text, r"TOTAL PROTEINS\s*([\d.]+)"),
        "Albumin": extract_value(text, r"ALBUMIN\s*([\d.]+)"),
        "Globulin": extract_value(text, r"GLOBULIN\s*([\d.]+)"),
        "A/G Ratio": extract_value(text, r"A/G RATIO\s*([\d.]+)"),

        # IRON PANEL
        "Transferrin Saturation": extract_value(text, r"TRANSFERRIN SATURATION\s*([\d.]+)"),
        "Serum Iron": extract_value(text, r"SERUM IRON LEVELS\s*([\d.]+)"),
        "TIBC": extract_value(text, r"TOTAL IRON BINDING CAPACITY\s*([\d.]+)"),
        "UIBC": extract_value(text, r"UIBC\s*([\d.]+)"),

        # LIPID PROFILE
        "Total Cholesterol": extract_value(text, r"TOTAL CHOLESTEROL\s*([\d.]+)"),
        "HDL": extract_value(text, r"H D L CHOLESTEROL\s*([\d.]+)"),
        "LDL": extract_value(text, r"L D L CHOLESTEROL\s*([\d.]+)"),
        "Triglycerides": extract_value(text, r"TRIGLYCERIDES\s*([\d.]+)"),
        "VLDL": extract_value(text, r"VLDL\s*([\d.]+)"),
        "Non HDL Cholesterol": extract_value(text, r"NON HDL CHOLESTEROL\s*([\d.]+)"),
        "LDL/HDL Ratio": extract_value(text, r"LDL\s*/\s*HDL RATIO\s*([\d.]+)"),
        "Chol/HDL Ratio": extract_value(text, r"T\.?\s*CHOLESTEROL/ HDL RATIO\s*([\d.]+)"),

        # INFLAMMATION
        "CRP": extract_value(text, r"C-REACTIVE PROTEIN\s*([\d.]+)"),

        # HEMATOLOGY
        "Hemoglobin": extract_value(text, r"HAEMOGLOBIN \(?HB\)?\s*([\d.]+)"),
        "RBC": extract_value(text, r"RBC COUNT.*?([\d.]+)"),
        "WBC": extract_value(text, r"TOTAL LEUCOCYTE COUNT.*?([\d,]+)"),
        "Platelets": extract_value(text, r"PLATELET COUNT\s*([\d.]+)"),
        "ESR": extract_value(text, r"ERYTHROCYTE SEDIMENTATION RATE\s*([\d.]+)"),

        # HORMONE PANEL
        "TSH": extract_value(text, r"TSH\s*([\d.]+)"),
        "T3": extract_value(text, r"T3\s*([\d.]+)"),
        "T4": extract_value(text, r"T4\s*([\d.]+)"),

        # VITAMINS
        "Vitamin D": extract_value(text, r"VITAMIN D\s*([\d.]+)"),
        "Vitamin B12": extract_value(text, r"VITAMIN B12\s*[>:=]*\s*([\d.]+)"),

        # ARTHRITIS
        "Rheumatoid Factor": extract_value(text, r"RHEUMATOID FACTOR TEST\s*([\d.]+)")
    }
