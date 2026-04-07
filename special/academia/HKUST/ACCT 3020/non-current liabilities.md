---
aliases:
  - long-term liabilities
  - long-term liability
  - non-current liabilities
  - non-current liability
tags:
  - flashcard/active/special/academia/HKUST/ACCT_3020/non-current_liabilities
  - language/in/English
---

# non-current liabilities

This note covers non-current (long-term) liabilities in ACCT 3020: bond and note fundamentals (indenture, face value, coupon/stated rate vs market/effective rate, par/discount/premium pricing); detailed journal entries for the effective interest method (discount and premium amortization, year-end accruals, bonds issued between payment dates); long-term notes payable (interest-bearing notes at discount, zero-interest-bearing notes, notes issued for noncash assets); and extinguishment and modification of debt (cash repurchase, equity/property exchange, and debtor-side accounting for modified terms).

## definition and classification

Non-current liabilities (long-term liabilities) are obligations expected to be settled more than 12 months after the reporting date. In this course, classification uses the 12-month criterion (operating cycle is not emphasized for long-term liabilities). Examples include mortgages and other long-term loans.

---

Flashcards for this section are as follows:

- non-current (long-term) liability ::@:: Obligation expected to be settled more than 12 months after the reporting date (e.g. mortgage, long-term loan).
- long-term liabilities classification criterion (course) ::@:: Use the 12-month rule (more than 12 months after reporting date); operating cycle is not emphasized for long-term liabilities.

## covenants and restrictions

Long-term debt agreements often contain covenants (restrictions) that limit what the company can do (e.g. restricting dividends). The purpose is to protect creditors: if the company pays out too much to shareholders, it may not have enough resources to repay debt.

---

Flashcards for this section are as follows:

- debt covenants ::@:: Restrictions in debt agreements (e.g. limits on dividends) designed to protect creditors and reduce default risk.
- why do lenders restrict dividends? ::@:: To prevent the company from paying out cash to shareholders that would reduce its ability to repay creditors.

## bonds: overview and key terms

A bond is a way for a company to borrow money from many investors. The bond contract is the bond indenture, which specifies key terms such as the maturity date, interest payment schedule, and the principal (face value) to be repaid at maturity. A common face value is 1,000 per bond, and interest payments are often semiannual (though annual or quarterly payments can also occur).

---

Flashcards for this section are as follows:

- bond ::@:: A borrowing instrument where a company raises funds from investors and repays principal at maturity with periodic interest payments.
- bond indenture ::@:: The bond contract specifying maturity date, interest payment schedule, and face value (principal) to be repaid.
- face value (bond) ::@:: Principal amount repaid at maturity; commonly 1,000 per bond.
- bond interest payment frequency ::@:: Often semiannual; can also be annual or quarterly depending on the bond terms.

## coupon rate versus market rate

The coupon (stated) rate determines the cash interest paid to bondholders: cash interest each period = face value × coupon rate (adjust for the period length if needed).

The market (effective) interest rate is the required rate of return for investors (opportunity cost). Interest expense recognized by the issuer is based on the carrying amount of the bond and the market rate: interest expense = carrying amount × market (effective) rate.

---

Flashcards for this section are as follows:

- coupon (stated) rate ::@:: Rate used to compute cash interest paid to bondholders (cash interest = face value × coupon rate, adjusted for period).
- market (effective) interest rate ::@:: Investors' required return (opportunity cost) used to price the bond and compute interest expense.
- bond cash interest vs interest expense ::@:: Cash interest uses face value × coupon rate; interest expense uses carrying amount × market (effective) rate.

## bond price intuition (par, discount, premium)

Bond price equals the present value of future cash payments (interest plus principal), discounted at the market (effective) interest rate.

If coupon rate equals market rate at issuance, the bond sells at par (price equals face value). If coupon rate is lower than market rate, the bond sells at a discount (price below face value). If coupon rate is higher than market rate, the bond sells at a premium (price above face value).

Representative journal entry examples at issuance:

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

<!-- markdownlint-disable-next-line MD028 -->
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

