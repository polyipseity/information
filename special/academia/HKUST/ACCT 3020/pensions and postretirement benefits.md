---
aliases:
  - DBO
  - defined benefit obligation
  - defined benefit plan
  - pension expense
  - pension worksheet
  - pensions and postretirement benefits
tags:
  - flashcard/active/special/academia/HKUST/ACCT_3020/pensions_and_postretirement_benefits
  - language/in/English
---

# pensions and postretirement benefits

This note covers defined benefit pension accounting under IFRS (IAS 19): defined benefit versus defined contribution plans, the defined benefit obligation, plan assets, components of pension cost (service cost, net interest, remeasurements), the pension worksheet approach, and presentation on the financial statements. All monetary examples use fictional companies and amounts.

## defined contribution versus defined benefit plans

Under a __defined contribution plan__ the employer contributes a fixed amount to a separately administered pension fund each period. Once that contribution is made, the employer's obligation ends. The employee bears all investment risk; if the fund underperforms, the employee receives smaller benefits. Hong Kong's Mandatory Provident Fund (MPF) is a defined contribution arrangement. Accounting is straightforward: expense equals contribution.

Under a __defined benefit plan__ the employer promises a specific retirement benefit — often based on years of service and final salary. The employer bears the investment risk and must fund the plan sufficiently. Because the ultimate obligation depends on long-term assumptions (employee turnover, salary growth, life expectancy, discount rates), companies employ independent actuaries to estimate the cost.

---

Flashcards for this section are as follows:

- defined contribution plan: what happens after the employer contributes? ::@:: The employer's obligation ends; the employee bears the investment risk and receives whatever the fund earns. <!--SR:!fsrs,2026-06-20T10:40:00.254Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:00.254Z!fsrs,2026-06-20T10:42:08.638Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:08.638Z-->
- defined benefit plan: who bears the investment risk? ::@:: The employer, because it has promised a specific future benefit regardless of how the fund performs. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T15:14:51.532Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:14:51.532Z-->
- why do defined benefit plans require actuaries? ::@:: The obligation depends on long-term assumptions (life expectancy, salary growth, discount rate, employee turnover) that only actuaries can reliably estimate. <!--SR:!fsrs,2026-08-08T16:44:25.485Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:25.485Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Mandatory Provident Fund (Hong Kong): defined contribution or defined benefit? ::@:: Defined contribution — the employer contributes a fixed percentage; the employee bears the investment risk. <!--SR:!fsrs,2026-06-20T10:42:05.548Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:05.548Z!fsrs,2026-06-20T10:40:27.643Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:27.643Z-->

## key pension concepts

The __defined benefit obligation (DBO)__ is the present value of all future pension payments that employees have earned to date, discounted at the yield on high-quality corporate bonds with maturity matching the obligation. The DBO rises each year because:

- employees earn more benefits through another year of service (__current service cost__);
- the obligation is one year closer to payment, so the discount unwinds (__interest cost__ = DBO × discount rate); and
- actuaries may revise their assumptions about mortality, salary growth, and similar factors, creating __actuarial gains or losses__.

__Plan assets__ are the fair value of investments held in a legally separate trust to fund the plan. They increase when the employer makes cash contributions and when the portfolio earns a return, and decrease when benefits are paid to retirees.

The __expected return on plan assets__ is computed as opening plan assets × discount rate (IAS 19 uses the same rate for both the DBO and the expected return). Differences between the actual return and the expected return are __asset gains or losses__.

The __funded status__ (net defined benefit obligation or net defined benefit asset) equals $\text{DBO} - \text{Fair value of plan assets}$.

A positive funded status means the plan is underfunded, which results in a __net defined benefit liability__ on the statement of financial position. A negative funded status means the plan is overfunded, which results in a __net defined benefit asset__ (subject to an asset ceiling test under IAS 19). The net defined benefit asset cannot exceed the present value of economic benefits available from refunds or reductions in future contributions (the __asset ceiling__ under IAS 19.64).

> _Illustration._ Suppose DBO is {@{€100&nbsp;000}@} and plan assets are {@{€130&nbsp;000}@} — an overfunding of {@{€30&nbsp;000}@}. If the present value of available future contribution reductions is only {@{€20&nbsp;000}@}, the recognized net defined benefit asset is {@{capped at €20&nbsp;000}@}; the remaining {@{€10&nbsp;000}@} is an asset ceiling effect that reduces equity via OCI. <!--SR:!fsrs,2026-08-08T16:25:08.950Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:08.950Z!fsrs,2026-08-08T16:24:54.267Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:54.267Z!fsrs,2026-08-08T16:24:55.410Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:55.410Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:24:59.717Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:59.717Z!fsrs,2026-08-08T16:03:09.453Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:03:09.453Z-->

---

Flashcards for this section are as follows:

- defined benefit obligation: what does it represent? ::@:: The present value of all future retirement payments that employees have already earned, discounted at the high-quality corporate bond yield. <!--SR:!fsrs,2026-08-08T18:14:41.600Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:14:41.600Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- what discount rate does IAS 19 use for both the DBO and the expected return on plan assets? ::@:: The yield on high-quality corporate bonds with duration matching the obligation. <!--SR:!fsrs,2026-06-20T10:43:35.374Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:35.374Z!fsrs,2026-06-20T10:48:33.351Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:33.351Z-->
- plan assets: four movements that change the balance ::@:: (1) Employer contributions increase; (2) actual return on investments increases; (3) benefits paid to retirees decrease; (4) plan amendments do not change plan assets directly. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T18:02:35.829Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:02:35.829Z-->
- funded status formula ::@:: DBO minus fair value of plan assets; a positive result is a net liability, a negative result is a net asset. <!--SR:!fsrs,2026-06-20T10:46:53.367Z,8,8.2956,1,2,1,0,0,2026-06-12T10:46:53.367Z!fsrs,2026-06-20T10:46:45.891Z,8,8.2956,1,2,1,0,0,2026-06-12T10:46:45.891Z-->
- when is a pension plan overfunded? ::@:: When the fair value of plan assets exceeds the DBO, resulting in a net defined benefit asset on the balance sheet. <!--SR:!fsrs,2026-06-20T10:45:09.790Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:09.790Z!fsrs,2026-06-20T10:43:22.168Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:22.168Z-->
- asset ceiling (IAS 19.64): what does it limit? ::@:: The recognized net defined benefit asset cannot exceed the PV of economic benefits available through refunds or future contribution reductions. _Example_: overfunding €30 000, but PV of available savings is only €20 000 → recognized asset = €20 000; the €10 000 excess is an asset ceiling effect reducing equity via OCI. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T18:14:59.379Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:14:59.379Z-->
- current service cost: definition ::@:: The increase in the DBO from employees earning one additional year of benefit credit during the current period. <!--SR:!fsrs,2026-06-20T10:43:52.140Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:52.140Z!fsrs,2026-06-20T10:48:34.099Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:34.099Z-->
- interest cost on the DBO: formula ::@:: Opening DBO × discount rate; represents the unwinding of the discount as the obligation is one year closer to payment. <!--SR:!fsrs,2026-06-20T10:43:53.629Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:53.629Z!fsrs,2026-06-20T10:45:19.436Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:19.436Z-->
- expected return on plan assets under IAS 19: formula ::@:: Opening fair value of plan assets × discount rate; IAS 19 uses the same rate for both the DBO and the expected return on plan assets. <!--SR:!fsrs,2026-06-20T10:44:51.250Z,8,8.2956,1,2,1,0,0,2026-06-12T10:44:51.250Z!fsrs,2026-06-20T10:48:32.540Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:32.540Z-->

