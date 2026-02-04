---
aliases:
  - ACCT 3010 depreciation
  - ACCT3010 depreciation
  - HKUST ACCT 3010 depreciation
  - HKUST ACCT3010 depreciation
  - depreciation
tags:
  - flashcard/active/special/academia/HKUST/ACCT_3010/depreciation
  - language/in/English
---

# depreciation

- HKUST ACCT 3010

---

- see: [general/depreciation](../../../../general/depreciation.md)

__Depreciation__ is a systematic and rational allocation of the cost of long‑lived assets over the periods in which those assets are expected to provide economic benefit.  The expense recognised each period reflects the consumption of the asset’s value, while accumulated depreciation reduces the carrying amount on the balance sheet.

_Amortization_ is similar to depreciation, but applies to _intangible assets_. _Depletion_ is also similar, but applies to natural resources, where the cost of extracted reserves is allocated over the period of extraction.

## factors

The calculation of depreciation requires answering three basic questions: What depreciable base is used? $$\text{Depreciable Base}= \text{Original Cost}-\text{Residual Value}$$ What is the asset’s useful life? And which method of cost apportionment best reflects the pattern of benefit?

Service lives differ from physical lives because assets are retired for _physical_ reasons (wear, damage) or _economic_ reasons (obsolescence, supersession).  Maintenance can extend service life; technological change can reduce it via obsolescence.

_Impairments_ occur when an asset’s recoverable amount falls below its carrying value; the loss is recognised immediately and may be reversed if circumstances improve.

## depreciation methods

No matter which depreciation method is used, the journal entries are similar: credit from "_accumulated depreciation_" (optionally with the asset type) and debit to "_depreciation expense_".

### activity method

Depreciation is tied to units of use: $$\text{depreciation charge} = \frac {(\text{cost} - \text{residual}) \times \text{used units} } {\text{estimated total units} } \,.$$

_Example_: a crane costing \$500 000 with a salvage value of \$50 000 and an estimated productive life of 30 000 hours.  If the crane operates 4 000 hours in year 1, depreciation is  $$(\$500\,000-\$50\,000)\times \frac{4\,000}{30\,000}= \$60\,000.$$

### straight-line method

Depreciation is spread evenly over the useful life: $$\text{depreciation charge} = \frac {\text{cost} - \text{residual} } {\text{estimated service life} } \,.$$

_Example_: a crane costing \$500 000 with a salvage value of \$50 000 and an estimated useful life of 5 years: $$\frac{\$500\,000-\$50\,000}{5} = \$90\,000 \text{ per year}.$$

### sum-of-the-years'-digits method

The _sum‑of‑the‑years’‑digits_ method accelerates depreciation by allocating larger expenses early in an asset’s life and smaller amounts later.  For an asset with a useful life of _n_ years, the denominator is the sum of the integers from 1 to _n_ (for example, for a five‑year life the sum is $5+4+3+2+1=15$).  In year k (with k counted starting at 1 from the first year), the depreciation fraction equals $(n-k+1)/15$.  Multiplying this fraction by the depreciable base—original cost minus residual value—yields the yearly expense.  Thus, in the first year a five‑year asset would be depreciated at $5/15$ of its basis (one‑third), with the rate declining each subsequent year.

_Example_: a crane costing \$500 000 with a salvage value of \$50 000 and an estimated useful life of 5 years. For a 5‑year life, the denominator is $5+4+3+2+1=15$.  Year 1 expense: $\frac{5}{15}\times (\$500\,000-\$50\,000)= \$150\,000$.

### declining balance

The _declining‑balance_ method, often implemented as double‑declining balance, applies a fixed depreciation rate to the _book value_ (which includes the _residual value_, thus is _not_ the depreciable base!) at the beginning of each period.  The rate is typically twice the straight‑line percentage (for example, a ten‑year life yields a straight‑line rate of 10%, so the double‑declining rate is 20%).  Depreciation for year 1 equals this rate times the asset’s cost; thereafter the same rate multiplies the reduced book value.

The expense decreases over time because the base shrinks, but the method never depreciates below the residual value—any excess depreciation is capped to preserve that minimum balance. The method may also depreciate the asset insufficiently enough for its book value to reach the residual value by the end of its useful life; in that case for the last year, ignore the method and depreciate the asset such that its book value matches the residual value.