- how is bond price determined? ::@:: Present value of future cash payments (interest and principal) discounted at the market (effective) interest rate.
- when does a bond sell at par? ::@:: When coupon (stated) rate equals market (effective) rate at issuance; price equals face value.
- bond sells at discount vs premium ::@:: Coupon &lt; market → discount (price &lt; face); coupon &gt; market → premium (price &gt; face).
- bond issued at discount: issuance entry (net method)? ::@:: Dr Cash (proceeds), Cr Bonds payable (carrying amount); no separate discount account.
- bond discount: why record at carrying amount (net)? ::@:: So Bonds payable on the balance sheet equals carrying amount; discount is amortized by crediting Bonds payable each interest date.
- bond issued at premium: issuance entry (net method)? ::@:: Dr Cash (proceeds), Cr Bonds payable (carrying amount).
- bond premium: how is it removed over time? ::@:: Each interest date, debit Bonds payable (premium amortized = coupon − interest expense); carrying amount decreases to face at maturity.

## bond price: present value calculation

Bond price = present value of face value (single amount at maturity) + present value of coupon payments (ordinary annuity: same amount at the end of each period). Use the __market (effective) interest rate__ to discount, not the coupon rate. For semi-annual payments: use half-year rate (annual rate ÷ 2) and number of periods = years × 2. The course uses present value tables: (1) __present value of one dollar__ for the face value; (2) __present value of ordinary annuity__ for the coupon stream (payments at end of each period).

---

Flashcards for this section are as follows:

- bond price formula (concept) ::@:: PV of face value + PV of coupon payments; discount at market (effective) rate.
- which rate to use for bond price discounting? ::@:: Market (effective) interest rate only; do not use coupon rate.
- present value of one dollar (bond tables) ::@:: Used for a single future amount (e.g. face value at maturity); look up periods and rate.
- present value of ordinary annuity (bond tables) ::@:: Used for equal payments at the end of each period (coupon payments); look up periods and rate.
- semi-annual bond: periods and rate ::@:: Number of periods = years × 2; use half-year rate (annual market rate ÷ 2, annual coupon rate ÷ 2 for coupon payment).

## effective interest method (bonds)

The course uses the __effective interest method__ only (not straight-line amortization). Interest expense each period = __carrying amount at start of period × market (effective) rate__ (use the per-period rate for semi-annual). Cash paid to investors = face value × coupon rate (coupon payment; constant each period for fixed-rate bonds).

- __Discount__: Bond sold below face value. Interest expense &gt; coupon payment; the difference is __discount amortization__, which is credited to Bonds payable (or to a separate Discount on bonds payable account if the book shows face value separately). Carrying amount increases each period and reaches face value at maturity.
- __Premium__: Bond sold above face value. Interest expense &lt; coupon payment; the difference is __premium amortization__, which is debited to Bonds payable (or to Premium on bonds payable). Carrying amount decreases each period to face value at maturity.

Why is interest expense different from the coupon? For a discount, the issuer effectively "lost" by selling below face; that cost is spread over the life of the bond as extra interest expense. For a premium, part of the premium is used to reduce interest expense each period. Because interest and amortization amounts are usually rounded in practice, small rounding differences may accumulate; the final period's interest expense and discount or premium amortization are adjusted slightly so the carrying amount equals the exact face value at maturity.

Representative journal entry examples:

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

<!-- markdownlint-disable-next-line MD028 -->
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

<!-- markdownlint-disable-next-line MD028 -->
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

- effective interest method (bonds) ::@:: Interest expense = carrying amount × market (effective) rate; amortize discount or premium so carrying amount moves to face value at maturity; no straight-line in this course.
- bond discount: why is interest expense &gt; coupon payment? ::@:: Discount is amortized to interest expense; the "loss" from issuing below face is spread over periods.
- bond premium: why is interest expense &lt; coupon payment? ::@:: Premium is amortized to reduce interest expense each period.
- discount amortization (bond) ::@:: Interest expense − coupon payment; increases carrying amount (Cr Bonds payable or reduce Discount on bonds payable).
- premium amortization (bond) ::@:: Coupon payment − interest expense; decreases carrying amount (Dr Bonds payable or Premium on bonds payable).
- rounding in bond interest schedule ::@:: Because interest and amortization are rounded, the last period's amounts may be adjusted slightly so that the final carrying amount equals the exact face value at maturity.
- bond (discount): interest date entry? ::@:: Dr Interest expense, Cr Interest payable (coupon), Cr Bonds payable (discount amortized).
- bond discount amortization: how is it recorded? ::@:: Credit Bonds payable (or reduce Discount on bonds payable) each period; amount = interest expense − coupon payment.
- bond (premium): interest date entry? ::@:: Dr Interest expense, Dr Bonds payable (premium amortized), Cr Interest payable (coupon).
- bond premium amortization: how is it recorded? ::@:: Debit Bonds payable (or Premium on bonds payable) each period; amount = coupon payment − interest expense.
- bond at maturity: journal entry? ::@:: Dr Bonds payable (face value), Cr Cash.
- bond maturity: why no gain or loss (typical case)? ::@:: Carrying amount has been amortized to face value; payment equals liability.
- bond schedule rounding: where is it fixed? ::@:: In the final period; interest expense and discount/premium amortization may be tweaked slightly so the ending carrying amount equals the exact face value.
- bond redeemed between interest dates: what does the final payment include? ::@:: Principal plus prorated interest for the final partial period up to redemption/maturity; no later coupon payment because the bond has been settled.