## components of pension cost

Under IAS 19, total pension cost has three components that are reported in different places:

| Component | Description | Income statement line |
| --- | --- | --- |
| __Current service cost__ | Increase in DBO from employees earning one more year of benefit | Operating (employee benefits expense) |
| __Past service cost__ | Change in DBO from a plan amendment or curtailment | Immediately in P&amp;L (operating or separately disclosed) |
| __Net interest on the net defined benefit obligation__ | Funded-status balance × discount rate | Finance costs (or income if asset) |
| __Remeasurements__ | (a) Asset gain/loss: actual minus expected return; (b) Liability gain/loss: actuarial assumption changes | Other comprehensive income (OCI) — never recycled to P&amp;L |

The net interest component equals (DBO − plan assets) × discount rate, which also equals interest cost on the DBO minus expected return on plan assets. Remeasurements accumulate in accumulated other comprehensive income (AOCI) within equity.

---

Flashcards for this section are as follows:

- IAS 19 pension cost: three components and where each goes ::@:: (1) Service cost (current and past) → P&L as operating; (2) net interest on the net DBO → P&L as finance; (3) remeasurements → OCI, not P&L. <!--SR:!fsrs,2026-06-20T10:42:06.473Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:06.473Z!fsrs,2026-06-20T10:40:52.912Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:52.912Z-->
- net interest on the net defined benefit obligation: formula ::@:: (DBO − plan assets) × discount rate, which also equals interest cost on the DBO less expected return on plan assets. <!--SR:!fsrs,2026-06-20T10:43:55.900Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:55.900Z!fsrs,2026-06-20T10:45:08.990Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:08.990Z-->
- remeasurements: what two items do they capture? ::@:: (1) Asset gains/losses (actual vs expected return); (2) liability gains/losses from actuarial assumption changes. <!--SR:!fsrs,2026-06-20T10:39:20.427Z,8,8.2956,1,2,1,0,0,2026-06-12T10:39:20.427Z!fsrs,2026-06-20T10:48:29.158Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:29.158Z-->
- remeasurements and OCI: can they be recycled to P&L? ::@:: No — under IAS 19, remeasurements are recognized in OCI and accumulate in AOCI permanently; they are never recycled to profit or loss. <!--SR:!fsrs,2026-08-08T16:03:08.683Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:03:08.683Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- past service cost: when is it recognized? ::@:: Immediately in the period of the plan amendment or curtailment, as an increase in pension cost in P&L. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:25:03.000Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:03.000Z-->

## pension worksheet

The __pension worksheet__ is a multi-column working tool (not a formal accounting record) that helps reconcile the DBO, plan assets, pension expense, OCI, and the pension asset/liability balance simultaneously. The worksheet has two sides:

- __Left (journal entry columns)__: Pension expense, OCI, Cash, Pension asset/liability.
- __Right (memo columns)__: Plan assets and DBO.

The balance in the Pension asset/liability column always equals DBO minus plan assets (funded status). The worksheet enables one to prepare the annual journal entry without separately computing each column.

---

Flashcards for this section are as follows:

- pension worksheet: what two sides does it have? ::@:: Left side: journal entry columns (pension expense, OCI, cash, pension asset/liability); right side: memo columns (plan assets, DBO). <!--SR:!fsrs,2026-06-20T10:40:06.054Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:06.054Z!fsrs,2026-06-20T10:41:27.324Z,8,8.2956,1,2,1,0,0,2026-06-12T10:41:27.324Z-->
- pension worksheet: what does the pension asset/liability column always equal? ::@:: The funded status: DBO minus fair value of plan assets. <!--SR:!fsrs,2026-06-20T10:48:07.214Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:07.214Z!fsrs,2026-06-20T10:48:40.261Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:40.261Z-->
- benefits paid: how do they affect the pension worksheet? ::@:: Benefits paid reduce both plan assets and the DBO by the same amount, so they have no net effect on the funded status or the pension liability balance. <!--SR:!fsrs,2026-06-20T10:45:13.516Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:13.516Z!fsrs,2026-06-20T10:40:30.915Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:30.915Z-->
- how to read the annual journal entry from the pension worksheet ::@:: Sum each left-side column: Pension expense total → Dr _Pension expense_; Cash total → Cr _Cash_; OCI total → Dr/Cr _OCI_ for remeasurements; the Pension asset/liability total is the balancing entry (Dr/Cr _Net defined benefit liability_). <!--SR:!fsrs,2026-08-08T18:15:03.620Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:03.620Z!fsrs,2026-08-30T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-20T00:00:00.000Z-->

### year 1: Aldgate AG (2025)

