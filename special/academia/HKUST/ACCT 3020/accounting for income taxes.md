---
aliases:
  - accounting for income taxes
  - deferred tax
  - deferred tax assets and liabilities
  - income tax expense
tags:
  - flashcard/active/special/academia/HKUST/ACCT_3020/accounting_for_income_taxes
  - language/in/English
---

# accounting for income taxes

This note covers the ACCT 3020 material on temporary and permanent differences, deferred tax liabilities, deferred tax assets, enacted tax-rate changes, and loss carryforwards and carrybacks. The topic is about timing. A company may report revenue or expense one way for IFRS and another way for tax law. When the difference will reverse later, the company records the future tax consequence now.

This note does __not__ repeat the short-term `income tax payable` material from [current liability](current%20liability.md#income-tax-payable). That earlier section covers the ordinary year-end tax payable entry. This note goes beyond that basic accrual and explains why __income tax expense__ can differ from __income taxes payable__.

## overview and the core split

The topic begins with a simple but crucial contrast:

- __income taxes payable__: the amount currently owed to the tax authority under tax rules; and
- __income tax expense__: the tax cost assigned to the accounting period under IFRS.

Over a multi-year sequence, these two amounts can differ year by year but still match in total after all temporary differences reverse.

The reason is that IFRS and tax law often recognize revenue or expense in different periods. The company therefore needs an __interperiod tax allocation__ rather than a one-line current payable only.

IAS 12 applies the __balance sheet liability method__: it measures deferred tax by examining the difference between the __carrying amount__ of each asset or liability and its __tax base__, rather than focusing only on the income-statement timing of revenue and expense.

---

Flashcards for this section are as follows:

- income taxes payable versus income tax expense ::@:: Income taxes payable is the amount currently owed under tax law, while income tax expense is the tax cost assigned to the accounting period under IFRS. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-07-26T03:29:29.326Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:29.326Z-->
- why can income taxes payable differ from income tax expense? ::@:: Because IFRS and tax rules may recognize the same revenue or expense in different periods. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- interperiod tax allocation: main purpose ::@:: To recognize the future tax consequences of timing differences in the period in which those differences arise. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->

## temporary differences and permanent differences

The course separates differences between IFRS and tax reporting into two families.

---

Flashcards for this section are as follows:

- book-tax differences: two families in this topic ::@:: Temporary differences reverse later and create deferred taxes, while permanent differences never reverse and therefore affect only current tax. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- temporary versus permanent difference: why is the split central? ::@:: Because deferred tax accounting starts by asking whether the book-tax difference will reverse in a future period. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

### temporary differences

A __temporary difference__ is the difference between the __book basis__ of an asset or liability and its __tax basis__ when that difference will create taxable or deductible amounts in future years.

Temporary differences always point to one of two future effects:

- __future taxable amounts__ -> deferred tax __liability__; or
- __future deductible amounts__ -> deferred tax __asset__.

Common temporary-difference examples in the course are:

- accounts receivable from revenue already recognized for IFRS but not yet taxable;
- installment sales, where tax recognition follows cash collection over time;
- depreciation, when tax depreciation and IFRS depreciation follow different patterns;
- warranty liabilities, which are expensed now for IFRS but deductible only when paid for tax;
- litigation losses, which may be accrued for IFRS but deductible only on settlement;
- revenue received in advance, which is taxed when cash is collected but recognized as IFRS revenue only when the performance obligation is satisfied in a later period;
- prepaid expenses, where the tax authority allows an immediate deduction but IFRS expenses the item over time, leaving a higher book base than tax base; and
- share-based payment arrangements, where the IFRS 2 expense is spread over the vesting period but the tax deduction typically arises only when shares vest or options are exercised.

---

Flashcards for this section are as follows:

- temporary difference: what makes it temporary? ::@:: The book basis and tax basis differ now, but that difference will later reverse and create future taxable or deductible amounts. <!--SR:!fsrs,2026-07-31T00:00:00.000Z,42,41.57871783,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- temporary differences: what two future effects must be classified? ::@:: Future taxable amounts create deferred tax liabilities, while future deductible amounts create deferred tax assets. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- revenue received in advance: which type of temporary difference does it create? ::@:: A deductible temporary difference, because the company is taxed when cash arrives but recognizes IFRS revenue later without further taxation, leaving a future non-taxable recognition that creates a tax saving. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- share-based payment (IFRS 2): what temporary difference does it typically create? ::@:: A deductible temporary difference, because the IFRS 2 expense is recognized over the vesting period while the tax deduction usually arises only when shares vest or options are exercised. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-26T03:29:03.725Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:03.725Z-->
- prepaid expenses: what type of temporary difference and deferred tax do they create? ::@:: A taxable temporary difference and a deferred tax liability, because the tax authority allows the deduction now while IFRS expenses the item over time, so the future IFRS expense will not be deductible again. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

### permanent differences

A __permanent difference__ affects either pretax financial income or taxable income, but it will __never reverse__.

Common course examples are:

- interest on certain government bonds that is recognized as revenue for IFRS but never taxed;
- fines and penalties that are expensed for IFRS but never deductible for tax; and
- some other non-deductible expenses such as certain insurance premiums for key officers or donation items depending on the tax law.

Permanent differences change the relation between pretax accounting income and taxable income, but they do __not__ create deferred tax assets or deferred tax liabilities.

---

Flashcards for this section are as follows:

- permanent difference: what is the defining feature? ::@:: It affects accounting income or taxable income now but never reverses in a later period. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- permanent differences: why do they not create deferred taxes? ::@:: Because there is no future taxable or deductible amount left to recognize in another period. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- permanent difference: definition ::@:: A difference between IFRS and tax reporting that will never reverse, so it affects only the current period and does not create deferred taxes. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- government bond interest: temporary or permanent difference? ::@:: Permanent difference, because it is recognized for IFRS but never taxed. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- fines and penalties: temporary or permanent difference? ::@:: Permanent difference, because they are expensed for IFRS but are not deductible for tax. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->

## deferred tax liabilities

A __deferred tax liability__ represents future taxes payable caused by existing __taxable temporary differences__.

---

Flashcards for this section are as follows:

- deferred tax liability: core idea ::@:: It records the future tax burden created when current temporary differences will make taxable income larger in later periods. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- deferred tax liability: usual book-basis direction ::@:: Book basis is greater than tax basis, so some amount recognized under IFRS today will still be taxed in the future. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

### taxable temporary differences and the Chelsea sequence

The standard course logic is:

- if __book basis is greater than tax basis__, future taxable amounts will appear; and
- those future taxable amounts create a deferred tax liability.

The Chelsea accounts-receivable sequence is the course's basic model for a deferred tax liability created by revenue recognized earlier for IFRS than for tax.

> _Accounts receivable difference._ Chelsea reports {@{&#36;30&nbsp;000 of accounts receivable}@} at the end of 2025 for IFRS purposes, but the receivable has {@{zero tax basis because the related revenue will not be taxed until cash is collected}@}. The tax rate is {@{40%, so the temporary difference creates a deferred tax liability}@}.
>
> | {@{Record 2025 income tax expense and deferred tax liability}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{28&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{16&nbsp;000}@} |
> | {@{Deferred tax liability}@} | | {@{12&nbsp;000}@} |
>
> _Explanation._ The current payable is based on the year's taxable income, but the receivable difference means Chelsea will pay more tax later when those receivables are collected. That future tax effect is recognized now as a deferred tax liability. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Reversal year for the Chelsea deferred tax liability._ In the next year, the remaining temporary difference has fallen, so the deferred tax liability must be reduced from its prior level. Assume current tax payable for 2026 is {@{&#36;36&nbsp;000}@}, while income tax expense remains {@{&#36;28&nbsp;000}@}.
>
> | {@{Record 2026 income taxes as the deferred tax liability reverses}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{28&nbsp;000}@} | |
> | {@{Deferred tax liability}@} | {@{8&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{36&nbsp;000}@} |
>
> _Explanation._ The debit to {@{Deferred tax liability}@} shows that part of the future tax burden recognized in 2025 is now being {@{used up as the receivables are collected and taxed}@}. <!--SR:!fsrs,2026-07-26T03:29:04.464Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:04.464Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Final reversal of the Chelsea deferred tax liability._ By the last reversal year, assume current tax payable is {@{&#36;32&nbsp;000}@} while income tax expense is still {@{&#36;28&nbsp;000}@}.
>
> | {@{Record final reversal of deferred tax liability}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{28&nbsp;000}@} | |
> | {@{Deferred tax liability}@} | {@{4&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{32&nbsp;000}@} |
>
> _Explanation._ The temporary difference is now {@{fully reversed, so the deferred tax liability falls to zero}@}. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Tax-rate change during the reversal sequence._ Suppose that after the 2026 reporting date but before the 2026 statements are issued, a new law is __enacted__ reducing the future tax rate from {@{40% to 35%, so the remaining 10&nbsp;000 temporary difference should produce a deferred tax liability of 3&nbsp;500 rather than 4&nbsp;000}@}.
>
> | {@{Remeasure the remaining Chelsea deferred tax liability for the enacted lower future tax rate}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax liability}@} | {@{500}@} | |
> | {@{Income tax expense}@} | | {@{500}@} |
>
> _Explanation._ The liability falls because the same remaining future taxable amount of {@{10&nbsp;000}@} will now be taxed at only {@{35% rather than 40%}@}. The adjustment is recorded {@{immediately in the period when the tax-rate change becomes enacted}@}. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

As the receivables are later collected and taxed, the difference reverses and the deferred tax liability falls.

- End of 2025: temporary difference 30 000 -> DTL 12 000.
- End of 2026: remaining difference 10 000 -> DTL 4 000.
- End of 2027: difference 0 -> DTL 0.

The key pattern is that the deferred tax liability is always measured from the __remaining__ temporary difference at the reporting date, not from the original difference forever.

---

Flashcards for this section are as follows:

- Chelsea receivable sequence: what is the underlying temporary difference? ::@:: Accounts receivable revenue has already been recognized for IFRS, but the receivable still has zero tax basis because taxation waits until cash collection. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Chelsea sequence: why does the deferred tax liability shrink over time? ::@:: Because the receivable difference reverses as cash is collected and taxed, leaving a smaller remaining future taxable amount at each reporting date. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- deferred tax liability: definition ::@:: The increase in taxes payable in future years caused by taxable temporary differences existing at the end of the current year. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- taxable temporary difference: usual direction of book basis versus tax basis ::@:: Book basis is greater than tax basis, so future taxable amounts will arise. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Chelsea receivable example: why does a deferred tax liability arise? ::@:: Because the receivable is already recognized for IFRS but has not yet been taxed, so future cash collection will trigger future taxable income. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- deferred tax liability measurement: what base is used each year? ::@:: The remaining temporary difference at the reporting date multiplied by the applicable tax rate. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- why can the deferred tax liability decrease even when current tax payable is high? ::@:: Because reversal of an old taxable temporary difference reduces the deferred tax balance even while current taxable income may still be large. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Chelsea deferred tax liability with an enacted future tax-rate cut: what happens? ::@:: Remeasure the remaining deferred tax liability using the new enacted future rate, debit the _Deferred tax liability_ for the reduction, and credit _Income tax expense_ because the future tax burden has fallen. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Chelsea 2025: AR &#36;30&nbsp;000 (zero tax basis), 40% rate → year-end DTL = ? ::@:: &#36;30&nbsp;000 × 40% = &#36;12&nbsp;000; income tax expense = payable &#36;16&nbsp;000 + DTL &#36;12&nbsp;000 = &#36;28&nbsp;000. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-12-23T00:00:00.000Z,167,167.48678403,1,2,4,0,0,2026-07-09T00:00:00.000Z-->

## deferred tax assets and non-recognition

A __deferred tax asset__ represents future tax savings caused by existing __deductible temporary differences__.

---

Flashcards for this section are as follows:

- deferred tax asset: core idea ::@:: It records a future tax saving created when IFRS recognizes an expense or liability now but tax law delays the deduction until later. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- deferred tax asset: why is it a future tax benefit? ::@:: Because the temporary difference will reduce taxes payable in a later period once the deduction becomes available on the tax return. <!--SR:!fsrs,2026-07-26T03:29:12.000Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:12.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

### deductible temporary differences

The course's main logic is:

- if the company has already recognized an expense or liability for IFRS purposes;
- but the tax deduction will only be allowed later;
- then the company has a future tax benefit and should record a deferred tax asset.

The warranty-liability example is the standard pattern.

> _Warranty liability._ Cunningham estimates warranty costs of {@{&#36;500&nbsp;000}@} in 2025 and records the expense and related warranty liability for IFRS. For tax, the deduction is allowed only when warranty costs are actually paid. The tax rate is {@{40%}@}.
>
> | {@{Recognize warranty expense under IFRS}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Warranty expense}@} | {@{500&nbsp;000}@} | |
> | {@{Warranty liability}@} | | {@{500&nbsp;000}@} |
>
> | {@{Record income taxes including deferred tax asset}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{600&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | {@{200&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{800&nbsp;000}@} |
>
> _Explanation._ The company has already recognized the warranty expense for IFRS, but tax law will only allow the deduction when cash is paid later. That future deduction creates a deferred tax asset of {@{200&nbsp;000}@}. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-26T03:29:21.204Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:21.204Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->

A litigation accrual works the same way: if IFRS records the expense now but tax only deducts it when paid, the company has a deductible temporary difference and therefore a deferred tax asset.

---

Flashcards for this section are as follows:

- deductible temporary difference: usual story line ::@:: IFRS recognizes the expense earlier than tax does, so the company has a future deduction still waiting to be used. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- warranty accrual: why does it create a deferred tax asset? ::@:: Because the warranty expense is already recognized under IFRS, but tax law waits until warranty claims are actually paid before allowing the deduction. <!--SR:!fsrs,2026-08-19T15:29:14.626Z,66,65.82761219,2.63070775,2,3,0,0,2026-06-14T15:29:14.626Z!fsrs,2026-08-09T15:28:48.705Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:28:48.705Z-->
- Cunningham: &#36;500&nbsp;000 warranty accrual, 40% rate → DTA = ? ::@:: &#36;500&nbsp;000 × 40% = &#36;200&nbsp;000; income tax expense = payable &#36;800&nbsp;000 − DTA &#36;200&nbsp;000 = &#36;600&nbsp;000. <!--SR:!fsrs,2026-07-26T03:29:05.674Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:05.674Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

### non-recognition and later reversal

__When not all of a deferred tax asset is recoverable.__

The course also teaches __non-recognition__ or reduction of deferred tax assets. A company must reduce the carrying amount of a deferred tax asset if it is __probable__ that some portion of the tax benefit will not be realized. IAS 12 uses the same __probable__ threshold for the initial recognition: a deferred tax asset is recognized only to the extent that it is probable that sufficient future taxable profit will be available against which the deductible temporary difference can be utilized. The slides define __probable__ as a level of likelihood of __at least slightly more than 50%__.

That means a deferred tax asset is not automatic forever. The company must ask whether future taxable income will be sufficient to use the benefit.

> _Partial non-recognition._ Jensen records an initial deferred tax asset of {@{€400&nbsp;000}@}, but later concludes that it is probable that {@{€100&nbsp;000}@} will not be realized.
>
> | {@{Reduce deferred tax asset for non-recognition}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{100&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | | {@{100&nbsp;000}@} | <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Show the full sequence instead of only the write-down._ Suppose the company first records the original deferred tax asset of {@{€400&nbsp;000}@}, then later concludes that only {@{€300&nbsp;000 is probable of realization}@}. The write-down is not the original recognition; it is a second step after the asset has already been booked.
>
> | {@{Recognize the original deferred tax asset before any non-recognition adjustment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax asset}@} | {@{400&nbsp;000}@} | |
> | {@{Income tax expense}@} | | {@{400&nbsp;000}@} |
>
> | {@{Then reduce the deferred tax asset to the amount now judged probable of realization}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{100&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | | {@{100&nbsp;000}@} |
>
> _Explanation._ Students often jump straight to the write-down entry and forget the sequence. The cleaner exam logic is: {@{recognize the full tax effect of the deductible temporary difference first}@}, then {@{write down the part that is not probable of realization}@}. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

If expectations later improve, part of that earlier reduction can be reversed.

<!-- markdownlint MD028 -->

> _Partial reversal of earlier non-recognition._ Suppose the deferred tax asset had been reduced from {@{€400&nbsp;000 to €300&nbsp;000}@}, but improved evidence now suggests that {@{€350&nbsp;000 is recoverable}@}.
>
> | {@{Increase deferred tax asset after expectations improve}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax asset}@} | {@{50&nbsp;000}@} | |
> | {@{Income tax expense}@} | | {@{50&nbsp;000}@} |
>
> _Explanation._ Reversing part of the earlier non-recognition {@{reduces current-period income tax expense}@} because more of the future tax benefit is now expected to be realized. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Reversal of a litigation-related deferred tax asset when the deduction is finally realized._ Assume a company had recognized a {@{€20&nbsp;000 deferred tax asset}@} from a litigation accrual in the prior year. In the settlement year, current tax payable is {@{€180&nbsp;000}@} while income tax expense is {@{€200&nbsp;000}@}.
>
> | {@{Record income taxes when a litigation-related deferred tax asset reverses}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{200&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | | {@{20&nbsp;000}@} |
> | {@{Income taxes payable}@} | | {@{180&nbsp;000}@} |
>
> _Explanation._ The deferred tax asset disappears because the tax deduction has now {@{actually been used on the tax return}@}. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- deferred tax asset non-recognition: what question is management testing? ::@:: Whether enough future taxable income is probable so that the company can actually realize the deferred tax benefit. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- deferred tax asset write-down and reversal: what is the direction of the income-tax effect? ::@:: Writing the asset down increases income tax expense, while restoring a realizable portion later reduces income tax expense. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- deferred tax asset non-recognition: when is a reduction required? ::@:: When it is probable that some portion or all of the deferred tax asset will not be realized through future taxable income. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- deferred tax asset reduction: income-statement effect ::@:: Reducing the deferred tax asset increases current income tax expense. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- improved evidence after DTA non-recognition: what entry is made? ::@:: Debit _Deferred tax asset_ and credit _Income tax expense_ for the amount now expected to be realizable. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- litigation-related deferred tax asset: what happens in the settlement year? ::@:: Credit the _Deferred tax asset_ and compare _Income tax expense_ with _Income taxes payable_ as the previously deferred tax benefit is realized. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- deferred tax asset non-recognition: what is the sequence students often miss? ::@:: First recognize the full deferred tax asset created by the deductible temporary difference, then record a separate write-down for any portion that is not probable of realization. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

## mixed current-tax and deferred-tax questions

The transcript's multi-item examples use one workflow again and again.

1. Start with __pretax financial income__ under IFRS.
2. Remove or add back __permanent differences__ to move toward taxable income, because those items affect current tax but do __not__ create deferred balances.
3. Identify which __temporary differences__ create future taxable amounts or future deductible amounts.
4. Compute __current tax payable__ from taxable income under tax law.
5. Compute the ending __deferred tax assets__ and __deferred tax liabilities__ from the temporary differences still remaining at the reporting date.
6. Combine the current and deferred pieces to obtain total __income tax expense__.

This is why a mixed deferred-tax question often contains two different-looking adjustments at once. A fine may increase taxable income now but never create a deferred item. A warranty accrual may also increase taxable income now, but unlike the fine it creates a __future deduction__ and therefore a deferred tax asset. The accounting job is to keep those effects separate instead of treating every book–tax difference as if it worked the same way.

> _Mixed current-and-deferred example._ Patel reports {@{pretax financial income of €1&nbsp;000&nbsp;000}@}. Included in that IFRS amount are a {@{non-deductible fine of €50&nbsp;000}@} and a {@{warranty expense accrual of €120&nbsp;000 that will be deductible only when paid}@}. The tax rate is {@{30%}@}. Taxable income is therefore {@{€1&nbsp;000&nbsp;000 + €50&nbsp;000 + €120&nbsp;000 = €1&nbsp;170&nbsp;000}@}, so current tax payable is {@{€351&nbsp;000}@}. The warranty accrual creates a deferred tax asset of {@{€36&nbsp;000}@}.
>
> | {@{Record current tax payable and deferred tax asset in one mixed question}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{315&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | {@{36&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{351&nbsp;000}@} |
>
> _Explanation._ The {@{fine is a permanent difference}@}, so it changes only current taxable income. The {@{warranty accrual is a deductible temporary difference}@}, so it creates a deferred tax asset. Total income tax expense is {@{€351&nbsp;000 − €36&nbsp;000 = €315&nbsp;000}@}. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- mixed deferred-tax question: first step ::@:: Start with pretax financial income under IFRS before separating permanent and temporary differences. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- permanent difference in a mixed tax question: what does it change? ::@:: It changes current taxable income but does not create a deferred tax asset or deferred tax liability. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- temporary difference in a mixed tax question: what extra step is needed? ::@:: Determine whether it creates future taxable amounts or future deductible amounts and then measure the related deferred tax balance. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- why can a fine and a warranty accrual not be treated the same way in a mixed deferred-tax problem? ::@:: Both may affect current taxable income, but a fine never reverses whereas a warranty accrual creates a future deduction and therefore a deferred tax asset. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- mixed tax example: why is the fine not part of the deferred-tax entry? ::@:: Because the fine is a permanent difference, so it changes taxable income now but never creates a future reversing amount. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- mixed tax example: why does the warranty accrual create a deferred tax asset? ::@:: Because IFRS recognizes the expense now but tax law allows the deduction only when the warranty cash outflow is paid later. <!--SR:!fsrs,2026-07-26T03:29:19.527Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:19.527Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Patel: pretax €1&nbsp;000&nbsp;000, fine €50&nbsp;000 (perm), warranty €120&nbsp;000 (temp), 30% rate → income tax expense = ? ::@:: Taxable income = €1&nbsp;170&nbsp;000; current tax = €351&nbsp;000; DTA = €36&nbsp;000; expense = €351&nbsp;000 − €36&nbsp;000 = €315&nbsp;000. <!--SR:!fsrs,2026-08-19T00:00:00.000Z,57,56.75502863,1,2,3,0,0,2026-06-23T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

## income tax expense: current plus deferred

The course repeatedly expresses total income tax expense as a combination of:

- __current tax__: the tax payable under the current year's tax return; and
- __deferred tax__: the change in the net deferred tax position.

A good working formula is:

- `Income tax expense = current tax payable + deferred tax expense`

where deferred tax expense can itself be positive or negative depending on whether deferred tax liabilities rise, deferred tax assets fall, or the opposite happens.

For a first-year deferred tax liability situation such as Chelsea's 2025, the logic is straightforward:

- current payable 16 000;
- deferred tax liability created 12 000;
- total income tax expense 28 000.

In later years, reversal entries can make current payable exceed income tax expense.

For a first-year deferred tax asset situation such as Hunt's litigation example, the numbers go the other way:

- current payable may be 200 000;
- deferred tax asset created 20 000;
- total income tax expense only 180 000.

That is why the course keeps returning to the phrase __current plus deferred__. It is the cleanest way to stop mixing current tax law with period-based IFRS expense allocation.

> _Current-plus-deferred example with both DTL and DTA._ Linton reports {@{pretax financial income of ¥800&nbsp;000}@}. That amount includes {@{¥20&nbsp;000 of non-taxable government bond interest}@}, a {@{¥60&nbsp;000 warranty accrual deductible only when paid}@}, and {@{¥100&nbsp;000 of installment-sale profit recognized for IFRS now but taxed later}@}. The tax rate is {@{25%}@}. Taxable income is {@{¥800&nbsp;000 − ¥20&nbsp;000 + ¥60&nbsp;000 − ¥100&nbsp;000 = ¥740&nbsp;000}@}, so current tax payable is {@{¥185&nbsp;000}@}. The warranty accrual creates a deferred tax asset of {@{¥15&nbsp;000}@}, while the installment-sale profit creates a deferred tax liability of {@{¥25&nbsp;000}@}. Total income tax expense is therefore {@{¥185&nbsp;000 + ¥25&nbsp;000 − ¥15&nbsp;000 = ¥195&nbsp;000}@}.
>
> | {@{Record income tax expense as current plus deferred pieces}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{195&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | {@{15&nbsp;000}@} | |
> | {@{Deferred tax liability}@} | | {@{25&nbsp;000}@} |
> | {@{Income taxes payable}@} | | {@{185&nbsp;000}@} |
>
> _Explanation._ The {@{government bond interest is permanent}@}, so it never enters deferred tax. The {@{warranty accrual lowers future taxes}@}, so it creates a deferred tax asset, while the {@{installment-sale difference increases future taxes}@}, so it creates a deferred tax liability. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-26T03:29:22.962Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:22.962Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- income tax expense: working formula in this course ::@:: Income tax expense equals current tax payable plus deferred tax expense or minus a deferred tax benefit. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- why can current tax payable exceed income tax expense? ::@:: Because a reversing deferred tax asset or liability may reduce the period's total tax expense relative to the current cash tax obligation. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- why can current tax payable be lower than income tax expense? ::@:: Because new taxable temporary differences can create deferred tax liabilities that add to current tax payable to produce total tax expense. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-10-18T00:00:00.000Z,101,100.76250358,1.25931726,2,4,0,0,2026-07-09T00:00:00.000Z-->
- current plus deferred: why is this phrase so central? ::@:: Because this deferred-tax topic allocates the tax consequences of timing differences across periods instead of treating tax expense as the same thing as the current tax return. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- current-plus-deferred example: what creates the deferred tax liability? ::@:: The installment-sale profit recognized for IFRS now but taxed later, because it creates future taxable amounts. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- current-plus-deferred example: what creates the deferred tax asset? ::@:: The warranty accrual recognized now for IFRS but deductible only when paid later, because it creates future deductible amounts. <!--SR:!fsrs,2026-08-09T15:29:29.258Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:29.258Z!fsrs,2026-08-16T15:28:43.221Z,63,63.33552034,2.98092302,2,3,0,0,2026-06-14T15:28:43.221Z-->
- Linton: pretax ¥800&nbsp;000, perm diff ¥20&nbsp;000, warranty ¥60&nbsp;000 (DTA), installment ¥100&nbsp;000 (DTL), 25% rate → income tax expense = ? ::@:: Taxable income = ¥740&nbsp;000; current tax = ¥185&nbsp;000; DTA = ¥15&nbsp;000; DTL = ¥25&nbsp;000; expense = ¥185&nbsp;000 + ¥25&nbsp;000 − ¥15&nbsp;000 = ¥195&nbsp;000. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-10-06T00:00:00.000Z,97,96.66081201,1.24776142,2,4,0,0,2026-07-01T00:00:00.000Z-->

## future tax rates and revisions of deferred taxes

Deferred taxes are not always measured using today's rate mechanically. If tax-law changes have already been __enacted__ for future years, the company must use those enacted future rates when measuring the future tax effects of existing temporary differences.

Two rules matter.

1. If future tax-rate changes are already enacted, measure the future reversals using those enacted rates.
2. When a tax-rate revision is enacted, adjust existing deferred tax accounts __immediately__ and take the effect to income tax expense in the period of the change.

> _Tax-rate revision example._ A company has a deferred tax liability of {@{&#36;1&nbsp;200&nbsp;000}@} based on a {@{40% tax rate}@}. A new law lowers the applicable future rate so that the correct deferred tax liability should now be only {@{&#36;1&nbsp;100&nbsp;000}@}.
>
> | {@{Reduce deferred tax liability for enacted tax-rate change}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax liability}@} | {@{100&nbsp;000}@} | |
> | {@{Income tax expense}@} | | {@{100&nbsp;000}@} |
>
> _Explanation._ Lower future tax rates mean a smaller future tax burden, so the deferred tax liability falls and current-period income tax expense is reduced. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-12-23T00:00:00.000Z,167,167.48678403,1,2,4,0,0,2026-07-09T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Tax-rate change affecting a deferred tax asset._ Assume instead that a company has a {@{deferred tax asset of €420&nbsp;000}@} measured using an enacted {@{35% future rate}@}. A new law increases the enacted future rate so the correct deferred tax asset should now be {@{€480&nbsp;000}@}.
>
> | {@{Increase deferred tax asset for enacted tax-rate change}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax asset}@} | {@{60&nbsp;000}@} | |
> | {@{Income tax expense}@} | | {@{60&nbsp;000}@} |
>
> _Explanation._ A higher enacted future tax rate makes future deductions {@{more valuable}@}, so the deferred tax asset increases and income tax expense falls. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- future tax rates: when may the company use a future tax rate instead of the current rate? ::@:: When the future tax-rate change has already been enacted. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- if a future tax rate has not yet been enacted, what rate is used? ::@:: The current rate. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- enacted tax-rate change: what happens to existing deferred tax balances? ::@:: They are remeasured immediately, and the effect goes to income tax expense in the period of the change. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- falling enacted future tax rates: what happens to a deferred tax liability? ::@:: It decreases because the future taxable amounts will now be taxed at a lower rate. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- falling enacted future tax rates: what happens to income tax expense when a deferred tax liability is revised downward? ::@:: Income tax expense decreases. <!--SR:!fsrs,2026-08-04T15:29:05.039Z,51,50.97888252,3.63132281,2,3,0,0,2026-06-14T15:29:05.039Z!fsrs,2026-08-09T15:29:34.631Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:34.631Z-->
- enacted increase in future tax rates: what happens to a deferred tax asset? ::@:: It increases because future deductible amounts now save more tax, so income tax expense decreases. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

## loss carryforwards and carrybacks

A __net operating loss__ means tax-deductible expenses exceed taxable revenues for the period. Tax law may let the company use that loss outside the current year.

---

Flashcards for this section are as follows:

- net operating loss: why does it matter beyond the current year? ::@:: Because tax law may let the company use that loss against taxable income from other years through a carryforward, a carryback, or both. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- carryforward versus carryback: high-level contrast ::@:: A carryforward creates a future benefit through a deferred tax asset, while a carryback creates an immediately realizable refund receivable from prior-year taxes. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

### loss carryforward

Under a __loss carryforward__, the company uses the current loss to reduce taxable income in future years. The accounting idea is the same as other future tax benefits: if realization is probable, the company records a deferred tax asset in the loss year.

IAS 12 imposes __no fixed time limit__ on how long an unused tax loss may be carried forward. This contrasts with US GAAP, which historically restricted carryforwards to 20 years. Under IFRS, the deferred tax asset is recognized as long as it is probable that sufficient future taxable profit will be available, regardless of how many years the loss may remain legally available under local tax law.

> _Carryforward example._ Groh has a {@{&#36;200&nbsp;000 net operating loss}@} in 2025. The enacted future tax rate is {@{20%}@}. The future tax benefit is {@{&#36;40&nbsp;000}@}.
>
> | {@{Recognize loss carryforward benefit in the loss year}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax asset}@} | {@{40&nbsp;000}@} | |
> | {@{Income tax expense (loss carryforward)}@} | | {@{40&nbsp;000}@} | <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->

When the company later earns taxable income and uses the carryforward, the deferred tax asset is reversed instead of recognizing the benefit again from scratch.

<!-- markdownlint MD028 -->

> _Realization of a previously recognized loss carryforward._ In the next year, assume taxable income before applying the carryforward is {@{&#36;250&nbsp;000}@}. The company uses the prior-year {@{&#36;200&nbsp;000 carryforward}@}, so current tax payable is only {@{&#36;10&nbsp;000}@} while income tax expense is {@{&#36;50&nbsp;000}@}.
>
> | {@{Record income taxes when a loss carryforward is realized}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{50&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | | {@{40&nbsp;000}@} |
> | {@{Income taxes payable}@} | | {@{10&nbsp;000}@} |
>
> _Explanation._ The deferred tax asset is {@{used up in the profitable year}@}; the tax benefit was recognized earlier, so only the reversal appears now. <!--SR:!fsrs,2026-08-09T15:29:06.088Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:06.088Z!fsrs,2026-08-09T15:29:35.676Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:35.676Z!fsrs,2026-08-09T15:29:15.820Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:15.820Z!fsrs,2026-08-09T15:28:44.940Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:28:44.940Z!fsrs,2026-08-09T15:29:31.319Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:31.319Z!fsrs,2026-08-09T15:28:47.769Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:28:47.769Z!fsrs,2026-08-16T15:29:15.309Z,63,63.33552034,2.98092302,2,3,0,0,2026-06-14T15:29:15.309Z!fsrs,2026-08-09T15:28:46.839Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:28:46.839Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- loss carryforward: what is recognized in the loss year if realization is probable? ::@:: A deferred tax asset for the future tax saving expected to be used against later taxable income. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- loss carryforward: what happens in the later profitable year? ::@:: The deferred tax asset is reversed as the company actually uses the carryforward on its tax return. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->

### loss carryback

Some tax systems also allow a __loss carryback__. The company applies the loss to prior years, receives a refund of taxes already paid, and recognizes the refund receivable in the loss year because the benefit is currently realizable.

The course appendix example uses the following ordering rule:

- apply the loss first to the __earliest year within the carryback window__ before moving to the later year, following the local tax rule used in the example.

> _Carryback plus carryforward example._ Groh has a {@{&#36;500&nbsp;000 loss}@}. It carries the loss back far enough to recover {@{&#36;65&nbsp;000 of previously paid taxes}@} and still has an unused loss amount left to carry forward.
>
> | {@{Recognize tax benefit of loss carryback}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax refund receivable}@} | {@{65&nbsp;000}@} | |
> | {@{Income tax expense (loss carryback)}@} | | {@{65&nbsp;000}@} | <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Combined carryback and carryforward entry._ Suppose a single {@{&#36;500&nbsp;000 loss}@} generates both a {@{&#36;65&nbsp;000 refund from carryback}@} and a remaining {@{&#36;200&nbsp;000 carryforward}@} taxed at {@{25%}@}, creating a {@{&#36;50&nbsp;000 deferred tax asset}@}.
>
> | {@{Record both the loss carryback and the remaining carryforward benefit}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax refund receivable}@} | {@{65&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | {@{50&nbsp;000}@} | |
> | {@{Income tax expense (loss carryback)}@} | | {@{65&nbsp;000}@} |
> | {@{Income tax expense (loss carryforward)}@} | | {@{50&nbsp;000}@} |
>
> _Explanation._ One loss year can create both an {@{immediately realizable refund asset}@} and a {@{future tax-benefit asset}@}. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Catch-up entry after earlier non-recognition of a loss carryforward._ Suppose the company did {@{not recognize a deferred tax asset in the loss year}@} because realization was not yet probable. In the next year, profitability returns and the {@{&#36;40&nbsp;000 tax benefit becomes realizable}@}.
>
> | {@{Recognize previously unrecorded deferred tax asset once realization becomes probable}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax asset}@} | {@{40&nbsp;000}@} | |
> | {@{Income tax expense (loss carryforward)}@} | | {@{40&nbsp;000}@} |
>
> | {@{Then record current-year income taxes using the now-recognized carryforward}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{50&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | | {@{40&nbsp;000}@} |
> | {@{Income taxes payable}@} | | {@{10&nbsp;000}@} |
>
> _Explanation._ The first entry is a {@{catch-up recognition of the deferred tax asset}@}; the second entry is the normal profitable-year reversal of that same asset. <!--SR:!fsrs,2026-08-09T15:29:37.940Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:37.940Z!fsrs,2026-08-09T15:29:30.346Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:30.346Z!fsrs,2026-08-09T15:29:33.048Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:33.048Z!fsrs,2026-08-09T15:29:36.924Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:36.924Z!fsrs,2026-08-09T15:28:49.550Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:28:49.550Z!fsrs,2026-08-16T15:25:27.587Z,63,63.33552034,2.98092302,2,3,0,0,2026-06-14T15:25:27.587Z!fsrs,2026-08-09T15:28:44.147Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:28:44.147Z!fsrs,2026-08-09T15:25:28.377Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:25:28.377Z!fsrs,2026-08-09T15:29:18.596Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:18.596Z!fsrs,2026-08-09T15:29:02.778Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:02.778Z!fsrs,2026-08-09T15:25:29.127Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:25:29.127Z!fsrs,2026-08-09T15:28:45.891Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:28:45.891Z!fsrs,2026-08-09T15:29:07.243Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:29:07.243Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z!fsrs,2026-07-11T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-03T00:00:00.000Z-->

If part of the loss is still available for future years and realization is probable, the company also records a deferred tax asset for the carryforward portion.

If realization is __not__ probable, the deferred tax asset is not recognized until the benefit becomes sufficiently realizable.

---

Flashcards for this section are as follows:

- loss carryback: why is a receivable recognized immediately? ::@:: Because the benefit is already realizable against taxes paid in prior years rather than being only a future possibility. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- carryback plus carryforward: can one loss year create both? ::@:: Yes. One part of the loss can recover prior taxes immediately, and the rest can still create a deferred tax asset for future years. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- net operating loss: definition ::@:: Tax-deductible expenses exceed taxable revenues. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2027-01-24T00:00:00.000Z,195,194.80158051,1,2,4,0,0,2026-07-13T00:00:00.000Z-->
- loss carryforward: accounting effect in the loss year ::@:: Recognize a deferred tax asset for the future tax benefit if realization is probable. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- loss carryforward: why is the credit shown as an income-tax item instead of ordinary revenue? ::@:: Because it is a tax benefit, not an operating revenue item. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- loss carryback: accounting effect in the loss year ::@:: Recognize an income tax refund receivable and the related tax benefit because the refund is currently realizable. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-07-26T03:29:26.967Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:26.967Z-->
- carryback plus carryforward: can both appear from one loss year? ::@:: Yes; part of the loss may generate a refund from prior years and the remainder may generate a deferred tax asset for future years. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- uncertain realization of a loss carryforward: what happens? ::@:: Do not recognize the deferred tax asset until it is probable that the future tax benefit will be realized. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- loss carryforward realized in a profitable year: what happens to the deferred tax asset? ::@:: It is credited and reduced to the extent the carryforward is used on the tax return. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- carryback ordering rule in this course: which prior year is used first? ::@:: Apply the loss first to the earliest year within the permitted carryback window before moving to later years. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- Groh carryforward: &#36;200&nbsp;000 NOL, future rate 20% → DTA in loss year = ? ::@:: &#36;200&nbsp;000 × 20% = &#36;40&nbsp;000; realization year: taxable income &#36;250&nbsp;000, carryforward &#36;200&nbsp;000, current tax = &#36;10&nbsp;000, income tax expense = &#36;50&nbsp;000. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

## interperiod tax allocation and presentation

The course appendix combines several temporary and permanent differences into one multi-year interperiod-tax-allocation problem. The point of that comprehensive example is not to add a new basic rule. It shows how the earlier rules interact in one schedule.

Typical ingredients in the comprehensive example are:

- installment-sale revenue recognized earlier for IFRS than for tax -> deferred tax liability;
- depreciation patterns that differ between IFRS and tax -> often deferred tax liability in early years;
- warranty-cost timing differences -> deferred tax asset;
- permanent differences such as non-taxable government bond interest or non-deductible fines -> no deferred tax balance; and
- a need to measure each future reversal using the enacted tax rate for the period in which reversal will occur.

The presentation rules in this topic are also exam-relevant:

- deferred tax assets and deferred tax liabilities are generally presented as __non-current__ in the course materials;
- companies may net deferred tax assets against deferred tax liabilities to show a net deferred tax position; and
- the income statement may show income tax expense as one line, with significant current-versus-deferred components disclosed on the face or in the notes.

A good way to read a comprehensive tax question is:

1. Separate __temporary__ differences from __permanent__ ones.
2. Decide whether each temporary difference creates future taxable or future deductible amounts.
3. Measure the deferred tax effect using the correct enacted rate.
4. Combine current tax and deferred tax to get total income tax expense.
5. Check whether any deferred tax asset needs to be reduced because realization is not probable.

> _Comprehensive interperiod-tax-allocation entry._ Assume a first-year company reports {@{pretax financial income of ¥412&nbsp;000}@}. Permanent differences are {@{¥28&nbsp;000 of non-taxable government bond interest}@} and {@{¥26&nbsp;000 of non-deductible fines}@}. Temporary differences create a {@{deferred tax liability of ¥186&nbsp;400}@} and a {@{deferred tax asset of ¥62&nbsp;400}@}. Current income taxes payable are {@{¥50&nbsp;000}@}. Total income tax expense is therefore {@{¥174&nbsp;000}@}.
>
> | {@{Record current and deferred tax effects in one comprehensive entry}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{174&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | {@{62&nbsp;400}@} | |
> | {@{Income taxes payable}@} | | {@{50&nbsp;000}@} |
> | {@{Deferred tax liability}@} | | {@{186&nbsp;400}@} |
>
> _Explanation._ This single entry bundles the topic's main workflow: {@{current tax payable plus net deferred tax expense after separating temporary and permanent differences}@}. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,42,41.57871783,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- comprehensive interperiod tax allocation: why separate temporary and permanent differences first? ::@:: Because temporary differences create deferred taxes while permanent differences do not. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- comprehensive tax problem: what question identifies whether the difference creates a deferred tax liability or asset? ::@:: Ask whether the difference creates future taxable amounts or future deductible amounts. <!--SR:!fsrs,2026-07-26T03:29:15.001Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:15.001Z!fsrs,2026-07-26T03:29:17.570Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:17.570Z-->
- permanent differences in a comprehensive schedule: do they enter deferred tax balances? ::@:: No; they affect taxable income but do not create deferred tax assets or liabilities. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- deferred tax presentation in this course: how are deferred tax balances generally classified? ::@:: As non-current. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- comprehensive tax workflow: what is the final combination step? ::@:: Combine current tax payable with the deferred tax effect to arrive at total income tax expense. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- comprehensive tax entry: why can both a deferred tax asset and deferred tax liability appear in the same journal entry? ::@:: Because different temporary differences can create future deductible amounts and future taxable amounts at the same reporting date, so the company records both pieces together with current tax payable. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Comprehensive entry: pretax ¥412&nbsp;000, current tax ¥50&nbsp;000, DTL ¥186&nbsp;400, DTA ¥62&nbsp;400 → income tax expense = ? ::@:: ¥50&nbsp;000 + ¥186&nbsp;400 − ¥62&nbsp;400 = ¥174&nbsp;000. <!--SR:!fsrs,2026-08-09T15:25:26.293Z,56,56.31604278,3.98153807,2,2,0,0,2026-06-14T15:25:26.293Z!fsrs,2026-08-16T15:29:38.927Z,63,63.33552034,2.98092302,2,3,0,0,2026-06-14T15:29:38.927Z-->

## intraperiod tax allocation

__Intraperiod tax allocation__ requires that the tax consequences of an item follow that item into the same presentation component rather than all flowing through profit or loss.

IAS 12 distinguishes three destinations for tax consequences within a single period:

- items recognized in __profit or loss__ carry their current or deferred tax charge or benefit through income tax expense in __profit or loss__;
- items recognized in __other comprehensive income (OCI)__ carry their deferred tax charge or benefit through __OCI__; and
- items recognized directly in __equity__ carry their deferred tax charge or benefit directly in __equity__.

A common example is a property revaluation under IAS 16. The revaluation increases the carrying amount above the tax base, creating a taxable temporary difference. Because the revaluation gain goes to OCI, the deferred tax liability on that difference also goes to OCI, not through income tax expense in profit or loss.

---

Flashcards for this section are as follows:

- intraperiod tax allocation: general rule ::@:: The tax consequence of an item follows that item into profit or loss, other comprehensive income, or equity — whichever component recognized the underlying transaction. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- revaluation surplus under IAS 16: where does the related deferred tax liability go? ::@:: Into other comprehensive income alongside the revaluation surplus, not through income tax expense in profit or loss. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- interperiod versus intraperiod tax allocation: contrast ::@:: Interperiod allocation assigns tax to the correct accounting period; intraperiod allocation assigns tax to the correct presentation component within a single period. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

## uncertain tax positions under IFRIC 23

When the tax treatment of a transaction is uncertain — for example, where the company has taken a position the tax authority might challenge — the company reflects that uncertainty in its tax balances using the guidance in IFRIC 23.

Key requirements:

- assume the tax authority will __examine the position with full knowledge__ of all relevant information;
- if it is __probable that the authority accepts the treatment__, recognize tax on that basis; and
- if it is __not probable__, measure the uncertain amount using either the __most likely amount__ (single most probable outcome) or the __expected value__ (probability-weighted sum of possible outcomes), whichever better predicts the resolution.

Recognized uncertain tax positions appear as additional current tax liabilities or as reductions in a deferred tax asset; they are not presented in a separate line item.

---

Flashcards for this section are as follows:

- IFRIC 23: what assumption does the entity make about the tax authority when assessing an uncertain tax position? ::@:: That the authority will examine the position with full knowledge of all relevant information. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- IFRIC 23: recognition threshold for an uncertain tax position ::@:: Whether it is probable that the tax authority will accept the entity's treatment; if not probable, a liability is recognized. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- IFRIC 23: two measurement approaches for an uncertain tax position ::@:: The most likely amount or the expected value, whichever better predicts the resolution of the uncertainty. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- uncertain tax position: where is the recognized liability presented? ::@:: As an additional current tax liability or as a reduction of a deferred tax asset, using existing IAS 12 line items rather than a separate caption. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

## effective tax rate reconciliation

IAS 12 requires a disclosed __reconciliation__ between income tax expense as reported and the amount that would result from applying the statutory rate to pretax financial income.

The reconciliation matters because __permanent differences__ cause the effective rate to diverge from the statutory rate. Temporary differences do __not__ cause a rate divergence: they shift timing but do not change the total lifetime tax charge.

The __effective tax rate__ for a period is $\text{income tax expense} \div \text{pretax financial income}$.

Typical reconciling items include:

- __non-deductible expenses__ (such as fines and penalties), which add tax expense without adding pretax income and therefore __push the effective rate above the statutory rate__; and
- __non-taxable income__ (such as government bond interest), which adds pretax income without adding taxable income and therefore __push the effective rate below the statutory rate__.

---

Flashcards for this section are as follows:

- effective tax rate: formula ::@:: Income tax expense divided by pretax financial income. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- why do permanent differences appear in the effective rate reconciliation but temporary differences do not? ::@:: Temporary differences reverse in later periods and leave no net lifetime tax effect, while permanent differences permanently alter the total tax paid relative to pretax accounting income. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- non-deductible expense: effect on the effective tax rate ::@:: Increases the effective rate above the statutory rate because taxable income is inflated relative to pretax financial income. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- non-taxable income: effect on the effective tax rate ::@:: Decreases the effective rate below the statutory rate because pretax financial income includes the exempt amount while taxable income does not. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

## multi-year exercise: depreciation, warranty, and rate change

This exercise combines a taxable temporary difference from accelerated depreciation, a deductible temporary difference from a warranty provision, and an enacted tax-rate change partway through. Working through all three years reinforces how to apply the balance-sheet approach and the rate-change remeasurement rule together.

__Scenario: Merton Ltd.__

Merton Ltd. begins operations on 1 January Year 1. Relevant data:

- __Equipment:__ cost €900&nbsp;000, depreciated straight-line over 3 years for IFRS (€300&nbsp;000 per year). For tax, the entire €900&nbsp;000 is deducted in Year 1. Tax depreciation in Years 2 and 3 is €nil.
- __Warranty:__ Merton accrues a €200&nbsp;000 warranty provision in Year 1. Payments are €120&nbsp;000 in Year 2 and €80&nbsp;000 in Year 3, deductible for tax when paid.
- __Tax rate:__ 30% for Years 1 and 2. A new law is __enacted at the end of Year 2__ setting the rate at 25% effective from Year 3 onwards.
- __Pretax financial income:__ €500&nbsp;000 (Year 1); €600&nbsp;000 (Year 2); €700&nbsp;000 (Year 3).

__Step 1 — taxable income and current tax payable.__

Year 1: add back IFRS dep €300&nbsp;000, deduct tax dep €900&nbsp;000, add back warranty €200&nbsp;000. Taxable income = €100&nbsp;000. Current tax = €100&nbsp;000 × 30% = €30&nbsp;000.

Year 2: add back IFRS dep €300&nbsp;000, no tax dep available. Warranty payments of €120&nbsp;000 now deductible. Taxable income = €780&nbsp;000. Current tax = €780&nbsp;000 × 30% = €234&nbsp;000.

Year 3: add back IFRS dep €300&nbsp;000, no tax dep available. Warranty payments of €80&nbsp;000 now deductible. Taxable income = €920&nbsp;000. Current tax = €920&nbsp;000 × 25% = €230&nbsp;000.

__Step 2 — deferred taxes at each year end, measured at the applicable enacted future rate.__

End of Year 1 (30% applies to all future reversals):

- Depreciation TD: €600&nbsp;000 excess tax dep already taken → future IFRS dep will not be deductible → taxable TD → DTL = €600&nbsp;000 × 30% = €180&nbsp;000.
- Warranty TD: €200&nbsp;000 warranty liability unpaid → future deductible payments → DTA = €200&nbsp;000 × 30% = €60&nbsp;000.

End of Year 2 (new enacted rate of 25% applies to Year 3 reversals):

- Depreciation TD remaining: €300&nbsp;000 → DTL = €300&nbsp;000 × 25% = €75&nbsp;000.
- Warranty TD remaining: €80&nbsp;000 → DTA = €80&nbsp;000 × 25% = €20&nbsp;000.

End of Year 3: both TDs fully reversed. DTL = €0; DTA = €0.

__Step 3 — income tax expense and journal entries.__

> Year 1 entry. DTL created for excess tax depreciation; DTA created for warranty accrual.
>
> | {@{Record Year 1 income taxes}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{150&nbsp;000}@} | |
> | {@{Deferred tax asset (warranty)}@} | {@{60&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{30&nbsp;000}@} |
> | {@{Deferred tax liability (depreciation)}@} | | {@{180&nbsp;000}@} |
>
> Expense = {@{&#36;30&nbsp;000}@} current tax + {@{&#36;180&nbsp;000}@} DTL created − {@{&#36;60&nbsp;000}@} DTA created = {@{&#36;150&nbsp;000}@}. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-26T03:29:20.459Z,41,41.28765564,1,2,3,0,0,2026-06-15T03:29:20.459Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Year 2 entry. Partial DTL reversal as €300&nbsp;000 of future taxable amounts are now current-year taxable; partial DTA reversal as €120&nbsp;000 of warranty payments are now deducted; and remeasurement of all remaining balances at the newly enacted 25% rate. All effects combine in one entry.
>
> | {@{Record Year 2 income taxes including rate-change remeasurement}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{169&nbsp;000}@} | |
> | {@{Deferred tax liability (depreciation)}@} | {@{105&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{234&nbsp;000}@} |
> | {@{Deferred tax asset (warranty)}@} | | {@{40&nbsp;000}@} |
>
> DTL falls from {@{&#36;180&nbsp;000}@} to {@{&#36;75&nbsp;000}@} (decrease {@{&#36;105&nbsp;000}@}: Dr _Deferred tax liability_). DTA falls from {@{&#36;60&nbsp;000}@} to {@{&#36;20&nbsp;000}@} (decrease {@{&#36;40&nbsp;000}@}: Cr _Deferred tax asset_). Expense = {@{&#36;234&nbsp;000 − &#36;105&nbsp;000 + &#36;40&nbsp;000 = &#36;169&nbsp;000}@}. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Year 3 entry. Both temporary differences reach zero.
>
> | {@{Record Year 3 income taxes as all temporary differences fully reverse}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{175&nbsp;000}@} | |
> | {@{Deferred tax liability (depreciation)}@} | {@{75&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{230&nbsp;000}@} |
> | {@{Deferred tax asset (warranty)}@} | | {@{20&nbsp;000}@} |
>
> Expense = {@{&#36;230&nbsp;000}@} current tax − {@{&#36;75&nbsp;000}@} DTL reversal + {@{&#36;20&nbsp;000}@} DTA reversal = {@{&#36;175&nbsp;000}@}. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2027-01-24T00:00:00.000Z,195,194.80158051,1,2,4,0,0,2026-07-13T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->

__Key observations:__

- In Year 2, the DTL debit (€105&nbsp;000) and DTA credit (€40&nbsp;000) pull income tax expense in opposite directions. The DTL falls by more than the DTA, so the rate cut produces a net tax benefit of €65&nbsp;000 in Year 2.
- When a DTL decreases because of a rate cut, the entry is a __debit__ (future tax burden shrinks → expense falls). When a DTA decreases because of a rate cut, the entry is a __credit__ (future tax saving shrinks → expense rises).
- By Year 3 both deferred balances are zero: the equipment has been fully depreciated for IFRS and all warranty claims have been paid.

---

Flashcards for this section are as follows:

- Merton exercise: why is Year 2 the most complex year to record? ::@:: Because the enacted rate cut simultaneously shrinks both the DTL and the DTA, and those two effects move income tax expense in opposite directions within the same entry. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- when a DTL decreases because of an enacted rate cut, what is the journal entry direction? ::@:: Debit the _Deferred tax liability_ and reduce _Income tax expense_, because the future tax burden has fallen. <!--SR:!fsrs,2026-07-31T00:00:00.000Z,42,41.57871783,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- when a DTA decreases because of an enacted rate cut, what is the journal entry direction? ::@:: Credit the _Deferred tax asset_ and increase _Income tax expense_, because some of the expected future tax saving has been lost. <!--SR:!fsrs,2026-12-23T00:00:00.000Z,167,167.48678403,1,2,4,0,0,2026-07-09T00:00:00.000Z!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z-->
- Merton exercise: in Year 2, does the net effect of the rate change increase or decrease income tax expense? ::@:: Decrease, because the DTL falls by €105&nbsp;000 while the DTA falls by only €40&nbsp;000, giving a net benefit of €65&nbsp;000. <!--SR:!fsrs,2026-08-28T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-18T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Merton exercise: what does the Year 3 entry reflect? ::@:: The full reversal of both remaining temporary differences: the last €300&nbsp;000 of IFRS depreciation reverses the DTL and the final €80&nbsp;000 warranty payment reverses the DTA. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Merton Year 1: taxable income €100&nbsp;000, equipment TD €600&nbsp;000 (DTL), warranty TD €200&nbsp;000 (DTA), 30% rate → income tax expense = ? ::@:: DTL = €600&nbsp;000 × 30% = €180&nbsp;000; DTA = €200&nbsp;000 × 30% = €60&nbsp;000; expense = €30&nbsp;000 + €180&nbsp;000 − €60&nbsp;000 = €150&nbsp;000. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Merton Year 2: current tax €234&nbsp;000, DTL falls from €180&nbsp;000 to €75&nbsp;000, DTA falls from €60&nbsp;000 to €20&nbsp;000 → income tax expense = ? ::@:: €234&nbsp;000 − €105&nbsp;000 (DTL decrease) + €40&nbsp;000 (DTA decrease) = €169&nbsp;000. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