## year-end accrual between interest payment dates

When the reporting date falls between two coupon payment dates, the entity accrues interest for the __fraction of the period__ that has elapsed. Prorate (1) the coupon payment (e.g. months elapsed ÷ 6 for semi-annual) and (2) the discount or premium amortization for that period the same way. Record Dr Interest expense (prorated, net of premium or plus discount amortization), Cr Interest payable (prorated coupon), and Cr Bonds payable (prorated discount amortization) or Dr Bonds payable (prorated premium amortization). The same prorating logic applies if the bond is redeemed or matures between payment dates: the final interest payment covers only the fraction of the period up to the redemption/maturity date.

Representative journal entry examples:

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

<!-- markdownlint-disable-next-line MD028 -->
> *Scenario.* Bond with face {@{100 000}@}, coupon {@{8%}@}, interest paid semi-annually (every 6 months). It is issued {@{4 months after the last interest date}@}. At issuance, investor pays accrued interest for 4 of 6 months: {@{100 000 × 8% × 4/12 = 2 667}@}. On the next interest date, issuer pays full coupon for 6 months: {@{100 000 × 8% × 6/12 = 4 000}@}.
>
>
> | {@{Issue bond at par between interest dates}@} | Dr            | Cr            |
> | ---------------------------------------------- | ------------- | ------------- |
> | {@{Cash}@}                                     | {@{102 667}@} |               |
> | {@{Bonds payable}@}                            |               | {@{100 000}@} |
> | {@{Interest expense}@}                         |               | {@{2 667}@}   |
>
> | {@{First interest payment after issue}@} | Dr          | Cr          |
> | ---------------------------------------- | ----------- | ----------- |
> | {@{Interest expense}@}                   | {@{4 000}@} |             |
> | {@{Cash}@}                               |             | {@{4 000}@} |
>
>
> *Explanation.* {@{Total interest expense over 2 months (from issue date to payment date) = 4 000 − 2 667 = 1 333 = 100 000 × 8% × 2/12}@}.