> Aldgate AG sponsors a defined benefit pension plan. On 1 January 2025, both the {@{DBO and the plan assets stand at €120&nbsp;000}@}; the plan is fully funded. The discount rate is {@{10%}@}. During 2025: current service cost €11&nbsp;000, employer cash contributions €9&nbsp;600, benefits paid to retirees €8&nbsp;400. Assume the actual return on plan assets equals the expected return.
>
> | Pension worksheet — 2025 | Pension expense | OCI | Cash | Pension asset/liability | Plan assets | DBO |
> | --- | ---: | ---: | ---: | ---: | ---: | ---: |
> | Opening balance (1 Jan 2025) | | | | 0 | 120&nbsp;000 | (120&nbsp;000) |
> | Current service cost | {@{11&nbsp;000}@} | | | {@{(11&nbsp;000)}@} | | {@{(11&nbsp;000)}@} |
> | Interest on DBO (10% × 120&nbsp;000) | {@{12&nbsp;000}@} | | | {@{(12&nbsp;000)}@} | | {@{(12&nbsp;000)}@} |
> | Expected return on assets (10% × 120&nbsp;000) | {@{(12&nbsp;000)}@} | | | {@{12&nbsp;000}@} | {@{12&nbsp;000}@} | |
> | Benefits paid | | | | {@{0}@} | {@{(8&nbsp;400)}@} | {@{8&nbsp;400}@} |
> | Employer contributions | | | {@{(9&nbsp;600)}@} | {@{9&nbsp;600}@} | {@{9&nbsp;600}@} | |
> | __Subtotals / year-end balance__ | __{@{11&nbsp;000}@}__ | __{@{0}@}__ | __{@{(9&nbsp;600)}@}__ | __{@{(1&nbsp;400)}@}__ | __{@{133&nbsp;200}@}__ | __{@{(134&nbsp;600)}@}__ |
>
> _Funded status check:_ DBO €134&nbsp;600 − Plan assets €133&nbsp;200 = {@{€1&nbsp;400 net liability}@}, matching the Pension asset/liability column.
>
> The annual journal entry is:
>
> | {@{Record 2025 pension expense and funding}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Pension expense}@} | {@{11&nbsp;000}@} | |
> | {@{Cash}@} | | {@{9&nbsp;600}@} |
> | {@{Net defined benefit liability}@} | | {@{1&nbsp;400}@} |
>
> _Explanation._ Because the plan is fully funded at the start, the {@{net interest component is zero}@}. Pension expense equals current service cost only. The employer's contribution of €9&nbsp;600 is less than the expense of €11&nbsp;000, so the funded status worsens by {@{€1&nbsp;400}@}, creating a net liability on the balance sheet. <!--SR:!fsrs,2026-08-08T18:14:37.729Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:14:37.729Z!fsrs,2026-08-08T18:15:13.923Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:13.923Z!fsrs,2026-08-08T16:46:41.148Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:46:41.148Z!fsrs,2026-08-08T16:44:37.121Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:37.121Z!fsrs,2026-08-08T16:24:35.656Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:35.656Z!fsrs,2026-08-08T15:17:33.247Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:17:33.247Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:27:35.433Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:27:35.433Z!fsrs,2026-08-08T16:24:54.923Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:54.923Z!fsrs,2026-08-08T16:03:07.667Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:03:07.667Z!fsrs,2026-08-08T16:41:37.942Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:37.942Z!fsrs,2026-08-08T16:24:57.574Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:57.574Z!fsrs,2026-08-08T18:14:44.086Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:14:44.086Z!fsrs,2026-08-08T16:24:37.017Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:37.017Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T15:18:35.428Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:18:35.428Z!fsrs,2026-08-08T16:42:00.588Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:42:00.588Z!fsrs,2026-08-08T15:12:45.006Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:12:45.006Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:41:45.950Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:45.950Z!fsrs,2026-08-08T18:15:23.287Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:23.287Z!fsrs,2026-08-08T16:41:56.342Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:56.342Z!fsrs,2026-08-08T16:03:04.723Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:03:04.723Z!fsrs,2026-08-08T18:15:15.984Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:15.984Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:24:34.634Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:34.634Z!fsrs,2026-08-08T18:20:02.988Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:20:02.988Z!fsrs,2026-08-08T18:20:00.304Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:20:00.304Z!fsrs,2026-08-08T18:20:04.054Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:20:04.054Z!fsrs,2026-08-08T16:44:24.104Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:24.104Z!fsrs,2026-08-08T16:24:38.267Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:38.267Z-->

---

Flashcards for this section are as follows:

- Aldgate AG 2025: why is the net interest component zero? ::@:: Because the plan is fully funded at the start of the year (DBO = plan assets = €120 000), so the net defined benefit obligation is zero. <!--SR:!fsrs,2026-08-08T17:01:09.825Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T17:01:09.825Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- pension expense when plan is fully funded at the start of the year ::@:: Pension expense equals current service cost only; the net interest component is zero because the funded status is zero. <!--SR:!fsrs,2026-06-20T10:45:18.242Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:18.242Z!fsrs,2026-06-20T10:48:35.335Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:35.335Z-->
- why does the pension liability arise even when the plan starts fully funded? ::@:: Because pension expense (service cost) exceeds cash contributions for the year, the funded status deteriorates and a liability is recognized. <!--SR:!fsrs,2026-06-20T10:45:12.244Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:12.244Z!fsrs,2026-06-20T10:45:12.860Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:12.860Z-->
- Aldgate AG 2025 (opening DBO €120 000, service cost €11 000, rate 10%, benefits paid €8 400): year-end DBO? ::@:: €134 600 = opening €120 000 + service cost €11 000 + interest €12 000 − benefits paid €8 400. <!--SR:!fsrs,2026-08-08T18:15:01.338Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:01.338Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- Aldgate AG 2025 (opening plan assets €120 000, rate 10%, benefits paid €8 400, contributions €9 600): year-end plan assets? ::@:: €133 200 = opening €120 000 + expected return €12 000 − benefits paid €8 400 + contributions €9 600. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-07-14T15:15:51.433Z,31,30.53476645,5.48972837,2,2,0,0,2026-06-13T15:15:51.433Z-->
- Aldgate AG 2025 (year-end DBO €134 600, year-end plan assets €133 200): net pension liability? ::@:: €1 400 = DBO €134 600 − plan assets €133 200. Equivalently: pension expense €11 000 − contributions €9 600 = €1 400. <!--SR:!fsrs,2026-06-20T10:41:23.141Z,8,8.2956,1,2,1,0,0,2026-06-12T10:41:23.141Z!fsrs,2026-06-20T10:40:24.977Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:24.977Z-->
- Aldgate AG 2025 (pension expense €11 000, contributions €9 600, net liability created €1 400): journal entry? ::@:: Dr _Pension expense_ €11 000; Cr _Cash_ €9 600; Cr _Net defined benefit liability_ €1 400. <!--SR:!fsrs,2026-06-20T10:46:49.147Z,8,8.2956,1,2,1,0,0,2026-06-12T10:46:49.147Z!fsrs,2026-06-20T10:41:24.160Z,8,8.2956,1,2,1,0,0,2026-06-12T10:41:24.160Z-->

## past service cost

__Past service cost__ arises when an employer amends the plan — for example, by granting employees credit for prior service or increasing the benefit formula retroactively. It represents the increase (or decrease) in the DBO caused by the amendment. Under IAS 19, past service cost is recognized immediately in profit or loss in the period of the amendment; no deferral is permitted.

A curtailment (significant reduction in employees covered) also produces immediate recognition of the change in DBO as a gain or loss.

---

Flashcards for this section are as follows:

- past service cost: when is it recognized under IAS 19? ::@:: Immediately in P&L in the period of the plan amendment; no deferral is allowed. <!--SR:!fsrs,2026-06-20T10:47:59.068Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:59.068Z!fsrs,2026-06-20T10:40:01.733Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:01.733Z-->
- past service cost: what does it represent? ::@:: The change in the DBO resulting from a plan amendment (e.g., granting credit for prior service), recognized immediately as an expense in the period. <!--SR:!fsrs,2026-06-20T10:39:21.367Z,8,8.2956,1,2,1,0,0,2026-06-12T10:39:21.367Z!fsrs,2026-06-20T10:43:57.089Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:57.089Z-->
- curtailment versus plan amendment: IAS 19 treatment ::@:: Both are recognized immediately in P&L in the period they occur; no amortization or deferral is permitted under IAS 19. <!--SR:!fsrs,2026-06-20T10:47:49.418Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:49.418Z!fsrs,2026-06-20T10:44:55.125Z,8,8.2956,1,2,1,0,0,2026-06-12T10:44:55.125Z-->

### past service cost: Aldgate AG (2026)

