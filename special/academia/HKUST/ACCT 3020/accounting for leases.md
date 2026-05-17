---
aliases:
  - IFRS 16
  - accounting for leases
  - finance lease
  - lease accounting
  - operating lease
  - right-of-use asset
tags:
  - flashcard/active/special/academia/HKUST/ACCT_3020/accounting_for_leases
  - language/in/English
---

# accounting for leases

This note covers IFRS 16 lease accounting: the recognition of right-of-use assets and lease liabilities, lessee finance and operating lease accounting, lessor classification tests, lessor sales-type (finance) and operating lease accounting, and sale-leaseback transactions. All monetary examples use fictional companies and amounts.

## leasing environment

A __lease__ is a contract that conveys the right to control the use of an identified asset for a period of time in exchange for consideration. The lessee obtains the right of use; the lessor retains legal title.

__Advantages for the lessee__: leasing provides up to 100% financing (no down payment required); protects against technological obsolescence (return the asset when a newer model is available); offers flexibility to match asset use to short-term needs; may result in lower financing cost than purchasing.

__Advantages for the lessor__: interest margin on the financing; tax benefits from retained asset ownership; residual value at lease end.

__IFRS 16 (Leases)__ requires lessees to recognize virtually all leases on the balance sheet as a __right-of-use (ROU) asset__ and a __lease liability__. Two exceptions allow straight-line expense treatment:

1. __Short-term leases__: underlying asset lease term ≤ 12 months (with no purchase option).
2. __Low-value leases__: underlying asset is of low value when new (indicative threshold ≈ USD 5 000).

For all other leases, the lessee recognizes the ROU asset and lease liability on the commencement date.

---

Flashcards for this section are as follows:

- IFRS 16 lessee: what must be recognized for almost all leases? ::@:: A right-of-use (ROU) asset and a lease liability on the commencement date.
- IFRS 16 lessee: two exceptions that allow lease payments to be expensed as incurred ::@:: Short-term leases (term ≤ 12 months) and low-value leases (asset value ≤ approximately USD 5 000 when new).
- why might a lessee prefer leasing to buying? ::@:: 100% financing; protection against obsolescence; flexibility; potentially lower cost than borrowing to buy.
- IFRS 16: who retains legal title in a lease? ::@:: The lessor; the lessee obtains the right of use, not legal ownership.

## lease term and lease payments

The lease term used for accounting purposes is the __non-cancelable period__ plus any optional extension periods the lessee is __reasonably certain__ to exercise (or termination option periods the lessee is reasonably certain NOT to exercise). A __bargain renewal option__ (renewal rate significantly below expected fair market rate) creates a strong presumption of exercise.

Payments included in the lease liability and ROU asset measurement:

- __Fixed payments__ (net of any lease incentives receivable).
- __Variable payments based on an index or rate__ (e.g., CPI-linked) measured using the current index/rate.
- __Guaranteed residual value__: the maximum amount the lessee could be required to pay. If the lessee expects the actual residual value to exceed the guaranteed amount, no expected shortfall payment need be included. If the expected value is lower than the guarantee, the lessee includes the expected payment (= max(guaranteed RV − expected FV, 0)) in the lease liability.
- __Bargain purchase option price__ — if the lessee is reasonably certain to exercise the option.

Payments NOT included: variable payments that depend on usage or performance (recognized as an expense when incurred).