<!-- markdownlint-disable-next-line MD028 -->
> *Scenario.* Semi-annual bond with face {@{100 000}@}, coupon {@{8%}@}, market rate {@{10%}@}. Issue price (excluding accrued interest) is {@{96 000}@}; bond is issued {@{4 months after the last interest date}@}. At issuance the investor pays {@{accrued coupon for 4 of the 6 months: 100 000 × 8% × 4/12 = 2 667}@}. Total cash raised by issuer = {@{96 000 (carrying amount) + 2 667 (pre-collected interest) = 98 667}@}, split between Bonds payable {@{96 000}@} and a credit to Interest expense (pre-collected) {@{2 667}@}.
>
>
> | {@{Issue bond at discount between interest dates}@} | Dr           | Cr           |
> | --------------------------------------------------- | ------------ | ------------ |
> | {@{Cash}@}                                          | {@{98 667}@} |              |
> | {@{Bonds payable}@}                                 |              | {@{96 000}@} |
> | {@{Interest expense}@}                              |              | {@{2 667}@}  |
>
>
> *Next interest date (2 months of the 6-month period for this holder).* Carrying amount at issue is {@{96 000}@}. Using the effective interest method, interest expense = {@{96 000 × 10% (market rate) × 2/12 (time fraction) = 1 600}@}. The full coupon paid at this date = {@{100 000 × 8% (stated coupon) × 6/12 (full period) = 4 000}@}, but only {@{4 000 × 2/6 = 1 333}@} is prorated to this 2-month holding period. Therefore, discount amortized in this period = {@{1 600 − 1 333 = 267}@}, representing the portion of the discount that reduces carrying amount.
>
> For bonds issued between coupon dates, we do not use Interest Payable. Instead, record the coupon payment in full, then adjust Interest Expense via the discount/premium amortization:
>
> | {@{First interest date — coupon payment}@}        | Dr          | Cr          |
> | ------------------------------------------------- | ----------- | ----------- |
> | {@{Interest expense}@}                            | {@{4 000}@} |             |
> | {@{Cash}@}                                        |             | {@{4 000}@} |
>
>
> | {@{First interest date — discount amortization}@} | Dr          | Cr          |
> | ------------------------------------------------- | ----------- | ----------- |
> | {@{Bonds payable}@}                               | {@{267}@}   |             |
> | {@{Interest expense}@}                            |             | {@{267}@}   |
>
> *Explanation.* Accrued interest at issue always uses {@{the coupon (stated) rate and the time since the last payment date}@}. At each coupon date, the two entries work together: (1) record full coupon to cash as {@{Interest Expense Dr 4 000}@}, and (2) immediately adjust by {@{debiting Bonds Payable Dr 267 and crediting Interest Expense Cr 267}@}. Net interest expense from both entries = {@{4 000 − 267 = 3 733}@}. Combined with the pre-collected Interest Expense credit at issuance {@{Cr 2 667}@}, the final net effect for the 2-month holding period = {@{3 733 − 2 667 = 1 600}@}, which precisely equals the effective interest per the formula {@{carrying amount × market rate × time fraction = 96 000 × 10% × 2/12 = 1 600}@}. This demonstrates that the effective interest method produces the correct holding-period interest regardless of coupon frequency.

---

Flashcards for this section are as follows:

