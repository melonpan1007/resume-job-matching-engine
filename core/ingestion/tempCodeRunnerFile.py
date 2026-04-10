import pandas as pd


def load_jobs(path="data/job_title_des.csv", limit=100):

    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()

    jobs = []

    for _, row in df.iterrows():

        title = str(row["Job Title"])
        desc = str(row["Job Description"])

        if len(desc) < 40:
            continue

        jobs.append({
            "title": title,
            "description": desc,
            "text": (title + " " + desc).lower()
        })

    return jobs[:limit]