The lessee uses the __implicit rate__ (rate the lessor uses to set the payments such that their PV equals the asset's fair value) if it can be readily determined. Otherwise, the lessee uses the __incremental borrowing rate__ (the rate the lessee would pay on a similar collateralized borrowing for a similar term).

---

Flashcards for this section are as follows:

- lease term under IFRS 16: what periods are included? ::@:: The non-cancelable period plus any optional extension periods (or termination options) the lessee is reasonably certain to exercise (or not exercise).
- bargain renewal option: how does it affect lease term? ::@:: Since the lessee is effectively certain to renew at a below-market rate, the renewal period is included in the lease term for measurement purposes.
- guaranteed residual value: what amount does the lessee include as a lease payment? ::@:: The expected payment = max(guaranteed residual − expected fair value at end of lease, 0). If expected FV ≥ guaranteed, the lessee includes nothing.
- lessee discount rate: primary and fallback ::@:: Use the implicit rate if known; otherwise use the incremental borrowing rate.
- variable lease payments based on usage: are they in the lease liability? ::@:: No — usage-based variable payments are expensed as incurred; only payments based on an index or rate are included.

## lessee accounting — finance lease

At the commencement date the lessee records:

- __Lease liability (LL)__ = present value of lease payments.
- __ROU asset__ = lease liability + any lease prepayments + initial direct costs incurred by the lessee − any incentives received from the lessor.

Subsequent measurement:

- __Lease liability__: reduced by cash payments and increased by interest accrued each period (effective interest method).
- __ROU asset__: amortized straight-line over the __shorter of the lease term or the useful life of the underlying asset__, unless ownership transfers or a bargain purchase option exists (in which case, depreciate over the useful life).
- Income statement: __interest expense__ (on LL) + __depreciation__ (on ROU asset) recognized separately.

---

Flashcards for this section are as follows:

- lessee finance lease: what two elements are recognized at commencement? ::@:: _Right-of-use asset_ and _lease liability_, both measured at the present value of lease payments.
- lessee finance lease: how is the lease liability subsequently measured? ::@:: Effective interest method: increased by interest accrued (carrying amount × rate) and reduced by cash payments.
- lessee finance lease: over what period is the ROU asset depreciated? ::@:: Over the shorter of the lease term and the useful life of the underlying asset, unless ownership transfers or a bargain purchase option exists (then use useful life).
- lessee income statement — finance lease: what two charges appear? ::@:: _Interest expense_ (on the lease liability) and _depreciation_ (on the ROU asset), separately shown.
- annuity-due lease: why is the first payment made on commencement date with no interest? ::@:: Because payment is at the start of the period; there has been no time for interest to accrue, so the full payment reduces the _lease liability_ directly.
- lessee ROU asset: initial measurement formula? ::@:: _ROU asset_ = _lease liability_ + any lease prepayments + initial direct costs incurred by the lessee − any lease incentives received from the lessor.

### finance lease: Oakhurst Mining and Navara Capital

> Navara Capital (lessor) leases a drilling rig to Oakhurst Mining (lessee). Terms: 5-year non-cancelable lease commencing 1 January 2025; annual payments of {@{€24&nbsp;854}@} at the start of each year (annuity-due). Fair value of rig at commencement: {@{€120&nbsp;000}@}; estimated useful life: 8 years; guaranteed residual value: €6&nbsp;000. Oakhurst expects the actual residual value at year 5 will exceed €6&nbsp;000, so {@{no shortfall payment is included in the lease payments}@}. Navara's implicit rate is 4% and is known to Oakhurst.
>
> Oakhurst's lease liability = PV of 5 annuity-due payments of €24&nbsp;854 at 4%:
>
> $\text{LL} = 24\,854 \times \underbrace{4.62989}_{\text{PV annuity-due, 4\%, 5 periods}} = €115\,069$
>
> Since the guaranteed residual is excluded (expected FV > guaranteed), {@{ROU asset = LL = €115&nbsp;069}@}.
>
> | Oakhurst Mining — lease liability amortization schedule | | | | |
> | --- | ---: | ---: | ---: | ---: |
> | __Date__ | __Payment__ | __Interest (4%)__ | __Principal__ | __Liability__ |
> | 1 Jan 2025 (opening) | — | — | — | {@{115&nbsp;069}@} |
> | 1 Jan 2025 (first payment) | {@{24&nbsp;854}@} | — | {@{24&nbsp;854}@} | {@{90&nbsp;215}@} |
> | 31 Dec 2025 | — | {@{3&nbsp;609}@} | — | {@{93&nbsp;824}@} |
> | 1 Jan 2026 (second payment) | 24&nbsp;854 | — | {@{24&nbsp;854}@} | {@{68&nbsp;970}@} |
> | 31 Dec 2026 | — | {@{2&nbsp;759}@} | — | {@{71&nbsp;729}@} |
> | 1 Jan 2027 | 24&nbsp;854 | — | {@{24&nbsp;854}@} | {@{46&nbsp;875}@} |
> | 31 Dec 2027 | — | {@{1&nbsp;875}@} | — | {@{48&nbsp;750}@} |
> | 1 Jan 2028 | 24&nbsp;854 | — | {@{24&nbsp;854}@} | {@{23&nbsp;896}@} |
> | 31 Dec 2028 | — | {@{956}@} | — | {@{24&nbsp;852}@} |
> | 1 Jan 2029 (final payment) | {@{24&nbsp;852}@} | — | {@{24&nbsp;852}@} | {@{0}@} |
>
> Depreciation per year: €115&nbsp;069 ÷ 5 years = {@{€23&nbsp;014}@}. (Oakhurst depreciates over the lease term since ownership does not transfer.)
>
> | {@{1 January 2025 — recognize lease and first payment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Right-of-use asset}@} | {@{115&nbsp;069}@} | |
> | {@{Lease liability}@} | | {@{115&nbsp;069}@} |
> | {@{Lease liability}@} | {@{24&nbsp;854}@} | |
> | {@{Cash}@} | | {@{24&nbsp;854}@} |

<!-- markdownlint-disable-next-line MD028 -->
> Interest = €90&nbsp;215 × 4% = €3&nbsp;609; depreciation = €115&nbsp;069 ÷ 5 = €23&nbsp;014 per year.
>
> | {@{31 December 2025 — interest and depreciation}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Interest expense}@} | {@{3&nbsp;609}@} | |
> | {@{Lease liability}@} | | {@{3&nbsp;609}@} |
> | {@{Depreciation expense}@} | {@{23&nbsp;014}@} | |
> | {@{Accumulated depreciation — ROU asset}@} | | {@{23&nbsp;014}@} |

<!-- markdownlint-disable-next-line MD028 -->
> Oakhurst Mining — LL at 31 Dec 2025 (after interest accrual): €93&nbsp;824. Second annual payment due 1 Jan 2026:
>
> | {@{1 January 2026 — second payment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Lease liability}@} | {@{24&nbsp;854}@} | |
> | {@{Cash}@} | | {@{24&nbsp;854}@} |

<!-- markdownlint-disable-next-line MD028 -->
> Oakhurst Mining — LL after second payment: €68&nbsp;970. Year 2 interest: €68&nbsp;970 × 4% = €2&nbsp;759; depreciation unchanged at €23&nbsp;014 per year.
>
> | {@{31 December 2026 — interest and depreciation}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Interest expense}@} | {@{2&nbsp;759}@} | |
> | {@{Lease liability}@} | | {@{2&nbsp;759}@} |
> | {@{Depreciation expense}@} | {@{23&nbsp;014}@} | |
> | {@{Accumulated depreciation — ROU asset}@} | | {@{23&nbsp;014}@} |

---

Flashcards for this section are as follows:

- Oakhurst Mining: why is the guaranteed residual value excluded from the lease liability? ::@:: Because Oakhurst expects the actual residual value to exceed the guarantee of €6 000, so the expected shortfall payment is zero and nothing is added to the lease liability for the residual.
- Oakhurst Mining (5 annuity-due payments of €24&nbsp;854, rate 4%, PV annuity-due factor 4.62989): initial lease liability? ::@:: €24&nbsp;854 × 4.62989 = €115&nbsp;069.
- Oakhurst Mining (LL after first payment = €90&nbsp;215, rate 4%): Year 1 interest accrual and LL at 31 Dec 2025? ::@:: Interest = €90&nbsp;215 × 4% = €3&nbsp;609; LL rises to €93&nbsp;824 at 31 Dec 2025.
- Oakhurst Mining (ROU asset = €115&nbsp;069, lease term 5 years, no ownership transfer): annual depreciation? ::@:: €115&nbsp;069 ÷ 5 = €23&nbsp;014 per year; depreciated over lease term since ownership does not transfer.

## guaranteed versus unguaranteed residual value — lessee

If the lessee guarantees a minimum residual value at the end of the lease, the lessee is potentially liable for any shortfall between the guaranteed amount and the asset's actual fair value at return. The lessee includes the __expected payment__ (not the full guarantee) in the lease liability: $\max(\text{guaranteed residual} - \text{expected FV at end of lease},\ 0)$. If the lessee expects the asset to be worth at least the guaranteed amount, the expected payment is zero and nothing is added to the lease liability beyond the periodic payments.