- bond: year-end between payment dates ::@:: Accrue interest for fraction of period: prorate coupon to Interest payable and prorate discount/premium amortization; use months in period (e.g. ÷6 for semi-annual).
- semi-annual coupon: prorate by months (e.g. 2 months of 6) ::@:: Use 2/6 of period coupon and 2/6 of period amortization; do not use 2/12 (period is 6 months, not 12).
- bond matures between payment dates: how to handle final interest? ::@:: Compute interest for the final partial period using the same fraction-of-period prorating (e.g. months elapsed ÷ 6) and pay that amount together with redemption of principal; there is no extra coupon on the next scheduled date because the bond has been settled.
- bond: year-end accrual between payment dates—what to prorate? ::@:: Prorate coupon (to Interest payable) and discount or premium amortization by fraction of period (e.g. months elapsed ÷ 6 for semi-annual).
- semi-annual period: 2 months elapsed—divide by 6 or 12? ::@:: Divide by 6; the coupon period is 6 months, so 2 months = 2/6 of the period.
- bond issued between interest dates (par): issuance entry? ::@:: Dr Cash (price + accrued coupon), Cr Bonds payable (face), Cr Interest expense (accrued coupon from last payment date to issue date). <br/> Why: the investor prepays the coupon that will be fully received at the next coupon date; this offset entry nets the issuer's expense to only the actual holding period.
- bond issued between interest dates: why does the investor pay accrued interest at issuance? ::@:: The next full coupon will be paid to whoever holds the bond on the coupon date. The purchasing investor compensates the issuer for the coupon "earned" before the purchase; the investor's effective return then covers only the stub period held.
- bond between interest dates: year-end accrual (par, discount, or premium) ::@:: If year-end falls between the issue date and the next coupon date, accrue interest for the stub from __issue date to year-end__ using the carrying amount (not face). <br/> General formula: interest expense = carrying amount × market rate × months-from-issue-to-year-end / 12. <br/> For discount/premium: also prorate the coupon and record discount or premium amortization. On the next coupon date, pay the full coupon; the portion from year-end to coupon is the new year's expense.
- bond between interest dates (par): when is the final interest paid? ::@:: If the bond remains to a regular coupon date, the last payment includes a full-period coupon plus principal; if it is redeemed between coupon dates, the final payment includes principal plus prorated interest for the final partial period only (no later coupon).
- bond issued between interest dates (discount/premium): what does investor pay at issue? ::@:: Carrying amount (issue price) + accrued coupon interest (using stated coupon rate and elapsed time since last payment date). <br/> The accrued portion compensates the issuer for the coupon that will be fully paid at the next coupon date, even though the investor only held it partway through the period.
- bond between interest dates (discount/premium): issuance entry? ::@:: Dr Cash (carrying amount + accrued coupon), Cr Bonds payable (carrying amount), Cr Interest expense (accrued coupon pre-collected). <br/> The Pre-collected credit nets the issuer's later full-coupon debit so net expense = carrying × market rate × actual holding fraction.
- bond between interest dates (discount/premium): post-issue interest using effective interest method? ::@:: Carrying amount at issue 96&nbsp;000. For the 2-month stub to next coupon: <br/> __Coupon payment entry__: Dr Interest expense 4&nbsp;000 (full 6-month coupon), Cr Cash 4&nbsp;000. <br/> __Amortization entry__: Dr Bonds payable 267 (discount reduces carrying amount), Cr Interest expense 267 (adjusts net expense). <br/> Net effect: Interest Expense = 4&nbsp;000 − 267 = 3&nbsp;733 from these entries + pre-collected 2&nbsp;667 (credit) = net 1&nbsp;600 for the 2-month holding period.
- bond between interest dates (discount/premium): interaction with year-end interest accrual ::@:: If year-end falls between the issue date and the next coupon date, use Interest Payable only for the accrual: Dr Interest expense (carrying × market × months-from-issue-to-year-end / 12), Cr Interest payable (prorated coupon portion), Cr Bonds payable (prorated discount amortization). <br/> When the coupon is paid at the next date: Dr Interest expense (full coupon), Cr Cash; then Dr Bonds payable (remaining amortization from year-end to coupon date), Cr Interest expense. <br/> Note: the pre-collected Interest expense credit at issuance covers the pre-issue portion; year-end accruals cover the post-issuance stub.
- bond between interest dates (discount/premium): final interest when redeemed between coupon dates? ::@:: Pay principal (face) plus prorated interest for the final partial period only (carrying × market × months / 12 for interest expense; coupon rate × face × months / 12 for cash coupon); no subsequent full coupon because the bond has been settled. Rounding is cleaned up in this final period so carrying equals face.
- bond between interest dates: intuitive mental model for cash vs. expense ::@:: __Cash coupon__ (always the same amount): on every coupon date the issuer pays the same full-period cash coupon, regardless of when the bond was issued — it is always face × coupon rate × period length. <br/> __Actual interest expense__ (depends on partial method): the issuer only incurs borrowing cost from the issue date onward; the pre-collected accrued interest at issuance is a negative-interest-expense offset that zeroes out the pre-issue portion. <br/> __Discount/premium amortization__: in the partial-period (stub) after issue, the effective-interest method applies to the actual carrying amount and the actual fraction elapsed since issue; this is a real economic amortization, not just a pro-rata share of the full-period schedule.

## notes payable and bonds

Long-term notes payable are very similar to bonds from an accounting perspective: both are measured at the present value of future cash flows and use the effective interest method to recognize interest expense and amortize any discount or premium. The main practical difference is that bonds are typically traded in public markets (many investors, transferable), whereas individual notes payable are usually private agreements with a single lender and are not easily traded.

Representative journal entry example for an interest-bearing long-term note at discount:

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

---

Flashcards for this section are as follows:

- notes payable vs bonds (accounting) ::@:: Both are measured at present value and use the effective interest method to recognize interest expense and amortize discount/premium.
- notes payable vs bonds (practical difference) ::@:: Bonds are widely traded instruments with many investors; long-term notes payable are usually private, non-tradable agreements with a single lender.
- interest-bearing note at discount: issuance entry (net)? ::@:: Dr Cash (present value), Cr Notes payable (present value).
- interest-bearing note at discount: first-year interest entry? ::@:: Dr Interest expense (carrying × market), Cr Cash (face × stated), Cr Notes payable (discount amortized).

## zero-interest-bearing notes and implicit interest rate

