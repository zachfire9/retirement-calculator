from financials import Financials

if __name__ == "__main__":
    initial_ira = 0
    initial_roth = 0
    ira_monthly_contributions = 1500
    roth_monthly_contributions = 459
    expected_rate_of_return = .05
    years_before_retirement = 30
    retirement_annual_spending_todays_dollars = 45000

    financials = Financials(initial_ira, initial_roth)
    result = financials.run(ira_monthly_contributions, roth_monthly_contributions, expected_rate_of_return, years_before_retirement)

    print 'Total Combined Amount Final'
    print result

    expected_annual_inflation = .03

    for x in range(1, years_before_retirement):
        retirement_annual_spending_todays_dollars = financials.inflation(retirement_annual_spending_todays_dollars, expected_annual_inflation)

    expected_retirement_rate_of_return = .02

    retirement = financials.retirement(result, retirement_annual_spending_todays_dollars, expected_retirement_rate_of_return, expected_annual_inflation)

    print 'Total Retirement Years'
    print retirement