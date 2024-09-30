from crewai import crew


class FinanceCrew:

    def __init__(
        self,
        grossAnnualIncome,
        healthInsurance,
        homeLoan,
        deductionsunder80C,
        taxRegime,
        query,
    ):
        self.income = grossAnnualIncome
        self.health_insurance = healthInsurance
        self.home_loan = homeLoan
        self.deuctions_80c = deductionsunder80C
        self.query = query
        self.tax_regime = taxRegime