A zero-interest-bearing note has no periodic coupon payments; the borrower receives less than the face value today and repays the full face value at maturity. The difference between the face value and the cash received is a discount that represents interest over the life of the note. The issuer records the note at its present value and uses an __implicit interest rate__ (the rate that discounts the maturity amount to the cash received) to compute interest expense each period; all interest is recognized via discount amortization.

Representative journal entry example:

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

- zero-interest-bearing note ::@:: Note with no periodic interest payments; borrower receives less than face value and repays full face value at maturity; the difference is a discount.
- implicit interest rate (note) ::@:: The discount rate that equates the maturity amount to the cash received (present value); used to compute interest expense on a zero-interest-bearing or implicit-interest note.
- interest on zero-interest-bearing note: how recognized? ::@:: As discount amortization using the implicit interest rate; no separate cash interest payments during the term.
- zero-interest-bearing note: issuance entry? ::@:: Dr Cash (present value received), Cr Notes payable (present value); no separate discount account under net method.
- zero-interest-bearing note: how is interest expense recorded? ::@:: Each period, Dr Interest expense, Cr Notes payable using the implicit interest rate; carrying amount increases to face value.

## notes for noncash transactions and fair value hierarchy

When a long-term note is issued in exchange for a noncash asset or service (e.g. land or architectural services), the preferred measurement is __fair value__. If the fair value of the asset or service can be determined reliably (e.g. from a cash selling price), record the asset at that fair value and record the note at the same amount (its present value). If the asset's fair value cannot be observed, use discounted cash flows: estimate future cash flows on the note and discount them at an appropriate rate to obtain the note's present value; this present value is also used to measure the related asset.

Representative journal entry examples:

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

<!-- markdownlint-disable-next-line MD028 -->
> *Scenario.* Company receives architectural services in exchange for a {@{5-year note with face 200 000}@} and no stated interest. No market price is available for the services, but an appropriate discount rate (after considering prime rate, covenants, collateral, and term) is {@{8%}@}. Present value of the note (discounted at 8%) is {@{136 000}@} (rounded).
>
>
> | {@{Record architectural services and note (use present value)}@} | Dr            | Cr            |
> | ---------------------------------------------------------------- | ------------- | ------------- |
> | {@{Construction in progress (or Building)}@}                     | {@{136 000}@} |               |
> | {@{Notes payable}@}                                              |               | {@{136 000}@} |

---

Flashcards for this section are as follows:

- note for noncash asset: which value to use? ::@:: Prefer the fair value of the asset or service received; record both the asset and the note at that fair value.
- when to use discounted cash flows for notes? ::@:: When fair value of the noncash asset/service is not observable; estimate future cash flows and discount at an appropriate rate to get present value.
- present value of note in noncash deal: what does it measure? ::@:: Both the carrying amount of the note payable and the cost of the related asset (when fair value must be inferred).
- note for noncash asset (fair value known): entry? ::@:: Dr Asset (fair value), Cr Notes payable (same fair value/present value).
- noncash note: fair value unknown—what amount to record? ::@:: Use present value of the note (discounted cash flows at an appropriate rate) for both the asset and the note payable.

## choosing a discount rate for notes payable

If an observable market rate for a similar instrument exists, use that rate as the discount rate for the note. If not, start from the __prime rate__ (inter-bank lending rate) and adjust for features that change the lender's risk: restrictive covenants (lower risk → lower rate), collateral (secured → lower rate than unsecured), and the payment schedule (shorter term → lower rate than long term). A higher assessed risk leads to a higher discount rate and a lower present value for the note.

---

Flashcards for this section are as follows:

- first choice of discount rate for a note ::@:: Use the market rate for a similar instrument (same term, cash-flow pattern, and credit risk) when available.
- when to base note discount rate on prime rate? ::@:: When there is no directly comparable market instrument; start from the prime rate and adjust for risk factors.
- effect of restrictive covenants and collateral on discount rate ::@:: Strong covenants and good collateral reduce lender risk and therefore reduce the required discount rate.
- note term and discount rate relationship ::@:: Shorter-term notes generally justify a lower discount rate than otherwise similar long-term notes.

## extinguishment of debt (overview)

