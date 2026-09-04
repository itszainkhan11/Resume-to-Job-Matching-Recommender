import pandas as pd

from matcher import ResumeJobMatcher


TEST_RESUMES = [
    {
        "resume": "Python developer experienced in machine learning, pandas, NumPy and scikit-learn.",
        "expected_job": "Machine Learning Engineer"
    },
    {
        "resume": "Professional working with SQL, Excel, data analysis and business reports.",
        "expected_job": "Data Analyst"
    },
    {
        "resume": "Frontend developer experienced with HTML, CSS, JavaScript and React.",
        "expected_job": "Frontend Developer"
    },
    {
        "resume": "Graphic designer experienced with Photoshop, Illustrator and visual design.",
        "expected_job": "Graphic Designer"
    },
    {
        "resume": "Cybersecurity professional experienced in network security, vulnerabilities and threat analysis.",
        "expected_job": "Cybersecurity Analyst"
    }
]


def evaluate():
    matcher = ResumeJobMatcher()

    correct = 0
    total = len(TEST_RESUMES)

    print("\nResume-to-Job Matching Evaluation")
    print("=" * 45)

    for test in TEST_RESUMES:
        results = matcher.match(test["resume"], top_k=3)

        predicted_job = results.iloc[0]["job_title"]

        if predicted_job == test["expected_job"]:
            correct += 1

        print(f"\nExpected: {test['expected_job']}")
        print(f"Predicted: {predicted_job}")

    accuracy = correct / total

    print("\n" + "=" * 45)
    print(f"Top-1 Accuracy: {accuracy:.2%}")
    print(f"Correct: {correct}/{total}")


if __name__ == "__main__":
    evaluate()
