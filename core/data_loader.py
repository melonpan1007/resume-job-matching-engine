import pandas as pd

def load_jobs():
    df = pd.read_csv("data/job_title_des.csv")

    # Clean missing values
    df = df.dropna(subset=["Job Title", "Job Description"])

    return df