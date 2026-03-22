---
aliases:
  - journal entries
  - journal entry
tags:
  - flashcard/active/special/academia/HKUST/ACCT_3020/journal_entries
  - language/in/English
---

# journal entries

This note collects all types of journal entries encountered in ACCT 3020. One entry type per section; each section has one or more brief examples. Each example is in a single blockquote: scenario (before the journal entry), the journal entry in a markdown table (Dr/Cr columns), and optionally explanation or calculation (after the table). Use the two-sided cards for concepts and how to create the entry; use cloze cards to memorise the examples. New entry types will be added as the course covers more topics (e.g. provisions, bonds, equity).

## borrowing on a short-term interest-bearing note

When the entity borrows cash and signs a short-term interest-bearing note, it receives cash and creates a liability.

> *Scenario.* Entity {@{borrows 50 000 on 1 November, 8% annual rate}@}, due in {@{six months}@}.
>
>
> | {@{Receive cash; record note}@} | Dr           | Cr           |
> | ------------------------------- | ------------ | ------------ |
> | {@{Cash}@}                      | {@{50 000}@} |              |
> | {@{Notes payable}@}             |              | {@{50 000}@} |

---

Flashcards for this section are as follows:

- short-term interest-bearing note: journal entry at borrowing? ::@:: Dr Cash, Cr Notes payable (amount = principal received).
- borrowing on short-term note: Entity borrows 50 000 on 8% note—entry? ::@:: Dr Cash 50 000, Cr Notes payable 50 000.

## accruing interest on a short-term note

Interest is recognised in the period it is incurred (accrual basis). The stated rate is usually annual; prorate for a fraction of a year: principal × rate × (months to year-end / 12).

> *Scenario.* Same note: {@{50 000, 8% per year. At 31 December, two months have elapsed}@}.
>
>
> | {@{Accrue interest to year-end}@} | Dr           | Cr           |
> | --------------------------------- | ------------ | ------------ |
> | {@{Interest expense}@}            | {@{833.33}@} |              |
> | {@{Interest payable}@}            |              | {@{833.33}@} |
>
>
> *Calculation.* {@{Interest}@} = {@{50 000 × 0.08 × 2/12}@} = {@{833.33}@}.

---

Flashcards for this section are as follows:

- short-term note: how is interest accrued at year-end? ::@:: Interest = principal × annual rate × (months to year-end / 12); Dr Interest expense, Cr Interest payable.
- short-term note interest accrual: Given principal 50 000, 8% annual rate, 2 months elapsed—entry? ::@:: Dr Interest expense 833.33, Cr Interest payable 833.33 (i.e. 50 000 × 0.08 × 2/12).

## settling a short-term interest-bearing note

At maturity the entity pays principal plus interest and clears the note and interest payable.

> *Scenario.* Note matures; {@{total cash paid 52 000 (principal 50 000 + interest 2 000)}@}. Assume {@{833.33 already accrued; remainder interest at settlement}@}.
>
>
> | {@{Settle note and interest; pay cash}@} | Dr             | Cr           |
> | ---------------------------------------- | -------------- | ------------ |
> | {@{Notes payable}@}                      | {@{50 000}@}   |              |
> | {@{Interest payable}@}                   | {@{833.33}@}   |              |
> | {@{Interest expense}@}                   | {@{1 166.67}@} |              |
> | {@{Cash}@}                               |                | {@{52 000}@} |
>

---

Flashcards for this section are as follows:

- short-term note: journal entry at settlement (due date)? ::@:: Dr Notes payable (principal), Dr Interest payable (accrued), Dr Interest expense (any remaining), Cr Cash (total paid).
- settling short-term note: Pay 52 000 (principal 50 000 + interest), 833.33 already in Interest payable—entry? ::@:: Dr Notes payable 50 000, Dr Interest payable 833.33, Dr Interest expense 1 166.67, Cr Cash 52 000.

## conversion of accounts payable to notes payable

When a supplier requires conversion of an account payable into a note (e.g. with interest), the obligation is reclassified. After conversion, interest is accrued from the note date to the next reporting date.