> On 1 January 2026 Aldgate AG amends its pension plan, granting retroactive benefits to employees. The amendment increases the DBO immediately by {@{€96&nbsp;600}@} (past service cost). Opening balances carried forward from 2025: DBO €134&nbsp;600; plan assets €133&nbsp;200; net pension liability €1&nbsp;400.
>
> After the amendment on 1 January 2026: DBO = {@{€231&nbsp;200}@}; net funded status = {@{€231&nbsp;200}@} − €133&nbsp;200 = {@{€98&nbsp;000 net liability}@}. Discount rate: 10%. Service cost: €11&nbsp;400; contributions: €24&nbsp;000; benefits paid: €9&nbsp;600; actual return equals expected return.
>
> | Pension worksheet — 2026 | Pension expense | OCI | Cash | Pension asset/liability | Plan assets | DBO |
> | --- | ---: | ---: | ---: | ---: | ---: | ---: |
> | Opening (after amendment, 1 Jan 2026) | | | | (98&nbsp;000) | 133&nbsp;200 | (231&nbsp;200) |
>
> Simplified Year 2 entry including all components:
>
> Net interest = opening funded status after amendment × 10% = €98&nbsp;000 × {@{10%}@} = {@{€9&nbsp;800}@}
>
> (Equivalently: interest on DBO €231&nbsp;200 × 10% = {@{€23&nbsp;120}@} minus expected return on plan assets €133&nbsp;200 × 10% = {@{€13&nbsp;320}@}; net interest = {@{€9&nbsp;800}@}.)
>
> Total pension expense in P&amp;L = current service cost €11&nbsp;400 + net interest {@{€9&nbsp;800}@} + past service cost {@{€96&nbsp;600}@} = {@{€117&nbsp;800}@}.
>
> | {@{Record 2026 pension expense, past service cost, and funding}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Pension expense (service + net interest + past service cost)}@} | {@{117&nbsp;800}@} | |
> | {@{Cash}@} | | {@{24&nbsp;000}@} |
> | {@{Net defined benefit liability}@} | | {@{93&nbsp;800}@} |
>
> _Year-end check._ DBO = €231&nbsp;200 + €11&nbsp;400 + €23&nbsp;120 − €9&nbsp;600 = {@{€256&nbsp;120}@}. Plan assets = €133&nbsp;200 + €24&nbsp;000 − €9&nbsp;600 + €13&nbsp;320 = {@{€160&nbsp;920}@}. Funded status = €256&nbsp;120 − €160&nbsp;920 = {@{€95&nbsp;200 net liability}@}. Previous liability €1&nbsp;400 + €93&nbsp;800 = {@{€95&nbsp;200}@} ✓. <!--SR:!fsrs,2026-08-08T16:44:40.878Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:40.878Z!fsrs,2026-08-08T15:12:38.881Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:12:38.881Z!fsrs,2026-08-15T16:24:45.881Z,63,62.51337484,2.98092302,2,3,0,0,2026-06-13T16:24:45.881Z!fsrs,2026-08-08T15:13:08.408Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:13:08.408Z!fsrs,2026-08-08T18:02:36.825Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:02:36.825Z!fsrs,2026-08-08T16:25:05.424Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:05.424Z!fsrs,2026-08-08T16:25:10.060Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:10.060Z!fsrs,2026-08-08T18:14:36.596Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:14:36.596Z!fsrs,2026-08-08T16:41:40.290Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:40.290Z!fsrs,2026-08-08T15:14:43.234Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:14:43.234Z!fsrs,2026-08-08T16:41:46.854Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:46.854Z!fsrs,2026-08-08T15:12:35.525Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:12:35.525Z!fsrs,2026-08-08T15:18:36.831Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:18:36.831Z!fsrs,2026-08-08T16:44:39.088Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:39.088Z!fsrs,2026-08-08T16:25:08.184Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:08.184Z!fsrs,2026-08-08T15:17:29.215Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:17:29.215Z!fsrs,2026-08-08T16:24:44.719Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:44.719Z!fsrs,2026-08-08T16:25:04.184Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:04.184Z!fsrs,2026-08-08T16:44:20.141Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:20.141Z!fsrs,2026-08-08T15:14:41.913Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:14:41.913Z!fsrs,2026-08-08T16:25:01.534Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:01.534Z!fsrs,2026-08-08T16:41:44.038Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:44.038Z!fsrs,2026-08-08T15:18:34.378Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:18:34.378Z-->

---

Flashcards for this section are as follows:

- Aldgate AG 2026 (PSC €96 600): how does past service cost affect pension expense? ::@:: The full past service cost (€96 600) is added to pension expense in the year of the amendment, significantly increasing the total charge. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:24:51.450Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:51.450Z-->
- after a plan amendment increases the DBO, what happens to the net interest component? ::@:: Net interest rises because the net funded status (DBO − plan assets) is now larger, increasing the interest charge in P&L. <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:42:03.439Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:42:03.439Z-->
- Aldgate AG 2026 (service cost €11 400, net liability after PSC €98 000, rate 10%, PSC €96 600): total pension expense? ::@:: €117 800 = current service cost €11 400 + net interest €9 800 (€98 000 × 10%) + past service cost €96 600. <!--SR:!fsrs,2026-06-20T10:42:04.619Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:04.619Z!fsrs,2026-06-20T10:44:45.075Z,8,8.2956,1,2,1,0,0,2026-06-12T10:44:45.075Z-->
- Aldgate AG 2026 (opening DBO €134 600, PSC €96 600, plan assets €133 200): funded status after amendment? ::@:: €98 000 net liability = amended DBO €231 200 (€134 600 + PSC €96 600) − plan assets €133 200. <!--SR:!fsrs,2026-06-20T10:47:18.433Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:18.433Z!fsrs,2026-06-20T10:43:24.782Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:24.782Z-->
- Aldgate AG 2026 (amended DBO €231 200, service cost €11 400, rate 10%, benefits paid €9 600): year-end DBO? ::@:: €256 120 = amended DBO €231 200 + service cost €11 400 + interest €23 120 (€231 200 × 10%) − benefits paid €9 600. <!--SR:!fsrs,2026-07-28T00:00:00.000Z,41,41.28765564,1,2,3,0,0,2026-06-17T00:00:00.000Z!fsrs,2026-06-20T10:45:23.083Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:23.083Z-->
- Aldgate AG 2026 (opening plan assets €133 200, rate 10%, contributions €24 000, benefits paid €9 600): year-end plan assets? ::@:: €160 920 = opening plan assets €133 200 + expected return €13 320 (€133 200 × 10%) + contributions €24 000 − benefits paid €9 600. <!--SR:!fsrs,2026-06-20T10:42:12.771Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:12.771Z!fsrs,2026-06-20T10:39:55.959Z,8,8.2956,1,2,1,0,0,2026-06-12T10:39:55.959Z-->
- Aldgate AG 2026 (pension expense €117 800, contributions €24 000, net liability increase €93 800): journal entry? ::@:: Dr _Pension expense_ €117 800; Cr _Cash_ €24 000; Cr _Net defined benefit liability_ €93 800. <!--SR:!fsrs,2026-06-20T10:43:32.662Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:32.662Z!fsrs,2026-06-20T10:45:22.292Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:22.292Z-->

## remeasurements and other comprehensive income

__Remeasurements__ capture two types of experience adjustments that cannot be forecast reliably:

1. __Asset gains and losses__: the difference between the actual return on plan assets and the expected return (opening plan assets × discount rate). If actual > expected, it is an asset gain; if actual < expected, it is an asset loss.
2. __Liability gains and losses__: changes in the DBO due to revisions in actuarial assumptions (mortality, salary growth, turnover, discount rate). If the actuary's year-end estimate of the DBO is higher than the rolled-forward DBO, there is a liability loss; if lower, a liability gain.

Under IAS 19, both types of remeasurement go to __other comprehensive income (OCI)__. They are never recycled to profit or loss. They accumulate in __accumulated OCI (AOCI)__ within equity.

> Brixton SE has plan assets of €180&nbsp;000 at the start of 2025. The discount rate is 6%, so the {@{expected return on plan assets}@} is {@{€10&nbsp;800}@}. The actual return for the year is {@{€13&nbsp;200}@}, giving an asset gain of {@{€2&nbsp;400}@}.
>
> | {@{Record remeasurement asset gain in OCI}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Plan assets (memo account)}@} | {@{2&nbsp;400}@} | |
> | {@{OCI — remeasurement gain (pension)}@} | | {@{2&nbsp;400}@} |
>
> _Explanation._ The €2&nbsp;400 excess of actual return over expected return is {@{not recognized in profit or loss; it is a credit to OCI}@} because IAS 19 classifies all remeasurements as OCI items that accumulate permanently in equity. <!--SR:!fsrs,2026-08-08T18:15:09.251Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:09.251Z!fsrs,2026-08-08T15:12:39.816Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:12:39.816Z!fsrs,2026-08-08T16:44:16.282Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:16.282Z!fsrs,2026-07-14T18:02:33.737Z,31,30.53476645,5.48972837,2,2,0,0,2026-06-13T18:02:33.737Z!fsrs,2026-08-08T16:24:48.600Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:48.600Z!fsrs,2026-08-08T16:24:41.384Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:41.384Z!fsrs,2026-08-08T16:25:00.300Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:00.300Z!fsrs,2026-08-08T15:17:31.295Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:17:31.295Z!fsrs,2026-08-15T16:41:55.177Z,63,62.51337484,2.98092302,2,3,0,0,2026-06-13T16:41:55.177Z!fsrs,2026-08-08T18:14:33.985Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:14:33.985Z-->

---

Flashcards for this section are as follows:

- asset gain on pension plan assets: definition ::@:: The excess of the actual return on plan assets over the expected return (opening plan assets × discount rate); recognized in OCI, not P&L. <!--SR:!fsrs,2026-06-20T10:43:33.450Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:33.450Z!fsrs,2026-06-20T10:40:03.886Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:03.886Z-->
- asset loss on pension plan assets: what triggers it? ::@:: The actual return on plan assets is less than the expected return; recognized as a debit to _OCI_. <!--SR:!fsrs,2026-06-20T10:45:21.241Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:21.241Z!fsrs,2026-06-20T10:48:03.531Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:03.531Z-->
- liability gain/loss on pensions: what causes it? ::@:: Revisions to actuarial assumptions (e.g., changes in mortality rates, salary assumptions, or the discount rate) that alter the actuary's estimate of the DBO at year-end. <!--SR:!fsrs,2026-06-20T10:42:16.958Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:16.958Z!fsrs,2026-06-20T10:48:30.637Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:30.637Z-->
- remeasurements and OCI: can the balance be reclassified to P&L in a later year? ::@:: No — IAS 19 prohibits recycling of pension remeasurements; they remain in AOCI permanently. <!--SR:!fsrs,2026-06-20T10:46:44.041Z,8,8.2956,1,2,1,0,0,2026-06-12T10:46:44.041Z!fsrs,2026-06-20T10:42:20.307Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:20.307Z-->
- rolled-forward DBO: how is it computed and why does it differ from the actuary's figure? ::@:: Opening DBO + service cost + interest cost − benefits paid; it differs from the actuary's year-end estimate by the actuarial gain or loss (actual experience vs assumptions). <!--SR:!fsrs,2026-07-28T00:00:00.000Z,41,41.28765564,1,2,3,0,0,2026-06-17T00:00:00.000Z!fsrs,2026-06-20T10:45:16.160Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:16.160Z-->
- Brixton SE (opening plan assets €180 000, rate 6%, actual return €13 200): asset gain and OCI treatment? ::@:: Actual return €13 200 − expected return €10 800 (€180 000 × 6%) = asset gain €2 400, recognized as a credit to _OCI_ (remeasurement). <!--SR:!fsrs,2026-06-20T10:44:43.406Z,8,8.2956,1,2,1,0,0,2026-06-12T10:44:43.406Z!fsrs,2026-06-20T10:40:55.013Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:55.013Z-->

### remeasurement: Aldgate AG (2027)

> 2027 opening: DBO €256&nbsp;120; plan assets €160&nbsp;920; net liability €95&nbsp;200. Service cost: €15&nbsp;600. Discount rate: 10%. Cash contributions: €28&nbsp;800. Benefits paid: €12&nbsp;600. Actual return on plan assets: €14&nbsp;400 (expected return: €160&nbsp;920 × 10% = {@{€16&nbsp;092}@}; asset loss = {@{€1&nbsp;692}@}). At year-end, the actuary revises the DBO to {@{€318&nbsp;000}@}; the worksheet-computed DBO is only {@{€284&nbsp;732}@} = €256&nbsp;120 + €15&nbsp;600 − €12&nbsp;600 + {@{€25&nbsp;612}@} (interest on DBO); the difference is a liability loss of {@{€33&nbsp;268}@}. Total remeasurement loss in OCI: €1&nbsp;692 + €33&nbsp;268 = {@{€34&nbsp;960}@}.
>
> Net interest = €95&nbsp;200 × 10% = {@{€9&nbsp;520}@}. Pension expense = service €15&nbsp;600 + net interest €9&nbsp;520 = {@{€25&nbsp;120}@}.
>
> | {@{Record 2027 pension expense and remeasurements}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Pension expense}@} | {@{25&nbsp;120}@} | |
> | {@{OCI — remeasurement loss (pension)}@} | {@{34&nbsp;960}@} | |
> | {@{Cash}@} | | {@{28&nbsp;800}@} |
> | {@{Net defined benefit liability}@} | | {@{31&nbsp;280}@} |
>
> _Year-end check._ Plan assets = €160&nbsp;920 + €28&nbsp;800 − €12&nbsp;600 + €14&nbsp;400 = {@{€191&nbsp;520}@}. DBO (per actuary) = €318&nbsp;000. Funded status = {@{€126&nbsp;480 net liability}@}. Prior liability €95&nbsp;200 + €31&nbsp;280 = €126&nbsp;480 ✓. <!--SR:!fsrs,2026-06-20T10:48:01.061Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:01.061Z!fsrs,2026-06-20T10:47:51.074Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:51.074Z!fsrs,2026-06-20T10:46:41.758Z,8,8.2956,1,2,1,0,0,2026-06-12T10:46:41.758Z!fsrs,2026-06-20T10:44:53.308Z,8,8.2956,1,2,1,0,0,2026-06-12T10:44:53.308Z!fsrs,2026-06-20T10:48:41.268Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:41.268Z!fsrs,2026-06-20T10:43:18.508Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:18.508Z!fsrs,2026-06-20T10:40:32.195Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:32.195Z!fsrs,2026-06-20T10:44:46.329Z,8,8.2956,1,2,1,0,0,2026-06-12T10:44:46.329Z!fsrs,2026-06-20T10:40:21.379Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:21.379Z!fsrs,2026-06-20T10:47:39.356Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:39.356Z!fsrs,2026-06-20T10:46:50.568Z,8,8.2956,1,2,1,0,0,2026-06-12T10:46:50.568Z!fsrs,2026-06-20T10:47:32.410Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:32.410Z!fsrs,2026-06-20T10:45:11.063Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:11.063Z!fsrs,2026-06-20T10:43:19.584Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:19.584Z!fsrs,2026-06-20T10:46:42.946Z,8,8.2956,1,2,1,0,0,2026-06-12T10:46:42.946Z!fsrs,2026-06-20T10:47:42.738Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:42.738Z!fsrs,2026-06-20T10:41:21.643Z,8,8.2956,1,2,1,0,0,2026-06-12T10:41:21.643Z!fsrs,2026-06-20T10:46:52.526Z,8,8.2956,1,2,1,0,0,2026-06-12T10:46:52.526Z!fsrs,2026-06-20T10:47:59.793Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:59.793Z!fsrs,2026-06-20T10:40:56.965Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:56.965Z-->

