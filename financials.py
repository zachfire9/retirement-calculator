class Financials:
    monthly_ira_contribution = 0
    monthly_roth_contribution = 0

    def __init__(self, initial_ira, initial_roth):
        self.current_ira = initial_ira
        self.current_roth = initial_roth

    def calculate_compound_interest(self, initial_amount, interval_contribution, compound_interval, interval_total, expected_return_rate):
        total_amount = initial_amount

        for i in range(interval_total):
            print "Start Year %s --------------------------------" % (i + 1)
            print total_amount
            for j in range(compound_interval):
                total_amount += interval_contribution
            total_amount += (total_amount * expected_return_rate)

        return total_amount

    def retirement(self, initial_amount, minimum_annual_spending, expected_return_rate, expected_annual_inflation):
        total_years = 1
        year_spending = minimum_annual_spending
        while (initial_amount > year_spending):
            print "Retirement Year %s --------------------------------" % total_years
            print initial_amount
            total_years += 1
            
            print "Year Spending w/ Inflation: %s" % year_spending
            initial_amount -= year_spending

            if initial_amount <= year_spending:
                initial_amount = 0
            else:
                initial_amount += (initial_amount * expected_return_rate)

            year_spending = self.inflation(year_spending, expected_annual_inflation)

        return total_years

    def inflation(self, amount, rate_of_inflation):
        amount_with_inflation = amount + (amount * rate_of_inflation)

        return amount_with_inflation

    def run(self, monthly_ira_contribution, monthly_roth_contribution, expected_return_rate, years_before_retirement):
        self.monthly_ira_contribution = monthly_ira_contribution
        self.monthly_roth_contribution = monthly_roth_contribution
        print 'IRA Calculation Start'
        self.current_ira = self.calculate_compound_interest(self.current_ira, self.monthly_ira_contribution, 12, years_before_retirement, expected_return_rate)
        print '----------------------------------------------'
        print 'IRA Calculation Final'
        print self.current_ira
        print '----------------------------------------------'
        print 'Roth Calculation Start'
        self.current_roth = self.calculate_compound_interest(self.current_roth, self.monthly_roth_contribution, 12, years_before_retirement, expected_return_rate)
        print '----------------------------------------------'
        print 'Roth Calculation Final'
        print self.current_roth
        print '----------------------------------------------'

        return self.current_ira + self.current_roth
