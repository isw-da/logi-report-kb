---
title: "Financial Functions"
id: 1500009568222
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009568222-Financial-Functions
updated_at: 2021-07-24T05:54:37Z
---

# Financial Functions

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589521-Date-Time-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions)

# Financial Functions

Below is a list of the financial functions used in Logi JReport Designer:

> * [DDB()](#DDB)
> * [FRAccRecTurnover()](#FRAccRecTurnover)
> * [FRCashFlowVsTotalDebt()](#FRCashFlowVsTotalDebt)
> * [FRCurrentRatio()](#FRCurrentRatio)
> * [FRDebtEquityRatio()](#FRDebtEquityRatio)
> * [FRDividendYield()](#FRDividendYield)
> * [FREarningsPerCommonShare()](#FREarningsPerCommonShare)
> * [FREquityVsTotalAssets()](#FREquityVsTotalAssets)
> * [FRGrossProfitMargin()](#FRGrossProfitMargin)
> * [FRInterestCoverage()](#FRInterestCoverage)
> * [FRInventoryTurnover()](#FRInventoryTurnover)
> * [FRNetProfitMargin()](#FRNetProfitMargin)
> * [FROperatingProfitMargin()](#FROperatingProfitMargin)
> * [FRPriceEarningsRatio()](#FRPriceEarningsRatio)
> * [FRQuickRatio()](#FRQuickRatio)
> * [FRReturnOnCommonEquity()](#FRReturnOnCommonEquity)
> * [FRReturnOnEquity()](#FRReturnOnEquity)
> * [FRReturnOnInvestedCapital()](#FRReturnOnInvestedCapital)
> * [FRReturnOnNetFixedAssets()](#FRReturnOnNetFixedAssets)
> * [FRReturnOnTotalAssets()](#FRReturnOnTotalAssets)
> * [FV()](#FV)
> * [IPmt()](#IPmt)
> * [IRR()](#IRR)
> * [MIRR()](#MIRR)
> * [NPer()](#NPer)
> * [NPV()](#NPV)
> * [Pmt()](#Pmt)
> * [PPmt()](#PPmt)
> * [PV()](#PV)
> * [Rate()](#Rate)
> * [SLN()](#SLN)
> * [SYD()](#SYD)

## DDB(cost, salvage, life, period, factor)

DDB returns a number specifying the depreciation of an asset for a specific time period, using the double-declining balance method or another method as specified by the factor argument.

**Overloads**

* DDB(cost, salvage, life, period)
* DDB(cost, salvage, life, period, factor)

**Parameters**

* cost - A Number or Currency that specifies the initial cost of the asset. The value is nonnegative and greater than or equal to salvage.
* salvage - A Number or Currency that specifies the value of the asset at the end of its useful life. The value is nonnegative.
* life - A positive Number that specifies the length of the useful life of the asset.
* period - A Number that specifies the period for which asset depreciation is calculated. The value is positive and less than or equal to life. The parameters life and period must have the same units.
* factor - An optional positive number that specifies the rate at which the balance declines. If omitted, 2 (double-declining method) will be used.

**Return value**

Number value.

**Examples**

Suppose a company purchases a fleet of cars for $560,000. The cars have a lifetime of 12 years and a salvage value of $30,000. They are depreciated using the double-declining method.

* `DDB(560000, 30000, 12, 1)` - Returns 93333.33. The first year's depreciation is $93,333.33.
* `DDB(560000, 30000, 13, 5)` - Returns 44164.37. The fourth year's depreciation is $44,164.37.
* `DDB(560000, 30000, 13, 13)` - Returns 11605.58. The final year's depreciation is $11,605.58.

## FRAccRecTurnover(Number accountReceivable, Number sales, DbDouble numOfDays)

This function computes the turnover of the account receivable.

**Parameters**

* accountReceivable - A Double value indicating the account receivable.
* sales - A Double value indicating the sales.
* numOfDays - A Double value indicating the number of days.

**Return value**

The return value is a Number.

**Examples**

* If the account receivable is 220000.00, the sales value is 450000.00, the number of days is 100, the return value of the following statement is 48.89.

  `FRAccRecTurnover(220000.00, 450000.00, 100)`
* `FRAccRecTurnover(10000,100000,360)` - Returns 36 days.

## FRCashFlowVsTotalDebt(Number cashFlow,Number totalDebt)

This function returns the result of cash flow vs total debt.

**Parameters**

* cashFlow - A Double value indicating the cash flow.
* totalDebt - A Double value indicating the total debt.

**Return value**

The return value is a Number.

**Example**

If the cash flow is 250000.00, the total debt is 280000.00, the return value of the following statement is 0.89.

`FRCashFlowVsTotalDebt(250000.00, 280000.00)`

## FRCurrentRatio(Number curAssets, Number curLiabilities)

This function computes the current ratio.

**Parameters**

* curAssets - A Double value indicating the current ratio.
* curLiabilities - A Double value indicating the current liabilities.

**Return value**

The return value is a Number.

**Example**

If the current assets are 1800000.00, the current liabilities are 150000.00, the return value of the following statement is 12.00.

`FRCurrentRatio(1800000.00, 150000.00)`

## FRDebtEquityRatio(Number totalLiabilities, Number totalEquity)

This function computes the debt equity ratio.

**Parameters**

* totalLiabilities - A Double value indicating the total liabilities.
* totalEquity - A Double value indicating the total equity.

**Return value**

The return value is a Number.

**Example**

If the total liabilities are 175000.00, the total equity is 215000.00, the return value of the following statement is 0.81.

`FRDebtEquityRatio(175000.00, 215000.00)`

## FRDividendYield(Number dividEnd, Number marketPrice)

This function computes the dividend yield.

**Parameters**

* dividend - A Double value indicating the dividend.
* marketPrice - A Double value indicating the market price.

**Return value**

The return value is a Number.

**Example**

If the dividend is 9.85, the market price is 10.87, the return value of the following statement is 0.91.

`FRDividendYield(9.85, 10.87)`

## FREarningsPerCommonShare(Number netProfit, Number preferredDividend, DbDouble numOfCommonShare)

This function computes the earnings of per common share.

**Parameters**

* netProfit - A Double value indicating the net profit.
* preferredDividend - A Double value indicating the preferred dividend.
* numOfCommonShare - A Double value indicating the number of common shares.

**Return value**

The return value is a Number.

**Example**

If the net profit is 300000.00, the preferred dividend is 180000.00, the number of common shares is 10000, the return value of the following statement is 12.

`FREarningsPerCommonShare(300000.00, 180000.00, 10000)`

## FREquityVsTotalAssets(Number totalEquity, Number totalAssets)

This function returns the result of equity vs. total assets.

**Parameters**

* totalEquity - A Double value indicating the total equity.
* totalAssets - A Double value indicating the total assets.

**Return value**

The return value is a Number.

**Example**

If the total equity is 215000.00, the total assets are 2200000.00, the return value of the following statement is 0.10.

`FREquityVsTotalAssets(215000.00, 2200000.00)`

## FRGrossProfitMargin(Number grossProfit, Number sales)

This function is used to compute the gross profit margin.

**Parameters**

* grossProfit - A Double value indicating the gross profit.
* sales - A Double value indicating the sales.

**Return value**

The return value is a Number.

**Example**

If the gross profit is 350000.00, the sales value is 450000.00, the return value of the following statement is 0.78.

`FRGrossProfitMargin(350000.00, 450000.00)`

## FRInterestCoverage(number cashFlow, number interestExpenses)

This function computes the interest coverage.

**Parameters**

* cashFlow - A Double value indicating the cash flow.
* interestExpenses - A Double value indicating the interest expenses.

**Return value**

The return value is a Number.

**Example**

If the cash flow is 250000.00, the interest expenses are 350000.00, the return value of the following statement is 0.71.

`FRInterestCoverage(250000.00, 350000.00)`

## FRInventoryTurnover(Number inventory, Number sales, Number numOfDays)

This function computes the turnover of the inventory.

**Parameters**

* inventory - A Double value indicating the inventory.
* sales - A Double value indicating the sales.
* numOfDays - A Double value indicating the number of days.

**Return value**

The return value is a Number.

**Example**

If the inventory is 165000.00, the sales value is 450000.00, the number of days is 100, the return value of the following statement is 36.67.

`FRInventoryTurnover(165000.00, 450000.00, 100)`

## FRNetProfitMargin(Number netProfit, Number sales)

This function is used to compute the net profit margin.

**Parameters**

* netProfit - A Double value indicating the net profit.
* sales - A Double value indicating the sales.

**Return value**

The return value is a Number.

**Example**

If the net profit is 300000.00, the sales value is 450000.00, the return value of the following statement is 0.67.

`FRNetProfitMargin(300000.00, 450000.00)`

## FROperatingProfitMargin(Number operatingProfit, Number sales)

This function computes the operating profit margin.

**Parameters**

* operatingProfit - A Double value indicating the operating profit.
* sales - A Double value indicating the sales.

**Return value**

The return value is a Number.

**Example**

If the operating profit is 380000.00, the sales value is 450000.00, the return value of the following statement is 0.84.

`FROperatingProfitMargin(380000.00, 450000.00)`

## FRPriceEarningsRatio(Number marketPrice, Number earningsPerShare)

This function computes the price earning ratio.

**Parameters**

* marketPrice - A Double value indicating the market price.
* earningPerShare - A Double value indicating the earning per share.

**Return value**

The return value is a Number.

**Example**

If the market price is 10.87, the earning per share is 12, the return value of the following statement is 0.91.

`FRPriceEarningsRatio(10.87, 12)`

## FRQuickRatio(Number curAssets, Number inventories, Number curLiabilities)

This function computes the quick ratio.

**Parameters**

* curAssets - A Double value indicating the current assets.
* inventories - A Double value indicating the inventory.
* curLiabilities - A Double value indicating the current liabilities.

**Return value**

The return value is a Number.

**Example**

If the current assets are 1800000.00, the inventory is 165000.00, the current liabilities are 150000.00, the return value of the following statement is 10.90.

`FRQuickRatio(1800000.00, 165000.00, 150000.00)`

## FRReturnOnCommonEquity(Number netProfit, Number preferredDividend, Number commonEquity)

This function returns the result of return on common equity.

**Parameters**

* netProfit - A Double value indicating the net profit.
* preferredDividend - A Double value indicating the preferred dividend.
* commonEquity - A Double value indicating the common equity.

**Return value**

The return value is a Number.

**Example**

If the net profit is 300000.00, the preferred dividend is 180000.00, the common equity is 208000.00, the return value of the following statement is 0.58.

`FRReturnOnCommonEquity(300000.00, 180000.00, 208000.00)`

## FRReturnOnEquity(Number netProfit, Number totalEquity)

This function returns the results of return on equity.

**Parameters**

* netProfit - A Double value indicating the net profit.
* totalEquity - A Double value indicating the total equity.

**Return value**

The return value is a Number.

**Example**

If the net profit is 300000.00, the total equity is 215000.00, the return value of the following statement is 1.40.

`FRReturnOnEquity(300000.00, 215000.00)`

## FRReturnOnInvestedCapital(Number netProfit, Number totalBankDebts, Number totalEquity)

This function returns the result of return on invested capital.

**Parameters**

* netProfit - A Double value indicating the net profit.
* totalBankDebts - A Double value indicating the total bank debts.
* totalEquity - A Double value indicating the total equity.

**Return value**

The return value is a Number.

**Example**

If the net profit is 300000.00, the total bank debts are 100000.00, the total equity is 215000.00, the return value of the following statement is 0.95.

`FRReturnOnInvestedCapital(300000.00, 100000.00, 215000.00)`

## FRReturnOnNetFixedAssets(Number netProfit, Number netFixedAssets)

This function returns the result of return on net fixed assets.

**Parameters**

* netProfit - A Double value indicating the net profit.
* netFixedAssets - A Double value indicating the net fixed assets.

**Return value**

The return value is a Number.

**Example**

If the net profit is 300000.00, the net fixed assets are 400000.00, the return value of the following statement is 0.75.

`FRReturnOnNetFixedAssets(300000.00, 400000.00)`

## FRReturnOnTotalAssets(Number netProfit, Number totalAssets)

This function returns the results of return on total assets.

**Parameters**

* netProfit - A Double value indicating the net profit.
* totalAssets - A Double value indicating the total assets.

**Return value**

The return value is a Number.

**Example**

If the net profit is 300000.00, the total assets are 2200000.00, the return value of the following statement is 0.14.

`FRReturnOntotalAssets(300000.00, 2200000.00)`

## FV(rate, periods, payment, presentMoney, type)

Returns a number specifying the future value of an annuity based on periodic, fixed payments and a fixed interest rate.

**Overloads**

* FV(rate, periods, payment)
* FV(rate, periods, payment, presentMoney)
* FV(rate, periods, payment, presentMoney, type)

**Parameters**

* rate - A Number that specifies the interest rate per period.
* periods - A positive Number that specifies the total number of payment periods in the annuity. The units used for specifying rate and periods must consistent. For example, if periods is the number of periods in months, then rate is a monthly interest rate.
* payment - A Number or Currency that specifies the payment to be made each period.
* presentMoney - An optional Number or Currency that specifies the present value of a series of future payments.
* type - An optional Number that specifies when payments are due. Specify 0 if payments are due at the end of the payment period, and 1 if payments are due at the beginning of the period. If omitted, 1 will be used.

**Return value**

Number value.

**Examples**

* Suppose that you put $1100 per month into a retirement savings plan that pays 6 percent annual interest, compounded monthly. How much will the account be worth after 20 years?

  `FV(0.06 / 12, 20 * 12, -1100)` - Returns 507144.99. So your account will have $507,145. The payment (-1100) is negative since you are paying out the money to the plan.

  The above example assumes that you make your payments into the plan at the end of the month. Thus, after the first month, your plan would have $1100 in it, since there wouldn't have been enough time for any interest to accrue.
* Suppose that instead, you make your payments at the start of the month,

  `FV(0.06 / 12, 20 * 12, -1100, 0, 1)` - Returns 510786.21 (rounded to the nearest integer). So your account will have $510,786. You will save $3,642 more by depositing at the beginning of the month.
* Now suppose that in addition to making payments at the start of the month, you start your plan with an initial deposit of $25,000,

  `FV(0.06 / 12, 20 * 12, -1100, -25000, 1)` - Returns 593541.33 (rounded to the nearest integer). Your account will have $ 593,541 after 20 years.
* You can also use the FV function to calculate the future value of a lump sum deposit. For example, if you deposit $25,000 into a plan that pays 6 percent annual interest compounded monthly for 20 years,

  `FV(0.06 / 12, 20 * 12, 0, -25000)` - Returns 82755.12 (rounded to the nearest integer). You would have $82755.12 in your account.

## IPmt(rate, period, periods, presentMoney, futureMoney, type)

IPmt returns a number specifying the interest payment for a given period of an annuity based on periodic, fixed payments and a fixed interest rate.

**Overloads**

* IPmt(rate, period, periods, presentMoney)
* IPmt(rate, period, periods, presentMoney, futureMoney)
* IPmt(rate, period, periods, presentMoney, futureMoney, type)

**Parameters**

* rate - A Number that specifies the interest rate per period.
* period - A Number that specifies the payment period in the range 1 through periods.
* periods - A positive Number that specifies the total number of payment periods in the annuity. The units used for specifying rate, period and periods must be consistent. For example, if periods is the number of periods in months, then rate is a monthly interest rate and period specifies a month.
* presentMoney - A Number or Currency that specifies the present value, or value today, of a series of future payments or receipts.
* futureMoney - An optional Number or Currency that specifies the future value, or cash balance you want after you've made the final payment. If omitted, 0 will be used.
* type - An optional Number that specifies when payments are due. Specify 0 if payments are due at the end of the payment period, and 1 if payments are due at the beginning of the period. If omitted, 0 will be used.

**Return value**

Number value.

**Examples**

* Suppose that you want to take out a $250,000 loan payable monthly over 15 years at an annual interest rate of 6.5 percent. The following formula returns the amount of interest that you pay in your first loan payment. Note that the monthly interest rate is 0.065 / 12 and the number of months of the loan is 15 \* 12.

  `IPmt(0.065 / 12, 1, 15 * 12, 250000)` - Returns the Number value -1354.17 (rounded to 2 decimals). The value is negative because it represents a payment out from you, whereas the loan amount of $250,000 is positive because it represents a payment in to you.
* The following formula returns the amount of interest that you pay in your 97th payment (after 10 years of payments).

  `IPmt(0.065 / 12, 9*12 + 1, 15 * 12, 250000)` - Returns -701.74 (rounded to 2 decimals). This shows that you would be making progress on the loan at this stage, with less of your monthly payment paying the interest.

## IRR(values, guess)

IRR returns a number specifying the internal rate of return for a series of periodic cash flows (payments and receipts).

**Overloads**

* IRR(values)
* IRR(values, guess)

**Parameters**

* values - A Number or Currency type array that specifies cash flow values. The array must contain at least one negative value (a payment) and one positive value (a receipt). The cash flows must occur at regular intervals such as monthly or yearly.
* guess - An optional Number value that is estimated to be returned by IRR. If omitted, guess is 0.1 (10 percent).

**Return value**

Number value.

**Example**

Suppose that you can choose one of two offers: $20,000 now or guaranteed payments of $5,000 after 1 year, $10,000 after 2 years and $15,000 after 3 years. Which is the better offer? One way to quantify this is to calculate the internal rate of return. If you take the second offer, you cannot take the first, which is like experiencing an initial payment of $20,000 followed by the receipts:

`inArray = ["-20000", "15000", "-10000", "25000"];  
IRR(inArray)`

Returns 0.201 (rounded to 3 decimals) or 20.1 percent interest. With all other things being equal, if you think that 20.1 percent is a good rate of return, you would prefer the second offer.

**Note:** The NPV and IRR functions are related since NPV (IRR (values), values) = 0. That is, the internal rate of return of a sequence of cash flows is the interest rate for which that sequence of cash flows has a net present value of 0. There is no direct formula for the IRR function and so Logi JReport calculates the value by iteration. The process depends on the initial guess for the internal rate of return. If the program reports an error, try changing the value of the guess argument to be closer to what you expect the internal rate of return to be.

## MIRR(valueArray, financeRate, reinvestRate)

Returns a number specifying the modified internal rate of return for a series of periodic cash flows (payments and receipts).

**Parameters**

* valueArray - A Number or Currency type array that specifies cash flow values. The array must contain at least one negative value (a payment) and one positive value (a receipt). The cash flows must occur at regular intervals such as monthly or yearly.
* financeRate - A Number that specifies the interest rate paid as the cost of financing.
* reinvestRate - A Number that specifies the interest rate received on gains from cash reinvestment.

**Return value**

Number value.

**Example**

Suppose that you run a business that makes equipment investments, which results in a loss in the first and fourth years. Your expected annual returns are: -$60,000, $60,000, $45,000, -$50,000, $65,000, $40,000. Your losses are financed at 10 percent while you reinvest your earnings in an account at 6 percent. The modified internal rate of return is:

`MIRR([-60000, 60000, 45000, -50000, 65000, 40000], 0.10, 0.06)` - Returns 0.1929 (rounded to 4 decimals) or 19.29 percent.

## NPer(rate, payment, presentMoney, futureMoney, type)

NPer returns a number specifying the number of periods for an annuity based on periodic, fixed payments and a fixed interest rate.

**Overloads**

* NPer (rate, payment, presentMoney)
* NPer (rate, payment, presentMoney, futureMoney)
* NPer (rate, payment, presentMoney, futureMoney, type)

**Parameters**

* rate - A Number that specifies the interest rate per period.
* payment - A Number or Currency that specifies the payment to be made each period. Payments usually contain principal and interest that doesn't change over the life of the annuity.
* presentMoney - A Number or Currency that specifies the present value, or value today, of a series of future payments or receipts.
* futureMoney - An optional number or Currency that specifies the future value or cash balance you want after you've made the final payment. If omitted, 0 will be used.
* type - An optional cumber that specifies when payments are due. Specify 0 if payments are due at the end of the payment period, and 1 if payments are due at the beginning of the period. If omitted, 0 will be used.

**Return value**

Number value.

**Examples**

* Suppose that you want a $250,000 loan to buy a house. The interest rate is 6.5 percent and you can afford to pay $3,000 per month. How long a mortgage would you need?

  `NPer(0.075/12, -3000, 250000)` - Returns 118.08 (rounded to 2 decimals) months.
* Rather than seeking a loan, suppose that you want to save $500,000 and then buy the house. You can get a 6.5 percent interest rate compounded monthly from your savings plan, and you want to save $3,000 per month. How long would you need to save before you had the required amount of money?

  `NPer(0.065/12, -3000, 0, 250000)` - Returns 68.96 (rounded to 2 decimals) months.

## NPV(rate, values)

Returns a number specifying the net present value of an investment based on a series of periodic cash flows (payments and receipts) and a discount rate.

**Parameters**

* rate - A Number that specifies the discount rate over the length of the period, expressed as a decimal.
* value - A Number or Currency type array that specifies cash flow values. Negative values represent payments and positive values receipts. The cash flow must occur at regular intervals, such as monthly or yearly.

**Return value**

Number value.

**Example**

Suppose that someone offers to pay you $15000 after 1 year, $20000 after 2 years, $25000 after 3 years and $12000 after 4 years. If the discount rate (the Time value of money) is 6.5 percent, the value of this offer to you today is:

`NPV(0.065, [15000, 20000, 25000, 12000])`

The formula returns 61741.8. So this scheme is worth $61,741.8 to you today. This is less than the sum of the payments, which is $72000, since you have to wait for this money.

**Note:** The NPV and IRR functions are related since NPV (IRR (values), values) = 0, which means that the internal rate of the return of a sequence of cash flow is the discount rate for which that sequence of cash flow has a net present value of 0.

## Pmt(rate, periods, presentMoney, futureMoney, type)

Returns a number specifying the payment for an annuity based on periodic, fixed payments and a fixed interest rate. To find the total amount paid out over the whole loan, multiply the payment per period (the value returned by Pmt) by the total number of periods.

**Overloads**

* Pmt(rate, periods, presentMoney)
* Pmt(rate, periods, presentMoney, futureMoney)
* Pmt(rate, periods, presentMoney, futureMoney, type)

**Parameters**

* rate - A Number that specifies the interest rate per period.
* periods - A positive Number that specifies the total number of payment periods in the annuity. The units used for specifying rate and periods must be consistent. For example, if periods is the number of periods in months, then rate will be a monthly interest rate.
* presentMoney - A Number or Currency that specifies the present value or principal. That is, the amount that a series of payments in the future is worth now.
* futureMoney - An optional Number or Currency that specifies the future value or cash balance you want after you've made the final payment. If omitted, 0 will be used.
* type - An optional Number that specifies when payments are due. Specify 0 if payments are due at the end of the payment period, and 1 if payments are due at the beginning of the period. If omitted, 0 will be used.

**Return value**

Number value.

**Examples**

* Suppose that you want to take out a $250,000 loan payable monthly over 15 years at an annual interest rate of 6.5 percent. The following formula returns your monthly loan payment. Note that the monthly interest rate is 0.065 / 12, and the number of months of the loan is 15 \* 12.

  `Pmt(0.065 / 12, 15 * 12, 250000)` - Returns the Number value -2177.77 (rounded to 2 decimals). The value is negative because it represents a payment out from you whereas the loan amount of $250,000 is positive because it represents a payment in to you.
* Now suppose that the payments are made at the beginning of the month instead of the end (default). Your monthly loan payment is calculated as:

  `Pmt(0.065 / 12, 15 * 12, 250000, 0, 1)` - Returns -2166.04 (rounded to 2 decimals). Note that your monthly payment is about $11.73 less each month than in the previous example where payments are made at the end of the month.
* Now suppose that you know that you'll receive $80,000 in 15 years. In this case, there is no need to fully pay off the loan. You only need to reduce the amount owed to $80,000 after 15 years. Note that the future value is negative since after 15 years you will need to pay out $80,000 to clear the loan. Your monthly loan payment is calculated as:

  `Pmt(0.065 / 12, 15 * 12, 250000, -80000)` - Returns -1914.22 (rounded to 2 decimals).

## PPmt(rate, period, periods, presentMoney, futureMoney, type)

Returns a number specifying the principal payment for a given period of an annuity based on periodic, fixed payments and a fixed interest rate.

**Overloads**

* PPmt(rate, period, periods, presentMoney)
* PPmt(rate, period, periods, presentMoney, futureMoney)
* PPmt(rate, period, periods, presentMoney, futureMoney, type)

**Parameters**

* rate - A Number that specifies the interest rate per period.
* period - A Number that specifies the payment period in the range 1 through periods.
* periods - A positive Number that specifies the total number of payment periods in the annuity. The units used for specifying rate, period and periods must be consistent. For example, if periods is the number of periods in months, then rate is a monthly interest rate and period specifies a month.
* presentMoney - A Number or Currency that specifies the present value, or value today, of a series of future payments or receipts.
* futureMoney - An optional Number or Currency that specifies the future value or cash balance you want after you've made the final payment. If omitted, 0 will be used.
* type - An optional Number that specifies when payments are due. Specify 0 if payments are due at the end of the payment period, and 1 if payments are due at the beginning of the period. If omitted, 0 will be used.

**Return value**

Number value.

**Examples**

* Suppose that you want to take out a $250,000 loan payable monthly over 15 years at an annual interest rate of 6.5 percent. The following formula returns the amount of principal that you pay in your first loan payment. Note that the monthly interest rate is 0.065 / 12 and the number of months of the loan is 15 \* 12.

  `PPmt (0.065 / 12, 1, 15 * 12, 250000)` - Returns the Number value -823.6 (rounded to 2 decimals). The value is negative because it represents a payment out from you whereas the loan amount of $250,000 is positive because it represents a payment in to you.
* The following formula returns the amount of principal that you pay in your 121st payment (after 10 years of payments):

  `PPmt (0.065 / 12, 9*12 + 1, 15 * 12, 250000)` - Returns -1476.03 (rounded to 2 decimals).

  You've made progress on the loan and are paying off more of the principal per payment. This is because less interest can accrue each month since more of the loan is paid off so that your fixed monthly payment is applied more to the principal.

## PV(rate, periods, payment, futureMoney, type)

Returns a number specifying the present value of an annuity based on periodic, fixed payments to be paid in the future and at a fixed interest rate.

**Overloads**

* PV (rate, periods, payment)
* PV (rate, periods, payment, futureMoney)
* PV (rate, periods, payment, futureMoney, type)

**Parameters**

* rate - A Number that specifies the interest rate per period.
* periods - A positive Number that specifies the total number of payment periods in the annuity. The units used for specifying rate and periods must be consistent. For example, if periods is the number of periods in months, rate will then be a monthly interest rate.
* payment - A Number or Currency that specifies payment to be made each period.
* futureMoney - an optional Number or Currency that specifies the future value or cash balance you want after you've made the final payment. If omitted, 0 will be used.
* type - An optional Number that specifies when payments are due. Specify 0 if payments are due at the end of the payment period, and 1 if payments are due at the beginning of the period. If omitted, 0 will be used.

**Return value**

Number value.

**Example**

Suppose that you want to buy a condo and can make payments of $1100 twice a month (24 annual payments). If the mortgage rates are 6.5 percent, and you want to pay off the condo in 10 years, what is the maximum loan that you can take out?

`PV(0.065 / 24, 10 * 24, -1100)` - Returns 193936 (rounded to the nearest dollar).

You can therefore afford a loan of about $194,000. Notice that the payment argument is negative since you are paying out the money each month.

## Rate(periods, payment, presentMoney, futureMoney, type, guess)

Rate returns a number specifying the interest rate per period for an annuity. The units of the returned value are consistent with the units of periods. For example, if periods is in months, then the rate returned will be a monthly interest rate.

**Overloads**

* Rate(periods, payment, presentMoney)
* Rate(periods, payment, presentMoney, futureMoney)
* Rate(periods, payment, presentMoney, futureMoney, type)
* Rate(periods, payment, presentMoney, futureMoney, type, guess)

**Parameters**

* periods - A positive Number that specifies the total number of payment periods in the annuity.
* payment - A Number or Currency that specifies the payment that is to be made for each period.
* presentMoney - A Number or Currency that specifies the present value, or value today, of a series of future payments or receipts.
* futureMoney - An optional Number or Currency that specifies the future value or cash balance you want after you've made the final payment. If omitted, 0 will be used.
* type - An optional Number that specifies when payments are due. Specify 0 if payments are due at the end of the payment period, and 1 if payments are due at the beginning of the period. If omitted, 0 will be used.
* guess - An optional Number value estimated to be returned by Rate. If omitted, guess is 0.1 (10 percent).

**Return value**

Number value.

**Examples**

* An electronics store offers to finance a $12500 television for $560 per month, over 2 years, with no money down. Is this a good deal? The first step in determining this is to figure out what interest rate the store is charging.

  `Rate(2 * 12, -560, 12500)` - Returns 0.00588 (rounded to 5 decimals). Notice that periods is 24 months, payment (-560) is negative since monthly payments are being paid, and the present value (12500) is positive since at the start of the loan, $12500 was effectively received (the value of the television). The interest rate returned is a monthly interest rate, since periods is in months.
* This next expression calculates the interest rate, expressed as a yearly interest rate and as a percent.

  `Rate(2 * 12, -560, 12500) * 12 * 100` - Returns 7.06 (rounded to 2 decimals). Thus, the store is charging an effective annual interest rate of 7.06 percent.

**Note:** There is no direct formula for the Rate function and so Reports calculates the value by iteration. The process depends on the initial guess for the rate. If the program reports an error, try changing the value of the guess argument to be closer to what you expect the interest rate to be.

## SLN(cost, salvage, life)

SLN returns a number specifying the straight-line depreciation of an asset for a single period.

**Parameters**

* cost - A Number or Currency that specifies the initial cost of the asset.
* salvage - A Number or Currency that specifies the value of the asset at the end of its useful life.
* life - A Number that specifies the length of the useful life of the asset. It must not equal 0.

**Return value**

Number value.

**Example**

Suppose a company purchases a fleet of cars for $560,000. The cars have a lifetime of 12 years and a salvage value of $30,000. The depreciation per year is:

`SLN(560000, 30000, 12)` - Returns 44166.67. Thus the depreciation per year is $44,166.67.

## SYD(cost, salvage, life, period)

SYD returns a number specifying the sum-of-years' digits depreciation of an asset for a single period.

**Parameters**

* cost - A Number or Currency that specifies the initial cost of the asset.
* salvage - A Number or Currency that specifies the value of the asset at the end of its useful life.
* life - A positive Number that specifies the length of the useful life of the asset.
* period - A Number that specifies the period for which asset depreciation is calculated. The value is positive and less than or equal to life. The Parameters life and period must have the same units.

**Return value**

Number value.

**Examples**

Suppose a company purchases a fleet of cars for $560,000. The cars have a lifetime of 12 years and a salvage value of $30,000. They are depreciated as follows:

* `SYD(560000, 30000, 12, 1)` - Returns 80000. The first year's depreciation is $81,538.46.
* `SYD(560000, 60000, 12, 5)` - Returns 56000. The fourth year's depreciation is $54,358.97.
* `SYD(560000, 60000, 12, 12)` - Returns 8000. The final year's depreciation is $6,794.87.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589521-Date-Time-Functions)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589541-Math-Functions)
