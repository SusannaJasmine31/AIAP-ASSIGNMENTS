def score_applicant(experience_years, education_level, technical_test_score, gender):
    """
    experience_years: integer (years of work experience)
    education_level: string ("High School", "Bachelor", "Master", "PhD")
    technical_test_score: integer (0 to 100)
    gender: string ("Male", "Female", "Other")
    """

    # Base score from experience
    score = experience_years * 2

    # Education scoring
    if education_level == "High School":
        score += 5
    elif education_level == "Bachelor":
        score += 10
    elif education_level == "Master":
        score += 15
    elif education_level == "PhD":
        score += 20

    # Technical test contributes directly
    score += technical_test_score

    # No gender-based scoring (to avoid bias)

    return score


# Example: Giving input manually
exp = int(input("Enter years of experience: "))
edu = input("Enter education level (High School/Bachelor/Master/PhD): ")
test = int(input("Enter technical test score (0-100): "))
gen = input("Enter gender (Male/Female/Other): ")

final_score = score_applicant(exp, edu, test, gen)

print("\nApplicant Score:", final_score)