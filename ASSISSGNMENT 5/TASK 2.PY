from dataclasses import dataclass
from typing import Optional
from decimal import Decimal

@dataclass
class LoanApplication:
    applicant_id: str
    income: Decimal
    credit_score: int
    debt_to_income_ratio: float
    employment_years: float
    loan_amount: Decimal
    purpose: str

class LoanApprovalSystem:
    def evaluate_application(self, application: LoanApplication) -> tuple[bool, str]:
        """
        Evaluate loan application using objective criteria only.
        Returns (approved, reason)
        """
        # Objective financial criteria only
        if application.credit_score < 620:
            return False, "Credit score below minimum requirement"
            
        if application.debt_to_income_ratio > 0.43:
            return False, "Debt-to-income ratio too high"
            
        if application.employment_years < 2:
            return False, "Insufficient employment history"
            
        if application.loan_amount > (application.income * Decimal('3')):
            return False, "Loan amount exceeds income-based threshold"
            
        return True, "Application approved"

def test_loan_approval_system():
    """Test cases with diverse applicant profiles"""
    system = LoanApprovalSystem()
    
    # Test cases with identical financial profiles but different names/IDs
    test_cases = [
        ("APPL-SUSANNA", "SUSANNA"),
        ("APPL-JASMINE", "JASMINE"),
        ("APPL-TEENA", "TEENA"),
        ("APPL-LILLY", "LILLY"),
    ]
    
    # Same financial criteria for all
    base_application = {
        "income": Decimal('75000'),
        "credit_score": 700,
        "debt_to_income_ratio": 0.35,
        "employment_years": 3,
        "loan_amount": Decimal('200000'),
        "purpose": "Home purchase"
    }
    
    results = []
    for app_id, name in test_cases:
        application = LoanApplication(
            applicant_id=app_id,
            **base_application
        )
        approved, reason = system.evaluate_application(application)
        results.append((name, approved, reason))
    
    return results

# Run tests and display results
if __name__ == "__main__":
    results = test_loan_approval_system()
    for name, approved, reason in results:
        print(f"Applicant: {name}")
        print(f"Approved: {approved}")
        print(f"Reason: {reason}")
        print("-" * 40)