An __unguaranteed residual value__ is the portion of the residual value that is not guaranteed by the lessee (or by an unrelated third party). The lessee has no obligation with respect to unguaranteed residuals; they do NOT enter the lessee's lease liability calculation. Because unguaranteed residuals are excluded, the lessee's lease liability (and ROU asset) is smaller.

If the asset is damaged and returned below the guaranteed amount, the lessee recognizes a loss on lease in the period of the shortfall. For example, if the guaranteed residual is €6&nbsp;000, the expected value at commencement is €8&nbsp;000 (so no initial shortfall payment), but at the end the asset is actually worth €0, the lessee must pay the full €6&nbsp;000 as a loss:

> Illustrative: guaranteed residual €6&nbsp;000; expected FV at commencement €8&nbsp;000 (no initial shortfall included); actual FV at return = €0 → lessee pays the full €6&nbsp;000 shortfall:
>
> | {@{Record loss on lease when asset returned below guaranteed residual}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Loss on lease}@} | {@{6&nbsp;000}@} | |
> | {@{Cash}@} | | {@{6&nbsp;000}@} |

---

Flashcards for this section are as follows:

- guaranteed residual value (lessee): formula for expected payment to include in lease liability ::@:: max(guaranteed residual − expected FV at end of lease, 0); if expected FV ≥ guaranteed, include zero.
- unguaranteed residual value (lessee): is it included in the lease liability? ::@:: No — the lessee has no obligation regarding unguaranteed residuals, so they are excluded from the lessee's _lease liability_.
- effect of unguaranteed residual on lessee vs lessor ::@:: Lessee excludes it (smaller LL and ROU); lessor includes its PV when computing the implicit rate and _lease receivable_.
- loss on lease: when does it arise? ::@:: When the leased asset is returned in worse condition than anticipated, so the lessee must pay the guaranteed residual shortfall; the lessee records a loss and a cash payment.
- loss on lease entry (lessee pays shortfall on return): accounts and direction? ::@:: Dr _Loss on lease_ (shortfall amount); Cr _Cash_ (shortfall amount); no debit to ROU asset because the lease has ended.

### unguaranteed residual: Pembury Retail and Quinton Equipment

> Quinton Equipment (lessor) leases a compactor to Pembury Retail (lessee). Terms: 3-year non-cancelable lease (annuity-due); annual payments of {@{£21&nbsp;854}@}; fair value £72&nbsp;000; economic life 7 years; {@{unguaranteed residual value £12&nbsp;000}@} at end of 3 years; Quinton uses an implicit rate of 6%; Pembury does not know this rate and uses an incremental borrowing rate of {@{6%}@}.
>
> Pembury's lease liability (unguaranteed residual excluded):
>
> $\text{LL} = 21\,854 \times \underbrace{2.83339}_{\text{PV annuity-due, 6\%, 3 periods}} = £61\,930$
>
> | {@{1 January 2025 — recognize lease and first payment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Right-of-use asset}@} | {@{61&nbsp;930}@} | |
> | {@{Lease liability}@} | | {@{61&nbsp;930}@} |
> | {@{Lease liability}@} | {@{21&nbsp;854}@} | |
> | {@{Cash}@} | | {@{21&nbsp;854}@} |
>
> _Explanation._ Pembury uses {@{only the annuity payments in the PV calculation}@}. The £12&nbsp;000 unguaranteed residual is NOT in Pembury's lease liability because Pembury bears {@{no obligation to make any payment related to the residual value}@}. As a result, Pembury's LL is £61&nbsp;930, {@{smaller than the £72&nbsp;000 fair value of the asset}@}.

---

Flashcards for this section are as follows:

- Pembury Retail / Quinton Equipment (payments = £21&nbsp;854/year, IBR = 6%, annuity-due, 3 years, FV = £72&nbsp;000, unguaranteed residual £12&nbsp;000): lessee lease liability and why it differs from asset fair value ::@:: LL = £61&nbsp;930 (PV of 3 annual payments of £21&nbsp;854 at 6% annuity-due); lower than the £72&nbsp;000 fair value because the £12&nbsp;000 unguaranteed residual is excluded from the lessee's lease liability.

## bargain purchase option

A __bargain purchase option (BPO)__ gives the lessee the right to buy the asset at a future price substantially below the expected fair value at the option date. Because it is "reasonably certain" the lessee will exercise, the lessee treats the BPO price as an additional payment at the end of the lease and includes its present value in the lease liability.

The BPO works like a guaranteed residual: the lessee adds PV(BPO price) to the lease liability. At exercise, the ROU asset converts to owned Equipment.

> _Example._ Suppose Oakhurst Mining's lease above (5-year rig, 4% rate) has no guaranteed residual but instead has a BPO at €2&nbsp;400 when the expected fair value is {@{€9&nbsp;600}@} — clearly a bargain. The PV of the BPO = €2&nbsp;400 / 1.04^5 = {@{€1&nbsp;973}@}. Oakhurst adds this to the lease liability:
>
> LL = PV of 5 payments + PV of BPO = €115&nbsp;069 + {@{€1&nbsp;973}@} = {@{€117&nbsp;042}@}
>
> | {@{1 January 2025 — recognize lease with BPO (modified Oakhurst example)}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Right-of-use asset}@} | {@{117&nbsp;042}@} | |
> | {@{Lease liability}@} | | {@{117&nbsp;042}@} |
>
> At exercise (1 January 2030): remaining lease liability ≈ €2&nbsp;400. The lessee pays the BPO price and the ROU asset is reclassified as Equipment.

---

Flashcards for this section are as follows:

- bargain purchase option: why is its price included in the lease liability? ::@:: Because the lessee is "reasonably certain" to exercise a below-market option; the discounted option price is treated as a future lease payment.
- bargain purchase option vs guaranteed residual: how does the lessee account for each? ::@:: Both are included at their PV in the lessee's _lease liability_ (guaranteed RV only to the extent of expected shortfall; BPO at the option price since exercise is certain).
- at exercise of a BPO: what accounting entry is made? ::@:: Pay the option price (Dr _Lease liability_ / Cr _Cash_), then reclassify the ROU asset to _Equipment_ (Dr _Equipment_ / Cr _Right-of-use asset_).