_Example_: a crane costing \$500 000 with a salvage value of \$50 000 and an estimated useful life of 5 years. Rate = twice the straight‑line rate (20%×2=40%).  Year 1: $0.40\times \$500\,000= \$200\,000$. The expense is capped so that book value never falls below residual value.

## impacts

_Impact on Rate of Return_: Since depreciation decreases asset, but typically does not affect income generated by the asset significantly, the rate of return for that asset increases over time.

_Impact on Return on Assets_: A high‑growth company such as Tesla retains large undepreciated property, plant and equipment (PPE), while an older automaker like Ford has largely depreciated PPE.  The difference in asset age distorts ROA calculations: fully depreciated assets generate income without further depreciation expense, lowering net income but also reducing the asset base that appears in the denominator.

## component depreciation

IFRS requires significant parts of an asset to be depreciated separately.  

Example: an airplane costing €100 000 000 with a 20‑year life and zero residual value is split into airframe (€60 M, 20 years), engines (€32 M, 8 years) and other components (€8 M, 5 years).  Annual depreciation per component: $$\frac{60\,000\,000}{20}=3\,000\,000,\quad\frac{32\,000\,000}{8}=4\,000\,000,\quad\frac{8\,000\,000}{5}=1\,600\,000,$$ totaling €8 600 000 for the year.

## partial periods

When an asset is bought or sold partway through a reporting period, its depreciation must be proportionally adjusted so that the expense reflects only the days it was actually in service.  Companies typically calculate the full‑year depreciation using the chosen method and then multiply by the fraction of the year during which the asset was owned. The fraction may differ according to different _fractional-year policies_; see below.

_Example_: a machine costing £45 000 with no residual value bought on 10 June 2025 has a straight‑line yearly expense of £9 000.  The first partial year (6⅔ months) accrues  $$\frac{6 + 2 / 3}{12}\times 9\,000 = £5\,000.$$ Accelerated methods follow the same prorating logic. Note that the fraction used for partial year can be different using different _fractional-year policies_; see below.

For assets bought or sold mid‑year, companies may adopt one of several _fractional‑year rules_ to prorate depreciation. Each method balances simplicity against accuracy, with firms choosing based on accounting policy or regulatory guidance.

- _Nearest fraction of a year_ ::@:: – the period is rounded to the nearest whole fraction (e.g., 6⅔ months for 10 June), using that proportion of the annual charge; <!--SR:!2026-03-14,55,310!2026-03-24,61,310-->
- _Nearest full month_ ::@:: – each month counts as one‑twelth of a year, so the depreciation for a purchase on 10 June would be $\frac{7}{12}$ of the yearly amount; <!--SR:!2026-03-21,58,310!2026-03-22,59,310-->
- _Half‑year rule_ ::@:: – the asset is treated as if it had been in service for exactly six months regardless of the actual acquisition date, simplifying calculation but potentially overstating or understating depreciation; <!--SR:!2026-03-20,57,310!2026-03-13,54,310-->
- _Full year in acquisition, none in disposal_ ::@:: – a new asset receives a full yearly charge even though it was only owned part‑time, while an asset sold before year’s end receives no depreciation for that period; <!--SR:!2026-03-17,58,310!2026-03-15,56,310-->
- _None in acquisition, full year in disposal_ ::@:: – the reverse of the previous rule: the newly acquired asset is not depreciated until the next fiscal year, but a disposed asset still accrues a full yearly charge for the period it was held. <!--SR:!2026-03-27,64,310!2026-03-30,67,310-->

## revision of depreciation rates

Revising depreciation rates is treated as an estimate change rather than an error.  When a company discovers that its original useful‑life assumption was too short, the firm reports the new estimate only in current and future periods, leaving prior results unchanged.  The adjustment is made by recalculating depreciation on the remaining book value (cost minus accumulated depreciation) divided by the revised remaining life. This prospective approach aligns with accounting standards that view changes in useful lives as part of the normal estimation process rather than errors requiring restatement.

_Example_: for Nestlé, after ten years the asset’s carrying amount was CHF45 000, and with an additional twenty‑year _remaining_ life the new annual charge became $\frac{45\,000}{20}=\text{CHF}\,2\,250$.