---

Flashcards for this section are as follows:

- Aldgate AG 2027 (actual return €14 400, expected return €16 092; actuarial DBO €318 000, rolled-forward DBO €284 732): total OCI remeasurement? ::@:: Asset loss €1 692 (actual return €14 400 < expected €16 092) plus liability loss €33 268 (actuarial DBO €318 000 > rolled-forward DBO €284 732) = €34 960 total debit to _OCI_. <!--SR:!fsrs,2026-06-20T10:40:22.330Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:22.330Z!fsrs,2026-06-20T10:42:24.066Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:24.066Z-->
- Aldgate AG 2027 (opening plan assets €160 920, contributions €28 800, benefits €12 600, actual return €14 400; actuary's DBO €318 000): year-end DBO and plan assets? ::@:: DBO €318 000 (per actuary); plan assets €191 520 (€160 920 + contributions €28 800 − benefits €12 600 + actual return €14 400). <!--SR:!fsrs,2026-06-20T10:45:08.119Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:08.119Z!fsrs,2026-06-20T10:48:08.972Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:08.972Z-->
- Aldgate AG 2027 (service cost €15 600, opening net liability €95 200, rate 10%): pension expense? ::@:: €25 120 = service cost €15 600 + net interest (€95 200 × 10% = €9 520). <!--SR:!fsrs,2026-06-20T10:48:10.861Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:10.861Z!fsrs,2026-06-20T10:47:30.130Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:30.130Z-->

## financial statement presentation

The employer presents a single net amount on the statement of financial position: either a __net defined benefit liability__ (DBO > plan assets) or a __net defined benefit asset__ (plan assets > DBO, subject to asset ceiling), classified as non-current.

Under IAS 1 presentation, pension cost in P&L comprises:

- Current service cost and past service cost (operating section, typically within employee benefits expense).
- Net interest on the net defined benefit obligation (finance costs; or finance income if overfunded).

Remeasurements (asset gains/losses and actuarial gains/losses) are presented in other comprehensive income. IAS 19 requires disclosure of the components separately.

---

Flashcards for this section are as follows:

- net defined benefit liability: where is it shown on the balance sheet? ::@:: As a single non-current liability (DBO minus fair value of plan assets); separately from other current liabilities. <!--SR:!fsrs,2026-08-08T18:02:34.886Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:02:34.886Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z-->
- pension cost in the income statement: two line items under IAS 1 ::@:: (1) Service cost (current + past) in operating expenses; (2) net interest on net DBO in finance costs. <!--SR:!fsrs,2026-06-20T10:40:28.913Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:28.913Z!fsrs,2026-06-20T10:43:34.403Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:34.403Z-->
- pension remeasurements: where in the financial statements? ::@:: In other comprehensive income (OCI), accumulating in AOCI within equity; never in profit or loss. <!--SR:!fsrs,2026-06-20T10:40:30.162Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:30.162Z!fsrs,2026-06-20T10:39:18.361Z,8,8.2956,1,2,1,0,0,2026-06-12T10:39:18.361Z-->
- AOCI and pensions: what does the balance represent? ::@:: The cumulative net remeasurement losses (or gains) from asset gain/loss and actuarial changes recognized in OCI since the plan's inception, which reduce (or increase) equity permanently. <!--SR:!fsrs,2026-06-20T10:45:33.605Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:33.605Z!fsrs,2026-06-20T10:42:19.572Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:19.572Z-->
- how does the net defined benefit liability change from year to year? ::@:: Opening liability + pension expense recognized in P&L + remeasurements recognized in OCI − cash contributions paid. <!--SR:!fsrs,2026-06-20T10:48:08.055Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:08.055Z!fsrs,2026-06-20T10:43:20.961Z,8,8.2956,1,2,1,0,0,2026-06-12T10:43:20.961Z-->

### three-year summary: Aldgate AG

> After the three-year Aldgate AG sequence: net defined benefit liability = {@{€126&nbsp;480}@} on the statement of financial position. The AOCI balance in equity holds the {@{cumulative net remeasurement loss of €34&nbsp;960}@} from 2027 (years 2025 and 2026 had no remeasurements in this example).
>
> 2027 statement of comprehensive income presentation:
>
> | | Amount |
> | --- | ---: |
> | Profit or loss: pension expense (service €15&nbsp;600 + net interest €9&nbsp;520) | {@{(25&nbsp;120)}@} |
> | OCI: remeasurement loss (asset loss €1&nbsp;692 + actuarial liability loss €33&nbsp;268) | {@{(34&nbsp;960)}@} |
> | __Total comprehensive income impact__ | __({@{60&nbsp;080}@})__ | <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T17:01:10.674Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T17:01:10.674Z!fsrs,2026-08-08T18:14:45.267Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:14:45.267Z!fsrs,2026-08-08T18:14:33.087Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:14:33.087Z-->

---

Flashcards for this section are as follows:

- Aldgate AG year 3 (DBO €318 000, plan assets €191 520): net defined benefit liability? ::@:: €126 480 = DBO €318 000 − plan assets €191 520. <!--SR:!fsrs,2026-06-20T10:40:58.313Z,8,8.2956,1,2,1,0,0,2026-06-12T10:40:58.313Z!fsrs,2026-06-20T10:47:58.461Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:58.461Z-->
- Aldgate AG year 3 (pension expense €25 120, OCI remeasurement loss €34 960): total comprehensive income impact? ::@:: P&L pension expense −€25 120 (service €15 600 + net interest €9 520) plus OCI remeasurement loss −€34 960 = total comprehensive income impact −€60 080. <!--SR:!fsrs,2026-06-20T10:45:14.416Z,8,8.2956,1,2,1,0,0,2026-06-12T10:45:14.416Z!fsrs,2026-06-20T10:48:39.034Z,8,8.2956,1,2,1,0,0,2026-06-12T10:48:39.034Z-->

## difficult exercise

The following exercise combines a mid-year plan amendment (past service cost), remeasurement gains on both the DBO and plan assets, and the standard service and net interest components. Work through each step before consulting the solution.

### plan amendment with remeasurement gains

> Dalston Consulting AG sponsors a defined benefit pension plan. Opening balances (1 January 2026): DBO {@{480&nbsp;000}@}; plan assets {@{390&nbsp;000}@}; net defined benefit liability {@{90&nbsp;000}@}. Discount rate: {@{8%}@}. During the year: current service cost {@{36&nbsp;000}@}; employer contributions {@{45&nbsp;000}@}; benefits paid to retirees {@{28&nbsp;800}@}.
>
> On 1 July 2026, the plan is amended; past service cost is {@{72&nbsp;000}@}, recognized immediately in P&L. Post-amendment DBO for interest purposes: 480&nbsp;000 + 72&nbsp;000 = {@{552&nbsp;000}@}. Actual return on plan assets: {@{36&nbsp;000}@}; expected return: 390&nbsp;000 × 8% = {@{31&nbsp;200}@}; asset gain: {@{4&nbsp;800}@}. At year-end the actuary revises DBO to {@{570&nbsp;000}@}.
>
> __Rolled-forward DBO (before actuarial revision):__ 552&nbsp;000 + 44&nbsp;160 (interest) + 36&nbsp;000 (service) − 28&nbsp;800 (benefits) = {@{603&nbsp;360}@}. Actuary's DBO 570&nbsp;000 < 603&nbsp;360 → liability gain = {@{33&nbsp;360}@}.
>
> __Net interest:__ post-amendment net liability (90&nbsp;000 + 72&nbsp;000) × 8% = {@{12&nbsp;960}@}. Equivalently: interest on DBO {@{44&nbsp;160}@} (552&nbsp;000 × 8%) minus expected return {@{31&nbsp;200}@} = {@{12&nbsp;960}@}.
>
> __Pension expense (P&L):__ service {@{36&nbsp;000}@} + net interest {@{12&nbsp;960}@} + past service cost {@{72&nbsp;000}@} = {@{120&nbsp;960}@}.
>
> __Net OCI (remeasurements):__ asset gain {@{4&nbsp;800}@} + liability gain {@{33&nbsp;360}@} = {@{38&nbsp;160}@} net gain → credited to _OCI_.
>
> | Pension worksheet — 2026 | Pension expense | OCI | Cash | Pension asset/liability | Plan assets | DBO |
> | --- | ---: | ---: | ---: | ---: | ---: | ---: |
> | Opening (1 Jan 2026) | | | | (90&nbsp;000) | 390&nbsp;000 | (480&nbsp;000) |
> | Past service cost | {@{72&nbsp;000}@} | | | {@{(72&nbsp;000)}@} | | {@{(72&nbsp;000)}@} |
> | Current service cost | {@{36&nbsp;000}@} | | | {@{(36&nbsp;000)}@} | | {@{(36&nbsp;000)}@} |
> | Interest on DBO (8% × 552&nbsp;000) | {@{44&nbsp;160}@} | | | {@{(44&nbsp;160)}@} | | {@{(44&nbsp;160)}@} |
> | Expected return (8% × 390&nbsp;000) | ({@{31&nbsp;200}@}) | | | {@{31&nbsp;200}@} | {@{31&nbsp;200}@} | |
> | Employer contributions | | | {@{(45&nbsp;000)}@} | {@{45&nbsp;000}@} | {@{45&nbsp;000}@} | |
> | Benefits paid | | | | {@{0}@} | {@{(28&nbsp;800)}@} | {@{28&nbsp;800}@} |
> | Asset gain — OCI | | ({@{4&nbsp;800}@}) | | {@{4&nbsp;800}@} | {@{4&nbsp;800}@} | |
> | Liability gain — OCI | | ({@{33&nbsp;360}@}) | | {@{33&nbsp;360}@} | | {@{33&nbsp;360}@} |
> | __Year-end balance__ | __{@{120&nbsp;960}@}__ | __{@{(38&nbsp;160)}@}__ | __{@{(45&nbsp;000)}@}__ | __{@{(127&nbsp;800)}@}__ | __{@{442&nbsp;200}@}__ | __{@{(570&nbsp;000)}@}__ |
>
> _Funded status check:_ DBO {@{570&nbsp;000}@} − plan assets {@{442&nbsp;200}@} = {@{127&nbsp;800 net liability}@} ✓. Net liability movement: 90&nbsp;000 + 120&nbsp;960 − 45&nbsp;000 − 38&nbsp;160 = {@{127&nbsp;800}@} ✓. <!--SR:!fsrs,2026-08-08T16:41:39.038Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:39.038Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:44:26.685Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:26.685Z!fsrs,2026-08-08T16:44:13.746Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:13.746Z!fsrs,2026-08-08T16:24:47.967Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:47.967Z!fsrs,2026-08-08T16:03:05.389Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:03:05.389Z!fsrs,2026-08-08T16:44:27.816Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:27.816Z!fsrs,2026-08-08T15:17:26.968Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:17:26.968Z!fsrs,2026-08-08T16:41:50.799Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:50.799Z!fsrs,2026-08-08T16:24:49.435Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:49.435Z!fsrs,2026-07-14T17:01:08.350Z,31,30.53476645,5.48972837,2,2,0,0,2026-06-13T17:01:08.350Z!fsrs,2026-08-08T16:44:28.676Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:28.676Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:44:12.351Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:12.351Z!fsrs,2026-08-08T15:16:00.974Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:16:00.974Z!fsrs,2026-08-08T18:15:12.991Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:12.991Z!fsrs,2026-08-08T16:41:58.328Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:58.328Z!fsrs,2026-08-08T18:20:06.721Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:20:06.721Z!fsrs,2026-08-08T18:20:09.139Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:20:09.139Z!fsrs,2026-08-08T16:24:56.255Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:56.255Z!fsrs,2026-08-08T16:24:56.809Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:56.809Z!fsrs,2026-08-08T16:24:58.383Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:58.383Z!fsrs,2026-08-08T18:15:16.991Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:16.991Z!fsrs,2026-08-08T16:44:34.671Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:34.671Z!fsrs,2026-08-08T16:24:59.084Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:59.084Z!fsrs,2026-08-08T15:16:02.051Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:16:02.051Z!fsrs,2026-08-08T16:25:02.450Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:02.450Z!fsrs,2026-08-08T16:24:53.684Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:53.684Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T18:20:05.704Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:20:05.704Z!fsrs,2026-08-08T16:44:15.288Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:15.288Z!fsrs,2026-08-08T16:03:06.972Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:03:06.972Z!fsrs,2026-08-08T16:25:04.817Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:04.817Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T15:17:36.222Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:17:36.222Z!fsrs,2026-08-08T18:20:02.270Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:20:02.270Z!fsrs,2026-08-08T16:24:52.884Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:52.884Z!fsrs,2026-08-08T15:13:07.430Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:13:07.430Z!fsrs,2026-08-08T16:24:50.934Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:50.934Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T18:15:20.834Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:20.834Z!fsrs,2026-08-08T18:02:37.342Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:02:37.342Z!fsrs,2026-08-08T18:15:05.717Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:05.717Z!fsrs,2026-08-08T18:14:35.517Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:14:35.517Z!fsrs,2026-08-08T18:20:01.470Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:20:01.470Z!fsrs,2026-08-08T16:44:42.721Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:42.721Z!fsrs,2026-08-08T16:24:39.784Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:39.784Z!fsrs,2026-08-08T16:44:22.205Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:22.205Z!fsrs,2026-08-08T16:27:34.983Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:27:34.983Z!fsrs,2026-08-08T16:41:59.804Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:59.804Z!fsrs,2026-08-08T18:20:04.820Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:20:04.820Z!fsrs,2026-08-08T16:24:47.084Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:24:47.084Z!fsrs,2026-08-08T16:44:30.671Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:30.671Z!fsrs,2026-08-08T16:25:07.434Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:25:07.434Z!fsrs,2026-08-08T18:15:08.168Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:08.168Z!fsrs,2026-08-08T15:15:54.164Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:15:54.164Z!fsrs,2026-08-08T16:03:03.855Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:03:03.855Z!fsrs,2026-08-08T18:15:22.317Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:22.317Z!fsrs,2026-08-08T18:14:43.217Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:14:43.217Z!fsrs,2026-08-08T16:41:42.363Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:42.363Z-->

<!-- markdownlint-disable-next-line MD028 -->
> Dalston Consulting AG 2026 — defined benefit pension journal entry: pension expense (P&L) = {@{120&nbsp;960}@}; cash contributions = {@{45&nbsp;000}@}; OCI remeasurement gain = {@{38&nbsp;160}@}; net liability increase = {@{37&nbsp;800}@}.
>
> | {@{Record 2026 pension cost, contributions, and remeasurements — Dalston Consulting AG}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Pension expense (P&L)}@} | {@{120&nbsp;960}@} | |
> | {@{Cash}@} | | {@{45&nbsp;000}@} |
> | {@{OCI — remeasurement gain}@} | | {@{38&nbsp;160}@} |
> | {@{Net defined benefit liability}@} | | {@{37&nbsp;800}@} |
>
> Pension expense {@{120&nbsp;960}@} increases the liability; contributions {@{45&nbsp;000}@} and the OCI gain {@{38&nbsp;160}@} reduce it. Net increase = {@{37&nbsp;800}@}; closing liability: 90&nbsp;000 + 37&nbsp;800 = {@{127&nbsp;800}@} ✓. <!--SR:!fsrs,2026-08-08T16:41:47.893Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:47.893Z!fsrs,2026-08-08T16:41:48.957Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:48.957Z!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:44:17.135Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:17.135Z!fsrs,2026-08-08T18:19:58.812Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:19:58.812Z!fsrs,2026-08-08T18:15:18.984Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:18.984Z!fsrs,2026-08-08T16:42:04.167Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:42:04.167Z!fsrs,2026-08-08T18:20:07.844Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:20:07.844Z!fsrs,2026-08-08T18:15:11.980Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T18:15:11.980Z!fsrs,2026-08-08T15:18:32.249Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:18:32.249Z!fsrs,2026-08-08T16:44:38.141Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:44:38.141Z!fsrs,2026-08-08T16:03:10.011Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:03:10.011Z!fsrs,2026-08-08T15:17:32.326Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T15:17:32.326Z!fsrs,2026-08-08T16:34:21.113Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:34:21.113Z-->