## lessor classification tests

The lessor classifies each lease as a __finance (sales-type) lease__ or an __operating lease__. A lease is a finance lease if it transfers substantially all risks and rewards of ownership. Any one of the following five tests, if met, indicates a finance lease:

| Test | Criterion | Guideline threshold |
| --- | --- | --- |
| 1. Transfer of ownership | Ownership transfers to lessee at lease end | — |
| 2. Bargain purchase option | Lessee has a BPO | — |
| 3. Lease term test | Lease term covers major part of asset's economic life | ≥ 75% |
| 4. Present value test | PV of lessee's payments ≥ substantially all fair value of asset | ≥ 90% |
| 5. No alternative use | Asset is so specialized the lessor cannot use it for another customer at end of lease | — |

If NONE of the five tests is met, the lessor classifies the lease as an __operating lease__.

The lessor uses the PV of the __lessee's contractual payments__ (excluding unguaranteed residual value) for test 4. Even if the total PV of payments plus unguaranteed residual equals 100% of fair value, the lessor evaluates the test only on what the lessee is contractually obligated to pay.

__IFRS vs US GAAP — lessor categories.__ IFRS 16 has only two lessor categories: __finance lease__ and __operating lease__. US GAAP (ASC 842) subdivides finance leases into __sales-type leases__ (manufacturer/dealer; fair value ≠ carrying amount → selling profit recognized on day 1) and __direct financing leases__ (non-dealer; no selling profit; only unearned interest income recognized). IFRS 16 treats both as a single finance lease category and always recognizes selling profit when the lessor is a manufacturer or dealer (identical in effect to a US GAAP sales-type lease).

---

Flashcards for this section are as follows:

- lessor classification: how many tests exist and what triggers finance lease classification? ::@:: Five tests; meeting ANY ONE triggers finance (sales-type) lease classification.
- PV test for lessor: what payments are used in the numerator? ::@:: The PV of the lessee's contractual payments (excluding unguaranteed residual value), compared to the asset's fair value.
- lessor finance (sales-type) lease day 1: what four accounts are affected? ::@:: Debit _Lease Receivable_ and _COGS_; credit _Sales Revenue_ and _Inventory_ — the sale and profit are recognized immediately.
- lessor finance lease: how is interest revenue recognized subsequently? ::@:: Effective interest method: Dr _Lease Receivable_; Cr _Interest Revenue_ each period (balance × rate).
- five lessor classification tests — mnemonic ::@:: "TOTAL": Transfer of ownership, Option (bargain purchase option), Term (≥ 75% of economic life), Amount (PV of lessee's payments ≥ 90% of fair value), Last resort (specialized asset, no alternative use for lessor).
- lessor classification tests: which two have quantitative thresholds, and what are they? ::@:: Lease term test (≥ 75% of the asset's economic life) and PV test (PV of lessee's contractual payments ≥ 90% of fair value). The other three — transfer of ownership, BPO, and no alternative use — are qualitative.
- IFRS 16 vs US GAAP ASC 842: how do lessor categories differ? ::@:: IFRS 16: two categories — finance lease and operating lease. US GAAP: three — sales-type (manufacturer/dealer, FV ≠ cost → day-1 selling profit), direct financing (non-dealer, no selling profit; only interest income), and operating. IFRS 16 always recognizes selling profit for manufacturer/dealer lessors (same effect as US GAAP sales-type).

### scenario 1 (both finance): Reigate Shipping and Southwick Trailers

> Southwick Trailers (lessor) leases a hydraulic lift to Reigate Shipping (lessee). Terms: 4-year non-cancelable lease commencing 1 January 2025 (annuity-due); payments of {@{€13&nbsp;419}@} per year; fair value of lift: {@{€48&nbsp;000}@}; cost on Southwick's books: {@{€36&nbsp;000}@}; estimated economic life: {@{4 years}@}; no residual value; implicit rate: 8%.
>
> Southwick evaluates the classification tests:
>
> 1. Transfer of ownership: no. 2. BPO: no. 3. Lease term: 4 / 4 years = {@{100%}@} ≥ 75% → __yes__. 4. PV test: PV of payments = €48&nbsp;000 = {@{100%}@} of fair value ≥ 90% → __yes__. 5. No alternative use: N/A.
>
> Two tests met → __finance (sales-type) lease__ for Southwick.
>
> Southwick's lease receivable on day 1 = PV of payments = {@{€48&nbsp;000}@}.
>
> | {@{1 January 2025 — record sales-type lease and receive first payment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Lease receivable}@} | {@{48&nbsp;000}@} | |
> | {@{Cost of goods sold}@} | {@{36&nbsp;000}@} | |
> | {@{Sales revenue}@} | | {@{48&nbsp;000}@} |
> | {@{Inventory}@} | | {@{36&nbsp;000}@} |
> | {@{Cash}@} | {@{13&nbsp;419}@} | |
> | {@{Lease receivable}@} | | {@{13&nbsp;419}@} |
>
> Remaining lease receivable after first payment: €48&nbsp;000 − €13&nbsp;419 = {@{€34&nbsp;581}@}.
>
> | {@{31 December 2025 — accrue interest revenue}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Lease receivable}@} | {@{2&nbsp;766}@} | |
> | {@{Interest revenue}@} | | {@{2&nbsp;766}@} |
>
> Interest: €34&nbsp;581 × 8% = {@{€2&nbsp;766}@}.

<!-- markdownlint-disable-next-line MD028 -->
> Reigate Shipping (lessee — Scenario 1) recognizes a finance lease. ROU asset = LL = {@{€48&nbsp;000}@}. Depreciation per year: €48&nbsp;000 / 4 = {@{€12&nbsp;000}@}.
>
> | {@{1 January 2025 — lessee recognizes lease and first payment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Right-of-use asset}@} | {@{48&nbsp;000}@} | |
> | {@{Lease liability}@} | | {@{48&nbsp;000}@} |
> | {@{Lease liability}@} | {@{13&nbsp;419}@} | |
> | {@{Cash}@} | | {@{13&nbsp;419}@} |

---

Flashcards for this section are as follows:

- Reigate/Southwick Scenario 1: why do both lessor and lessee have finance lease accounting? ::@:: The lease term equals 100% of the asset's useful life; lessee makes all the payments that equal 100% of fair value — both tests are met; and under IFRS 16 lessee always capitalizes.
- Reigate/Southwick Scenario 1 (FV = cost basis for lessee = €48&nbsp;000, cost on Southwick's books = €36&nbsp;000): lessor selling profit on day 1? ::@:: _Sales revenue_ €48&nbsp;000 − _COGS_ €36&nbsp;000 = €12&nbsp;000; recognized immediately on the commencement date.
- Reigate/Southwick Scenario 1 (lease receivable after first payment = €34&nbsp;581, rate 8%): Year 1 interest revenue? ::@:: €34&nbsp;581 × 8% = €2&nbsp;766; Dr _Lease Receivable_ €2&nbsp;766; Cr _Interest Revenue_ €2&nbsp;766.

## lessor accounting — operating lease

For an operating lease, the lessor __retains the asset on the balance sheet__ and continues to depreciate it. Lease payments received are recognized as __lease revenue__ on a straight-line basis over the lease term.

---

Flashcards for this section are as follows:

- lessor operating lease: does the lessor remove the asset from its balance sheet? ::@:: No — the lessor keeps the asset on the balance sheet and continues to depreciate it.
- lessor operating lease: how is lease revenue recognized? ::@:: Straight-line over the lease term, regardless of the payment pattern.
- lessor operating lease: why might lease receivable NOT be recorded? ::@:: Because no receivable (asset derecognition) has occurred; revenue is earned over time as the lessee has the right to use the asset.

### operating lease: Quinton Equipment and Pembury Retail

Quinton Equipment classifies the compactor lease (Pembury Retail) as an __operating lease__:

- Lease term test: 3 / 7 years = 43% < 75% → fails.
- PV test: PV of lessee's payments £61&nbsp;930 / fair value £72&nbsp;000 = 86% < 90% → fails.
- No transfer, no BPO, no alternative-use issue.

> Quinton Equipment (operating lessor) — Pembury Retail compactor lease (annual payment £21&nbsp;854, annuity-due):
>
> 1 January 2025 — first rental payment received:
>
> | {@{Receive first rental payment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{21&nbsp;854}@} | |
> | {@{Unearned lease revenue}@} | | {@{21&nbsp;854}@} |
>
> 31 December 2025 — recognize revenue for the period:
>
> | {@{Recognize lease revenue for 2025}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unearned lease revenue}@} | {@{21&nbsp;854}@} | |
> | {@{Lease revenue}@} | | {@{21&nbsp;854}@} |
>
> Quinton also records depreciation on the compactor (e.g., double-declining-balance on cost £72&nbsp;000 over 5-year economic life: Year 1 = £72&nbsp;000 × 40% = {@{£28&nbsp;800}@}):
>
> | {@{Record depreciation on leased equipment (Year 1)}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Depreciation expense}@} | {@{28&nbsp;800}@} | |
> | {@{Accumulated depreciation — equipment}@} | | {@{28&nbsp;800}@} |

---

Flashcards for this section are as follows:

- Quinton (operating lessor): why does the compactor fail the finance lease tests? ::@:: Lease term = 43% < 75% (lease term test fails); PV of lessee's payments = 86% < 90% (PV test fails); no other tests met.
- Quinton Equipment operating lessor (annuity-due, payment £21&nbsp;854 received 1 Jan): journal entries on 1 Jan and 31 Dec? ::@:: 1 Jan: Dr _Cash_ £21&nbsp;854 / Cr _Unearned Lease Revenue_ £21&nbsp;854. 31 Dec: Dr _Unearned Lease Revenue_ £21&nbsp;854 / Cr _Lease Revenue_ £21&nbsp;854.

## lessee and lessor asymmetry in classification

IFRS 16 and typical exam scenarios allow the lessee and lessor to classify the SAME lease differently. The lessor applies the five tests strictly. The lessee — under IFRS 16 — capitalizes all leases (except exceptions), so the lessee effectively always has a "finance" type accounting treatment (ROU + LL, with depreciation + interest on the income statement).

---

Flashcards for this section are as follows:

- lessee and lessor asymmetry: is it possible for the same lease to be classified differently? ::@:: Yes — the lessor applies classification tests strictly; the lessee under IFRS 16 capitalizes all leases (except exceptions).
- PV test from lessor's perspective: does unguaranteed residual count? ::@:: No — the lessor compares only the PV of the lessee's contractual payments to the fair value; unguaranteed residual is excluded from the lessee's payments.

### scenario 2 (lessee finance, lessor operating): Reigate and Southwick

> Same lift as Scenario 1, but the economic life is 6 years and there is an {@{unguaranteed residual value of €9&nbsp;600}@} at the end of year 4. Southwick sets payments so that the total PV (payments plus unguaranteed RV) equals the fair value of €48&nbsp;000. Payments: (€48&nbsp;000 − PV of €9&nbsp;600) / PV annuity-due factor = (€48&nbsp;000 − €7&nbsp;056) / 3.57710 = {@{€11&nbsp;447}@} per year.
>
> Southwick's classification tests:
>
> Lease term: 4 / 6 = {@{67%}@} < 75% → fails. PV test: lessee's payments €11&nbsp;447 × 3.57710 = {@{€40&nbsp;944}@} / €48&nbsp;000 = {@{85.3%}@} < 90% → fails. Other tests: no transfer, no BPO, Southwick can re-lease the lift. All five tests fail → {@{Southwick: operating lease}@}.
>
> Reigate (lessee) under IFRS 16 capitalizes: ROU = LL = {@{€40&nbsp;944}@} (no unguaranteed residual). First payment: Dr _Lease liability_ €11&nbsp;447; Cr _Cash_ €11&nbsp;447. Remaining LL = €29&nbsp;497.
>
> Reigate depreciates over 6 years (useful life): {@{€40&nbsp;944 / 6 = €6&nbsp;824}@}/year.
>
> Southwick records only: Dr _Cash_; Cr _Unearned Lease Revenue_ (Jan 1) → Dr _Unearned Lease Revenue_; Cr _Lease Revenue_ (Dec 31).

---

Flashcards for this section are as follows:

