import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import clean_text


MODEL_NAME = "all-MiniLM-L6-v2"


class ResumeJobMatcher:
    def __init__(self, jobs_path="data/jobs.csv"):
        self.model = SentenceTransformer(MODEL_NAME)
        self.jobs = pd.read_csv(jobs_path)

        self.jobs["clean_description"] = (
            self.jobs["job_description"]
            .fillna("")
            .apply(clean_text)
        )

        self.job_embeddings = self.model.encode(
            self.jobs["clean_description"].tolist(),
            normalize_embeddings=True
        )

    def match(self, resume_text, top_k=5):
        resume_text = clean_text(resume_text)

        if not resume_text:
            return pd.DataFrame()

        resume_embedding = self.model.encode(
            [resume_text],
            normalize_embeddings=True
        )

        scores = cosine_similarity(
            resume_embedding,
            self.job_embeddings
        )[0]

        results = self.jobs.copy()
        results["similarity_score"] = scores

        results = results.sort_values(
            "similarity_score",
            ascending=False
        )

        return results[
            ["job_id", "job_title", "job_description", "similarity_score"]
        ].head(top_k)
