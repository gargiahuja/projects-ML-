normal_ranges = {
    # Diabetes
    "Fasting Glucose": (70, 110),
    "HbA1c": (4.0, 5.6),
    "Estimated Avg Glucose": (70, 140),

    # Liver
    "Total Bilirubin": (0.3, 1.2),
    "Conjugated Bilirubin": (0.0, 0.3),
    "Unconjugated Bilirubin": (0.1, 1.0),
    "Total Proteins": (5.7, 8.2),
    "Albumin": (3.5, 5.0),
    "Globulin": (2.0, 4.1),
    "A/G Ratio": (1.0, 2.0),

    # Iron studies
    "Transferrin Saturation": (16, 50),
    "Serum Iron": (60, 170),
    "TIBC": (250, 425),
    "UIBC": (130, 336),

    # Lipid
    "Total Cholesterol": (0, 200),
    "HDL": (40, 60),
    "LDL": (0, 100),
    "Triglycerides": (0, 150),
    "VLDL": (5, 30),
    "Non HDL Cholesterol": (0, 130),
    "LDL/HDL Ratio": (0, 3.5),
    "Chol/HDL Ratio": (0, 5),

    # Inflammation
    "CRP": (0, 5),

    # Hematology
    "Hemoglobin": (12, 15),
    "RBC": (3.8, 5.8),
    "WBC": (4000, 10000),
    "Platelets": (1.5, 4.5),  # in lakh
    "ESR": (0, 20),

    # Thyroid
    "TSH": (0.55, 4.78),
    "T3": (0.6, 1.8),
    "T4": (3.2, 12.6),

    # Vitamins
    "Vitamin D": (30, 100),
    "Vitamin B12": (187, 883),

    # Arthritis
    "Rheumatoid Factor": (0, 14)
}

def check_abnormal(params):
    status = {}
    for k, v in params.items():
        lo, hi = normal_ranges.get(k, (None, None))

        if v is None:
            status[k] = "❓ Not found"
        elif lo is None or hi is None:
            status[k] = f"ℹ️ No reference range"
        elif v < lo:
            status[k] = f"⬇️ Low ({v})"
        elif v > hi:
            status[k] = f"⬆️ High ({v})"
        else:
            status[k] = f"✅ Normal ({v})"
    return status