- Scenario 2 (Reigate/Southwick): why does Southwick classify as operating while Reigate capitalizes? ::@:: Southwick fails both the lease term test (4/6 = 67% < 75%) and the PV test (85.3% < 90%); Reigate must capitalize under IFRS 16 regardless.
- Reigate/Southwick Scenario 2 (3 annuity-due payments of €11&nbsp;447 at 8%, PV annuity-due factor 3.57710; unguaranteed RV €9&nbsp;600 excluded): Reigate's lease liability? ::@:: LL = €11&nbsp;447 × 3.57710 = €40&nbsp;944; unguaranteed residual excluded because Reigate has no obligation to pay it.
- Reigate/Southwick Scenario 2 (Reigate's ROU = €40&nbsp;944, economic life 6 years, lease term 4 years): depreciation period and annual amount? ::@:: Depreciated over 6 years (economic/useful life) because ownership does not transfer; €40&nbsp;944 ÷ 6 = €6&nbsp;824 per year.

## unguaranteed residual — effect on lessor finance lease

When the lessor classifies a finance lease and the asset has an unguaranteed residual value, the lessor still includes the PV of the unguaranteed residual in the lease receivable (it is part of the lessor's expected recovery). However, the unguaranteed residual reduces __both__ Sales Revenue and COGS from the lessor's day-1 journal entry, keeping gross profit unchanged but recognizing lower revenue up front.

> _Example._ If Southwick (in Scenario 2) had classified the lease as finance rather than operating, the lease receivable would include both the PV of lease payments and the PV of the unguaranteed residual. Sales Revenue and COGS would each be reduced by the PV of the unguaranteed residual (€7&nbsp;056), so gross profit = (Sales Revenue − €7&nbsp;056) − (COGS − €7&nbsp;056) = same gross profit as without the residual._

---

Flashcards for this section are as follows:

- lessor finance lease with unguaranteed residual: how does it affect the day-1 journal entry? ::@:: Deduct the PV of the unguaranteed residual from both _Sales Revenue_ and _COGS_; gross profit is unchanged.
- lessor finance lease: does unguaranteed residual enter the lease receivable? ::@:: Yes — the lessor includes the PV of the unguaranteed residual in the _lease receivable_ (it is the lessor's expected asset recovery at lease end).

### lessor finance lease with unguaranteed residual: Meridian and Cliffdale

> Meridian Equipment Finance (manufacturer/dealer lessor) leases a specialized printing press to Cliffdale Manufacturing (lessee) on 1 January 2025. Key data:
>
> - Fair value (= sales price): {@{€100&nbsp;000}@}; cost on Meridian's books: {@{€78&nbsp;000}@}.
>
> - 5-year non-cancelable lease, annuity-due (payments at start of each year).
>
> - Economic life: {@{6 years}@}; unguaranteed residual value at end of year 5: {@{€10&nbsp;000}@}.
>
> - Implicit rate: {@{8%}@} (not disclosed to Cliffdale, who uses IBR 10%).
>
> __Meridian's lease payment calculation:__
>
> $\text{PV of URV} = 10\,000 / 1.08^5 = 10\,000 / 1.4693 = {@{6\,806}@}$
>
> $\text{Amount to recover from payments} = 100\,000 - 6\,806 = {@{93\,194}@}$
>
> $\text{PV annuity-due, 8\%, 5 periods} = \frac{1 - 1.08^{-5}}{0.08} \times 1.08 = {@{4.3121}@}$
>
> $\text{Annual payment} = 93\,194 / 4.3121 = {@{21\,614}@}$
>
> __Classification tests (Meridian as lessor):__
>
> Lease term: 5 / 6 = {@{83%}@} ≥ 75% → met. PV test: €93&nbsp;194 / €100&nbsp;000 = {@{93.2%}@} ≥ 90% → met. Two tests satisfied → {@{finance (sales-type) lease}@}.

<!-- markdownlint-disable-next-line MD028 -->
> Meridian (FV €100&nbsp;000, cost €78&nbsp;000, annual payment €21&nbsp;614, URV €10&nbsp;000, rate 8%, 5 years) — gross investment, net investment, unearned income, and selling profit:
>
> __Gross investment, net investment, and unearned income:__
>
> $\text{Gross investment} = 5 \times 21\,614 + 10\,000 = {@{118\,070}@}$
>
> $\text{Net investment (= FV)} = 93\,194 + 6\,806 = {@{100\,000}@}$
>
> $\text{Unearned interest income} = 118\,070 - 100\,000 = {@{18\,070}@}$
>
> __Selling profit — same whether residual is guaranteed or unguaranteed:__
>
> | | Unguaranteed RV | Guaranteed RV |
> | --- | ---: | ---: |
> | Sales revenue | {@{93&nbsp;194}@} | 100&nbsp;000 |
> | Cost of goods sold | {@{71&nbsp;194}@} | 78&nbsp;000 |
> | __Selling profit__ | __{@{22&nbsp;000}@}__ | __{@{22&nbsp;000}@}__ |
>
> Both Sales and COGS are reduced by PV(URV) = {@{€6&nbsp;806}@}, leaving gross profit unchanged at {@{€22&nbsp;000}@}. The unguaranteed residual portion is recognized in interest revenue over the lease term rather than on day 1.

<!-- markdownlint-disable-next-line MD028 -->
> Meridian — day-1 journal entries (gross investment method), first payment received, and Year 1 interest revenue:
>
> __Day-1 entries (Meridian — gross investment method):__
>
> | {@{1 January 2025 — recognize finance lease (gross investment method)}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Lease receivable (gross investment)}@} | {@{118&nbsp;070}@} | |
> | {@{Cost of goods sold}@} | {@{71&nbsp;194}@} | |
> | {@{Sales revenue}@} | | {@{93&nbsp;194}@} |
> | {@{Inventory}@} | | {@{78&nbsp;000}@} |
> | {@{Unearned interest income}@} | | {@{18&nbsp;070}@} |
>
> | {@{1 January 2025 — receive first annual payment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{21&nbsp;614}@} | |
> | {@{Lease receivable}@} | | {@{21&nbsp;614}@} |
>
> Net investment after first payment: €100&nbsp;000 − €21&nbsp;614 = {@{€78&nbsp;386}@}.
>
> | {@{31 December 2025 — recognize Year 1 interest revenue}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unearned interest income}@} | {@{6&nbsp;271}@} | |
> | {@{Interest revenue}@} | | {@{6&nbsp;271}@} |
>
> Interest = €78&nbsp;386 × 8% = {@{€6&nbsp;271}@}. Net investment rises to {@{€84&nbsp;657}@}.

<!-- markdownlint-disable-next-line MD028 -->
> __Cliffdale (lessee)__ does not know the implicit rate; uses IBR 10%:
>
> $\text{LL} = 21\,614 \times \underbrace{4.1699}_{\text{PV annuity-due, 10\%, 5 periods}} = {@{€90\,128}@}$
>
> ROU asset = LL = {@{€90&nbsp;128}@}; depreciated over 5 years (lease term, no ownership transfer): €90&nbsp;128 / 5 = {@{€18&nbsp;026}@}/year. Note: Cliffdale's LL (€90&nbsp;128) differs from Meridian's net investment (€100&nbsp;000) because they use different discount rates.
>
> | {@{1 January 2025 — Cliffdale recognizes lease and first payment}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Right-of-use asset}@} | {@{90&nbsp;128}@} | |
> | {@{Lease liability}@} | | {@{90&nbsp;128}@} |
> | {@{Lease liability}@} | {@{21&nbsp;614}@} | |
> | {@{Cash}@} | | {@{21&nbsp;614}@} |

---

Flashcards for this section are as follows:

- lessor: gross investment vs net investment ::@:: Gross investment = total undiscounted receipts (payments + URV); net investment = PV at implicit rate (= FV of asset at inception); unearned income = gross − net.
- lessor finance lease with unguaranteed residual: how does it affect selling profit vs guaranteed residual? ::@:: Selling profit is identical; only the gross revenue and _COGS_ figures differ — both reduced by PV(URV) to defer the unguaranteed portion into _interest revenue_ over the lease term.
- Meridian/Cliffdale (FV = sales price €100&nbsp;000, cost €78&nbsp;000, PV of URV €6&nbsp;806): selling profit calculation ::@:: _Sales_ = €100 000 − €6 806 = €93 194; _COGS_ = €78 000 − €6 806 = €71 194; selling profit = €22 000 (same as FV − cost = 100 000 − 78 000).
- lessor gross investment method: what two accounts carry the lease? ::@:: _Lease Receivable_ (gross investment) and _Unearned Interest Income_ (contra); Net Lease Receivable = Gross − Unearned.
- lessee and lessor: why can LL differ from net investment? ::@:: The lessee uses the implicit rate if known; otherwise IBR. Meridian's net investment = €100 000 at 8%; Cliffdale's LL = €90 128 at 10%.

## special lease features

Executory costs are costs of maintaining the leased asset (insurance, property tax, maintenance). If the lessor includes them in a fixed payment, the lessee includes them in the lease liability calculation (the whole fixed payment is a "lease payment"). If the lessee pays executory costs separately and directly, they are variable costs expensed as incurred.

__Initial direct costs (IDC)__ are incremental costs that would not have been incurred without the lease (e.g., legal fees for a specific lease, commissions).

- __Lessee__: adds IDC to the ROU asset (debit _ROU_, credit _Cash_).
- __Lessor — operating lease__: defers IDC and amortizes over the lease term.
- __Lessor — finance (sales-type) lease__: expenses IDC immediately at commencement, offset against the lease profit.

---

Flashcards for this section are as follows:

- executory costs paid by the lessor and included in the fixed payment: how does the lessee treat them? ::@:: They are part of the fixed lease payment and are included in the _lease liability_ calculation.
- executory costs paid directly by the lessee (not part of the fixed payment): treatment? ::@:: Treated as variable costs; expensed as incurred. They are NOT included in the _lease liability_.
- initial direct costs — lessee treatment ::@:: Added to the ROU asset (debit _ROU asset_, credit _Cash_); amortized as part of depreciation.
- initial direct costs — lessor treatment (operating vs finance) ::@:: Operating: deferred and amortized over the lease term. Finance: expensed immediately at commencement.

### lease modifications and remeasurements

If the lease is modified (e.g., extension agreed), the lessee remeasures the lease liability using a revised discount rate and adjusts the ROU asset. If the extension is for a different asset, it is treated as a new lease.

---

Flashcards for this section are as follows:

- lease modification: how does the lessee remeasure the lease liability and where does the adjustment go? ::@:: Remeasure at PV of revised future payments using a revised discount rate; increase or decrease the _ROU asset_ by the same amount.
- lease modification — same asset extended vs new/different asset: accounting treatment? ::@:: Same asset extended: remeasure _LL_ with revised rate and adjust _ROU_. New or different asset added by the modification: treat the modification as a separate new lease with its own _ROU asset_ and _lease liability_.

## sale-leaseback transactions

In a sale-leaseback, the company sells an asset to an investor (buyer-lessor) and simultaneously leases it back. The key accounting question is whether the transfer of the asset qualifies as a genuine sale.

__Genuine sale.__ If the buyer-lessor obtains control of the asset (IFRS 15 criteria met), the seller-lessee:

1. Derecognizes the asset.
2. Recognizes a gain only for the proportion of rights __transferred__ to the buyer-lessor (IFRS 16.98); the remaining gain is deferred through the ROU asset being measured below the lease liability.
3. Recognizes the leaseback as a new _ROU asset_ + _lease liability_.

Under IFRS 16, the gain recognized = $(\text{Sale price} - \text{Carrying value}) \times \dfrac{\text{FV} - \text{PV(leaseback payments)}}{\text{FV}}$ and the ROU asset = $\text{Carrying amount} \times \dfrac{\text{PV(leaseback payments)}}{\text{FV}}$ (IFRS 16.98).

> Vanderbilt SA (seller-lessee) sells its office building to Westbury Bank (buyer-lessor) on 1 January 2025. Building: cost {@{€800&nbsp;000}@}, accumulated depreciation {@{€200&nbsp;000}@}, carrying value {@{€600&nbsp;000}@}. Sale price = fair value = {@{€660&nbsp;000}@}; total gain = €60&nbsp;000. Vanderbilt simultaneously leases back for 4 of the remaining 15 years; PV of leaseback payments = {@{€330&nbsp;000}@} (50% of FV).
>
> Rights transferred = (€660&nbsp;000 − €330&nbsp;000) / €660&nbsp;000 = {@{50%}@}.
>
> Gain recognized = €60&nbsp;000 × 50% = {@{€30&nbsp;000}@}. ROU asset = €600&nbsp;000 × 50% = {@{€300&nbsp;000}@}.
>
> | {@{1 January 2025 — sale and leaseback combined}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{660&nbsp;000}@} | |
> | {@{Accumulated depreciation}@} | {@{200&nbsp;000}@} | |
> | {@{Right-of-use asset}@} | {@{300&nbsp;000}@} | |
> | {@{Building}@} | | {@{800&nbsp;000}@} |
> | {@{Lease liability}@} | | {@{330&nbsp;000}@} |
> | {@{Gain on sale — rights transferred}@} | | {@{30&nbsp;000}@} |
>
> The lease liability (€330&nbsp;000) exceeds the ROU asset (€300&nbsp;000) by {@{€30&nbsp;000}@} — the deferred gain embedded in the net lease position for rights retained. Only {@{€30&nbsp;000}@} appears in profit.

__Failed sale (finance leaseback).__ If the leaseback is classified as a finance lease, the transfer is __not a genuine sale__ (IFRS 15 conditions not met). The seller-lessee does NOT derecognize the asset; instead, it records the proceeds as a financial liability (borrowing).

> Thornhill Aviation (seller-lessee) sells a wide-body aircraft (carrying value {@{€32&nbsp;400&nbsp;000}@}) to Upton Finance for {@{€36&nbsp;000&nbsp;000}@} and immediately leases it back under a {@{7-year finance leaseback}@}. The transfer fails to qualify as a sale.
>
> | {@{Record failed sale as financing (seller-lessee)}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{36&nbsp;000&nbsp;000}@} | |
> | {@{Financial liability (notes payable)}@} | | {@{36&nbsp;000&nbsp;000}@} |
>
> The aircraft remains on Thornhill's balance sheet. No gain is recognized. Lease payments are split into principal repayment and interest expense on the financial liability.

---

Flashcards for this section are as follows:

- sale-leaseback: the key accounting question ::@:: Does the transfer of the asset qualify as a genuine sale (i.e., does the buyer-lessor obtain control)?
- genuine sale-leaseback: seller-lessee accounting under IFRS 16 ::@:: Derecognize asset; recognize gain proportionate to rights transferred (IFRS 16.98); record leaseback as _ROU asset_ (proportionate carrying amount) + _lease liability_ — not full gain.
- IFRS 16 sale-leaseback: how is the proportionate gain computed? ::@:: Gain recognized = total gain × (FV − PV of leaseback) / FV; _ROU asset_ = previous carrying amount × PV of leaseback / FV.
- Vanderbilt SA (sale price = FV = €660&nbsp;000, carrying value €600&nbsp;000, PV of leaseback payments €330&nbsp;000): proportionate gain recognized ::@:: €60 000 × 50% = €30 000 (rights transferred = 50%); _ROU asset_ = €300 000; the €30 000 deferred portion is embedded in the LL > ROU net position.
- failed sale-leaseback (finance leaseback): accounting for the seller-lessee ::@:: Do not derecognize the asset; record cash received as a financial liability; no gain recognized.
- failed sale-leaseback: why is no gain recognized? ::@:: Because control has not transferred; the arrangement is economically a secured borrowing, not a disposal.

## financial statement presentation

__Lessee.__

__Statement of financial position:__

- ROU assets: presented within non-current assets (separately or included with property, plant, and equipment).
- Lease liabilities: split between current (portion due within 12 months) and non-current.

__Income statement:__

- Finance lease: depreciation expense + interest expense (two separate lines).
- Operating lease (lessee, under the exceptions or where IFRS allows a simpler presentation): single lease cost, straight-line.

__Lessor.__

- Finance lease: Lease receivable on the balance sheet; interest revenue on the income statement.
- Operating lease: Asset on balance sheet; lease revenue on income statement.

Recognizing leases on the balance sheet increases both assets (ROU) and liabilities (LL). Common effects:

- Return on assets (ROA) decreases (same profit over a larger asset base).
- Debt-to-equity ratio increases.
- EBITDA increases: rent expense (which previously reduced EBITDA) disappears and is replaced by depreciation and interest expense — both of which are added back in the EBITDA calculation — so the full former rent cost is removed from EBITDA. EBIT, however, may fall in early years: depreciation + interest in year 1 of the lease typically exceeds the old straight-line rent because interest is front-loaded on a large opening liability, making the total recognized cost higher than the equivalent rent expense.
- Operating cash flow increases: principal repayments on the lease liability shift from operating activities to financing activities in the cash flow statement; only the interest component may remain in operating activities.

---

Flashcards for this section are as follows:

- lessee balance sheet: where are ROU assets and lease liabilities presented? ::@:: ROU assets in non-current assets; lease liabilities split between current (due within 12 months) and non-current.
- lessee income statement — finance lease versus operating (short-term/low-value) exception ::@:: Finance: _depreciation_ + _interest expense_ separately. Exception: single lease cost on a straight-line basis.
- effect of lease capitalization on ROA ::@:: ROA decreases because the asset base grows (ROU asset added) without a corresponding immediate increase in profit.
- lessor operating lease income statement ::@:: Lease revenue recognized straight-line; no sale profit on day 1; asset stays on balance sheet and is depreciated.
- lease capitalization: effect on EBITDA vs EBIT? ::@:: EBITDA increases (rent no longer deducted; depreciation and interest are added back in the EBITDA calculation). EBIT may fall in early years because depreciation + interest on a large opening liability typically exceeds the old straight-line rent.
- lease capitalization: effect on operating cash flow vs financing cash flow? ::@:: Operating cash flow increases; principal repayments on the lease liability shift to financing outflows. Interest paid may remain in operating activities.
- lease capitalization: effect on debt-to-equity ratio? ::@:: Increases, because the lease liability is added as a financial debt; equity is unchanged.
- lease capitalization: why does ROA decrease while EBITDA increases? ::@:: EBITDA rises because rent is removed from the cost base. ROA uses operating profit ÷ total assets; total assets grow (ROU added) and EBIT may also fall in early years — both factors push ROA down.