Extinguishment of long-term debt occurs when the obligation is settled before or at maturity, either by paying cash (e.g. repurchasing bonds), by transferring other assets (e.g. giving land to the lender), or by issuing equity instruments (e.g. shares) in full settlement. At the extinguishment date, the entity compares the carrying amount of the liability to the consideration paid or assets/equity transferred: if consideration &lt; carrying amount, there is a gain; if consideration &gt; carrying amount, there is a loss. When a noncash asset is transferred, remeasure the asset to fair value first (recognising any gain or loss on the asset), then compare the liability's carrying amount to the fair value of the asset to determine the gain or loss on extinguishment. When shares are issued to settle the debt, measure the consideration at the fair value of the shares (or, if that is not available, the fair value/present value of the liability).

Representative journal entry examples:

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

<!-- markdownlint-disable-next-line MD028 -->
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

<!-- markdownlint-disable-next-line MD028 -->
> *Scenario.* Debtor has a building with carrying amount {@{21 000 000}@} and fair value {@{16 000 000}@}. A note payable has carrying amount {@{20 000 000}@}. The lender agrees to accept the building in full settlement of the note.
>
>
> | {@{Remeasure building to fair value}@} | Dr              | Cr              |
> | -------------------------------------- | --------------- | --------------- |
> | {@{Loss on disposal of building}@}     | {@{5 000 000}@} |                 |
> | {@{Building}@}                         |                 | {@{5 000 000}@} |
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

- extinguishment of debt: when does it occur? ::@:: When a long-term liability is settled before or at maturity, by paying cash, transferring other assets, or issuing equity instruments (e.g. shares) in full settlement.
- gain vs loss on extinguishment of debt ::@:: Compare carrying amount of the liability with consideration given; consideration &lt; carrying → gain, consideration &gt; carrying → loss.
- extinguishment using a noncash asset: two-step view ::@:: First remeasure the asset to fair value (gain or loss on asset), then compare liability carrying amount to asset fair value to find gain or loss on extinguishment.
- early extinguishment of debt with cash: how to find gain or loss? ::@:: Compare cash paid with carrying amount; cash > carrying → loss, cash < carrying → gain.
- debt settled by issuing shares: basic journal entry ::@:: Dr Notes/Bonds payable (carrying amount), Dr/Cr Gain or Loss on extinguishment (for the difference), Cr Share capital (par) and Cr Share premium (issue proceeds in excess of par) based on fair value of shares issued.
- debt-for-equity swap: how to measure consideration? ::@:: Use the fair value of the shares issued when available; if not, use the fair value or present value of the liability's remaining cash flows.
- extinguishment by transferring property: why two gains/losses? ::@:: One from remeasuring the asset to fair value; another from comparing liability carrying amount to asset fair value when settling the debt.

## modification of debt terms

Sometimes a long-term liability is not repaid in cash but its terms are changed instead (e.g. principal reduced, maturity extended, or interest rate lowered) because the borrower is in financial difficulty. Under IFRS, when the change in terms is significant, the restructuring is treated as an __extinguishment__ of the old debt and the recognition of a __new__ liability measured at fair value.

Conceptually, the steps are:

1. Measure the fair value of the restructured (new) note based on the revised terms and a current market-based borrowing rate for the debtor.
2. Derecognise the old liability at its carrying amount.
3. Recognise the new liability at its fair value.
4. Recognise the difference between the old carrying amount and the new fair value as a gain or loss on extinguishment.

After the modification date, the new liability is amortized using the new effective interest rate (the market-based rate used to compute its fair value), with interest expense recognised at that rate and any difference between interest expense and cash interest treated as discount or premium amortization.

Representative journal entry example:

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

- modification of debt terms (IFRS course focus) ::@:: Treat a significant change of terms as extinguishment of the old debt and recognition of a new liability measured at fair value; recognise a gain or loss equal to old carrying amount minus fair value of new debt.
- modified debt: which rate for new effective interest? ::@:: Use the current market-based borrowing rate used to measure the fair value of the restructured note; apply it to the new carrying amount to compute interest expense.
- modification of debt terms (debtor, lecture slide) ::@:: Derecognise the old note at its carrying amount, recognise the new restructured note at fair value, and record the difference as a gain or loss on extinguishment of debt.
- modification of debt terms (debtor): numerical gain in slide example? ::@:: Old carrying amount 10 500 000 minus fair value of new note 7 201 336; gain = 3 298 664.