When a company changes its estimate of an asset’s remaining useful life while it is depreciating the asset on a _double‑declining balance_ basis, the new rate is applied only to the updated book value at the beginning of each future period.  The double‑rate (twice the straight‑line percentage) is recalculated based on the revised life (not revised _remaining_ life), and depreciation for subsequent years is computed as this new rate times the asset’s current carrying amount (not _depreciable base_).  Prior depreciation charges remain unchanged; the change is disclosed prospectively.

_Example_: Adapting Nestlé’s example to a double‑declining balance method: after ten years the machinery still carries CHF45 000.  If the company originally used a straight‑line rate of 5% (20 years) but now estimates a 30‑year life, the revised straight‑line rate would be $1/30\approx3.33\,\%$.  The double‑declining rate therefore becomes $2/30 \approx 6.67\,\%$.  Depreciation for year 11 would then be $\frac 2 {30} \times45\,000= \text{CHF}\,3\,000$, and this new charge applies to all future periods until the asset is fully depreciated.

## impairments

An asset is impaired when a company cannot recover its carrying amount either by using it or selling it.  Companies review each asset annually for indicators of impairment, such as a decline in cash‑generating ability.  The test compares the asset’s _recoverable amount_—the higher of fair value less costs to sell and value‑in‑use—to its carrying amount.  If recoverable amount is less than carrying amount, an impairment loss equals the difference. The journal entry is: credit from "_accumulated depreciation_" (optionally with the asset type) and debit to "_loss on impairment_".

_Example_: A company has equipment with a carrying amount of €200 000.  Its fair value less costs to sell is €180 000 and its value‑in‑use is €205 000.  Because value‑in‑use is higher than the carrying amount, no loss is recorded.  If the value‑in‑use were €175 000, the impairment loss would be $$200\,000-\max(180\,000,\;175\,000)=20\,000 \,.$$

> [!example] __impairment and revision__
>
> At 31 Dec 2026, equipment cost VND26 000 000 with accumulated depreciation VND12 000 000, giving a carrying amount of VND14 000 000.  Straight‑line depreciation on the original life (4 years, residual VND2 000 000) produced VND6 000 000 for 2026. _After_ accounting for straight-line depreciation, the recoverable amount was determined to be VND11 000 000; therefore a loss of $$14\,000\,000-11\,000\,000=3\,000\,000$$ was recorded.
>
> The subsequent depreciation entry for 2027 used the revised residual value (now zero) and remaining life (2 years): $$\text{Depreciation Expense}= \frac{26\,000\,000-0}{4}=5\,500\,000 .$$

---

> [!example] __calculating value-in-use__
>
> A machine with carrying amount $200 000 and remaining useful life 5 years was tested.  Because market data were scarce, value‑in‑use was estimated using a discount rate of 8 %.  Cash flows of $40 000 per year for five years plus a residual $10 000 gave a present value of $166 514.20.  The impairment loss is $$200\,000-166\,514=33\,486 .$$

### impairment reversal

When the circumstances that caused an impairment change, a company may recover part or all of the previously recorded loss; however, the reversal cannot exceed the amount of the original impairment.  The asset’s carrying amount is increased only up to the level it had before the impairment was first recognized, ensuring that earnings are not overstated by more than the initial write‑down. The journal entry is: credit from "_recovery of impairment loss_" and debit to "_accumulated depreciation_" (optionally with the asset type).

_Example_: A company purchased equipment on 1 Jan 2025 for HK$300 000, depreciated straight‑line over three years.  In 2025 an impairment loss of HK$20 000 was _additionally_ recorded, reducing the carrying amount from HK$200&nbsp;000 to HK$180&nbsp;000. When the recoverable amount rose to HK$96 000 in 2026—greater than the new carrying value of HK$90 000—the company reversed $6 000 of the earlier loss, restoring the asset’s book value to HK$96 000.

### cash-generating units

For impairment purposes, when a single asset cannot be assessed independently because its cash flows arise only in concert with other assets, companies group them into the smallest set that can generate cash flows on their own.  These groups are called _cash‑generating units_ (CGUs).  Impairments are tested at CGU level.

### assets held for disposal