> *Scenario.* Account payable {@{10 000 converted to note on 1 October; 8% per year}@}. At 31 December, {@{accrue 3 months' interest}@}.
>
> **At conversion:**
>
>
> | {@{Reclassify AP to note}@} | Dr           | Cr           |
> | --------------------------- | ------------ | ------------ |
> | {@{Accounts payable}@}      | {@{10 000}@} |              |
> | {@{Notes payable}@}         |              | {@{10 000}@} |
>
>
> **At year-end (accrual):**
>
>
> | {@{Accrue interest to reporting date}@} | Dr        | Cr        |
> | --------------------------------------- | --------- | --------- |
> | {@{Interest expense}@}                  | {@{200}@} |           |
> | {@{Interest payable}@}                  |           | {@{200}@} |
>
>
> *Calculation.* {@{10 000 × 0.08 × 3/12}@} = {@{200}@}.

---

Flashcards for this section are as follows:

- conversion of AP to note: journal entry at conversion? ::@:: Dr Accounts payable, Cr Notes payable (same amount).
- after conversion to note: Given principal, rate, and months to reporting date, how is interest recorded? ::@:: Accrue interest (principal × rate × months/12); Dr Interest expense, Cr Interest payable.
- conversion example: AP 10 000 → note 1 Oct, 8%—conversion entry? ::@:: Dr Accounts payable 10 000, Cr Notes payable 10 000.
- conversion example: note 10 000, 8%, 3 months to year-end—accrual entry? ::@:: Dr Interest expense 200, Cr Interest payable 200.

## accruing implicit interest on a note issued at discount

**Implicit interest** (also called embedded interest) is the difference between the cash the entity receives when it issues a note and the amount it must repay at maturity. It arises when a note is **issued at a discount**: cash received is less than the amount due at maturity (there is no separately stated interest rate; the interest is "built in" to the discount). When that happens, the difference is implicit interest. Allocate it over the term; credit **Notes payable** (not Interest payable) so the carrying amount increases to the maturity amount.

> *Scenario.* Entity {@{receives 75 000 and must repay 81 000 in 12 months. Implicit interest 6 000}@}. After 3 months, {@{allocate 3/12 of the discount}@}.
>
>
> | {@{Allocate implicit interest; credit Notes payable}@} | Dr          | Cr          |
> | ------------------------------------------------------ | ----------- | ----------- |
> | {@{Interest expense}@}                                 | {@{1 500}@} |             |
> | {@{Notes payable}@}                                    |             | {@{1 500}@} |
>
>
> *Calculation.* {@{6 000 × 3/12}@} = {@{1 500}@}. Crediting {@{Notes payable (not Interest payable) increases the carrying amount toward the}@} maturity amount.

---

Flashcards for this section are as follows:

- what is implicit interest? ::@:: The difference between cash received when the note is issued and the amount due at maturity; interest is "built in" to the discount, not separately stated.
- when does implicit interest arise? ::@:: When a note is issued at a discount (cash received < amount due at maturity); no separate interest rate is stated.
- implicit interest note: why credit Notes payable not Interest payable? ::@:: So the carrying amount of the note increases to the maturity amount; if credited to Interest payable the note would stay at the original amount.
- implicit interest note: Given total discount and term, allocation formula and entry? ::@:: Allocate total implicit interest over term (e.g. discount × months elapsed / 12); Dr Interest expense, Cr Notes payable.
- implicit interest note: receive 75 000, repay 81 000 in 12 months—accrual for 3 months? ::@:: Dr Interest expense 1 500, Cr Notes payable 1 500 (i.e. 6 000 × 3/12).

## settling a note with implicit interest at maturity

At the due date the note's carrying amount equals the maturity amount; the entity pays cash and clears the liability.

> *Scenario.* Note matures; {@{carrying amount 81 000, pay 81 000 cash}@}.
>
>
> | {@{Pay note at maturity}@} | Dr           | Cr           |
> | -------------------------- | ------------ | ------------ |
> | {@{Notes payable}@}        | {@{81 000}@} |              |
> | {@{Cash}@}                 |              | {@{81 000}@} |
>

---

Flashcards for this section are as follows:

- implicit interest note at maturity: journal entry? ::@:: Dr Notes payable (full maturity amount), Cr Cash.
- settling note with implicit interest: carrying amount 81 000 at due date—entry? ::@:: Dr Notes payable 81 000, Cr Cash 81 000.

## asset retirement obligation (decommissioning): initial recognition

When a company has a legal obligation to dismantle/remove an asset at the end of its useful life (e.g. an oil platform), it recognizes a provision (liability) measured at present value, and capitalizes the same amount as part of the asset's cost (PPE).

> *Scenario.* Company erects an oil platform on day 1. It must dismantle it in {@{5 years}@} at an expected cost of {@{1 000 000}@}. Discount rate {@{10%}@}. Recognise the obligation on day 1.
>
>
> | {@{Recognise ARO asset and liability}@} | Dr            | Cr            |
> | --------------------------------------- | ------------- | ------------- |
> | {@{Oil platform (PPE)}@}                | {@{620 921}@} |               |
> | {@{Environmental liability (ARO)}@}     |               | {@{620 921}@} |
>
>
> *Calculation.* PV = {@{1 000 000 ÷ (1.10^5)}@} = {@{620 921}@}.

---

Flashcards for this section are as follows:

- asset retirement obligation (ARO): initial recognition entry? ::@:: Recognize liability at PV and capitalize same amount in PPE (Dr PPE; Cr Environmental liability (ARO)).
- ARO: why record an asset at initial recognition? ::@:: Because the dismantling/restoration obligation is necessary to operate the asset and provides future benefits; allocate via depreciation over useful life.

## asset retirement obligation: depreciation of capitalized ARO cost

The capitalized ARO amount in PPE is depreciated over the asset's useful life.

> *Scenario.* Capitalized ARO cost is {@{620 921}@}; useful life {@{5 years}@}; straight-line. Record year-end depreciation (for the ARO component).
>
>
> | {@{Depreciate capitalized ARO cost}@}         | Dr            | Cr            |
> | --------------------------------------------- | ------------- | ------------- |
> | {@{Depreciation expense}@}                    | {@{124 184}@} |               |
> | {@{Accumulated depreciation — oil platform}@} |               | {@{124 184}@} |
>
>
> *Calculation.* {@{620 921 ÷ 5}@} = {@{124 184}@} (rounded).

---

Flashcards for this section are as follows:

- ARO: depreciation of capitalized cost (entry)? ::@:: Dr Depreciation expense; Cr Accumulated depreciation (depreciate the capitalized ARO amount over useful life).

## asset retirement obligation: accretion of liability (interest expense)

The ARO liability is recognised initially at present value, which is less than the expected future cash outflow. Conceptually, the difference between the initial present value and the eventual settlement amount is the time value of money: even though no extra cash is borrowed, the entity has a long-term obligation and must unwind the discount over time. Accretion (interest expense) increases the liability each period so it grows from present value to the expected settlement amount by the end of the useful life.

> *Scenario.* Beginning ARO liability {@{620 921}@}; discount rate {@{10%}@}. Record year 1 accretion.
>
>
> | {@{Accrete ARO liability (interest expense)}@} | Dr           | Cr           |
> | ---------------------------------------------- | ------------ | ------------ |
> | {@{Interest expense}@}                         | {@{62 092}@} |              |
> | {@{Environmental liability (ARO)}@}            |              | {@{62 092}@} |
>
>
> *Calculation.* {@{620 921 × 0.10}@} = {@{62 092}@} (rounded).

---

Flashcards for this section are as follows:

- ARO: why does the liability increase over time? ::@:: Accretion/interest expense increases the liability from PV at recognition to the expected cash outflow at settlement.
- ARO: accretion entry? ::@:: Dr Interest expense; Cr Environmental liability (ARO) (interest = carrying amount × discount rate).
- ARO accretion: economic rationale for interest? ::@:: The liability was initially recorded at a discounted present value below the expected future payment; accretion unwinds that discount over time as interest expense so the carrying amount reaches the full settlement amount.

## asset retirement obligation: settlement (gain or loss)

At settlement, the entity clears the ARO liability and pays cash (or records a payable). If the actual settlement differs from the liability carrying amount, recognize a gain or loss on settlement.

> *Scenario.* At the end of year 5, ARO liability carrying amount is {@{1 000 000}@}. Company pays contractor {@{995 000}@} to dismantle platform. Record settlement.
>
>
> | {@{Settle ARO liability; recognize gain/loss}@} | Dr              | Cr            |
> | ----------------------------------------------- | --------------- | ------------- |
> | {@{Environmental liability (ARO)}@}             | {@{1 000 000}@} |               |
> | {@{Cash / Accounts payable}@}                   |                 | {@{995 000}@} |
> | {@{Gain on settlement}@}                        |                 | {@{5 000}@}   |
>

---

Flashcards for this section are as follows:

- ARO: settlement entry (general form)? ::@:: Dr Environmental liability (carrying amount); Cr Cash/Payable (amount paid); Cr Gain on settlement (or Dr Loss) for difference.

## recognising income tax payable

At the end of the reporting period, if tax is owed but not yet paid, the entity recognises tax expense and a current liability.

> *Scenario.* Year-end: {@{income tax expense 120 000, payable within four months}@}.
>
>
> | {@{Recognise tax expense and payable}@}   | Dr            | Cr            |
> | ----------------------------------------- | ------------- | ------------- |
> | {@{Tax expense (or Income tax expense)}@} | {@{120 000}@} |               |
> | {@{Tax payable (or Income tax payable)}@} |               | {@{120 000}@} |
>

---

Flashcards for this section are as follows:

- income tax payable: when and what entry? ::@:: At reporting date when tax is owed but not yet paid; Dr Tax expense, Cr Tax payable; classified as current liability.
- income tax example: tax expense 120 000 owed at year-end—entry? ::@:: Dr Tax expense 120 000, Cr Tax payable 120 000.

## compensated absence: recognising vacation pay when earned

When employees earn the right to paid vacation (e.g. after a vesting period), the entity recognises expense and a liability in the period the right is earned, even if payment is later.

> *Scenario.* End of year 1: {@{20 unused vacation weeks earned at 480 per week}@}. Total {@{9 600}@}.
>
>
> | {@{Recognise expense and wages payable}@} | Dr          | Cr          |
> | ----------------------------------------- | ----------- | ----------- |
> | {@{Salaries and wages expense}@}          | {@{9 600}@} |             |
> | {@{Wages payable}@}                       |             | {@{9 600}@} |
>

---

Flashcards for this section are as follows:

- compensated absence: when to recognise expense and liability? ::@:: When the right is earned (e.g. at end of vesting period), even if payment is in a later period; Dr Salaries and wages expense, Cr Wages payable.
- vacation pay earned: 20 weeks at 480/week at end of year 1—entry? ::@:: Dr Salaries and wages expense 9 600, Cr Wages payable 9 600.

## compensated absence: paying vacation when taken

When employees take vacation and are paid, the entity clears the wages payable. If the current wage rate is higher than the rate when the right was earned, the difference is additional expense in the period of payment.

> *Scenario.* Wages payable {@{9 600 (20 weeks at 480). Employees take vacation; current rate 540 per week}@}. Cash paid {@{10 800; difference 1 200 expense in payment period}@}.
>
>
> | {@{Clear wages payable; expense difference; pay cash}@} | Dr          | Cr           |
> | ------------------------------------------------------- | ----------- | ------------ |
> | {@{Wages payable}@}                                     | {@{9 600}@} |              |
> | {@{Salaries and wages expense}@}                        | {@{1 200}@} |              |
> | {@{Cash}@}                                              |             | {@{10 800}@} |
>
>
> *Explanation.* Liability (9 600) is cleared; {@{remainder (1 200) is expense at current rate}@}.

---

Flashcards for this section are as follows:

- compensated absence: journal entry when vacation is paid (current rate > accrued rate)? ::@:: Dr Wages payable (accrued amount), Dr Salaries and wages expense (difference to current rate), Cr Cash (total paid).
- vacation pay paid: Wages payable 9 600, pay 20 weeks at 540/week—entry? ::@:: Dr Wages payable 9 600, Dr Salaries and wages expense 1 200, Cr Cash 10 800.

## warranty provision (assurance type)

At the end of the reporting period, the entity estimates the future warranty cost arising from current-year sales and recognizes expense and a provision (matching concept). Only the estimated future amount is recorded as a provision; costs already incurred in the period are expensed separately (e.g. Dr Warranty expense, Cr Cash, Inventory, or Accrued Payroll).

> *Scenario.* Company sold {@{1 000 machines in 2025; each under one-year warranty. Past experience: warranty cost 200 per unit}@}. Total estimated 200 000; {@{4 000 incurred in 2025; 16 000 estimated for 2026}@}. Record {@{provision at end of 2025}@}.
>
>
> | {@{Recognise warranty expense and provision}@} | Dr           | Cr           |
> | ---------------------------------------------- | ------------ | ------------ |
> | {@{Warranty expense}@}                         | {@{16 000}@} |              |
> | {@{Warranty liability}@}                       |              | {@{16 000}@} |
>
>
> *Explanation.* Total expected cost 200 000; {@{4 000 already incurred (expensed when paid); provision for future claims from 2025 sales = 16 000}@}.

---

Flashcards for this section are as follows:

- warranty provision (assurance): year-end entry? ::@:: Dr Warranty expense, Cr Warranty liability (estimated future cost from current-year sales).
- assurance warranty: total 200 000, 4 000 incurred in year, rest next year—provision amount and entry? ::@:: Provision 16 000; Dr Warranty expense 16 000, Cr Warranty liability 16 000.

## warranty claim (settlement)

When a customer claims under the warranty, the entity settles the obligation by crediting Cash, Inventory, or Accrued Payroll (depending on how the repair is satisfied) and reduces the warranty liability.

> *Scenario.* In 2026 a customer {@{claims warranty; company pays 100 cash to satisfy the claim}@}.
>
>
> | {@{Settle claim; reduce liability}@}      | Dr        | Cr        |
> | ----------------------------------------- | --------- | --------- |
> | {@{Warranty liability}@}                  | {@{100}@} |           |
> | {@{Cash, Inventory, or Accrued Payroll}@} |           | {@{100}@} |
>

---

Flashcards for this section are as follows:

- warranty claim: journal entry when customer claims? ::@:: Dr Warranty liability, Cr Cash, Inventory, or Accrued Payroll (depending on how repair is satisfied).
- warranty claim: pay 100 cash to satisfy claim—entry? ::@:: Dr Warranty liability 100, Cr Cash 100 (or Cr Inventory or Accrued Payroll, as applicable).

## service-type warranty: recording cash as unearned revenue

The product is sold with an assurance-type warranty (handled as above: expense + provision in period of sale). When the customer pays separately for an extended (service-type) warranty, that amount is a separate **performance obligation**: the cash is not earned in the year of sale; it is deferred as unearned warranty revenue and recognized as revenue as the entity satisfies the performance obligation over the service period. In the typical case, that period begins after the assurance-type warranty has expired (see example below).

> *Scenario.* Automobile sold with {@{one-year assurance-type warranty}@}; customer pays {@{900 for an additional three-year warranty (service-type)}@}, covering years 2–4. Total cash {@{30 900; only the 900 is deferred}@}. The 900 will be earned over the three-year service period (after year 1 assurance expires).
>
>
> | {@{Record cash; revenue and unearned warranty}@} | Dr           | Cr           |
> | ------------------------------------------------ | ------------ | ------------ |
> | {@{Cash}@}                                       | {@{30 900}@} |              |
> | {@{Sales revenue}@}                              |              | {@{30 000}@} |
> | {@{Unearned warranty revenue}@}                  |              | {@{900}@}    |
>
>
> *Explanation.* 900 is for the extended (service-type) coverage; {@{revenue is recognized only over the service-type period (e.g. straight-line over years 2–4), after the assurance-type warranty has expired}@}.

---

Flashcards for this section are as follows:

- service-type warranty: initial entry when customer pays for extended warranty? ::@:: Dr Cash, Cr Sales revenue (product), Cr Unearned warranty revenue (warranty amount); revenue recognized as the performance obligation is satisfied over the service period.
- automobile 30 000 + 900 extended warranty (service-type, years 2–4)—entry at sale? ::@:: Dr Cash 30 900, Cr Sales revenue 30 000, Cr Unearned warranty revenue 900.

## service-type warranty: recognizing revenue over time

Revenue from the service-type warranty is recognized as the entity satisfies the **performance obligation** over the service period (e.g. straight-line). In the example below, the service period is the three years after the one-year assurance-type warranty has expired. One year of that service period: recognize one-third of the unearned amount.

> *Scenario.* Unearned warranty revenue {@{900 for three-year service-type warranty (years 2–4)}@}. {@{One year of the service period has passed (e.g. end of year 2); recognize 300 revenue}@}.
>
>
> | {@{Recognise warranty revenue (e.g. straight-line)}@} | Dr        | Cr        |
> | ----------------------------------------------------- | --------- | --------- |
> | {@{Unearned warranty revenue}@}                       | {@{300}@} |           |
> | {@{Warranty revenue}@}                                |           | {@{300}@} |
>
>
> *Explanation.* Straight-line over the 3-year service period: {@{900 ÷ 3}@} = {@{300}@} per year; {@{revenue is earned only during the service-type period (after assurance-type warranty has expired)}@}.

---

Flashcards for this section are as follows:

- service-type warranty: when is revenue recognized? ::@:: As the entity satisfies the performance obligation over the service period (in the typical example, that period begins after the assurance-type warranty has expired).
- service-type warranty: entry as time passes? ::@:: Dr Unearned warranty revenue, Cr Warranty revenue (e.g. straight-line over the service-type term).
- unearned warranty revenue 900, 3-year service period—recognize 1 year—entry? ::@:: Dr Unearned warranty revenue 300, Cr Warranty revenue 300.

## premium liability: provision

The entity estimates the cost of premiums that will be redeemed as a result of current-period sales and recognizes expense and a provision in the period of sale. Net cost per redemption = (cost to provide item − cash received from customer).

> *Scenario.* Company sells cake mix; {@{promotion: 10 box tops plus 1 dollar = one bowl. Bowls cost 2 dollars each, customer pays 1 dollar}@}. Estimate {@{60% of box tops redeemed}@}. {@{In 2025, 300 000 boxes sold; 60 000 box tops redeemed in 2025 (6 000 bowls)}@}. At end of 2025, {@{future redemptions from 2025 sales: 12 000 bowls; net cost 1 per bowl. Provision = 12 000}@}.
>
>
> | {@{Recognise premium expense and provision}@} | Dr           | Cr           |
> | --------------------------------------------- | ------------ | ------------ |
> | {@{Premium expense}@}                         | {@{12 000}@} |              |
> | {@{Premium liability}@}                       |              | {@{12 000}@} |
>
>
> *Explanation.* Future redemptions from 2025 sales: {@{18 000 bowls total (300 000 × 0.60 ÷ 10) − 6 000 already redeemed = 12 000 bowls}@}; net cost 1 per bowl.

---

Flashcards for this section are as follows:

- premium provision: when and what entry? ::@:: At end of period, estimate future redemptions from current-year sales; Dr Premium expense, Cr Premium liability (net cost per redemption × estimated future redemptions).
- premium: net cost per redemption? Given bowl cost 2 and customer pays 1, what is net cost? ::@:: Cost to provide item minus cash received from customer; net cost 1 (e.g. bowl cost 2, customer pays 1 → net cost 1).

## premium redemption

When a customer redeems (e.g. 10 box tops plus 1 dollar for one bowl), the entity receives cash, delivers the premium item from inventory, and reduces the premium liability.

> *Scenario.* Customer {@{redeems 10 box tops and 1 dollar; company gives one bowl (cost 2 dollars)}@}. Cash received {@{1; liability reduced by 1 (net cost)}@}.
>
>
> | {@{Receive cash; reduce liability; give inventory}@} | Dr      | Cr      |
> | ---------------------------------------------------- | ------- | ------- |
> | {@{Cash}@}                                           | {@{1}@} |         |
> | {@{Premium liability}@}                              | {@{1}@} |         |
> | {@{Inventory of premiums}@}                          |         | {@{2}@} |
>
>
> *Explanation.* Cash 1 received; {@{inventory (bowl) 2 given; net cost 1 was already expensed via provision, so Premium liability decreases by 1}@}.

---

Flashcards for this section are as follows:

- premium redemption: entry when customer redeems (e.g. 10 box tops plus 1 for bowl)? ::@:: Dr Cash (from customer), Dr Premium liability, Cr Inventory of premiums (cost of item given).
- premium redemption: receive 1, give bowl cost 2, liability reduced 1 —entry? ::@:: Dr Cash 1, Dr Premium liability 1, Cr Inventory of premiums 2.

## premium expiry (no redemption)

When redemption rights expire (e.g. customers do not redeem by the deadline), the entity removes the remaining premium liability and recognizes revenue (or other income).

> *Scenario.* At end of 2026, {@{5 000 of the premium liability remains; no further redemptions (expired)}@}. Transfer {@{to income}@}.
>
>
> | {@{Remove liability; recognise revenue}@} | Dr          | Cr          |
> | ----------------------------------------- | ----------- | ----------- |
> | {@{Premium liability}@}                   | {@{5 000}@} |             |
> | {@{Premium revenue (or Other income)}@}   |             | {@{5 000}@} |
>
>
> *Explanation.* Obligation no longer exists; {@{previously recognized expense is effectively reversed as revenue}@}.

---

Flashcards for this section are as follows:

- premium expiry: when redemption rights expire, entry? ::@:: Dr Premium liability, Cr Premium revenue (or Other income).
- premium liability 5 000 expires unused—entry? ::@:: Dr Premium liability 5 000, Cr Premium revenue (or Other income) 5 000.

## onerous contract provision

When a contract becomes onerous (unavoidable costs exceed expected benefits), recognize a provision measured at the lower of (1) cost to fulfil and (2) compensation/penalty to exit.

> *Scenario.* Company must keep {@{paying unavoidable contract costs of 200 000}@} (cannot cancel and cannot sublet). Recognise the onerous contract provision.
>
>
> | {@{Recognise onerous contract provision}@} | Dr            | Cr            |
> | ------------------------------------------ | ------------- | ------------- |
> | {@{Loss on onerous contract}@}             | {@{200 000}@} |               |
> | {@{Onerous contract liability}@}           |               | {@{200 000}@} |
>

<!-- markdownlint MD028 -->

> *Scenario.* {@{Same contract}@}, but the company can {@{cancel by paying a penalty of 80 000}@}. Recognise the onerous contract provision.
>
>
> | {@{Recognise onerous contract provision (use lower amount)}@} | Dr           | Cr           |
> | ------------------------------------------------------------- | ------------ | ------------ |
> | {@{Loss on onerous contract}@}                                | {@{80 000}@} |              |
> | {@{Onerous contract liability}@}                              |              | {@{80 000}@} |
>

---

Flashcards for this section are as follows:

- onerous contract provision: entry? ::@:: Dr Loss (onerous contract), Cr Onerous contract liability (amount = lower of fulfilment cost and exit penalty).

## restructuring provision

When a restructuring creates a present obligation (detailed formal plan + valid expectation), recognize a restructuring provision for direct/traceable costs.

> *Scenario.* Company closes {@{a division and communicates the plan to affected parties (valid expectation)}@}. Estimated restructuring costs {@{500 000}@}. Recognise restructuring provision.
>
>
> | {@{Recognise restructuring provision}@} | Dr            | Cr            |
> | --------------------------------------- | ------------- | ------------- |
> | {@{Restructuring expense}@}             | {@{500 000}@} |               |
> | {@{Restructuring liability}@}           |               | {@{500 000}@} |
>

---

Flashcards for this section are as follows:

- restructuring provision: entry? ::@:: Dr Restructuring expense, Cr Restructuring liability (for qualifying direct/traceable costs once obligation exists).

## bond issued at discount (issuance)

When a bond is issued at a discount (market rate > coupon rate), the issuer receives cash less than face value. The course uses the simplified method: record Bonds payable at the amount that will appear on the balance sheet (carrying amount). Alternatively, some texts show Dr Cash, Dr Discount on bonds payable, Cr Bonds payable (face value); be consistent throughout.

> *Scenario.* Company issues {@{5-year bonds, face 100 000, coupon 9%, market 11%; bond price 92 608}@}. Record issuance.
>
>
> | {@{Issue bond at discount (net method)}@} | Dr           | Cr           |
> | ----------------------------------------- | ------------ | ------------ |
> | {@{Cash}@}                                | {@{92 608}@} |              |
> | {@{Bonds payable}@}                       |              | {@{92 608}@} |
>
>
> *Explanation.* Carrying amount equals {@{bond price; the discount (7 392) is not shown in a separate account under the net method but is embedded in Bonds payable}@}. At maturity, Bonds payable is {@{increased by amortization to face value}@}.

---

Flashcards for this section are as follows:

- bond issued at discount: issuance entry (net method)? ::@:: Dr Cash (proceeds), Cr Bonds payable (carrying amount); no separate discount account.
- bond discount: why record at carrying amount (net)? ::@:: So Bonds payable on the balance sheet equals carrying amount; discount is amortized by crediting Bonds payable each interest date.

## bond interest payment (discount amortization)

On each interest payment date, the issuer records interest expense (carrying amount × market rate), the coupon to Interest payable (or Cash if paid same day), and the discount amortization as a credit to Bonds payable. Interest expense > coupon; the difference increases the carrying amount.

> *Scenario.* First interest period: {@{interest expense 10 187, coupon 9 000, discount amortized 1 187}@}. Coupon paid on payment date.
>
>
> | {@{Recognise interest and amortise discount}@} | Dr           | Cr          |
> | ---------------------------------------------- | ------------ | ----------- |
> | {@{Interest expense}@}                         | {@{10 187}@} |             |
> | {@{Interest payable}@}                         |              | {@{9 000}@} |
> | {@{Bonds payable}@}                            |              | {@{1 187}@} |
>
>
> *Explanation.* Interest expense equals {@{carrying amount × market rate and the discount amortized = interest expense − coupon}@}; credit {@{Bonds payable to increase carrying amount toward face value}@}. On payment date: Dr Interest payable 9 000, Cr Cash 9 000.

---

Flashcards for this section are as follows:

- bond (discount): interest date entry? ::@:: Dr Interest expense, Cr Interest payable (coupon), Cr Bonds payable (discount amortized).
- bond discount amortization: how is it recorded? ::@:: Credit Bonds payable (or reduce Discount on bonds payable) each period; amount = interest expense − coupon payment.

## bond issued at premium (issuance)

When a bond is issued at a premium (market rate < coupon rate), the issuer receives cash greater than face value. Record Bonds payable at carrying amount (net method).

> *Scenario.* Company issues {@{5-year bonds, face 100 000, coupon 8% semi-annual, market 6% semi-annual; bond price 108 530}@}. Record issuance.
>
>
> | {@{Issue bond at premium (net method)}@} | Dr            | Cr            |
> | ---------------------------------------- | ------------- | ------------- |
> | {@{Cash}@}                               | {@{108 530}@} |               |
> | {@{Bonds payable}@}                      |               | {@{108 530}@} |
>
>
> *Explanation.* Carrying amount {@{includes the premium at issuance}@}; that premium is amortized by debiting {@{Bonds payable each interest date so the carrying amount decreases to face value at maturity}@}.

---

Flashcards for this section are as follows:

- bond issued at premium: issuance entry (net method)? ::@:: Dr Cash (proceeds), Cr Bonds payable (carrying amount).
- bond premium: how is it removed over time? ::@:: Each interest date, debit Bonds payable (premium amortized = coupon − interest expense); carrying amount decreases to face at maturity.

## bond interest payment (premium amortization)

On each interest payment date with a premium bond, interest expense (carrying × market rate) is less than the coupon. The difference is premium amortization: debit Bonds payable to reduce carrying amount.

> *Scenario.* First semi-annual period: {@{interest expense 3 256, coupon 4 000, premium amortized 744}@}. Cash paid on payment date.
>
>
> | {@{Recognise interest and amortise premium}@} | Dr          | Cr          |
> | --------------------------------------------- | ----------- | ----------- |
> | {@{Interest expense}@}                        | {@{3 256}@} |             |
> | {@{Bonds payable}@}                           | {@{744}@}   |             |
> | {@{Interest payable}@}                        |             | {@{4 000}@} |
>
>
> *Explanation.* Premium amortized equals {@{coupon − interest expense}@}; debit {@{Bonds payable to decrease carrying amount toward face value}@}. On payment date: Dr Interest payable 4 000, Cr Cash 4 000.

---

Flashcards for this section are as follows:

- bond (premium): interest date entry? ::@:: Dr Interest expense, Dr Bonds payable (premium amortized), Cr Interest payable (coupon).
- bond premium amortization: how is it recorded? ::@:: Debit Bonds payable (or Premium on bonds payable) each period; amount = coupon payment − interest expense.

## bond repayment at maturity

At maturity the issuer pays the face value and removes the bond liability. Under the effective interest method, carrying amount equals face value at maturity (discount and premium fully amortized).

> *Scenario.* {@{5-year bond, face 100 000, matures; carrying amount equals face value}@}.
>
>
> | {@{Repay bond at maturity}@} | Dr            | Cr            |
> | ---------------------------- | ------------- | ------------- |
> | {@{Bonds payable}@}          | {@{100 000}@} |               |
> | {@{Cash}@}                   |               | {@{100 000}@} |
>
>
> *Explanation.* Liability is settled and there is {@{no gain or loss if carrying amount equals face value at maturity}@}; in practice, the final period's {@{interest expense and discount or premium amortization may be adjusted slightly to remove any rounding differences so the carrying amount equals the exact face value}@}. If the bond is redeemed or matures between regular interest payment dates, the final cash settlement includes {@{principal plus prorated interest for the partial period up to the redemption/maturity date, with no further coupon on the next scheduled date because the bond no longer exists}@}.

---

Flashcards for this section are as follows:

- bond at maturity: journal entry? ::@:: Dr Bonds payable (face value), Cr Cash.
- bond maturity: why no gain or loss (typical case)? ::@:: Carrying amount has been amortized to face value; payment equals liability.
- bond schedule rounding: where is it fixed? ::@:: In the final period; interest expense and discount/premium amortization may be tweaked slightly so the ending carrying amount equals the exact face value.
- bond redeemed between interest dates: what does the final payment include? ::@:: Principal plus prorated interest for the final partial period up to redemption/maturity; no later coupon payment because the bond has been settled.

## bond interest accrual at year-end (fraction of period)

When the reporting date falls between two coupon payment dates, accrue interest for the elapsed fraction of the period. Prorate both the coupon and the discount or premium amortization (e.g. 2 months of a 6-month period: multiply by 2/6; do not use 2/12 because the period is 6 months).

> *Scenario.* Semi-annual bond; {@{year-end is 2 months into the current 6-month period}@}. Full-period coupon {@{4 000}@}, full-period premium amortization {@{744}@}. Prorate: 2/6.
>
>
> | {@{Accrue interest and premium amortization (2 months of 6)}@} | Dr          | Cr          |
> | -------------------------------------------------------------- | ----------- | ----------- |
> | {@{Interest expense}@}                                         | {@{1 085}@} |             |
> | {@{Bonds payable}@}                                            | {@{248}@}   |             |
> | {@{Interest payable}@}                                         |             | {@{1 333}@} |
>
>
> *Explanation.* Interest payable equals {@{4 000 × 2/6 = 1 333}@}, premium amortized equals {@{744 × 2/6 = 248}@}, and interest expense equals {@{1 333 − 248 = 1 085}@}. For a discount bond, credit Bonds payable (prorated discount amortization) instead of debiting.

---

Flashcards for this section are as follows:

- bond: year-end accrual between payment dates—what to prorate? ::@:: Prorate coupon (to Interest payable) and discount or premium amortization by fraction of period (e.g. months elapsed ÷ 6 for semi-annual).
- semi-annual period: 2 months elapsed—divide by 6 or 12? ::@:: Divide by 6; the coupon period is 6 months, so 2 months = 2/6 of the period.

## bond issued between interest payment dates (par)

When a bond is issued between interest payment dates, the investor pays the issuer the accrued interest from the last payment date up to the issue date. On the next interest payment date, the issuer pays the full-period coupon; the net interest expense for the issuer over the partial period is the portion from issue date to payment date. If the bond remains outstanding until a regular coupon date, the last coupon is a full-period coupon; if the bond is redeemed or matures between coupon dates, the final cash settlement instead includes only prorated interest for the final partial period plus principal. Any small rounding differences in the effective-interest schedule are cleaned up in the final period's interest and amortization.

> *Scenario.* Bond with face {@{100 000}@}, coupon {@{8%}@}, interest paid semi-annually (every 6 months). It is issued {@{4 months after the last interest date}@}. At issuance, investor pays accrued interest for 4 of 6 months: {@{100 000 × 8% × 4/12 = 2 667}@}. On the next interest date, issuer pays full coupon for 6 months: {@{100 000 × 8% × 6/12 = 4 000}@}.
>
>
> | {@{Issue bond at par between interest dates}@} | Dr            | Cr            |
> | ---------------------------------------------- | ------------- | ------------- |
> | {@{Cash}@}                                     | {@{102 667}@} |               |
> | {@{Bonds payable}@}                            |               | {@{100 000}@} |
> | {@{Interest expense}@}                         |               | {@{2 667}@}   |
>
>
>
> | {@{First interest payment after issue}@} | Dr          | Cr          |
> | ---------------------------------------- | ----------- | ----------- |
> | {@{Interest expense}@}                   | {@{4 000}@} |             |
> | {@{Cash}@}                               |             | {@{4 000}@} |
>
>
> *Explanation.* {@{Total interest expense over 2 months (from issue date to payment date) = 4 000 − 2 667 = 1 333 = 100 000 × 8% × 2/12}@}.

---

Flashcards for this section are as follows:

- bond issued between interest dates (par): issuance entry? ::@:: Dr Cash (price + accrued interest), Cr Bonds payable (face or carrying amount), Cr Interest expense (accrued interest from last payment date to issue date).
- bond issued between interest dates: why does investor pay accrued interest? ::@:: So that on the next payment date the investor receives the full coupon, even though they held the bond for only part of the period.
- bond between interest dates (par): when is the final interest paid? ::@:: If the bond remains to a regular coupon date, the last payment includes a full-period coupon plus principal; if it is redeemed between coupon dates, the final payment includes principal plus prorated interest for the final partial period only (no later coupon).

## bond issued between interest payment dates (discount or premium)

If a bond is issued between interest payment dates at a discount or premium, the investor still pays accrued coupon interest to the issuer at issuance, and the bond is recorded at its carrying amount (price excluding accrued interest). On each subsequent interest date, the issuer records interest expense using the effective interest method (carrying amount × market rate × fraction of period), records the full coupon to Interest payable (or Cash), and records discount or premium amortization as the difference. If the bond is redeemed or matures between coupon dates, the final cash settlement includes only prorated interest for the final partial period plus principal; the next scheduled coupon is not paid because the bond has been settled. The final period's interest and amortization may be adjusted slightly for rounding so that the carrying amount equals the exact face value at settlement.

> *Scenario.* Semi-annual bond with face {@{100 000}@}, coupon {@{8%}@}, market rate {@{10%}@}. Issue price (excluding accrued interest) is {@{96 000}@}; bond is issued {@{4 months after the last interest date}@}. At issuance the investor pays accrued coupon for 4 of the 6 months: {@{100 000 × 8% × 4/12 = 2 667}@}.
>
>
> | {@{Issue bond at discount between interest dates}@} | Dr           | Cr           |
> | --------------------------------------------------- | ------------ | ------------ |
> | {@{Cash}@}                                          | {@{98 667}@} |              |
> | {@{Bonds payable}@}                                 |              | {@{96 000}@} |
> | {@{Interest expense}@}                              |              | {@{2 667}@}  |
>
>
> *Next interest date (2 months of the 6-month period for this holder).* Carrying amount at issue is {@{96 000}@}. Interest expense for 2 months = {@{96 000 × 10% × 2/12 = 1 600}@}. Full 6‑month coupon = {@{100 000 × 8% × 6/12 = 4 000}@}. Discount amortized for this 2‑month holding period = {@{(4 000 − 2 667) − 1 600 = (1 333 − 1 600) = −267}@}; in practice you would use the full schedule and adjust the final period for rounding.
>
>
> | {@{First interest date (conceptual)}@}              | Dr          | Cr                |
> | --------------------------------------------------- | ----------- | ----------------- |
> | {@{Interest expense}@}                              | {@{1 600}@} |                   |
> | {@{Interest payable}@}                              |             | {@{4 000}@}       |
> | {@{Bonds payable (discount/premium amortization)}@} |             | {@{(balancing)}@} |
>
>
> *Explanation.* Accrued interest at issue always uses {@{the coupon (stated) rate and the time since the last payment date}@}; discount/premium amortization still follows the {@{effective interest method using the market rate and the carrying amount, with any rounding absorbed in the final period}@}.

---

Flashcards for this section are as follows:

- bond between interest dates (discount/premium): what does investor pay at issue? ::@:: Price for the bond (carrying amount) plus accrued coupon interest from last payment date to issue date (based on coupon rate).
- bond between interest dates (discount/premium): how is interest recorded after issue? ::@:: Use effective interest method: Dr Interest expense (carrying × market × fraction of period), Cr Interest payable (full coupon), and adjust Bonds payable for discount or premium amortization; clean up rounding in the final period so carrying equals face value.
- bond between interest dates (discount/premium): final interest when redeemed between coupon dates? ::@:: Pay principal plus prorated interest for the final partial period only; the next scheduled full coupon is not paid because the bond has been settled.

## zero-interest-bearing note: issuance and interest

A zero-interest-bearing (implicit-interest) note has no periodic cash interest payments; the borrower receives cash below face and repays the full face at maturity. Interest expense is recognized by amortizing the discount using the implicit rate.

> *Scenario.* Company issues {@{3-year zero-interest-bearing note with face 10 000}@}; receives cash {@{7 721}@}. Implicit interest rate is {@{9%}@} (so that {@{10 000}@} discounted at 9% for 3 years equals {@{7 721}@}).
>
>
> | {@{Issue zero-interest-bearing note}@} | Dr          | Cr          |
> | -------------------------------------- | ----------- | ----------- |
> | {@{Cash}@}                             | {@{7 721}@} |             |
> | {@{Notes payable}@}                    |             | {@{7 721}@} |
>
>
> *Year 1 (no cash interest paid; discount amortization only).* Carrying amount at start of year 1 is {@{7 721}@}. Interest expense = {@{7 721 × 9% = 695}@}.
>
>
> | {@{Accrue implicit interest (year 1)}@} | Dr        | Cr        |
> | --------------------------------------- | --------- | --------- |
> | {@{Interest expense}@}                  | {@{695}@} |           |
> | {@{Notes payable}@}                     |           | {@{695}@} |
>
>
> *Explanation.* Over time, {@{Notes payable increases each year by the interest expense so that the carrying amount grows from 7 721 to 10 000 by maturity}@}; at maturity the entry is {@{Dr Notes payable 10 000, Cr Cash 10 000}@}.

---

Flashcards for this section are as follows:

- zero-interest-bearing note: issuance entry? ::@:: Dr Cash (present value received), Cr Notes payable (present value); no separate discount account under net method.
- zero-interest-bearing note: how is interest expense recorded? ::@:: Each period, Dr Interest expense, Cr Notes payable using the implicit interest rate; carrying amount increases to face value.

## interest-bearing long-term note issued at discount

An interest-bearing long-term note can also be issued at a discount (stated rate below market). The borrower records the note at its present value and uses the effective interest method to amortize the discount.

> *Scenario.* Company issues {@{3-year note with face 10 000}@}, stated interest {@{8%}@} annually, market rate {@{10%}@}. Present value (issue price) is {@{9 510}@} (rounded).
>
>
> | {@{Issue interest-bearing note at discount}@} | Dr          | Cr          |
> | --------------------------------------------- | ----------- | ----------- |
> | {@{Cash}@}                                    | {@{9 510}@} |             |
> | {@{Notes payable}@}                           |             | {@{9 510}@} |
>
>
> *First year interest.* Carrying amount at start of year 1 is {@{9 510}@}. Interest expense = {@{9 510 × 10% = 951}@}. Cash interest paid = {@{10 000 × 8% = 800}@}. Discount amortized = {@{151}@}.
>
>
> | {@{Year 1 interest: cash and discount amortization}@} | Dr        | Cr        |
> | ----------------------------------------------------- | --------- | --------- |
> | {@{Interest expense}@}                                | {@{951}@} |           |
> | {@{Cash}@}                                            |           | {@{800}@} |
> | {@{Notes payable}@}                                   |           | {@{151}@} |
>

---

Flashcards for this section are as follows:

- interest-bearing note at discount: issuance entry (net)? ::@:: Dr Cash (present value), Cr Notes payable (present value).
- interest-bearing note at discount: first-year interest entry? ::@:: Dr Interest expense (carrying × market), Cr Cash (face × stated), Cr Notes payable (discount amortized).

## note issued for noncash asset (fair value known)

When a note is issued for a noncash asset and the asset's fair value is known, measure both the asset and the note at that fair value.

> *Scenario.* Company buys land and gives a {@{5-year, zero-interest-bearing note with face 220 000}@}. Land's cash selling price is {@{200 000}@}. Record the transaction in the buyer's books.
>
>
> | {@{Acquire land by issuing note (fair value known)}@} | Dr            | Cr            |
> | ----------------------------------------------------- | ------------- | ------------- |
> | {@{Land}@}                                            | {@{200 000}@} |               |
> | {@{Notes payable}@}                                   |               | {@{200 000}@} |
>
>
> *Explanation.* Land is recorded at {@{fair value (its cash selling price) and the note payable is recorded at the same present value}@}; the difference between {@{220 000 face and 200 000 present value is a discount that will be amortized over the note's life}@}.

---

Flashcards for this section are as follows:

- note for noncash asset (fair value known): entry? ::@:: Dr Asset (fair value), Cr Notes payable (same fair value/present value).

## note issued for noncash asset (fair value unknown; use present value)

If the fair value of the noncash asset or service is not observable, use discounted cash flows to determine the present value of the note and use that amount to measure both the asset and the note.

> *Scenario.* Company receives architectural services in exchange for a {@{5-year note with face 200 000}@} and no stated interest. No market price is available for the services, but an appropriate discount rate (after considering prime rate, covenants, collateral, and term) is {@{8%}@}. Present value of the note (discounted at 8%) is {@{136 000}@} (rounded).
>
>
> | {@{Record architectural services and note (use present value)}@} | Dr            | Cr            |
> | ---------------------------------------------------------------- | ------------- | ------------- |
> | {@{Construction in progress (or Building)}@}                     | {@{136 000}@} |               |
> | {@{Notes payable}@}                                              |               | {@{136 000}@} |
>

---

Flashcards for this section are as follows:

- noncash note: fair value unknown—what amount to record? ::@:: Use present value of the note (discounted cash flows at an appropriate rate) for both the asset and the note payable.

## extinguishment of debt with cash (bond repurchase)

When debt is retired early by paying cash, compare the cash paid with the carrying amount of the liability to determine a gain or loss on extinguishment.

> *Scenario.* Bond has carrying amount {@{95 000}@}. The issuer repurchases it for {@{101 000}@} (101% of 100 000 face). Record the extinguishment.
>
>
> | {@{Repurchase bond above carrying amount}@} | Dr           | Cr            |
> | ------------------------------------------- | ------------ | ------------- |
> | {@{Bonds payable}@}                         | {@{95 000}@} |               |
> | {@{Loss on extinguishment of debt}@}        | {@{6 000}@}  |               |
> | {@{Cash}@}                                  |              | {@{101 000}@} |
>
>
> *Explanation.* The loss equals {@{cash paid 101 000 − carrying amount 95 000 = 6 000}@}. If cash paid were less than carrying amount, the difference would instead be a gain.

---

Flashcards for this section are as follows:

- early extinguishment of debt with cash: how to find gain or loss? ::@:: Compare cash paid with carrying amount; cash > carrying → loss, cash < carrying → gain.

## extinguishment of debt by issuing shares

When a note or bond payable is settled by issuing the company's own shares (debt-for-equity swap), the liability is extinguished and equity increases instead of cash being paid. Measure the consideration at the fair value of the shares issued when that is reliably determinable; otherwise use the fair value or present value of the liability's remaining cash flows. Recognise any difference between the liability's carrying amount and the consideration as a gain or loss on extinguishment.

> *Scenario.* Note payable has carrying amount {@{20 000 000}@}. The lender agrees to accept {@{2 000 000 ordinary shares with par 5}@} to settle the note. On the issue date, the shares trade at {@{8}@} per share (fair value {@{16 000 000}@}). Record the settlement.
>
>
> | {@{Settle note payable by issuing shares (debt-for-equity)}@} | Dr               | Cr               |
> | ------------------------------------------------------------- | ---------------- | ---------------- |
> | {@{Notes payable}@}                                           | {@{20 000 000}@} |                  |
> | {@{Gain on extinguishment of debt}@}                          |                  | {@{4 000 000}@}  |
> | {@{Share capital — ordinary (par 5)}@}                        |                  | {@{10 000 000}@} |
> | {@{Share premium — ordinary}@}                                |                  | {@{6 000 000}@}  |
>
>
> *Explanation.* Shares are measured at fair value {@{16 000 000 (2 000 000 × 8)}@}; equity increases by that amount (par {@{10 000 000}@}, premium {@{6 000 000}@}). The liability's carrying amount exceeds consideration, so the debtor recognises a gain on extinguishment of {@{20 000 000 − 16 000 000 = 4 000 000}@}.

---

Flashcards for this section are as follows:

- debt settled by issuing shares: basic journal entry ::@:: Dr Notes/Bonds payable (carrying amount), Dr/Cr Gain or Loss on extinguishment (for the difference), Cr Share capital (par) and Cr Share premium (issue proceeds in excess of par) based on fair value of shares issued.
- debt-for-equity swap: how to measure consideration? ::@:: Use the fair value of the shares issued when available; if not, use the fair value or present value of the liability's remaining cash flows.

## extinguishment of debt by transferring property

If debt is settled by transferring a noncash asset (e.g. land or a building), there are two effects: (1) gain or loss on the asset (remeasure asset to fair value), and (2) gain or loss on extinguishment (compare liability's carrying amount to the asset's fair value).

> *Scenario.* Debtor has a building with carrying amount {@{21 000 000}@} and fair value {@{16 000 000}@}. A note payable has carrying amount {@{20 000 000}@}. The lender agrees to accept the building in full settlement of the note.
>
>
> | {@{Remeasure building to fair value}@} | Dr              | Cr              |
> | -------------------------------------- | --------------- | --------------- |
> | {@{Loss on disposal of building}@}     | {@{5 000 000}@} |                 |
> | {@{Building}@}                         |                 | {@{5 000 000}@} |
>
>
>
> | {@{Settle note payable by transferring building}@} | Dr               | Cr               |
> | -------------------------------------------------- | ---------------- | ---------------- |
> | {@{Notes payable}@}                                | {@{20 000 000}@} |                  |
> | {@{Building}@}                                     |                  | {@{16 000 000}@} |
> | {@{Gain on extinguishment of debt}@}               |                  | {@{4 000 000}@}  |
>
>
> *Explanation.* The asset loss equals {@{21 000 000 − 16 000 000 = 5 000 000}@}, and the extinguishment gain equals {@{liability 20 000 000 − asset fair value 16 000 000 = 4 000 000}@}; the two effects are reported separately.

---

Flashcards for this section are as follows:

- extinguishment by transferring property: why two gains/losses? ::@:: One from remeasuring the asset to fair value; another from comparing liability carrying amount to asset fair value when settling the debt.

## modification of debt terms (debtor)

When the borrower and lender agree to change the terms of a long-term liability (e.g. reduce principal, extend maturity, or lower the interest rate) because the borrower is in financial difficulty, IFRS treats a significant restructuring as an **extinguishment** of the old debt and recognition of a **new** note at fair value.

> *Scenario (based on lecture slide).* On December 31, 2025, a company has a loan with carrying amount {@{10 500 000}@}. The lender agrees to restructure it by reducing principal, extending maturity, and lowering the stated interest rate. The fair value of the restructured note (based on a current market borrowing rate of 15%) is {@{7 201 336}@}. Record the modification in the debtor's books.
>
>
> | {@{Record extinguishment and new restructured note}@} | Dr               | Cr              |
> | ----------------------------------------------------- | ---------------- | --------------- |
> | {@{Notes payable (old)}@}                             | {@{10 500 000}@} |                 |
> | {@{Gain on extinguishment of debt}@}                  |                  | {@{3 298 664}@} |
> | {@{Notes payable (new)}@}                             |                  | {@{7 201 336}@} |
>
>
> *Explanation.* The gain on extinguishment equals {@{old carrying amount 10 500 000 − fair value of new note 7 201 336 = 3 298 664}@}. After this entry, the new note {@{with initial carrying amount 7 201 336 is amortized using the new effective interest rate (15%), with interest expense recognised at 15%}@} and the difference between {@{interest expense and cash interest treated as discount amortization each period}@}.

---

Flashcards for this section are as follows:

- modification of debt terms (debtor, lecture slide) ::@:: Derecognise the old note at its carrying amount, recognise the new restructured note at fair value, and record the difference as a gain or loss on extinguishment of debt.
- modification of debt terms (debtor): numerical gain in slide example? ::@:: Old carrying amount 10 500 000 minus fair value of new note 7 201 336; gain = 3 298 664.

## issuing ordinary shares for non-cash consideration (patent)

When ordinary shares are issued in exchange for a patent or other non-cash asset, the transaction is measured at fair value. The journal entry always debits the asset (e.g. Patents) and credits Share capital at par plus Share premium for the excess over par. The fair value hierarchy is: (1) fair value of goods/services received; (2) fair value of shares issued; (3) discounted cash flows.

> *Scenario 1.* Company issues {@{10 000 ordinary shares, par 10}@} in exchange for a patent. The fair value of the patent is not reliably known, but the shares trade at {@{140 000}@}.
>
>
> | {@{Issue ordinary shares for patent (measure at share fair value)}@} | Dr            | Cr            |
> | -------------------------------------------------------------------- | ------------- | ------------- |
> | {@{Patents}@}                                                        | {@{140 000}@} |               |
> | {@{Share capital — ordinary (10 000 × 10)}@}                         |               | {@{100 000}@} |
> | {@{Share premium — ordinary}@}                                       |               | {@{40 000}@}  |
>

<!-- markdownlint MD028 -->

> *Scenario 2.* Fair value of the shares is not known, but the patent's fair value is {@{150 000}@}.
>
>
> | {@{Issue ordinary shares for patent (measure at patent fair value)}@} | Dr            | Cr            |
> | --------------------------------------------------------------------- | ------------- | ------------- |
> | {@{Patents}@}                                                         | {@{150 000}@} |               |
> | {@{Share capital — ordinary (10 000 × 10)}@}                          |               | {@{100 000}@} |
> | {@{Share premium — ordinary}@}                                        |               | {@{50 000}@}  |
>

<!-- markdownlint MD028 -->

> *Scenario 3.* Neither share nor patent fair value is observable; an independent consultant values the patent at {@{125 000}@} based on discounted expected cash flows.
>
>
> | {@{Issue ordinary shares for patent (measure at DCF value)}@} | Dr            | Cr            |
> | ------------------------------------------------------------- | ------------- | ------------- |
> | {@{Patents}@}                                                 | {@{125 000}@} |               |
> | {@{Share capital — ordinary (10 000 × 10)}@}                  |               | {@{100 000}@} |
> | {@{Share premium — ordinary}@}                                |               | {@{25 000}@}  |
>
>
> *Explanation.* In each case, the asset is recorded at its measured fair value and equity is credited for the same amount (par plus premium); only the measurement basis (shares, patent, or discounted cash flows) changes.

---

Flashcards for this section are as follows:

- non-cash share issue (patent): general entry structure ::@:: Dr Patents (or other asset) at fair value; Cr Share capital — ordinary at par; Cr Share premium — ordinary for the excess over par.
- non-cash share issue: measurement hierarchy in examples ::@:: Use (1) fair value of goods/services received, (2) if unavailable, fair value of shares issued, and (3) if neither is observable, discounted cash flow value of the asset/service.
- non-cash share issue example (Scenario 1): patent for 10 000 shares, share FV 140 000, par 10—entry? ::@:: Dr Patents 140 000; Cr Share capital — ordinary 100 000; Cr Share premium — ordinary 40 000.
- non-cash share issue example (Scenario 2): patent FV 150 000 for 10 000 shares, par 10—entry? ::@:: Dr Patents 150 000; Cr Share capital — ordinary 100 000; Cr Share premium — ordinary 50 000.
- non-cash share issue example (Scenario 3): patent DCF value 125 000 for 10 000 shares, par 10—entry? ::@:: Dr Patents 125 000; Cr Share capital — ordinary 100 000; Cr Share premium — ordinary 25 000.

## issuing ordinary shares for cash with share issue costs

Direct share issue costs (e.g. underwriting fees) reduce the proceeds credited to equity, not profit or loss. The slide example uses the net approach.

> *Scenario.* Company issues {@{300 000 ordinary shares at 3 per share}@}; par value is {@{1 per share}@}. Underwriting costs are {@{20 000}@}. Net cash received is {@{880 000}@}.
>
>
> | {@{Issue ordinary shares for cash (net of underwriting costs)}@} | Dr            | Cr            |
> | ---------------------------------------------------------------- | ------------- | ------------- |
> | {@{Cash}@}                                                       | {@{880 000}@} |               |
> | {@{Share capital — ordinary (300 000 × 1)}@}                     |               | {@{300 000}@} |
> | {@{Share premium — ordinary}@}                                   |               | {@{580 000}@} |
>
>
> *Explanation.* Gross proceeds are {@{900 000 (300 000 × 3)}@}; underwriting costs of {@{20 000}@} reduce the amount credited to equity, so only {@{880 000}@} is recorded in Cash and Share premium is {@{580 000}@} instead of {@{600 000}@}.

---

Flashcards for this section are as follows:

- share issue with underwriting costs: equity effect (net method) ::@:: Record Cash net of direct share issue costs; Cr Share capital at par and Cr Share premium for the remaining net proceeds; do not expense underwriting costs.
- share issue with underwriting costs: numbers in example? ::@:: Gross proceeds 900 000 (300 000 × 3), underwriting costs 20 000, net cash 880 000, Share premium — ordinary 580 000.

## issuing preference shares for cash

When preference shares are issued for cash, the journal entry mirrors that for ordinary shares: debit Cash and credit Share capital — preference at par plus Share premium — preference for the excess.

> *Scenario.* Company issues {@{10 000 preference shares, par 10, for 12 cash per share}@}.
>
>
> | {@{Issue preference shares for cash}@}         | Dr            | Cr            |
> | ---------------------------------------------- | ------------- | ------------- |
> | {@{Cash}@}                                     | {@{120 000}@} |               |
> | {@{Share capital — preference (10 000 × 10)}@} |               | {@{100 000}@} |
> | {@{Share premium — preference}@}               |               | {@{20 000}@}  |
>

---

Flashcards for this section are as follows:

- issuance of preference shares for cash: basic entry ::@:: Dr Cash (issue price × number of shares), Cr Share capital — preference at par, Cr Share premium — preference for the excess over par.
- issuance of 10 000 preference shares, par 10, at 12—entry? ::@:: Dr Cash 120 000; Cr Share capital — preference 100 000; Cr Share premium — preference 20 000.

## cash dividend on ordinary shares

Cash dividends on ordinary shares are recorded in two stages: (1) declaration (create a liability) and (2) payment. There is no entry on the date of record. Companies do not declare or pay cash dividends on treasury shares.

> *Scenario.* On June 10, Roadway Freight Corp. declares a cash dividend of {@{0.50 per share on 1.8 million ordinary shares}@}, payable July 16 to shareholders of record June 24. Total dividend is {@{900 000}@}.
>
>
> | {@{At date of declaration (June 10)}@}            | Dr            | Cr            |
> | ------------------------------------------------- | ------------- | ------------- |
> | {@{Retained earnings (Cash dividends declared)}@} | {@{900 000}@} |               |
> | {@{Dividends payable}@}                           |               | {@{900 000}@} |
>
>
>
> | {@{At date of record (June 24)}@} | Dr  | Cr  |
> | --------------------------------- | --- | --- |
> | {@{No entry}@}                    |     |     |
>
>
>
> | {@{At date of payment (July 16)}@} | Dr            | Cr            |
> | ---------------------------------- | ------------- | ------------- |
> | {@{Dividends payable}@}            | {@{900 000}@} |               |
> | {@{Cash}@}                         |               | {@{900 000}@} |
>

---

Flashcards for this section are as follows:

- cash dividend on ordinary shares: key dates and entries ::@:: Date of declaration: Dr Retained earnings, Cr Dividends payable; date of record: no entry; date of payment: Dr Dividends payable, Cr Cash.
- Roadway cash dividend example: 0.50 on 1.8 million shares—amount and declaration entry? ::@:: Amount 900 000; Dr Retained earnings (Cash dividends declared) 900 000, Cr Dividends payable 900 000.

## property dividend (non-cash asset)

Property dividends are dividends payable in assets other than cash (e.g. investments). The asset to be distributed is first remeasured to fair value at the declaration date (recognising any unrealised gain or loss), then the property dividend is recorded at fair value.

> *Scenario.* Tsen Ltd. transfers to shareholders some of its investments in securities, with carrying amount {@{1 250 000}@}. On December 28, 2024, it declares a property dividend to shareholders of record January 15, 2025, to be distributed January 30, 2025. At the declaration date, the investments have fair value {@{2 000 000}@}.
>
>
> | {@{At date of declaration (remeasure and declare dividend)}@} | Dr              | Cr              |
> | ------------------------------------------------------------- | --------------- | --------------- |
> | {@{Equity investments}@}                                      | {@{750 000}@}   |                 |
> | {@{Unrealised holding gain or loss — income}@}                |                 | {@{750 000}@}   |
> | {@{Retained earnings (Property dividends declared)}@}         | {@{2 000 000}@} |                 |
> | {@{Property dividends payable}@}                              |                 | {@{2 000 000}@} |
>
>
>
> | {@{At date of distribution (January 30, 2025)}@} | Dr              | Cr              |
> | ------------------------------------------------ | --------------- | --------------- |
> | {@{Property dividends payable}@}                 | {@{2 000 000}@} |                 |
> | {@{Equity investments}@}                         |                 | {@{2 000 000}@} |
>

---

Flashcards for this section are as follows:

- property dividend: two journal steps ::@:: First remeasure asset to fair value and recognise unrealised gain or loss; then Dr Retained earnings and Cr Property dividends payable at fair value, followed by Dr Property dividends payable and Cr Asset on distribution.
- Tsen property dividend example: FV 2 000 000, CV 1 250 000—remeasurement entry? ::@:: Dr Equity investments 750 000, Cr Unrealised holding gain or loss — income 750 000.

## liquidating dividend

Liquidating dividends are dividends not based on earnings; they represent a return of capital. The dividend announcement should disclose which portion is income and which portion is a return of capital. In journal entries, the income portion reduces Retained earnings and the capital portion reduces contributed capital (e.g. Share premium).

> *Scenario.* McChesney Mines issues a dividend to ordinary shareholders of {@{1 200 000}@}. The announcement states that {@{900 000}@} is income and {@{300 000}@} is a return of capital.
>
>
> | {@{At date of declaration}@}   | Dr            | Cr              |
> | ------------------------------ | ------------- | --------------- |
> | {@{Retained earnings}@}        | {@{900 000}@} |                 |
> | {@{Share premium — ordinary}@} | {@{300 000}@} |                 |
> | {@{Dividends payable}@}        |               | {@{1 200 000}@} |
>
>
>
> | {@{At date of payment}@} | Dr              | Cr              |
> | ------------------------ | --------------- | --------------- |
> | {@{Dividends payable}@}  | {@{1 200 000}@} |                 |
> | {@{Cash}@}               |                 | {@{1 200 000}@} |
>

---

Flashcards for this section are as follows:

- liquidating dividend: how to split between income and capital? ::@:: Dr Retained earnings for the income portion and Dr Share premium (then Share capital if needed) for the capital portion; Cr Dividends payable for the total.
- McChesney liquidating dividend example: 1 200 000 total (900 000 income, 300 000 capital)—declaration entry? ::@:: Dr Retained earnings 900 000, Dr Share premium — ordinary 300 000, Cr Dividends payable 1 200 000.

## share dividend on ordinary shares

Share dividends are pro rata issues of the company's own shares to existing shareholders without receiving consideration. In this course, small share dividends are recorded at par value. There are two entries: declaration (reclassification within equity) and distribution (issue of shares).

> *Scenario.* Vine plc has {@{100 000 ordinary shares, par 1}@}, retained earnings {@{50 000}@}, and declares a {@{10% share dividend}@}. It issues {@{10 000 additional shares}@}. Fair value at the time is {@{8 per share}@}, but the entry uses par value.
>
>
> | {@{At date of declaration (10% share dividend)}@} | Dr           | Cr           |
> | ------------------------------------------------- | ------------ | ------------ |
> | {@{Retained earnings (Share dividend declared)}@} | {@{10 000}@} |              |
> | {@{Ordinary share dividend distributable}@}       |              | {@{10 000}@} |
>
>
>
> | {@{At date of distribution}@}               | Dr           | Cr           |
> | ------------------------------------------- | ------------ | ------------ |
> | {@{Ordinary share dividend distributable}@} | {@{10 000}@} |              |
> | {@{Share capital — ordinary}@}              |              | {@{10 000}@} |
>

---

Flashcards for this section are as follows:

- share dividend (small): declaration and distribution entries ::@:: Declaration: Dr Retained earnings, Cr Ordinary share dividend distributable (at par); distribution: Dr Ordinary share dividend distributable, Cr Share capital — ordinary.
- Vine share dividend example: 10% on 100 000 shares, par 1—declaration entry? ::@:: Dr Retained earnings 10 000, Cr Ordinary share dividend distributable 10 000.

## preference share dividends: four patterns

Preference dividends can have different patterns depending on whether the shares are cumulative and/or participating. The slide example uses:

- Ordinary shares: par {@{400 000}@}.
- Preference shares: par {@{100 000}@}, dividend rate {@{6%}@}.
- Total dividend for the year: {@{50 000}@}.

Let "6% of par" denote {@{6 000}@} for preference (6% × 100 000) and {@{24 000}@} for ordinary (6% × 400 000).

---

### 1. Non-cumulative, non-participating preference shares (regular)

Preference shareholders receive only the current year's preference dividend; the remainder goes to ordinary shareholders.

> *Allocation.* Preference dividend {@{6 000 (6% × 100 000)}@}; ordinary dividend {@{44 000 (50 000 − 6 000)}@}.
>
>
> | {@{Declare dividend (non-cumulative, non-participating)}@} | Dr           | Cr           |
> | ---------------------------------------------------------- | ------------ | ------------ |
> | {@{Retained earnings}@}                                    | {@{50 000}@} |              |
> | {@{Dividends payable — preference}@}                       |              | {@{6 000}@}  |
> | {@{Dividends payable — ordinary}@}                         |              | {@{44 000}@} |
>

---

Flashcards for this section are as follows:

- non-cumulative, non-participating preference shares: allocation in example ::@:: Out of a 50 000 dividend, preference receives 6 000 (6% × 100 000) and ordinary receives 44 000.

### 2. Cumulative, non-participating preference shares

Assume dividends were omitted for the past two years. Cumulative preference shareholders must receive all arrears plus the current year's preference dividend before any ordinary dividend is paid.

> *Allocation.* Arrears {@{2 years × 6 000 = 12 000}@} plus current year {@{6 000}@} gives preference dividend {@{18 000}@}; ordinary dividend is {@{32 000 (50 000 − 18 000)}@}.
>
>
> | {@{Declare dividend (cumulative, non-participating)}@} | Dr           | Cr           |
> | ------------------------------------------------------ | ------------ | ------------ |
> | {@{Retained earnings}@}                                | {@{50 000}@} |              |
> | {@{Dividends payable — preference}@}                   |              | {@{18 000}@} |
> | {@{Dividends payable — ordinary}@}                     |              | {@{32 000}@} |
>

---

Flashcards for this section are as follows:

- cumulative, non-participating preference shares: allocation in example ::@:: With two years of arrears, preference receives 18 000 in total (12 000 arrears + 6 000 current) and ordinary receives 32 000 out of a 50 000 dividend.

> *Note on dividends in arrears.* Even for cumulative preference shares, {@{no liability is recorded for dividends in arrears until the board declares a dividend}@}; the arrears are {@{disclosed in the notes to the financial statements, not recognised as Dividends payable}@} until declaration.

### 3. Non-cumulative, participating preference shares

Preference shareholders first receive their 6% preference dividend; ordinary shareholders receive a matching 6% on their par value. Any remaining dividend is shared between preference and ordinary shareholders in proportion to par value.

> *Step 1 (6% on both classes).* Preference {@{6 000}@}; ordinary {@{24 000}@}. Remaining dividend {@{50 000 − (6 000 + 24 000) = 20 000}@}.
>
> *Step 2 (share remaining 20 000 based on par).* Total par {@{100 000 + 400 000 = 500 000}@}; preference share {@{100 000 ÷ 500 000 = 20% → 4 000}@}; ordinary share {@{400 000 ÷ 500 000 = 80% → 16 000}@}.
>
> *Final allocation.* Preference dividend {@{6 000 + 4 000 = 10 000}@}; ordinary dividend {@{24 000 + 16 000 = 40 000}@}.
>
>
> | {@{Declare dividend (non-cumulative, participating)}@} | Dr           | Cr           |
> | ------------------------------------------------------ | ------------ | ------------ |
> | {@{Retained earnings}@}                                | {@{50 000}@} |              |
> | {@{Dividends payable — preference}@}                   |              | {@{10 000}@} |
> | {@{Dividends payable — ordinary}@}                     |              | {@{40 000}@} |
>

---

Flashcards for this section are as follows:

- non-cumulative, participating preference shares: allocation in example ::@:: Step 1 gives 6 000 to preference and 24 000 to ordinary; Step 2 splits the remaining 20 000 as 4 000 to preference and 16 000 to ordinary, so totals are 10 000 and 40 000 respectively.

### 4. Cumulative, participating preference shares

Combine the cumulative feature (pay arrears first) and the participating feature (share in extra dividends). For example, with two years of arrears:

> *Step 1 (arrears and current preference dividend).* Arrears {@{12 000}@} and current year {@{6 000}@} give preference total before participation {@{18 000}@}.
>
> *Step 2 (match 6% on ordinary for current year).* Ordinary receives {@{24 000}@}.
>
> Remaining dividend after Step 1 and Step 2 is {@{50 000 − (18 000 + 24 000) = 8 000}@}.
>
> *Step 3 (share remaining 8 000 based on par).* Preference {@{20% × 8 000 = 1 600}@}; ordinary {@{80% × 8 000 = 6 400}@}.
>
> *Final allocation.* Preference dividend {@{18 000 + 1 600 = 19 600}@}; ordinary dividend {@{24 000 + 6 400 = 30 400}@}.
>
>
> | {@{Declare dividend (cumulative, participating)}@} | Dr           | Cr           |
> | -------------------------------------------------- | ------------ | ------------ |
> | {@{Retained earnings}@}                            | {@{50 000}@} |              |
> | {@{Dividends payable — preference}@}               |              | {@{19 600}@} |
> | {@{Dividends payable — ordinary}@}                 |              | {@{30 400}@} |
>

---

Flashcards for this section are as follows:

- preference dividends: four patterns overview ::@:: Non-cumulative/non-participating, cumulative/non-participating, non-cumulative/participating, cumulative/participating—each changes how total dividends are allocated between preference and ordinary shareholders.
- cumulative preference shares: what are dividends in arrears? ::@:: Unpaid preference dividends from prior years that must be paid before any ordinary dividend when dividends resume.
- participating preference shares: how are extra dividends shared? ::@:: After each class receives its stated dividend (and arrears for cumulative), any remaining dividend is shared between preference and ordinary shareholders, usually in proportion to par value.
- preference dividend allocation example (non-cumulative, participating): totals? ::@:: Preference receives 10 000 (6 000 + 4 000) and ordinary receives 40 000 (24 000 + 16 000) out of a 50 000 total dividend.
