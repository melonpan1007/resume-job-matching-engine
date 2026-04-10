import pandas as pd

def load_jobs(path="data/job_title_des.csv", demo_mode=True):

    df = pd.read_csv(path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Drop empty rows
    df = df.dropna(subset=["Job Title", "Job Description"])

    # Remove small descriptions
    df = df[df["Job Description"].str.len() > 40]

    # -----------------------------
    # 🔥 DEMO MODE (FAST)
    # -----------------------------
    if demo_mode:
        df = df[df["Job Title"].str.contains("engineer|developer", case=False)]
        df = df.head(20)

    return df.reset_index(drop=True)