---

Flashcards for this section are as follows:

- Dalston 2026 (service cost 36&nbsp;000, opening net liability 90&nbsp;000, PSC 72&nbsp;000, rate 8%): total pension expense in P&L? ::@:: 120&nbsp;960 = current service cost 36&nbsp;000 + net interest 12&nbsp;960 [(90&nbsp;000 + 72&nbsp;000) × 8%] + past service cost 72&nbsp;000. <!--SR:!fsrs,2026-06-20T10:47:37.361Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:37.361Z!fsrs,2026-06-20T10:42:07.553Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:07.553Z-->
- Dalston 2026 (opening net liability 90&nbsp;000, PSC 72&nbsp;000, rate 8%; DBO after amendment 552&nbsp;000, opening plan assets 390&nbsp;000): net interest? ::@:: (90&nbsp;000 + 72&nbsp;000) × 8% = 12&nbsp;960; equivalently interest on adjusted DBO 552&nbsp;000 × 8% = 44&nbsp;160 minus expected return 390&nbsp;000 × 8% = 31&nbsp;200. <!--SR:!fsrs,2026-06-20T10:42:16.128Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:16.128Z!fsrs,2026-06-20T10:42:01.562Z,8,8.2956,1,2,1,0,0,2026-06-12T10:42:01.562Z-->
- Dalston 2026 (actual return 36&nbsp;000, expected return 31&nbsp;200; rolled-forward DBO 603&nbsp;360, actuary's DBO 570&nbsp;000): total OCI remeasurement gain? ::@:: Net gain 38&nbsp;160 = asset gain 4&nbsp;800 (actual return 36&nbsp;000 minus expected 31&nbsp;200) + liability gain 33&nbsp;360 (rolled-forward DBO 603&nbsp;360 minus actuary's DBO 570&nbsp;000). <!--SR:!fsrs,2026-08-29T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-19T00:00:00.000Z!fsrs,2026-08-08T16:41:57.478Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T16:41:57.478Z-->
- Dalston 2026 (pension expense 120&nbsp;960, contributions 45&nbsp;000, OCI gain 38&nbsp;160): journal entry — which accounts are credited? ::@:: _Cash_ 45&nbsp;000 (contributions); _OCI — remeasurement gain_ 38&nbsp;160; _net defined benefit liability_ 37&nbsp;800. <!--SR:!fsrs,2026-06-20T10:41:25.117Z,8,8.2956,1,2,1,0,0,2026-06-12T10:41:25.117Z!fsrs,2026-06-20T10:47:41.861Z,8,8.2956,1,2,1,0,0,2026-06-12T10:47:41.861Z-->
- Dalston 2026 (DBO 570&nbsp;000, plan assets 442&nbsp;200): closing net defined benefit liability? ::@:: 127&nbsp;800 = DBO 570&nbsp;000 − plan assets 442&nbsp;200; verified as 90&nbsp;000 + 120&nbsp;960 − 45&nbsp;000 − 38&nbsp;160. <!--SR:!fsrs,2026-06-20T10:44:48.929Z,8,8.2956,1,2,1,0,0,2026-06-12T10:44:48.929Z!fsrs,2026-07-28T00:00:00.000Z,41,41.28765564,1,2,3,0,0,2026-06-17T00:00:00.000Z-->