Assets held for sale or disposal are reported at the lower of cost and fair value less costs to sell, similar to _inventory_; no depreciation or amortization is taken while they remain in that category. However, unlike inventory, their carrying amount may be adjusted up or down as long as it never exceeds the pre‑impairment book value.

## revaluation

Revaluation is a method whereby _long‑lived tangible_ assets are measured at fair value rather than historical cost after acquisition. Land, and assets that are depreciated, such as equipment or machinery, can be revalued. The journal entry is: Debit or credit the asset account such that it matches the new fair value. Then, recognize gains or losses using the correct account.

An _upward_ revaluation, if there is no previous impairment loss, creates an "_unrealized gain on revaluation_" that is recognised in other comprehensive income (OCI) and carried in equity; otherwise, it reverses a previous impairment loss first being affecting OCI. Similarly, a _downward_ revaluation, i.e. impairment, first reduces unrealized gain in OCI before affecting profit or loss via "_loss on impairment_". Note, due to special handling depreciation (mentioned below), it is possible for both impairment loss and unrealized gain to have positive normal balances.

When the relevant assets are sold, any remaining unrealized gain are reclassified as net income (i.e. _realizing_ the gain) by crediting "_retained earnings_" and debiting "_accumulated other comprehensive income_", effectively _netting_ the "_unrealized gain on revaluation_" balance. However, any "accumulated" impairment loss is not transferred, as impairment loss itself is already a realized expense.

### revaluation issues

A company may choose to revalue only one _class of assets_, such as buildings, while leaving other classes—land, equipment, etc.—at cost.  When a specific class is selected, the revaluation applies _to all assets within that class_; an asset class is a grouping of items that share a similar nature and use in the company’s operations.  Firms must also make every effort to keep these values up‑to‑date, ensuring that each revalued group accurately reflects current market realities.

Network Rail Limited elected to use fair value for its railway network.  In the year ending 31 Mar 2023, the company increased long‑lived tangible assets by £4&nbsp;289 million.  The revaluation reflects changes in market conditions, indexation and borrowing costs, illustrating how a large infrastructure asset can be treated as a single class for revaluation purposes.

### reevaluation of land

Handling reevaluation of land is simpler because depreciation does not need to be considered. The journal entry is: Debit or credit the asset account such that it matches the new fair value. Then, recognize gains or losses using the correct account.

> [!example] __land__
>
> On 1 Jan 2025 the land cost €400 000.  At 31 Dec 2025 its fair value was €520 000, an increase of €120 000.
>
> ```text
> Land                                       120 000
>     Unrealised Gain on Revaluation – Land           120 000
> ```
>
> The gain appears in OCI and the land is reported at €520 000. On 31 Dec 2026 the fair value fell to €380 000, a decline of €140 000.  The unrealised gain is reduced and an impairment loss is recognised.
>
> ```text
> Unrealised Gain on Revaluation – Land  120 000
> Loss on Impairment                      20 000
>     Land                                        140 000
> ```
>
> The remaining impairment loss of €20 000 reduces net income. On 31 Dec 2027 the land value rose to €415 000; the previous impairment is reversed and the residual increase is added to OCI.
>
> ```text
> Land                                       35 000
>     Recovery of Impairment Loss                    20 000
>     Unrealised Gain on Revaluation – Land          15 000
> ```
>
> When the land was sold on 2 Jan 2028 for €415 000, the cash entry and the transfer of the remaining OCI to retained earnings were recorded:
>
> ```text
> Cash                                    415 000
>    Land                                          415 000
> Accumulated Other Comprehensive Income   15 000
>    Retained Earnings                              15 000
> ```
>
> Note that any "accumulated" impairment loss is not transferred, as impairment loss itself is already an expense.

### reevaluation of depreciable assets

Handling reevaluation of depreciable assets is harder because depreciation needs to be considered. Whenever a reevaluation happens, first _reset_ the asset's "_accumulated depreciation_" as if the asset is newly purchased. Then the remaining steps are similar to reevaluation of land.

The new carrying amount becomes the basis for all future depreciation calculations.  If the revaluation increases the asset’s value, the remaining useful life (or any revised estimate of it) is applied to the higher figure, which usually raises the periodic depreciation expense.  Conversely, a downward revaluation may trigger an impairment loss that is charged directly to profit or loss; after the loss, depreciation is calculated on the reduced carrying amount, often resulting in lower expenses for the remaining life.

