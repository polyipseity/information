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

- income taxes payable versus income tax expense ::@:: Income taxes payable is the amount currently owed under tax law, while income tax expense is the tax cost assigned to the accounting period under IFRS. <!--SR:!fsrs,2026-06-17T14:15:06.001Z,8,8.2956,1,2,1,0,0,2026-06-09T14:15:06.001Z!fsrs,2026-06-14T08:05:49.743Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:05:49.743Z-->
- why can income taxes payable differ from income tax expense? ::@:: Because IFRS and tax rules may recognize the same revenue or expense in different periods. <!--SR:!fsrs,2026-06-18T07:59:51.568Z,8,8.2956,1,2,1,0,0,2026-06-10T07:59:51.568Z!fsrs,2026-06-17T03:41:53.278Z,8,8.2956,1,2,1,0,0,2026-06-09T03:41:53.278Z-->
- interperiod tax allocation: main purpose ::@:: To recognize the future tax consequences of timing differences in the period in which those differences arise. <!--SR:!fsrs,2026-06-18T07:29:17.576Z,8,8.2956,1,2,1,0,0,2026-06-10T07:29:17.576Z!fsrs,2026-06-17T14:52:25.303Z,8,8.2956,1,2,1,0,0,2026-06-09T14:52:25.303Z-->

## temporary differences and permanent differences

The course separates differences between IFRS and tax reporting into two families.

---

Flashcards for this section are as follows:

- book-tax differences: two families in this topic ::@:: Temporary differences reverse later and create deferred taxes, while permanent differences never reverse and therefore affect only current tax. <!--SR:!fsrs,2026-06-17T12:05:20.370Z,8,8.2956,1,2,1,0,0,2026-06-09T12:05:20.370Z!fsrs,2026-06-18T06:07:37.363Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:37.363Z-->
- temporary versus permanent difference: why is the split central? ::@:: Because deferred tax accounting starts by asking whether the book-tax difference will reverse in a future period. <!--SR:!fsrs,2026-06-18T07:27:01.602Z,8,8.2956,1,2,1,0,0,2026-06-10T07:27:01.602Z!fsrs,2026-06-18T08:00:02.287Z,8,8.2956,1,2,1,0,0,2026-06-10T08:00:02.287Z-->

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

- temporary difference: what makes it temporary? ::@:: The book basis and tax basis differ now, but that difference will later reverse and create future taxable or deductible amounts. <!--SR:!fsrs,2026-06-18T06:07:33.934Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:33.934Z!fsrs,2026-06-18T06:13:22.988Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:22.988Z-->
- temporary differences: what two future effects must be classified? ::@:: Future taxable amounts create deferred tax liabilities, while future deductible amounts create deferred tax assets. <!--SR:!fsrs,2026-06-18T06:13:19.196Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:19.196Z!fsrs,2026-06-17T12:43:46.345Z,8,8.2956,1,2,1,0,0,2026-06-09T12:43:46.345Z-->
- revenue received in advance: which type of temporary difference does it create? ::@:: A deductible temporary difference, because the company is taxed when cash arrives but recognizes IFRS revenue later without further taxation, leaving a future non-taxable recognition that creates a tax saving. <!--SR:!fsrs,2026-06-17T08:34:56.167Z,8,8.2956,1,2,1,0,0,2026-06-09T08:34:56.167Z!fsrs,2026-06-18T07:27:02.210Z,8,8.2956,1,2,1,0,0,2026-06-10T07:27:02.210Z-->
- share-based payment (IFRS 2): what temporary difference does it typically create? ::@:: A deductible temporary difference, because the IFRS 2 expense is recognized over the vesting period while the tax deduction usually arises only when shares vest or options are exercised. <!--SR:!fsrs,2026-06-18T07:59:50.619Z,8,8.2956,1,2,1,0,0,2026-06-10T07:59:50.619Z!fsrs,2026-06-14T08:05:32.986Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:05:32.986Z-->
- prepaid expenses: what type of temporary difference and deferred tax do they create? ::@:: A taxable temporary difference and a deferred tax liability, because the tax authority allows the deduction now while IFRS expenses the item over time, so the future IFRS expense will not be deductible again. <!--SR:!fsrs,2026-06-17T03:48:34.416Z,8,8.2956,1,2,1,0,0,2026-06-09T03:48:34.416Z!fsrs,2026-06-18T02:49:51.469Z,8,8.2956,1,2,1,0,0,2026-06-10T02:49:51.469Z-->

### permanent differences

A __permanent difference__ affects either pretax financial income or taxable income, but it will __never reverse__.

Common course examples are:

- interest on certain government bonds that is recognized as revenue for IFRS but never taxed;
- fines and penalties that are expensed for IFRS but never deductible for tax; and
- some other non-deductible expenses such as certain insurance premiums for key officers or donation items depending on the tax law.

Permanent differences change the relation between pretax accounting income and taxable income, but they do __not__ create deferred tax assets or deferred tax liabilities.

---

Flashcards for this section are as follows:

- permanent difference: what is the defining feature? ::@:: It affects accounting income or taxable income now but never reverses in a later period. <!--SR:!fsrs,2026-06-17T15:33:14.263Z,8,8.2956,1,2,1,0,0,2026-06-09T15:33:14.263Z!fsrs,2026-06-17T07:25:03.241Z,8,8.2956,1,2,1,0,0,2026-06-09T07:25:03.241Z-->
- permanent differences: why do they not create deferred taxes? ::@:: Because there is no future taxable or deductible amount left to recognize in another period. <!--SR:!fsrs,2026-06-17T08:11:35.945Z,8,8.2956,1,2,1,0,0,2026-06-09T08:11:35.945Z!fsrs,2026-06-18T05:50:31.806Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:31.806Z-->
- permanent difference: definition ::@:: A difference between IFRS and tax reporting that will never reverse, so it affects only the current period and does not create deferred taxes. <!--SR:!fsrs,2026-06-17T03:37:12.340Z,8,8.2956,1,2,1,0,0,2026-06-09T03:37:12.340Z!fsrs,2026-06-18T05:58:32.077Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:32.077Z-->
- government bond interest: temporary or permanent difference? ::@:: Permanent difference, because it is recognized for IFRS but never taxed. <!--SR:!fsrs,2026-06-18T07:29:15.569Z,8,8.2956,1,2,1,0,0,2026-06-10T07:29:15.569Z!fsrs,2026-06-18T06:07:54.781Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:54.781Z-->
- fines and penalties: temporary or permanent difference? ::@:: Permanent difference, because they are expensed for IFRS but are not deductible for tax. <!--SR:!fsrs,2026-06-18T05:52:17.977Z,8,8.2956,1,2,1,0,0,2026-06-10T05:52:17.977Z!fsrs,2026-06-17T12:28:27.098Z,8,8.2956,1,2,1,0,0,2026-06-09T12:28:27.098Z-->

## deferred tax liabilities

A __deferred tax liability__ represents future taxes payable caused by existing __taxable temporary differences__.

---

Flashcards for this section are as follows:

- deferred tax liability: core idea ::@:: It records the future tax burden created when current temporary differences will make taxable income larger in later periods. <!--SR:!fsrs,2026-06-17T03:48:46.425Z,8,8.2956,1,2,1,0,0,2026-06-09T03:48:46.425Z!fsrs,2026-06-18T06:13:27.957Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:27.957Z-->
- deferred tax liability: usual book-basis direction ::@:: Book basis is greater than tax basis, so some amount recognized under IFRS today will still be taxed in the future. <!--SR:!fsrs,2026-06-18T06:12:53.875Z,8,8.2956,1,2,1,0,0,2026-06-10T06:12:53.875Z!fsrs,2026-06-18T06:08:18.308Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:18.308Z-->

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
> _Explanation._ The current payable is based on the year's taxable income, but the receivable difference means Chelsea will pay more tax later when those receivables are collected. That future tax effect is recognized now as a deferred tax liability. <!--SR:!fsrs,2026-06-17T08:32:20.076Z,8,8.2956,1,2,1,0,0,2026-06-09T08:32:20.076Z!fsrs,2026-06-18T05:54:58.738Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:58.738Z!fsrs,2026-06-18T05:58:09.851Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:09.851Z!fsrs,2026-06-18T05:50:58.993Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:58.993Z!fsrs,2026-06-17T14:31:46.138Z,8,8.2956,1,2,1,0,0,2026-06-09T14:31:46.138Z!fsrs,2026-06-17T03:42:14.602Z,8,8.2956,1,2,1,0,0,2026-06-09T03:42:14.602Z!fsrs,2026-06-18T06:04:19.527Z,8,8.2956,1,2,1,0,0,2026-06-10T06:04:19.527Z!fsrs,2026-06-17T12:51:04.444Z,8,8.2956,1,2,1,0,0,2026-06-09T12:51:04.444Z!fsrs,2026-06-17T13:15:35.019Z,8,8.2956,1,2,1,0,0,2026-06-09T13:15:35.019Z!fsrs,2026-06-18T05:49:34.940Z,8,8.2956,1,2,1,0,0,2026-06-10T05:49:34.940Z-->