To account for this difference in depreciation, companies _may transfer_ between "_retained earnings_" and "_accumulated other comprehensive income_", where the latter _effectively_ affects the "_unrealized gain on revaluation_" balance simultaneously. First, compute how much the asset has increased (or decreased if negative) by subtracting the unrealized gain (accounting for previous transfers) by the impairment loss. If zero, no transfer is needed. Otherwise, subtract the carrying value by this amount, and then use it to calculate the depreciation expense as if there were at its original depreciation schedule. Finally, subtract it from the actual depreciation expense to calculate the _excess_ (or _missing_ if negative) depreciation expense. If positive, then transfer this difference from "RE" to "AOCI" (decreasing the unrealized gain balance) to realize part of the gain and expend it as depreciation expense. If negative, then transfer this difference from "AOCI" to "RE" (increasing the unrealized gain balance) to record unrealized gain due to impairment decreasing depreciation expense.

> [!example] __depreciable assets__
>
> On 2 Jan 2025 the company bought equipment for ¥500 000 and straight‑line depreciation of ¥100 000 was recorded at 31 Dec 2025.
>
> ```text
> Depreciation Expense                      100 000
>     Accumulated Depreciation – Equipment           100 000
> ```
>
> An appraisal on that date gave a fair value of ¥460 000.  The revaluation is made by removing the accumulated depreciation (as if the assets were new), reducing the asset account, and recognising an unrealised gain.
>
> ```text
> Accumulated Depreciation – Equipment            100 000
>     Equipment                                            40 000
>     Unrealised Gain on Revaluation – Equipment           60 000
> ```
>
> The equipment is now carried at ¥460 000. Subsequent depreciation needs to consider unrealized gain or impairment loss; see the more complex example below.

---

> [!example] __depreciable assets, more complex__
>
> In 2025, after recording €200 000 of depreciation (5 years of life), the asset’s carrying amount was €800 000.  An appraisal valued it at €950 000; revaluation involved zeroing accumulated depreciation and reducing the equipment account.
>
> ```text
> Accumulated Depreciation – Equipment            200 000
>     Equipment                                             50 000
>     Unrealised Gain on Revaluation – Equipment           150 000
> ```
>
> In 2026, after further depreciation of €237 500 (with 4 years of remaining life) to a book value of €712&nbsp;500. Note the original depreciation would have been €200&nbsp;000.
>
> ```text
> Accumulated Other Comprehensive Income  37 500
>     Retained Earnings                           37 500
> ```
>
> Remaining balance in unrealized gain is €112&nbsp;500. In the same year 2026, a new appraisal gave a fair value of €570 000.  The entry to reset accumulated depreciation, adjust the asset and recognise impairment was:
>
> ```text
> Accumulated Depreciation – Equipment        237 500
> Loss on Impairment                           30 000
> Unrealised Gain on Revaluation – Equipment  112 500
>     Equipment                                        380 000
> ```
>
> In 2027, after depreciation of €190 000 (3 years of remaining life) to a book value of €380&nbsp;000. Note the original depreciation would have been €200&nbsp;000.
>
> ```text
> Retained Earnings                           10 000
>     Accumulated Other Comprehensive Income          10 000
> ```
>
> Remaining balance in unrealized gain is €10&nbsp;000. In the same year 2027, a revaluation to €450 000, the following was recorded, splitting the gain of €70&nbsp;000 between impairment reversal first and then unrealized gain:
>
> ```text
> Accumulated Depreciation – Equipment        190 000
>     Recovery of Loss on Impairment                    30 000
>     Unrealised Gain on Revaluation – Equipment        40 000
>     Equipment                                        120 000
> ```
>
> Finally, when Nokia sold the equipment on 2 Jan 2028 for €450 000, no gain or loss was recognised because the carrying amount equalled fair value.  The residual OCI balance was transferred to retained earnings:
>
> ```text
> Cash                                    450 000
>     Equipment                                    450 000
> Accumulated Other Comprehensive Income   50 000
>     Retained Earnings                             50 000
> ```