<!-- markdownlint-disable-next-line MD028 -->
> _Reversal year for the Chelsea deferred tax liability._ In the next year, the remaining temporary difference has fallen, so the deferred tax liability must be reduced from its prior level. Assume current tax payable for 2026 is {@{&#36;36&nbsp;000}@}, while income tax expense remains {@{&#36;28&nbsp;000}@}.
>
> | {@{Record 2026 income taxes as the deferred tax liability reverses}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{28&nbsp;000}@} | |
> | {@{Deferred tax liability}@} | {@{8&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{36&nbsp;000}@} |
>
> _Explanation._ The debit to {@{Deferred tax liability}@} shows that part of the future tax burden recognized in 2025 is now being {@{used up as the receivables are collected and taxed}@}. <!--SR:!fsrs,2026-06-14T08:01:54.715Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:01:54.715Z!fsrs,2026-06-18T06:09:14.290Z,8,8.2956,1,2,1,0,0,2026-06-10T06:09:14.290Z!fsrs,2026-06-18T07:26:40.241Z,8,8.2956,1,2,1,0,0,2026-06-10T07:26:40.241Z!fsrs,2026-06-17T03:37:13.177Z,8,8.2956,1,2,1,0,0,2026-06-09T03:37:13.177Z!fsrs,2026-06-17T07:25:06.999Z,8,8.2956,1,2,1,0,0,2026-06-09T07:25:06.999Z!fsrs,2026-06-18T05:51:11.463Z,8,8.2956,1,2,1,0,0,2026-06-10T05:51:11.463Z!fsrs,2026-06-18T06:12:47.191Z,8,8.2956,1,2,1,0,0,2026-06-10T06:12:47.191Z!fsrs,2026-06-17T13:49:59.866Z,8,8.2956,1,2,1,0,0,2026-06-09T13:49:59.866Z!fsrs,2026-06-18T05:50:40.156Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:40.156Z-->

<!-- markdownlint-disable-next-line MD028 -->
> _Final reversal of the Chelsea deferred tax liability._ By the last reversal year, assume current tax payable is {@{&#36;32&nbsp;000}@} while income tax expense is still {@{&#36;28&nbsp;000}@}.
>
> | {@{Record final reversal of deferred tax liability}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{28&nbsp;000}@} | |
> | {@{Deferred tax liability}@} | {@{4&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{32&nbsp;000}@} |
>
> _Explanation._ The temporary difference is now {@{fully reversed, so the deferred tax liability falls to zero}@}. <!--SR:!fsrs,2026-06-17T05:01:59.765Z,8,8.2956,1,2,1,0,0,2026-06-09T05:01:59.765Z!fsrs,2026-06-18T05:55:03.029Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:03.029Z!fsrs,2026-06-18T06:08:16.179Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:16.179Z!fsrs,2026-06-18T02:09:50.677Z,8,8.2956,1,2,1,0,0,2026-06-10T02:09:50.677Z!fsrs,2026-06-17T12:20:29.091Z,8,8.2956,1,2,1,0,0,2026-06-09T12:20:29.091Z!fsrs,2026-06-18T06:12:49.408Z,8,8.2956,1,2,1,0,0,2026-06-10T06:12:49.408Z!fsrs,2026-06-18T06:41:25.925Z,8,8.2956,1,2,1,0,0,2026-06-10T06:41:25.925Z!fsrs,2026-06-18T05:53:59.783Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:59.783Z-->

<!-- markdownlint-disable-next-line MD028 -->
> _Tax-rate change during the reversal sequence._ Suppose that after the 2026 reporting date but before the 2026 statements are issued, a new law is __enacted__ reducing the future tax rate from {@{40% to 35%, so the remaining 10&nbsp;000 temporary difference should produce a deferred tax liability of 3&nbsp;500 rather than 4&nbsp;000}@}.
>
> | {@{Remeasure the remaining Chelsea deferred tax liability for the enacted lower future tax rate}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax liability}@} | {@{500}@} | |
> | {@{Income tax expense}@} | | {@{500}@} |
>
> _Explanation._ The liability falls because the same remaining future taxable amount of {@{10&nbsp;000}@} will now be taxed at only {@{35% rather than 40%}@}. The adjustment is recorded {@{immediately in the period when the tax-rate change becomes enacted}@}. <!--SR:!fsrs,2026-06-18T06:08:35.320Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:35.320Z!fsrs,2026-06-18T05:54:28.288Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:28.288Z!fsrs,2026-06-18T06:08:45.249Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:45.249Z!fsrs,2026-06-18T05:50:51.071Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:51.071Z!fsrs,2026-06-18T07:27:58.184Z,8,8.2956,1,2,1,0,0,2026-06-10T07:27:58.184Z!fsrs,2026-06-17T08:32:29.293Z,8,8.2956,1,2,1,0,0,2026-06-09T08:32:29.293Z!fsrs,2026-06-18T08:00:56.590Z,8,8.2956,1,2,1,0,0,2026-06-10T08:00:56.590Z!fsrs,2026-06-18T05:55:39.992Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:39.992Z-->

As the receivables are later collected and taxed, the difference reverses and the deferred tax liability falls.

- End of 2025: temporary difference 30 000 -> DTL 12 000.
- End of 2026: remaining difference 10 000 -> DTL 4 000.
- End of 2027: difference 0 -> DTL 0.

The key pattern is that the deferred tax liability is always measured from the __remaining__ temporary difference at the reporting date, not from the original difference forever.

---

Flashcards for this section are as follows:

- Chelsea receivable sequence: what is the underlying temporary difference? ::@:: Accounts receivable revenue has already been recognized for IFRS, but the receivable still has zero tax basis because taxation waits until cash collection. <!--SR:!fsrs,2026-06-17T08:32:25.771Z,8,8.2956,1,2,1,0,0,2026-06-09T08:32:25.771Z!fsrs,2026-06-18T06:09:17.202Z,8,8.2956,1,2,1,0,0,2026-06-10T06:09:17.202Z-->
- Chelsea sequence: why does the deferred tax liability shrink over time? ::@:: Because the receivable difference reverses as cash is collected and taxed, leaving a smaller remaining future taxable amount at each reporting date. <!--SR:!fsrs,2026-06-17T03:40:54.732Z,8,8.2956,1,2,1,0,0,2026-06-09T03:40:54.732Z!fsrs,2026-06-18T07:59:52.424Z,8,8.2956,1,2,1,0,0,2026-06-10T07:59:52.424Z-->
- deferred tax liability: definition ::@:: The increase in taxes payable in future years caused by taxable temporary differences existing at the end of the current year. <!--SR:!fsrs,2026-06-17T15:57:15.810Z,8,8.2956,1,2,1,0,0,2026-06-09T15:57:15.810Z!fsrs,2026-06-18T05:50:22.639Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:22.639Z-->
- taxable temporary difference: usual direction of book basis versus tax basis ::@:: Book basis is greater than tax basis, so future taxable amounts will arise. <!--SR:!fsrs,2026-06-18T08:00:58.741Z,8,8.2956,1,2,1,0,0,2026-06-10T08:00:58.741Z!fsrs,2026-06-18T07:30:31.279Z,8,8.2956,1,2,1,0,0,2026-06-10T07:30:31.279Z-->
- Chelsea receivable example: why does a deferred tax liability arise? ::@:: Because the receivable is already recognized for IFRS but has not yet been taxed, so future cash collection will trigger future taxable income. <!--SR:!fsrs,2026-06-18T06:13:50.517Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:50.517Z!fsrs,2026-06-17T09:00:51.463Z,8,8.2956,1,2,1,0,0,2026-06-09T09:00:51.463Z-->
- deferred tax liability measurement: what base is used each year? ::@:: The remaining temporary difference at the reporting date multiplied by the applicable tax rate. <!--SR:!fsrs,2026-06-18T06:13:21.433Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:21.433Z!fsrs,2026-06-18T07:26:59.216Z,8,8.2956,1,2,1,0,0,2026-06-10T07:26:59.216Z-->
- why can the deferred tax liability decrease even when current tax payable is high? ::@:: Because reversal of an old taxable temporary difference reduces the deferred tax balance even while current taxable income may still be large. <!--SR:!fsrs,2026-06-17T08:15:16.337Z,8,8.2956,1,2,1,0,0,2026-06-09T08:15:16.337Z!fsrs,2026-06-18T07:28:16.641Z,8,8.2956,1,2,1,0,0,2026-06-10T07:28:16.641Z-->
- Chelsea deferred tax liability with an enacted future tax-rate cut: what happens? ::@:: Remeasure the remaining deferred tax liability using the new enacted future rate, debit the _Deferred tax liability_ for the reduction, and credit _Income tax expense_ because the future tax burden has fallen. <!--SR:!fsrs,2026-06-18T05:58:00.202Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:00.202Z!fsrs,2026-06-18T05:58:34.854Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:34.854Z-->
- Chelsea 2025: AR &#36;30&nbsp;000 (zero tax basis), 40% rate → year-end DTL = ? ::@:: &#36;30&nbsp;000 × 40% = &#36;12&nbsp;000; income tax expense = payable &#36;16&nbsp;000 + DTL &#36;12&nbsp;000 = &#36;28&nbsp;000. <!--SR:!fsrs,2026-06-18T05:52:52.683Z,8,8.2956,1,2,1,0,0,2026-06-10T05:52:52.683Z!fsrs,2026-06-12T08:01:59.991Z,2,2.29815136,3.4641143,2,2,0,0,2026-06-10T08:01:59.991Z-->

## deferred tax assets and non-recognition

A __deferred tax asset__ represents future tax savings caused by existing __deductible temporary differences__.

---

Flashcards for this section are as follows:

- deferred tax asset: core idea ::@:: It records a future tax saving created when IFRS recognizes an expense or liability now but tax law delays the deduction until later. <!--SR:!fsrs,2026-06-18T05:58:01.955Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:01.955Z!fsrs,2026-06-17T03:43:24.940Z,8,8.2956,1,2,1,0,0,2026-06-09T03:43:24.940Z-->
- deferred tax asset: why is it a future tax benefit? ::@:: Because the temporary difference will reduce taxes payable in a later period once the deduction becomes available on the tax return. <!--SR:!fsrs,2026-06-14T08:06:12.665Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:06:12.665Z!fsrs,2026-06-18T06:07:15.587Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:15.587Z-->

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
> _Explanation._ The company has already recognized the warranty expense for IFRS, but tax law will only allow the deduction when cash is paid later. That future deduction creates a deferred tax asset of {@{200&nbsp;000}@}. <!--SR:!fsrs,2026-06-17T15:53:22.793Z,8,8.2956,1,2,1,0,0,2026-06-09T15:53:22.793Z!fsrs,2026-06-18T05:53:50.864Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:50.864Z!fsrs,2026-06-18T06:09:12.517Z,8,8.2956,1,2,1,0,0,2026-06-10T06:09:12.517Z!fsrs,2026-06-18T05:58:04.095Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:04.095Z!fsrs,2026-06-18T05:55:07.873Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:07.873Z!fsrs,2026-06-18T06:08:40.094Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:40.094Z!fsrs,2026-06-18T05:50:38.679Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:38.679Z!fsrs,2026-06-17T04:25:35.565Z,8,8.2956,1,2,1,0,0,2026-06-09T04:25:35.565Z!fsrs,2026-06-18T08:01:04.812Z,8,8.2956,1,2,1,0,0,2026-06-10T08:01:04.812Z!fsrs,2026-06-14T08:05:34.427Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:05:34.427Z!fsrs,2026-06-17T13:16:12.300Z,8,8.2956,1,2,1,0,0,2026-06-09T13:16:12.300Z!fsrs,2026-06-17T03:48:47.924Z,8,8.2956,1,2,1,0,0,2026-06-09T03:48:47.924Z!fsrs,2026-06-18T05:53:19.829Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:19.829Z!fsrs,2026-06-17T04:58:46.492Z,8,8.2956,1,2,1,0,0,2026-06-09T04:58:46.492Z!fsrs,2026-06-17T12:10:21.019Z,8,8.2956,1,2,1,0,0,2026-06-09T12:10:21.019Z-->

A litigation accrual works the same way: if IFRS records the expense now but tax only deducts it when paid, the company has a deductible temporary difference and therefore a deferred tax asset.

---

Flashcards for this section are as follows:

- deductible temporary difference: usual story line ::@:: IFRS recognizes the expense earlier than tax does, so the company has a future deduction still waiting to be used. <!--SR:!fsrs,2026-06-18T05:49:16.609Z,8,8.2956,1,2,1,0,0,2026-06-10T05:49:16.609Z!fsrs,2026-06-17T04:58:45.046Z,8,8.2956,1,2,1,0,0,2026-06-09T04:58:45.046Z-->
- warranty accrual: why does it create a deferred tax asset? ::@:: Because the warranty expense is already recognized under IFRS, but tax law waits until warranty claims are actually paid before allowing the deduction. <!--SR:!2026-05-21,4,277!2000-01-01,1,250-->
- Cunningham: &#36;500&nbsp;000 warranty accrual, 40% rate → DTA = ? ::@:: &#36;500&nbsp;000 × 40% = &#36;200&nbsp;000; income tax expense = payable &#36;800&nbsp;000 − DTA &#36;200&nbsp;000 = &#36;600&nbsp;000. <!--SR:!fsrs,2026-06-14T08:05:36.464Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:05:36.464Z!fsrs,2026-06-18T06:08:31.866Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:31.866Z-->

### non-recognition and later reversal

__When not all of a deferred tax asset is recoverable.__

The course also teaches __non-recognition__ or reduction of deferred tax assets. A company must reduce the carrying amount of a deferred tax asset if it is __probable__ that some portion of the tax benefit will not be realized. IAS 12 uses the same __probable__ threshold for the initial recognition: a deferred tax asset is recognized only to the extent that it is probable that sufficient future taxable profit will be available against which the deductible temporary difference can be utilized. The slides define __probable__ as a level of likelihood of __at least slightly more than 50%__.

That means a deferred tax asset is not automatic forever. The company must ask whether future taxable income will be sufficient to use the benefit.

> _Partial non-recognition._ Jensen records an initial deferred tax asset of {@{€400&nbsp;000}@}, but later concludes that it is probable that {@{€100&nbsp;000}@} will not be realized.
>
> | {@{Reduce deferred tax asset for non-recognition}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{100&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | | {@{100&nbsp;000}@} | <!--SR:!fsrs,2026-06-18T02:49:48.950Z,8,8.2956,1,2,1,0,0,2026-06-10T02:49:48.950Z!fsrs,2026-06-18T05:55:06.184Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:06.184Z!fsrs,2026-06-17T07:10:18.031Z,8,8.2956,1,2,1,0,0,2026-06-09T07:10:18.031Z!fsrs,2026-06-18T06:07:13.901Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:13.901Z!fsrs,2026-06-18T05:53:05.957Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:05.957Z!fsrs,2026-06-17T12:54:47.221Z,8,8.2956,1,2,1,0,0,2026-06-09T12:54:47.221Z!fsrs,2026-06-17T08:11:26.448Z,8,8.2956,1,2,1,0,0,2026-06-09T08:11:26.448Z-->

<!-- markdownlint-disable-next-line MD028 -->
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
> _Explanation._ Students often jump straight to the write-down entry and forget the sequence. The cleaner exam logic is: {@{recognize the full tax effect of the deductible temporary difference first}@}, then {@{write down the part that is not probable of realization}@}. <!--SR:!fsrs,2026-06-17T14:31:50.720Z,8,8.2956,1,2,1,0,0,2026-06-09T14:31:50.720Z!fsrs,2026-06-17T03:40:53.281Z,8,8.2956,1,2,1,0,0,2026-06-09T03:40:53.281Z!fsrs,2026-06-18T05:52:59.400Z,8,8.2956,1,2,1,0,0,2026-06-10T05:52:59.400Z!fsrs,2026-06-18T06:12:53.127Z,8,8.2956,1,2,1,0,0,2026-06-10T06:12:53.127Z!fsrs,2026-06-17T03:48:41.070Z,8,8.2956,1,2,1,0,0,2026-06-09T03:48:41.070Z!fsrs,2026-06-18T05:53:33.442Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:33.442Z!fsrs,2026-06-18T05:50:37.725Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:37.725Z!fsrs,2026-06-18T05:53:18.365Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:18.365Z!fsrs,2026-06-18T05:53:48.965Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:48.965Z!fsrs,2026-06-18T05:54:39.893Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:39.893Z!fsrs,2026-06-17T12:43:57.309Z,8,8.2956,1,2,1,0,0,2026-06-09T12:43:57.309Z!fsrs,2026-06-17T15:53:21.510Z,8,8.2956,1,2,1,0,0,2026-06-09T15:53:21.510Z-->

If expectations later improve, part of that earlier reduction can be reversed.

<!-- markdownlint-disable-next-line MD028 -->
> _Partial reversal of earlier non-recognition._ Suppose the deferred tax asset had been reduced from {@{€400&nbsp;000 to €300&nbsp;000}@}, but improved evidence now suggests that {@{€350&nbsp;000 is recoverable}@}.
>
> | {@{Increase deferred tax asset after expectations improve}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax asset}@} | {@{50&nbsp;000}@} | |
> | {@{Income tax expense}@} | | {@{50&nbsp;000}@} |
>
> _Explanation._ Reversing part of the earlier non-recognition {@{reduces current-period income tax expense}@} because more of the future tax benefit is now expected to be realized. <!--SR:!fsrs,2026-06-18T05:53:06.697Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:06.697Z!fsrs,2026-06-18T07:30:33.626Z,8,8.2956,1,2,1,0,0,2026-06-10T07:30:33.626Z!fsrs,2026-06-18T07:46:42.001Z,8,8.2956,1,2,1,0,0,2026-06-10T07:46:42.001Z!fsrs,2026-06-18T07:27:55.020Z,8,8.2956,1,2,1,0,0,2026-06-10T07:27:55.020Z!fsrs,2026-06-17T04:59:06.379Z,8,8.2956,1,2,1,0,0,2026-06-09T04:59:06.379Z!fsrs,2026-06-18T06:45:51.320Z,8,8.2956,1,2,1,0,0,2026-06-10T06:45:51.320Z-->

<!-- markdownlint-disable-next-line MD028 -->
> _Reversal of a litigation-related deferred tax asset when the deduction is finally realized._ Assume a company had recognized a {@{€20&nbsp;000 deferred tax asset}@} from a litigation accrual in the prior year. In the settlement year, current tax payable is {@{€180&nbsp;000}@} while income tax expense is {@{€200&nbsp;000}@}.
>
> | {@{Record income taxes when a litigation-related deferred tax asset reverses}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{200&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | | {@{20&nbsp;000}@} |
> | {@{Income taxes payable}@} | | {@{180&nbsp;000}@} |
>
> _Explanation._ The deferred tax asset disappears because the tax deduction has now {@{actually been used on the tax return}@}. <!--SR:!fsrs,2026-06-18T06:14:05.854Z,8,8.2956,1,2,1,0,0,2026-06-10T06:14:05.854Z!fsrs,2026-06-18T05:29:59.046Z,8,8.2956,1,2,1,0,0,2026-06-10T05:29:59.046Z!fsrs,2026-06-18T05:54:57.272Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:57.272Z!fsrs,2026-06-17T08:11:27.775Z,8,8.2956,1,2,1,0,0,2026-06-09T08:11:27.775Z!fsrs,2026-06-18T07:26:37.958Z,8,8.2956,1,2,1,0,0,2026-06-10T07:26:37.958Z!fsrs,2026-06-18T03:45:57.549Z,8,8.2956,1,2,1,0,0,2026-06-10T03:45:57.549Z!fsrs,2026-06-18T06:13:36.931Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:36.931Z!fsrs,2026-06-17T14:31:45.116Z,8,8.2956,1,2,1,0,0,2026-06-09T14:31:45.116Z-->

---

Flashcards for this section are as follows:

- deferred tax asset non-recognition: what question is management testing? ::@:: Whether enough future taxable income is probable so that the company can actually realize the deferred tax benefit. <!--SR:!fsrs,2026-06-18T05:49:36.423Z,8,8.2956,1,2,1,0,0,2026-06-10T05:49:36.423Z!fsrs,2026-06-18T05:55:25.792Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:25.792Z-->
- deferred tax asset write-down and reversal: what is the direction of the income-tax effect? ::@:: Writing the asset down increases income tax expense, while restoring a realizable portion later reduces income tax expense. <!--SR:!fsrs,2026-06-17T03:48:44.304Z,8,8.2956,1,2,1,0,0,2026-06-09T03:48:44.304Z!fsrs,2026-06-18T05:49:29.170Z,8,8.2956,1,2,1,0,0,2026-06-10T05:49:29.170Z-->
- deferred tax asset non-recognition: when is a reduction required? ::@:: When it is probable that some portion or all of the deferred tax asset will not be realized through future taxable income. <!--SR:!fsrs,2026-06-17T12:59:28.974Z,8,8.2956,1,2,1,0,0,2026-06-09T12:59:28.974Z!fsrs,2026-06-17T14:31:51.613Z,8,8.2956,1,2,1,0,0,2026-06-09T14:31:51.613Z-->
- deferred tax asset reduction: income-statement effect ::@:: Reducing the deferred tax asset increases current income tax expense. <!--SR:!fsrs,2026-06-17T04:27:53.911Z,8,8.2956,1,2,1,0,0,2026-06-09T04:27:53.911Z!fsrs,2026-06-18T05:50:25.381Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:25.381Z-->
- improved evidence after DTA non-recognition: what entry is made? ::@:: Debit _Deferred tax asset_ and credit _Income tax expense_ for the amount now expected to be realizable. <!--SR:!fsrs,2026-06-17T04:26:53.770Z,8,8.2956,1,2,1,0,0,2026-06-09T04:26:53.770Z!fsrs,2026-06-18T06:08:47.664Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:47.664Z-->
- litigation-related deferred tax asset: what happens in the settlement year? ::@:: Credit the _Deferred tax asset_ and compare _Income tax expense_ with _Income taxes payable_ as the previously deferred tax benefit is realized. <!--SR:!fsrs,2026-06-18T05:53:24.130Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:24.130Z!fsrs,2026-06-18T05:29:52.840Z,8,8.2956,1,2,1,0,0,2026-06-10T05:29:52.840Z-->
- deferred tax asset non-recognition: what is the sequence students often miss? ::@:: First recognize the full deferred tax asset created by the deductible temporary difference, then record a separate write-down for any portion that is not probable of realization. <!--SR:!fsrs,2026-06-18T06:08:52.574Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:52.574Z!fsrs,2026-06-18T03:55:42.021Z,8,8.2956,1,2,1,0,0,2026-06-10T03:55:42.021Z-->

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
> _Explanation._ The {@{fine is a permanent difference}@}, so it changes only current taxable income. The {@{warranty accrual is a deductible temporary difference}@}, so it creates a deferred tax asset. Total income tax expense is {@{€351&nbsp;000 − €36&nbsp;000 = €315&nbsp;000}@}. <!--SR:!fsrs,2026-06-18T05:52:11.810Z,8,8.2956,1,2,1,0,0,2026-06-10T05:52:11.810Z!fsrs,2026-06-17T09:00:48.652Z,8,8.2956,1,2,1,0,0,2026-06-09T09:00:48.652Z!fsrs,2026-06-17T13:50:02.768Z,8,8.2956,1,2,1,0,0,2026-06-09T13:50:02.768Z!fsrs,2026-06-18T06:08:22.037Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:22.037Z!fsrs,2026-06-17T12:05:54.204Z,8,8.2956,1,2,1,0,0,2026-06-09T12:05:54.204Z!fsrs,2026-06-18T03:05:00.445Z,8,8.2956,1,2,1,0,0,2026-06-10T03:05:00.445Z!fsrs,2026-06-17T13:16:11.102Z,8,8.2956,1,2,1,0,0,2026-06-09T13:16:11.102Z!fsrs,2026-06-18T05:52:53.924Z,8,8.2956,1,2,1,0,0,2026-06-10T05:52:53.924Z!fsrs,2026-06-18T05:54:49.897Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:49.897Z!fsrs,2026-06-18T06:53:17.881Z,8,8.2956,1,2,1,0,0,2026-06-10T06:53:17.881Z!fsrs,2026-06-18T06:13:45.748Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:45.748Z!fsrs,2026-06-18T05:55:33.816Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:33.816Z!fsrs,2026-06-17T14:17:32.344Z,8,8.2956,1,2,1,0,0,2026-06-09T14:17:32.344Z!fsrs,2026-06-18T05:53:02.704Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:02.704Z!fsrs,2026-06-18T05:58:02.644Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:02.644Z!fsrs,2026-06-18T05:54:01.217Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:01.217Z!fsrs,2026-06-18T05:53:58.734Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:58.734Z-->

---

Flashcards for this section are as follows:

- mixed deferred-tax question: first step ::@:: Start with pretax financial income under IFRS before separating permanent and temporary differences. <!--SR:!fsrs,2026-06-18T06:53:16.441Z,8,8.2956,1,2,1,0,0,2026-06-10T06:53:16.441Z!fsrs,2026-06-17T12:09:31.621Z,8,8.2956,1,2,1,0,0,2026-06-09T12:09:31.621Z-->
- permanent difference in a mixed tax question: what does it change? ::@:: It changes current taxable income but does not create a deferred tax asset or deferred tax liability. <!--SR:!fsrs,2026-06-18T05:50:43.977Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:43.977Z!fsrs,2026-06-17T08:32:28.018Z,8,8.2956,1,2,1,0,0,2026-06-09T08:32:28.018Z-->
- temporary difference in a mixed tax question: what extra step is needed? ::@:: Determine whether it creates future taxable amounts or future deductible amounts and then measure the related deferred tax balance. <!--SR:!fsrs,2026-06-18T05:50:27.595Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:27.595Z!fsrs,2026-06-18T05:55:35.899Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:35.899Z-->
- why can a fine and a warranty accrual not be treated the same way in a mixed deferred-tax problem? ::@:: Both may affect current taxable income, but a fine never reverses whereas a warranty accrual creates a future deduction and therefore a deferred tax asset. <!--SR:!fsrs,2026-06-17T15:33:48.220Z,8,8.2956,1,2,1,0,0,2026-06-09T15:33:48.220Z!fsrs,2026-06-17T05:06:03.401Z,8,8.2956,1,2,1,0,0,2026-06-09T05:06:03.401Z-->
- mixed tax example: why is the fine not part of the deferred-tax entry? ::@:: Because the fine is a permanent difference, so it changes taxable income now but never creates a future reversing amount. <!--SR:!fsrs,2026-06-17T04:26:31.216Z,8,8.2956,1,2,1,0,0,2026-06-09T04:26:31.216Z!fsrs,2026-06-18T06:04:21.884Z,8,8.2956,1,2,1,0,0,2026-06-10T06:04:21.884Z-->
- mixed tax example: why does the warranty accrual create a deferred tax asset? ::@:: Because IFRS recognizes the expense now but tax law allows the deduction only when the warranty cash outflow is paid later. <!--SR:!fsrs,2026-06-14T08:02:01.370Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:02:01.370Z!fsrs,2026-06-18T06:07:32.220Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:32.220Z-->
- Patel: pretax €1&nbsp;000&nbsp;000, fine €50&nbsp;000 (perm), warranty €120&nbsp;000 (temp), 30% rate → income tax expense = ? ::@:: Taxable income = €1&nbsp;170&nbsp;000; current tax = €351&nbsp;000; DTA = €36&nbsp;000; expense = €351&nbsp;000 − €36&nbsp;000 = €315&nbsp;000. <!--SR:!fsrs,2026-06-22T08:01:58.324Z,12,11.6874828,1,2,2,0,0,2026-06-10T08:01:58.324Z!fsrs,2026-06-18T05:51:08.877Z,8,8.2956,1,2,1,0,0,2026-06-10T05:51:08.877Z-->

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
> _Explanation._ The {@{government bond interest is permanent}@}, so it never enters deferred tax. The {@{warranty accrual lowers future taxes}@}, so it creates a deferred tax asset, while the {@{installment-sale difference increases future taxes}@}, so it creates a deferred tax liability. <!--SR:!fsrs,2026-06-17T03:43:28.943Z,8,8.2956,1,2,1,0,0,2026-06-09T03:43:28.943Z!fsrs,2026-06-18T06:09:15.245Z,8,8.2956,1,2,1,0,0,2026-06-10T06:09:15.245Z!fsrs,2026-06-18T05:49:58.637Z,8,8.2956,1,2,1,0,0,2026-06-10T05:49:58.637Z!fsrs,2026-06-14T08:06:08.796Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:06:08.796Z!fsrs,2026-06-18T05:58:06.807Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:06.807Z!fsrs,2026-06-18T05:53:21.380Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:21.380Z!fsrs,2026-06-17T14:31:49.736Z,8,8.2956,1,2,1,0,0,2026-06-09T14:31:49.736Z!fsrs,2026-06-18T05:53:00.377Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:00.377Z!fsrs,2026-06-17T12:09:28.617Z,8,8.2956,1,2,1,0,0,2026-06-09T12:09:28.617Z!fsrs,2026-06-18T05:50:45.357Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:45.357Z!fsrs,2026-06-18T05:50:34.612Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:34.612Z!fsrs,2026-06-18T05:50:24.293Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:24.293Z!fsrs,2026-06-18T07:27:00.660Z,8,8.2956,1,2,1,0,0,2026-06-10T07:27:00.660Z!fsrs,2026-06-17T13:43:38.571Z,8,8.2956,1,2,1,0,0,2026-06-09T13:43:38.571Z!fsrs,2026-06-17T03:40:41.811Z,8,8.2956,1,2,1,0,0,2026-06-09T03:40:41.811Z!fsrs,2026-06-18T05:53:09.034Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:09.034Z!fsrs,2026-06-18T05:52:15.298Z,8,8.2956,1,2,1,0,0,2026-06-10T05:52:15.298Z!fsrs,2026-06-18T05:52:57.894Z,8,8.2956,1,2,1,0,0,2026-06-10T05:52:57.894Z!fsrs,2026-06-17T05:10:16.882Z,8,8.2956,1,2,1,0,0,2026-06-09T05:10:16.882Z!fsrs,2026-06-18T07:29:10.280Z,8,8.2956,1,2,1,0,0,2026-06-10T07:29:10.280Z!fsrs,2026-06-18T05:29:55.574Z,8,8.2956,1,2,1,0,0,2026-06-10T05:29:55.574Z!fsrs,2026-06-18T06:53:33.563Z,8,8.2956,1,2,1,0,0,2026-06-10T06:53:33.563Z-->

---

Flashcards for this section are as follows:

- income tax expense: working formula in this course ::@:: Income tax expense equals current tax payable plus deferred tax expense or minus a deferred tax benefit. <!--SR:!fsrs,2026-06-17T12:43:55.864Z,8,8.2956,1,2,1,0,0,2026-06-09T12:43:55.864Z!fsrs,2026-06-18T06:07:16.986Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:16.986Z-->
- why can current tax payable exceed income tax expense? ::@:: Because a reversing deferred tax asset or liability may reduce the period's total tax expense relative to the current cash tax obligation. <!--SR:!fsrs,2026-06-18T05:58:25.012Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:25.012Z!fsrs,2026-06-18T06:07:14.851Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:14.851Z-->
- why can current tax payable be lower than income tax expense? ::@:: Because new taxable temporary differences can create deferred tax liabilities that add to current tax payable to produce total tax expense. <!--SR:!fsrs,2026-06-17T13:35:07.602Z,8,8.2956,1,2,1,0,0,2026-06-09T13:35:07.602Z!fsrs,2026-06-12T08:02:13.284Z,2,2.29815136,3.4641143,2,2,0,0,2026-06-10T08:02:13.284Z-->
- current plus deferred: why is this phrase so central? ::@:: Because this deferred-tax topic allocates the tax consequences of timing differences across periods instead of treating tax expense as the same thing as the current tax return. <!--SR:!fsrs,2026-06-17T04:59:18.087Z,8,8.2956,1,2,1,0,0,2026-06-09T04:59:18.087Z!fsrs,2026-06-18T05:57:57.894Z,8,8.2956,1,2,1,0,0,2026-06-10T05:57:57.894Z-->
- current-plus-deferred example: what creates the deferred tax liability? ::@:: The installment-sale profit recognized for IFRS now but taxed later, because it creates future taxable amounts. <!--SR:!fsrs,2026-06-18T05:29:53.788Z,8,8.2956,1,2,1,0,0,2026-06-10T05:29:53.788Z!fsrs,2026-06-18T05:58:55.142Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:55.142Z-->
- current-plus-deferred example: what creates the deferred tax asset? ::@:: The warranty accrual recognized now for IFRS but deductible only when paid later, because it creates future deductible amounts. <!--SR:!2000-01-01,1,250!2026-05-21,4,270-->
- Linton: pretax ¥800&nbsp;000, perm diff ¥20&nbsp;000, warranty ¥60&nbsp;000 (DTA), installment ¥100&nbsp;000 (DTL), 25% rate → income tax expense = ? ::@:: Taxable income = ¥740&nbsp;000; current tax = ¥185&nbsp;000; DTA = ¥15&nbsp;000; DTL = ¥25&nbsp;000; expense = ¥185&nbsp;000 + ¥25&nbsp;000 − ¥15&nbsp;000 = ¥195&nbsp;000. <!--SR:!fsrs,2026-06-17T03:45:43.550Z,8,8.2956,1,2,1,0,0,2026-06-09T03:45:43.550Z!fsrs,2026-06-10T08:11:24.400Z,0,1.33589976,5.10228691,1,2,0,1,2026-06-10T08:01:24.400Z-->

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
> _Explanation._ Lower future tax rates mean a smaller future tax burden, so the deferred tax liability falls and current-period income tax expense is reduced. <!--SR:!fsrs,2026-06-18T05:58:05.068Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:05.068Z!fsrs,2026-06-18T05:55:32.707Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:32.707Z!fsrs,2026-06-17T12:43:19.331Z,8,8.2956,1,2,1,0,0,2026-06-09T12:43:19.331Z!fsrs,2026-06-18T06:13:26.901Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:26.901Z!fsrs,2026-06-12T08:01:52.823Z,2,2.29815136,3.4641143,2,2,0,0,2026-06-10T08:01:52.823Z!fsrs,2026-06-18T06:08:34.672Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:34.672Z!fsrs,2026-06-18T07:59:54.742Z,8,8.2956,1,2,1,0,0,2026-06-10T07:59:54.742Z!fsrs,2026-06-18T07:46:45.346Z,8,8.2956,1,2,1,0,0,2026-06-10T07:46:45.346Z-->

<!-- markdownlint-disable-next-line MD028 -->
> _Tax-rate change affecting a deferred tax asset._ Assume instead that a company has a {@{deferred tax asset of €420&nbsp;000}@} measured using an enacted {@{35% future rate}@}. A new law increases the enacted future rate so the correct deferred tax asset should now be {@{€480&nbsp;000}@}.
>
> | {@{Increase deferred tax asset for enacted tax-rate change}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax asset}@} | {@{60&nbsp;000}@} | |
> | {@{Income tax expense}@} | | {@{60&nbsp;000}@} |
>
> _Explanation._ A higher enacted future tax rate makes future deductions {@{more valuable}@}, so the deferred tax asset increases and income tax expense falls. <!--SR:!fsrs,2026-06-17T12:10:21.800Z,8,8.2956,1,2,1,0,0,2026-06-09T12:10:21.800Z!fsrs,2026-06-17T14:19:24.085Z,8,8.2956,1,2,1,0,0,2026-06-09T14:19:24.085Z!fsrs,2026-06-17T08:15:17.393Z,8,8.2956,1,2,1,0,0,2026-06-09T08:15:17.393Z!fsrs,2026-06-18T06:13:53.000Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:53.000Z!fsrs,2026-06-18T04:18:10.619Z,8,8.2956,1,2,1,0,0,2026-06-10T04:18:10.619Z!fsrs,2026-06-18T05:50:48.958Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:48.958Z-->

---

Flashcards for this section are as follows:

- future tax rates: when may the company use a future tax rate instead of the current rate? ::@:: When the future tax-rate change has already been enacted. <!--SR:!fsrs,2026-06-18T05:58:07.922Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:07.922Z!fsrs,2026-06-17T04:26:32.358Z,8,8.2956,1,2,1,0,0,2026-06-09T04:26:32.358Z-->
- if a future tax rate has not yet been enacted, what rate is used? ::@:: The current rate. <!--SR:!fsrs,2026-06-18T07:59:49.739Z,8,8.2956,1,2,1,0,0,2026-06-10T07:59:49.739Z!fsrs,2026-06-18T06:13:47.033Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:47.033Z-->
- enacted tax-rate change: what happens to existing deferred tax balances? ::@:: They are remeasured immediately, and the effect goes to income tax expense in the period of the change. <!--SR:!fsrs,2026-06-17T03:37:09.193Z,8,8.2956,1,2,1,0,0,2026-06-09T03:37:09.193Z!fsrs,2026-06-18T06:08:22.846Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:22.846Z-->
- falling enacted future tax rates: what happens to a deferred tax liability? ::@:: It decreases because the future taxable amounts will now be taxed at a lower rate. <!--SR:!fsrs,2026-06-17T14:14:56.225Z,8,8.2956,1,2,1,0,0,2026-06-09T14:14:56.225Z!fsrs,2026-06-18T06:07:12.865Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:12.865Z-->
- falling enacted future tax rates: what happens to income tax expense when a deferred tax liability is revised downward? ::@:: Income tax expense decreases. <!--SR:!2026-05-20,3,257!2000-01-01,1,250-->
- enacted increase in future tax rates: what happens to a deferred tax asset? ::@:: It increases because future deductible amounts now save more tax, so income tax expense decreases. <!--SR:!fsrs,2026-06-18T05:53:52.799Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:52.799Z!fsrs,2026-06-18T05:29:58.287Z,8,8.2956,1,2,1,0,0,2026-06-10T05:29:58.287Z-->

## loss carryforwards and carrybacks

A __net operating loss__ means tax-deductible expenses exceed taxable revenues for the period. Tax law may let the company use that loss outside the current year.

---

Flashcards for this section are as follows:

- net operating loss: why does it matter beyond the current year? ::@:: Because tax law may let the company use that loss against taxable income from other years through a carryforward, a carryback, or both. <!--SR:!fsrs,2026-06-17T04:26:56.222Z,8,8.2956,1,2,1,0,0,2026-06-09T04:26:56.222Z!fsrs,2026-06-18T07:29:12.443Z,8,8.2956,1,2,1,0,0,2026-06-10T07:29:12.443Z-->
- carryforward versus carryback: high-level contrast ::@:: A carryforward creates a future benefit through a deferred tax asset, while a carryback creates an immediately realizable refund receivable from prior-year taxes. <!--SR:!fsrs,2026-06-17T04:26:36.563Z,8,8.2956,1,2,1,0,0,2026-06-09T04:26:36.563Z!fsrs,2026-06-18T06:09:11.170Z,8,8.2956,1,2,1,0,0,2026-06-10T06:09:11.170Z-->

### loss carryforward

Under a __loss carryforward__, the company uses the current loss to reduce taxable income in future years. The accounting idea is the same as other future tax benefits: if realization is probable, the company records a deferred tax asset in the loss year.

IAS 12 imposes __no fixed time limit__ on how long an unused tax loss may be carried forward. This contrasts with US GAAP, which historically restricted carryforwards to 20 years. Under IFRS, the deferred tax asset is recognized as long as it is probable that sufficient future taxable profit will be available, regardless of how many years the loss may remain legally available under local tax law.

> _Carryforward example._ Groh has a {@{&#36;200&nbsp;000 net operating loss}@} in 2025. The enacted future tax rate is {@{20%}@}. The future tax benefit is {@{&#36;40&nbsp;000}@}.
>
> | {@{Recognize loss carryforward benefit in the loss year}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Deferred tax asset}@} | {@{40&nbsp;000}@} | |
> | {@{Income tax expense (loss carryforward)}@} | | {@{40&nbsp;000}@} | <!--SR:!fsrs,2026-06-18T05:58:29.859Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:29.859Z!fsrs,2026-06-18T06:09:19.308Z,8,8.2956,1,2,1,0,0,2026-06-10T06:09:19.308Z!fsrs,2026-06-17T12:43:18.057Z,8,8.2956,1,2,1,0,0,2026-06-09T12:43:18.057Z!fsrs,2026-06-18T02:41:52.467Z,8,8.2956,1,2,1,0,0,2026-06-10T02:41:52.467Z!fsrs,2026-06-18T06:12:52.556Z,8,8.2956,1,2,1,0,0,2026-06-10T06:12:52.556Z!fsrs,2026-06-18T08:01:02.791Z,8,8.2956,1,2,1,0,0,2026-06-10T08:01:02.791Z!fsrs,2026-06-18T06:12:51.774Z,8,8.2956,1,2,1,0,0,2026-06-10T06:12:51.774Z!fsrs,2026-06-17T12:43:13.432Z,8,8.2956,1,2,1,0,0,2026-06-09T12:43:13.432Z-->

When the company later earns taxable income and uses the carryforward, the deferred tax asset is reversed instead of recognizing the benefit again from scratch.

<!-- markdownlint-disable-next-line MD028 -->
> _Realization of a previously recognized loss carryforward._ In the next year, assume taxable income before applying the carryforward is {@{&#36;250&nbsp;000}@}. The company uses the prior-year {@{&#36;200&nbsp;000 carryforward}@}, so current tax payable is only {@{&#36;10&nbsp;000}@} while income tax expense is {@{&#36;50&nbsp;000}@}.
>
> | {@{Record income taxes when a loss carryforward is realized}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{50&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | | {@{40&nbsp;000}@} |
> | {@{Income taxes payable}@} | | {@{10&nbsp;000}@} |
>
> _Explanation._ The deferred tax asset is {@{used up in the profitable year}@}; the tax benefit was recognized earlier, so only the reversal appears now. <!--SR:!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2026-05-21,4,270!2000-01-01,1,250-->

---

Flashcards for this section are as follows:

- loss carryforward: what is recognized in the loss year if realization is probable? ::@:: A deferred tax asset for the future tax saving expected to be used against later taxable income. <!--SR:!fsrs,2026-06-17T03:43:34.523Z,8,8.2956,1,2,1,0,0,2026-06-09T03:43:34.523Z!fsrs,2026-06-18T06:12:55.893Z,8,8.2956,1,2,1,0,0,2026-06-10T06:12:55.893Z-->
- loss carryforward: what happens in the later profitable year? ::@:: The deferred tax asset is reversed as the company actually uses the carryforward on its tax return. <!--SR:!fsrs,2026-06-18T06:09:18.135Z,8,8.2956,1,2,1,0,0,2026-06-10T06:09:18.135Z!fsrs,2026-06-17T08:11:34.686Z,8,8.2956,1,2,1,0,0,2026-06-09T08:11:34.686Z-->

### loss carryback

Some tax systems also allow a __loss carryback__. The company applies the loss to prior years, receives a refund of taxes already paid, and recognizes the refund receivable in the loss year because the benefit is currently realizable.

The course appendix example uses the following ordering rule:

- apply the loss first to the __earliest year within the carryback window__ before moving to the later year, following the local tax rule used in the example.

> _Carryback plus carryforward example._ Groh has a {@{&#36;500&nbsp;000 loss}@}. It carries the loss back far enough to recover {@{&#36;65&nbsp;000 of previously paid taxes}@} and still has an unused loss amount left to carry forward.
>
> | {@{Recognize tax benefit of loss carryback}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax refund receivable}@} | {@{65&nbsp;000}@} | |
> | {@{Income tax expense (loss carryback)}@} | | {@{65&nbsp;000}@} | <!--SR:!fsrs,2026-06-18T06:08:27.817Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:27.817Z!fsrs,2026-06-18T07:26:32.695Z,8,8.2956,1,2,1,0,0,2026-06-10T07:26:32.695Z!fsrs,2026-06-17T04:26:38.628Z,8,8.2956,1,2,1,0,0,2026-06-09T04:26:38.628Z!fsrs,2026-06-18T06:09:20.656Z,8,8.2956,1,2,1,0,0,2026-06-10T06:09:20.656Z!fsrs,2026-06-18T07:29:56.259Z,8,8.2956,1,2,1,0,0,2026-06-10T07:29:56.259Z!fsrs,2026-06-18T05:54:26.652Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:26.652Z!fsrs,2026-06-17T12:09:37.560Z,8,8.2956,1,2,1,0,0,2026-06-09T12:09:37.560Z-->

<!-- markdownlint-disable-next-line MD028 -->
> _Combined carryback and carryforward entry._ Suppose a single {@{&#36;500&nbsp;000 loss}@} generates both a {@{&#36;65&nbsp;000 refund from carryback}@} and a remaining {@{&#36;200&nbsp;000 carryforward}@} taxed at {@{25%}@}, creating a {@{&#36;50&nbsp;000 deferred tax asset}@}.
>
> | {@{Record both the loss carryback and the remaining carryforward benefit}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax refund receivable}@} | {@{65&nbsp;000}@} | |
> | {@{Deferred tax asset}@} | {@{50&nbsp;000}@} | |
> | {@{Income tax expense (loss carryback)}@} | | {@{65&nbsp;000}@} |
> | {@{Income tax expense (loss carryforward)}@} | | {@{50&nbsp;000}@} |
>
> _Explanation._ One loss year can create both an {@{immediately realizable refund asset}@} and a {@{future tax-benefit asset}@}. <!--SR:!fsrs,2026-06-18T06:07:52.992Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:52.992Z!fsrs,2026-06-17T13:37:00.745Z,8,8.2956,1,2,1,0,0,2026-06-09T13:37:00.745Z!fsrs,2026-06-17T03:38:35.380Z,8,8.2956,1,2,1,0,0,2026-06-09T03:38:35.380Z!fsrs,2026-06-18T07:29:03.408Z,8,8.2956,1,2,1,0,0,2026-06-10T07:29:03.408Z!fsrs,2026-06-17T13:43:39.470Z,8,8.2956,1,2,1,0,0,2026-06-09T13:43:39.470Z!fsrs,2026-06-18T06:13:20.341Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:20.341Z!fsrs,2026-06-18T07:29:11.329Z,8,8.2956,1,2,1,0,0,2026-06-10T07:29:11.329Z!fsrs,2026-06-18T06:08:19.649Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:19.649Z!fsrs,2026-06-18T05:54:20.356Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:20.356Z!fsrs,2026-06-18T07:29:13.950Z,8,8.2956,1,2,1,0,0,2026-06-10T07:29:13.950Z!fsrs,2026-06-18T07:28:56.159Z,8,8.2956,1,2,1,0,0,2026-06-10T07:28:56.159Z-->

<!-- markdownlint-disable-next-line MD028 -->
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
> _Explanation._ The first entry is a {@{catch-up recognition of the deferred tax asset}@}; the second entry is the normal profitable-year reversal of that same asset. <!--SR:!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2026-05-21,4,270!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250!2000-01-01,1,250-->

If part of the loss is still available for future years and realization is probable, the company also records a deferred tax asset for the carryforward portion.

If realization is __not__ probable, the deferred tax asset is not recognized until the benefit becomes sufficiently realizable.

---

Flashcards for this section are as follows:

- loss carryback: why is a receivable recognized immediately? ::@:: Because the benefit is already realizable against taxes paid in prior years rather than being only a future possibility. <!--SR:!fsrs,2026-06-18T07:26:39.242Z,8,8.2956,1,2,1,0,0,2026-06-10T07:26:39.242Z!fsrs,2026-06-18T06:07:29.512Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:29.512Z-->
- carryback plus carryforward: can one loss year create both? ::@:: Yes. One part of the loss can recover prior taxes immediately, and the rest can still create a deferred tax asset for future years. <!--SR:!fsrs,2026-06-18T05:53:32.088Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:32.088Z!fsrs,2026-06-18T05:55:04.717Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:04.717Z-->
- net operating loss: definition ::@:: Tax-deductible expenses exceed taxable revenues. <!--SR:!fsrs,2026-06-18T06:07:19.557Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:19.557Z!fsrs,2026-06-12T08:05:46.582Z,2,2.3065,2.11121424,2,2,0,0,2026-06-10T08:05:46.582Z-->
- loss carryforward: accounting effect in the loss year ::@:: Recognize a deferred tax asset for the future tax benefit if realization is probable. <!--SR:!fsrs,2026-06-18T05:50:56.795Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:56.795Z!fsrs,2026-06-18T05:52:14.215Z,8,8.2956,1,2,1,0,0,2026-06-10T05:52:14.215Z-->
- loss carryforward: why is the credit shown as an income-tax item instead of ordinary revenue? ::@:: Because it is a tax benefit, not an operating revenue item. <!--SR:!fsrs,2026-06-18T05:08:51.365Z,8,8.2956,1,2,1,0,0,2026-06-10T05:08:51.365Z!fsrs,2026-06-18T08:00:03.157Z,8,8.2956,1,2,1,0,0,2026-06-10T08:00:03.157Z-->
- loss carryback: accounting effect in the loss year ::@:: Recognize an income tax refund receivable and the related tax benefit because the refund is currently realizable. <!--SR:!fsrs,2026-06-17T14:14:54.074Z,8,8.2956,1,2,1,0,0,2026-06-09T14:14:54.074Z!fsrs,2026-06-14T08:01:26.568Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:01:26.568Z-->
- carryback plus carryforward: can both appear from one loss year? ::@:: Yes; part of the loss may generate a refund from prior years and the remainder may generate a deferred tax asset for future years. <!--SR:!fsrs,2026-06-18T05:55:38.612Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:38.612Z!fsrs,2026-06-18T02:09:53.913Z,8,8.2956,1,2,1,0,0,2026-06-10T02:09:53.913Z-->
- uncertain realization of a loss carryforward: what happens? ::@:: Do not recognize the deferred tax asset until it is probable that the future tax benefit will be realized. <!--SR:!fsrs,2026-06-17T15:52:26.737Z,8,8.2956,1,2,1,0,0,2026-06-09T15:52:26.737Z!fsrs,2026-06-18T06:53:15.412Z,8,8.2956,1,2,1,0,0,2026-06-10T06:53:15.412Z-->
- loss carryforward realized in a profitable year: what happens to the deferred tax asset? ::@:: It is credited and reduced to the extent the carryforward is used on the tax return. <!--SR:!fsrs,2026-06-18T06:07:24.270Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:24.270Z!fsrs,2026-06-18T06:09:16.206Z,8,8.2956,1,2,1,0,0,2026-06-10T06:09:16.206Z-->
- carryback ordering rule in this course: which prior year is used first? ::@:: Apply the loss first to the earliest year within the permitted carryback window before moving to later years. <!--SR:!fsrs,2026-06-18T05:50:48.108Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:48.108Z!fsrs,2026-06-17T03:48:42.466Z,8,8.2956,1,2,1,0,0,2026-06-09T03:48:42.466Z-->
- Groh carryforward: &#36;200&nbsp;000 NOL, future rate 20% → DTA in loss year = ? ::@:: &#36;200&nbsp;000 × 20% = &#36;40&nbsp;000; realization year: taxable income &#36;250&nbsp;000, carryforward &#36;200&nbsp;000, current tax = &#36;10&nbsp;000, income tax expense = &#36;50&nbsp;000. <!--SR:!fsrs,2026-06-17T08:15:10.043Z,8,8.2956,1,2,1,0,0,2026-06-09T08:15:10.043Z!fsrs,2026-06-18T08:00:55.035Z,8,8.2956,1,2,1,0,0,2026-06-10T08:00:55.035Z-->

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
> _Explanation._ This single entry bundles the topic's main workflow: {@{current tax payable plus net deferred tax expense after separating temporary and permanent differences}@}. <!--SR:!fsrs,2026-06-17T08:32:13.408Z,8,8.2956,1,2,1,0,0,2026-06-09T08:32:13.408Z!fsrs,2026-06-17T08:11:28.721Z,8,8.2956,1,2,1,0,0,2026-06-09T08:11:28.721Z!fsrs,2026-06-17T12:09:29.565Z,8,8.2956,1,2,1,0,0,2026-06-09T12:09:29.565Z!fsrs,2026-06-18T06:08:26.299Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:26.299Z!fsrs,2026-06-18T05:50:41.347Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:41.347Z!fsrs,2026-06-18T05:52:54.887Z,8,8.2956,1,2,1,0,0,2026-06-10T05:52:54.887Z!fsrs,2026-06-17T08:11:29.840Z,8,8.2956,1,2,1,0,0,2026-06-09T08:11:29.840Z!fsrs,2026-06-18T06:08:27.136Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:27.136Z!fsrs,2026-06-18T06:08:33.818Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:33.818Z!fsrs,2026-06-18T05:52:09.429Z,8,8.2956,1,2,1,0,0,2026-06-10T05:52:09.429Z!fsrs,2026-06-18T07:45:28.999Z,8,8.2956,1,2,1,0,0,2026-06-10T07:45:28.999Z!fsrs,2026-06-17T13:16:14.795Z,8,8.2956,1,2,1,0,0,2026-06-09T13:16:14.795Z!fsrs,2026-06-18T02:41:56.050Z,8,8.2956,1,2,1,0,0,2026-06-10T02:41:56.050Z!fsrs,2026-06-18T06:13:38.253Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:38.253Z!fsrs,2026-06-17T03:41:52.121Z,8,8.2956,1,2,1,0,0,2026-06-09T03:41:52.121Z!fsrs,2026-06-17T04:26:13.248Z,8,8.2956,1,2,1,0,0,2026-06-09T04:26:13.248Z!fsrs,2026-06-17T08:32:16.288Z,8,8.2956,1,2,1,0,0,2026-06-09T08:32:16.288Z-->

---

Flashcards for this section are as follows:

- comprehensive interperiod tax allocation: why separate temporary and permanent differences first? ::@:: Because temporary differences create deferred taxes while permanent differences do not. <!--SR:!fsrs,2026-06-18T06:08:23.885Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:23.885Z!fsrs,2026-06-18T05:49:38.284Z,8,8.2956,1,2,1,0,0,2026-06-10T05:49:38.284Z-->
- comprehensive tax problem: what question identifies whether the difference creates a deferred tax liability or asset? ::@:: Ask whether the difference creates future taxable amounts or future deductible amounts. <!--SR:!fsrs,2026-06-14T08:06:11.171Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:06:11.171Z!fsrs,2026-06-14T08:01:25.450Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:01:25.450Z-->
- permanent differences in a comprehensive schedule: do they enter deferred tax balances? ::@:: No; they affect taxable income but do not create deferred tax assets or liabilities. <!--SR:!fsrs,2026-06-17T04:58:47.990Z,8,8.2956,1,2,1,0,0,2026-06-09T04:58:47.990Z!fsrs,2026-06-17T03:43:26.882Z,8,8.2956,1,2,1,0,0,2026-06-09T03:43:26.882Z-->
- deferred tax presentation in this course: how are deferred tax balances generally classified? ::@:: As non-current. <!--SR:!fsrs,2026-06-17T04:59:03.246Z,8,8.2956,1,2,1,0,0,2026-06-09T04:59:03.246Z!fsrs,2026-06-17T12:39:18.945Z,8,8.2956,1,2,1,0,0,2026-06-09T12:39:18.945Z-->
- comprehensive tax workflow: what is the final combination step? ::@:: Combine current tax payable with the deferred tax effect to arrive at total income tax expense. <!--SR:!fsrs,2026-06-18T02:41:51.115Z,8,8.2956,1,2,1,0,0,2026-06-10T02:41:51.115Z!fsrs,2026-06-18T05:38:49.936Z,8,8.2956,1,2,1,0,0,2026-06-10T05:38:49.936Z-->
- comprehensive tax entry: why can both a deferred tax asset and deferred tax liability appear in the same journal entry? ::@:: Because different temporary differences can create future deductible amounts and future taxable amounts at the same reporting date, so the company records both pieces together with current tax payable. <!--SR:!fsrs,2026-06-17T13:33:38.921Z,8,8.2956,1,2,1,0,0,2026-06-09T13:33:38.921Z!fsrs,2026-06-18T04:11:18.888Z,8,8.2956,1,2,1,0,0,2026-06-10T04:11:18.888Z-->
- Comprehensive entry: pretax ¥412&nbsp;000, current tax ¥50&nbsp;000, DTL ¥186&nbsp;400, DTA ¥62&nbsp;400 → income tax expense = ? ::@:: ¥50&nbsp;000 + ¥186&nbsp;400 − ¥62&nbsp;400 = ¥174&nbsp;000. <!--SR:!2000-01-01,1,250!2026-05-21,4,270-->

## intraperiod tax allocation

__Intraperiod tax allocation__ requires that the tax consequences of an item follow that item into the same presentation component rather than all flowing through profit or loss.

IAS 12 distinguishes three destinations for tax consequences within a single period:

- items recognized in __profit or loss__ carry their current or deferred tax charge or benefit through income tax expense in __profit or loss__;
- items recognized in __other comprehensive income (OCI)__ carry their deferred tax charge or benefit through __OCI__; and
- items recognized directly in __equity__ carry their deferred tax charge or benefit directly in __equity__.

A common example is a property revaluation under IAS 16. The revaluation increases the carrying amount above the tax base, creating a taxable temporary difference. Because the revaluation gain goes to OCI, the deferred tax liability on that difference also goes to OCI, not through income tax expense in profit or loss.

---

Flashcards for this section are as follows:

- intraperiod tax allocation: general rule ::@:: The tax consequence of an item follows that item into profit or loss, other comprehensive income, or equity — whichever component recognized the underlying transaction. <!--SR:!fsrs,2026-06-18T06:13:33.894Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:33.894Z!fsrs,2026-06-18T06:07:16.222Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:16.222Z-->
- revaluation surplus under IAS 16: where does the related deferred tax liability go? ::@:: Into other comprehensive income alongside the revaluation surplus, not through income tax expense in profit or loss. <!--SR:!fsrs,2026-06-18T04:51:11.448Z,8,8.2956,1,2,1,0,0,2026-06-10T04:51:11.448Z!fsrs,2026-06-18T06:07:18.092Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:18.092Z-->
- interperiod versus intraperiod tax allocation: contrast ::@:: Interperiod allocation assigns tax to the correct accounting period; intraperiod allocation assigns tax to the correct presentation component within a single period. <!--SR:!fsrs,2026-06-17T15:57:17.329Z,8,8.2956,1,2,1,0,0,2026-06-09T15:57:17.329Z!fsrs,2026-06-18T05:50:32.770Z,8,8.2956,1,2,1,0,0,2026-06-10T05:50:32.770Z-->

## uncertain tax positions under IFRIC 23

When the tax treatment of a transaction is uncertain — for example, where the company has taken a position the tax authority might challenge — the company reflects that uncertainty in its tax balances using the guidance in IFRIC 23.

Key requirements:

- assume the tax authority will __examine the position with full knowledge__ of all relevant information;
- if it is __probable that the authority accepts the treatment__, recognize tax on that basis; and
- if it is __not probable__, measure the uncertain amount using either the __most likely amount__ (single most probable outcome) or the __expected value__ (probability-weighted sum of possible outcomes), whichever better predicts the resolution.

Recognized uncertain tax positions appear as additional current tax liabilities or as reductions in a deferred tax asset; they are not presented in a separate line item.

---

Flashcards for this section are as follows:

- IFRIC 23: what assumption does the entity make about the tax authority when assessing an uncertain tax position? ::@:: That the authority will examine the position with full knowledge of all relevant information. <!--SR:!fsrs,2026-06-18T05:54:53.806Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:53.806Z!fsrs,2026-06-18T07:28:13.922Z,8,8.2956,1,2,1,0,0,2026-06-10T07:28:13.922Z-->
- IFRIC 23: recognition threshold for an uncertain tax position ::@:: Whether it is probable that the tax authority will accept the entity's treatment; if not probable, a liability is recognized. <!--SR:!fsrs,2026-06-18T07:29:57.862Z,8,8.2956,1,2,1,0,0,2026-06-10T07:29:57.862Z!fsrs,2026-06-17T12:44:19.128Z,8,8.2956,1,2,1,0,0,2026-06-09T12:44:19.128Z-->
- IFRIC 23: two measurement approaches for an uncertain tax position ::@:: The most likely amount or the expected value, whichever better predicts the resolution of the uncertainty. <!--SR:!fsrs,2026-06-18T05:58:30.729Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:30.729Z!fsrs,2026-06-18T05:51:09.730Z,8,8.2956,1,2,1,0,0,2026-06-10T05:51:09.730Z-->
- uncertain tax position: where is the recognized liability presented? ::@:: As an additional current tax liability or as a reduction of a deferred tax asset, using existing IAS 12 line items rather than a separate caption. <!--SR:!fsrs,2026-06-18T05:30:01.053Z,8,8.2956,1,2,1,0,0,2026-06-10T05:30:01.053Z!fsrs,2026-06-18T06:12:46.253Z,8,8.2956,1,2,1,0,0,2026-06-10T06:12:46.253Z-->

## effective tax rate reconciliation

IAS 12 requires a disclosed __reconciliation__ between income tax expense as reported and the amount that would result from applying the statutory rate to pretax financial income.

The reconciliation matters because __permanent differences__ cause the effective rate to diverge from the statutory rate. Temporary differences do __not__ cause a rate divergence: they shift timing but do not change the total lifetime tax charge.

The __effective tax rate__ for a period is $\text{income tax expense} \div \text{pretax financial income}$.

Typical reconciling items include:

- __non-deductible expenses__ (such as fines and penalties), which add tax expense without adding pretax income and therefore __push the effective rate above the statutory rate__; and
- __non-taxable income__ (such as government bond interest), which adds pretax income without adding taxable income and therefore __push the effective rate below the statutory rate__.

---

Flashcards for this section are as follows:

- effective tax rate: formula ::@:: Income tax expense divided by pretax financial income. <!--SR:!fsrs,2026-06-18T06:08:41.380Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:41.380Z!fsrs,2026-06-18T07:29:18.354Z,8,8.2956,1,2,1,0,0,2026-06-10T07:29:18.354Z-->
- why do permanent differences appear in the effective rate reconciliation but temporary differences do not? ::@:: Temporary differences reverse in later periods and leave no net lifetime tax effect, while permanent differences permanently alter the total tax paid relative to pretax accounting income. <!--SR:!fsrs,2026-06-17T07:10:49.707Z,8,8.2956,1,2,1,0,0,2026-06-09T07:10:49.707Z!fsrs,2026-06-18T05:55:01.476Z,8,8.2956,1,2,1,0,0,2026-06-10T05:55:01.476Z-->
- non-deductible expense: effect on the effective tax rate ::@:: Increases the effective rate above the statutory rate because taxable income is inflated relative to pretax financial income. <!--SR:!fsrs,2026-06-18T06:12:50.118Z,8,8.2956,1,2,1,0,0,2026-06-10T06:12:50.118Z!fsrs,2026-06-17T12:59:45.129Z,8,8.2956,1,2,1,0,0,2026-06-09T12:59:45.129Z-->
- non-taxable income: effect on the effective tax rate ::@:: Decreases the effective rate below the statutory rate because pretax financial income includes the exempt amount while taxable income does not. <!--SR:!fsrs,2026-06-18T06:14:06.733Z,8,8.2956,1,2,1,0,0,2026-06-10T06:14:06.733Z!fsrs,2026-06-18T07:30:32.750Z,8,8.2956,1,2,1,0,0,2026-06-10T07:30:32.750Z-->

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
> Expense = {@{&#36;30&nbsp;000}@} current tax + {@{&#36;180&nbsp;000}@} DTL created − {@{&#36;60&nbsp;000}@} DTA created = {@{&#36;150&nbsp;000}@}. <!--SR:!fsrs,2026-06-18T05:54:51.206Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:51.206Z!fsrs,2026-06-17T05:10:15.570Z,8,8.2956,1,2,1,0,0,2026-06-09T05:10:15.570Z!fsrs,2026-06-17T09:00:23.434Z,8,8.2956,1,2,1,0,0,2026-06-09T09:00:23.434Z!fsrs,2026-06-18T05:29:56.548Z,8,8.2956,1,2,1,0,0,2026-06-10T05:29:56.548Z!fsrs,2026-06-18T05:53:07.685Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:07.685Z!fsrs,2026-06-17T05:02:01.291Z,8,8.2956,1,2,1,0,0,2026-06-09T05:02:01.291Z!fsrs,2026-06-18T05:53:16.631Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:16.631Z!fsrs,2026-06-17T12:44:11.853Z,8,8.2956,1,2,1,0,0,2026-06-09T12:44:11.853Z!fsrs,2026-06-18T05:54:15.686Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:15.686Z!fsrs,2026-06-18T07:58:17.877Z,8,8.2956,1,2,1,0,0,2026-06-10T07:58:17.877Z!fsrs,2026-06-14T08:05:15.135Z,4,3.94605407,1,2,2,0,0,2026-06-10T08:05:15.135Z!fsrs,2026-06-17T05:10:18.300Z,8,8.2956,1,2,1,0,0,2026-06-09T05:10:18.300Z!fsrs,2026-06-18T06:44:57.503Z,8,8.2956,1,2,1,0,0,2026-06-10T06:44:57.503Z-->

<!-- markdownlint-disable-next-line MD028 -->
> Year 2 entry. Partial DTL reversal as €300&nbsp;000 of future taxable amounts are now current-year taxable; partial DTA reversal as €120&nbsp;000 of warranty payments are now deducted; and remeasurement of all remaining balances at the newly enacted 25% rate. All effects combine in one entry.
>
> | {@{Record Year 2 income taxes including rate-change remeasurement}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{169&nbsp;000}@} | |
> | {@{Deferred tax liability (depreciation)}@} | {@{105&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{234&nbsp;000}@} |
> | {@{Deferred tax asset (warranty)}@} | | {@{40&nbsp;000}@} |
>
> DTL falls from {@{&#36;180&nbsp;000}@} to {@{&#36;75&nbsp;000}@} (decrease {@{&#36;105&nbsp;000}@}: Dr _Deferred tax liability_). DTA falls from {@{&#36;60&nbsp;000}@} to {@{&#36;20&nbsp;000}@} (decrease {@{&#36;40&nbsp;000}@}: Cr _Deferred tax asset_). Expense = {@{&#36;234&nbsp;000 − &#36;105&nbsp;000 + &#36;40&nbsp;000 = &#36;169&nbsp;000}@}. <!--SR:!fsrs,2026-06-18T04:49:05.985Z,8,8.2956,1,2,1,0,0,2026-06-10T04:49:05.985Z!fsrs,2026-06-18T06:08:28.563Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:28.563Z!fsrs,2026-06-18T06:07:23.121Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:23.121Z!fsrs,2026-06-17T04:25:36.995Z,8,8.2956,1,2,1,0,0,2026-06-09T04:25:36.995Z!fsrs,2026-06-18T03:59:45.061Z,8,8.2956,1,2,1,0,0,2026-06-10T03:59:45.061Z!fsrs,2026-06-18T04:12:48.031Z,8,8.2956,1,2,1,0,0,2026-06-10T04:12:48.031Z!fsrs,2026-06-18T06:13:32.092Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:32.092Z!fsrs,2026-06-18T03:05:04.098Z,8,8.2956,1,2,1,0,0,2026-06-10T03:05:04.098Z!fsrs,2026-06-18T07:28:18.065Z,8,8.2956,1,2,1,0,0,2026-06-10T07:28:18.065Z!fsrs,2026-06-18T05:51:12.923Z,8,8.2956,1,2,1,0,0,2026-06-10T05:51:12.923Z!fsrs,2026-06-17T08:15:20.511Z,8,8.2956,1,2,1,0,0,2026-06-09T08:15:20.511Z!fsrs,2026-06-17T05:01:58.737Z,8,8.2956,1,2,1,0,0,2026-06-09T05:01:58.737Z!fsrs,2026-06-18T05:54:41.261Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:41.261Z!fsrs,2026-06-18T06:08:24.866Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:24.866Z!fsrs,2026-06-18T07:46:38.580Z,8,8.2956,1,2,1,0,0,2026-06-10T07:46:38.580Z!fsrs,2026-06-18T06:13:48.500Z,8,8.2956,1,2,1,0,0,2026-06-10T06:13:48.500Z-->

<!-- markdownlint-disable-next-line MD028 -->
> Year 3 entry. Both temporary differences reach zero.
>
> | {@{Record Year 3 income taxes as all temporary differences fully reverse}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{175&nbsp;000}@} | |
> | {@{Deferred tax liability (depreciation)}@} | {@{75&nbsp;000}@} | |
> | {@{Income taxes payable}@} | | {@{230&nbsp;000}@} |
> | {@{Deferred tax asset (warranty)}@} | | {@{20&nbsp;000}@} |
>
> Expense = {@{&#36;230&nbsp;000}@} current tax − {@{&#36;75&nbsp;000}@} DTL reversal + {@{&#36;20&nbsp;000}@} DTA reversal = {@{&#36;175&nbsp;000}@}. <!--SR:!fsrs,2026-06-18T07:28:58.018Z,8,8.2956,1,2,1,0,0,2026-06-10T07:28:58.018Z!fsrs,2026-06-17T03:43:33.257Z,8,8.2956,1,2,1,0,0,2026-06-09T03:43:33.257Z!fsrs,2026-06-18T06:07:30.540Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:30.540Z!fsrs,2026-06-18T05:53:56.883Z,8,8.2956,1,2,1,0,0,2026-06-10T05:53:56.883Z!fsrs,2026-06-18T02:09:52.780Z,8,8.2956,1,2,1,0,0,2026-06-10T02:09:52.780Z!fsrs,2026-06-12T08:01:28.101Z,2,2.3065,2.11121424,2,2,0,0,2026-06-10T08:01:28.101Z!fsrs,2026-06-18T05:58:26.187Z,8,8.2956,1,2,1,0,0,2026-06-10T05:58:26.187Z!fsrs,2026-06-18T05:57:58.815Z,8,8.2956,1,2,1,0,0,2026-06-10T05:57:58.815Z!fsrs,2026-06-18T06:10:03.439Z,8,8.2956,1,2,1,0,0,2026-06-10T06:10:03.439Z!fsrs,2026-06-18T07:46:44.171Z,8,8.2956,1,2,1,0,0,2026-06-10T07:46:44.171Z!fsrs,2026-06-18T05:49:27.681Z,8,8.2956,1,2,1,0,0,2026-06-10T05:49:27.681Z!fsrs,2026-06-17T07:10:50.409Z,8,8.2956,1,2,1,0,0,2026-06-09T07:10:50.409Z!fsrs,2026-06-18T04:33:51.859Z,8,8.2956,1,2,1,0,0,2026-06-10T04:33:51.859Z-->

__Key observations:__

- In Year 2, the DTL debit (€105&nbsp;000) and DTA credit (€40&nbsp;000) pull income tax expense in opposite directions. The DTL falls by more than the DTA, so the rate cut produces a net tax benefit of €65&nbsp;000 in Year 2.
- When a DTL decreases because of a rate cut, the entry is a __debit__ (future tax burden shrinks → expense falls). When a DTA decreases because of a rate cut, the entry is a __credit__ (future tax saving shrinks → expense rises).
- By Year 3 both deferred balances are zero: the equipment has been fully depreciated for IFRS and all warranty claims have been paid.

---

Flashcards for this section are as follows:

- Merton exercise: why is Year 2 the most complex year to record? ::@:: Because the enacted rate cut simultaneously shrinks both the DTL and the DTA, and those two effects move income tax expense in opposite directions within the same entry. <!--SR:!fsrs,2026-06-18T06:08:44.434Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:44.434Z!fsrs,2026-06-18T05:51:13.935Z,8,8.2956,1,2,1,0,0,2026-06-10T05:51:13.935Z-->
- when a DTL decreases because of an enacted rate cut, what is the journal entry direction? ::@:: Debit the _Deferred tax liability_ and reduce _Income tax expense_, because the future tax burden has fallen. <!--SR:!fsrs,2026-06-18T06:12:48.405Z,8,8.2956,1,2,1,0,0,2026-06-10T06:12:48.405Z!fsrs,2026-06-18T03:03:28.952Z,8,8.2956,1,2,1,0,0,2026-06-10T03:03:28.952Z-->
- when a DTA decreases because of an enacted rate cut, what is the journal entry direction? ::@:: Credit the _Deferred tax asset_ and increase _Income tax expense_, because some of the expected future tax saving has been lost. <!--SR:!fsrs,2026-06-12T08:02:14.533Z,2,2.29815136,3.4641143,2,2,0,0,2026-06-10T08:02:14.533Z!fsrs,2026-06-17T04:59:02.038Z,8,8.2956,1,2,1,0,0,2026-06-09T04:59:02.038Z-->
- Merton exercise: in Year 2, does the net effect of the rate change increase or decrease income tax expense? ::@:: Decrease, because the DTL falls by €105&nbsp;000 while the DTA falls by only €40&nbsp;000, giving a net benefit of €65&nbsp;000. <!--SR:!fsrs,2026-06-17T13:43:34.959Z,8,8.2956,1,2,1,0,0,2026-06-09T13:43:34.959Z!fsrs,2026-06-18T06:08:39.151Z,8,8.2956,1,2,1,0,0,2026-06-10T06:08:39.151Z-->
- Merton exercise: what does the Year 3 entry reflect? ::@:: The full reversal of both remaining temporary differences: the last €300&nbsp;000 of IFRS depreciation reverses the DTL and the final €80&nbsp;000 warranty payment reverses the DTA. <!--SR:!fsrs,2026-06-18T07:28:17.391Z,8,8.2956,1,2,1,0,0,2026-06-10T07:28:17.391Z!fsrs,2026-06-18T05:54:18.225Z,8,8.2956,1,2,1,0,0,2026-06-10T05:54:18.225Z-->
- Merton Year 1: taxable income €100&nbsp;000, equipment TD €600&nbsp;000 (DTL), warranty TD €200&nbsp;000 (DTA), 30% rate → income tax expense = ? ::@:: DTL = €600&nbsp;000 × 30% = €180&nbsp;000; DTA = €200&nbsp;000 × 30% = €60&nbsp;000; expense = €30&nbsp;000 + €180&nbsp;000 − €60&nbsp;000 = €150&nbsp;000. <!--SR:!fsrs,2026-06-18T07:59:53.731Z,8,8.2956,1,2,1,0,0,2026-06-10T07:59:53.731Z!fsrs,2026-06-18T06:10:02.052Z,8,8.2956,1,2,1,0,0,2026-06-10T06:10:02.052Z-->
- Merton Year 2: current tax €234&nbsp;000, DTL falls from €180&nbsp;000 to €75&nbsp;000, DTA falls from €60&nbsp;000 to €20&nbsp;000 → income tax expense = ? ::@:: €234&nbsp;000 − €105&nbsp;000 (DTL decrease) + €40&nbsp;000 (DTA decrease) = €169&nbsp;000. <!--SR:!fsrs,2026-06-18T06:07:28.333Z,8,8.2956,1,2,1,0,0,2026-06-10T06:07:28.333Z!fsrs,2026-06-18T06:14:04.948Z,8,8.2956,1,2,1,0,0,2026-06-10T06:14:04.948Z-->
