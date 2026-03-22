---
aliases:
  - equity
  - equity and dividends
  - equity reporting
tags:
  - flashcard/active/special/academia/HKUST/ACCT_3020/equity
  - language/in/English
---

# equity

This note covers the equity topics in ACCT 3020: issuing shares (for cash and non-cash consideration), share issue costs, preference shares, treasury shares (cost method), and the main types of dividends (cash, property, liquidating, and share dividends). Journal-entry mechanics are collected in `journal entries.md`.

## issuing shares for non-cash consideration

When a company issues shares and receives non-cash assets or services (e.g. land, a patent, or professional services), the transaction is measured at fair value. The measurement hierarchy in this course is:

1. Use the __fair value of the goods or services received__ if it can be measured reliably.
2. If that is not available, use the __fair value of the shares issued__ (e.g. market price on the issue date).
3. If neither is observable, use a __discounted cash flow__ estimate: present value of expected future cash flows from the asset or service.

In all cases, the amount recorded for the asset or service equals the amount credited to equity (share capital at par plus share premium).

---

Flashcards for this section are as follows:

- non-cash share issue: primary measurement basis ::@:: Use the fair value of the goods or services received, if it can be measured reliably.
- non-cash share issue: when to use share fair value? ::@:: When the fair value of the asset/service is not reliably measurable but the fair value of the shares (e.g. market price) is known.
- non-cash share issue: last resort measurement ::@:: Use discounted cash flows (present value of expected future cash flows) when neither asset/service fair value nor share fair value is observable.

## share issue costs: direct versus indirect

Share issue costs are split into:

- __Direct (traceable)__ costs that can be specifically identified with a share issue (e.g. underwriting fees, legal fees for the prospectus, accounting fees for valuation, printing the prospectus).
- __Indirect (allocated)__ costs that relate to running the company more generally (e.g. salaries of the in-house investor relations department, allocated head-office overhead).

Direct share issue costs are deducted from equity: reduce share premium first (and share capital if premium is exhausted). Indirect costs are expensed as incurred (e.g. administrative expense).

---

Flashcards for this section are as follows:

- direct share issue costs: examples and treatment ::@:: Underwriting, legal, accounting, and prospectus printing costs that relate specifically to a share issue; reduce share premium (and share capital if needed), not expensed.
- indirect/allocated share issue costs: examples and treatment ::@:: Ongoing salaries or allocated overhead (e.g. investor relations, head office); not traceable to a specific issue, so expensed as incurred (e.g. administrative expense).

## preference shares: key features

Preference shares give investors priority over ordinary shareholders for dividends and (often) for return of capital on liquidation, but usually with limited or no voting rights. Key variations include:

- __Dividend priority__: fixed rate, paid before ordinary dividends (if declared).
- __Liquidation preference__: receive assets before ordinary shareholders on winding up.
- __Convertible__: may be convertible into ordinary shares under specified terms.
- __Callable__: issuer can redeem (buy back) preference shares under specified terms.
- __Voting__: may be non-voting or have limited voting rights (e.g. only when dividends are in arrears).

Two important labels used in this course are:

- __Cumulative__: if a dividend is not declared in a year, it is "in arrears." In a later year when dividends resume, preference shareholders must receive all arrears plus the current year's preference dividend before any ordinary dividends are paid.
- __Participating__: after preference shareholders receive their stated dividend (and any arrears if cumulative), they also share in any additional dividends with ordinary shareholders, usually in proportion to par value.

Putting "cumulative" and "participating" together gives four patterns for how total dividends are allocated between preference and ordinary shareholders:

- __Non-cumulative, non-participating__: preference shareholders get only this year's stated preference dividend (if declared); all remaining dividend goes to ordinary shareholders. Missed dividends from past years are lost.
- __Cumulative, non-participating__: preference shareholders get any dividends in arrears from prior years __plus__ the current year's stated dividend before any ordinary dividend is paid; whatever is left goes to ordinary shareholders, but preference does not share beyond its fixed amount.
- __Non-cumulative, participating__: preference shareholders get their stated dividend for the current year, ordinary shareholders get a matching "same percentage" on their par, and any extra dividend is shared between the two classes in proportion to par value. There are no arrears because the shares are non-cumulative.
- __Cumulative, participating__: first settle arrears and the current year's preference dividend, then give ordinary shareholders a matching "same percentage" for the current year, and finally share any remaining dividend between preference and ordinary shareholders in proportion to par value.

Intuitively:

- Cumulative preference shares behave like a "dividend debt": unpaid amounts build up and must be cleared before ordinary shareholders can receive anything.
- Participating preference shares behave like "enhanced" preference: after their fixed preference return, they also join the ordinary shareholders in any extra payout based on their relative capital at risk (par value).

However, even for cumulative preference shares, __dividends in arrears are not recorded as a liability__ until the board actually declares the dividend; instead, the arrears are usually disclosed in the notes to the financial statements.

---

Flashcards for this section are as follows:

- preference vs ordinary shares: main economic difference ::@:: Preference shareholders have priority for dividends and often for liquidation proceeds; ordinary shareholders are residual claimants with voting control.
- common features of preference shares ::@:: Fixed dividend, priority in dividends and liquidation, may be convertible or callable, often limited or no voting rights.
- cumulative preference shares ::@:: If dividends are skipped in some years, the unpaid amounts (dividends in arrears) must be paid to preference shareholders before any ordinary dividend is paid in later years.
- participating preference shares ::@:: After receiving their stated dividend (and any arrears if cumulative), participating preference shareholders also share in additional dividends with ordinary shareholders, typically in proportion to par value.
- four preference share patterns: high-level allocation ::@:: Non-cumulative/non-participating: preference gets only this year's fixed dividend; cumulative/non-participating: pay arrears plus current fixed dividend before ordinary; non-cumulative/participating: pay fixed dividends on both classes, then share extra based on par; cumulative/participating: clear arrears and current preference, match current ordinary rate, then share any remaining dividend based on par.
- dividends in arrears: liability or disclosure? ::@:: For cumulative preference shares, unpaid dividends accumulate as "dividends in arrears" and are disclosed in the notes, but no Dividends payable liability is recognised until the board declares the dividend.

## treasury shares (cost method)

Treasury shares are the company's own shares that it has repurchased. Under the cost method used in this course:

- On repurchase, debit `Treasury shares` at __cost__ and credit `Cash`.
- `Treasury shares` is a __contra-equity__ account (reduces total equity), not an asset and not an expense.
- On reissue above cost: credit `Treasury shares` at cost and credit `Share premium — treasury` for the excess.
- On reissue below cost: first use any existing `Share premium — treasury` balance; any further shortfall is debited to retained earnings (not treated as a loss in profit or loss).

Management often repurchases shares when they believe the shares are undervalued or to adjust capital structure.

---

Flashcards for this section are as follows:

- treasury shares (cost method): acquisition entry ::@:: Dr Treasury shares at cost, Cr Cash; Treasury shares is a contra-equity account, not an asset.
- treasury shares reissued above cost: equity effect ::@:: Credit Treasury shares at cost and credit Share premium — treasury for the excess over cost.
- treasury shares reissued below cost: equity effect ::@:: Debit Share premium — treasury first and then retained earnings for any remaining shortfall; no loss is recognised in profit or loss.

## dividends: cash, property, liquidating, and share

__Cash dividends.__ Three key dates:

- __Date of declaration__: recognise liability (Dr Retained earnings; Cr Dividends payable).
- __Date of record__: no journal entry (used to determine which shareholders receive the dividend).
- __Date of payment__: pay cash (Dr Dividends payable; Cr Cash).

__Property dividends.__ When dividends are paid in non-cash assets (e.g. investment shares, inventory), first remeasure the asset to fair value (recognising any unrealised gain or loss in income, per course convention), then:

- Dr Retained earnings (at fair value of the property), Cr Property dividend payable.
- On distribution: Dr Property dividend payable, Cr Asset (at fair value).

__Liquidating dividends.__ When a dividend exceeds retained earnings and represents a return of capital (often in liquidation), the dividend is split into:

- Part from retained earnings (return of profit).
- Part from contributed capital (e.g. share premium, then share capital).

__Share dividends.__ The company issues additional shares to existing shareholders instead of paying cash. In this course, small share dividends are recorded at par value:

- On declaration: Dr Retained earnings (par value × number of new shares), Cr Ordinary share dividend distributable.
- On issuance: Dr Ordinary share dividend distributable, Cr Share capital (par value).

Total equity is unchanged by a small share dividend, but the composition shifts from retained earnings to share capital.

---

Flashcards for this section are as follows:

- cash dividend: journal entries on declaration and payment ::@:: Date of declaration: Dr Retained earnings, Cr Dividends payable; date of payment: Dr Dividends payable, Cr Cash; no entry on date of record.
- property dividend: two-step accounting ::@:: First remeasure the asset to fair value (recognise unrealised gain or loss); then Dr Retained earnings and Cr Property dividend payable at fair value, followed by Dr Property dividend payable and Cr Asset on distribution.
- liquidating dividend: how to split? ::@:: Amount up to retained earnings is treated as a normal dividend; any excess is treated as a return of capital (reduce share premium first, then share capital).
- share dividend (small): effect on equity ::@:: Total equity unchanged; Retained earnings decreases and Share capital increases by the par value of new shares via Ordinary share dividend distributable.
- dividend types in this course ::@:: Cash dividends reduce total equity and working capital; property and liquidating dividends also reduce total equity; small share dividends do not change total equity but reclassify amounts within equity (Retained earnings to Share capital).
- dividend calculations (overview) ::@:: Cash dividend = dividend per share × number of shares; property dividend measured at fair value of asset; liquidating dividend is split between Retained earnings (income portion) and Share premium/Share capital (return of capital); small share dividend amount = par value × number of new shares issued (e.g. % × existing shares × par).

## return on ordinary shareholders' equity (ROE)

Return on ordinary shareholders' equity measures how efficiently a company generates profit for ordinary shareholders based on the equity they have invested and retained. In this course, ROE focuses on the return available to ordinary shareholders __after__ preference dividends.

The basic formula is:

- __ROE__ = {@{(Profit for the year − Preference dividends) ÷ Average ordinary shareholders' equity}@}.

Where:

- Profit for the year is profit after tax.
- Preference dividends (on cumulative preference shares) include both current-year dividends and any dividends in arrears that relate to the year.
- Average ordinary shareholders' equity is typically the average of ordinary share capital plus reserves and retained earnings attributable to ordinary shareholders (beginning and ending balances).

Intuitively:

- ROE answers "for each dollar of ordinary shareholders' equity, how many dollars of profit (after preference claims) did the company generate this year?"
- Higher ROE suggests more efficient use of ordinary shareholders' capital, but differences in leverage, business risk, and accounting policies must be considered when comparing firms.

---

Flashcards for this section are as follows:

- ROE: formula in this course ::@:: (Profit for the year − Preference dividends) ÷ Average ordinary shareholders' equity.
- ROE: why subtract preference dividends? ::@:: Because ROE is meant to measure the return available to ordinary shareholders after satisfying the fixed claims of preference shareholders.
- ROE: what goes into ordinary shareholders' equity? ::@:: Ordinary share capital plus reserves and retained earnings attributable to ordinary shareholders, usually averaged over the period (beginning and ending).
- ROE: intuitive interpretation ::@:: For each dollar of ordinary shareholders' equity invested in the company, ROE shows how many dollars of profit (after preference dividends) were generated during the year.

## share dividends versus share splits

Both share dividends and share splits increase the number of shares outstanding, but their accounting effects differ:

- A __share dividend__ transfers an amount from retained earnings to share capital (and possibly share premium); total equity is unchanged, but the mix between retained earnings and share capital changes. Par value per share stays the same; number of shares increases.
- A __share split__ (e.g. 2-for-1) changes par value and the number of shares (par per share halves and share count doubles in a 2-for-1 split) but does not change total share capital or retained earnings; no journal entry is recorded in this course.

---

Flashcards for this section are as follows:

- share dividend vs share split: key accounting difference ::@:: Share dividend transfers retained earnings to share capital (par unchanged; shares ↑); share split changes par per share and number of shares but leaves share capital and retained earnings unchanged (no journal entry).
- 2-for-1 share split: effect on par and shares ::@:: Par value per share halves and the number of shares doubles; total share capital remains the same.

## retained earnings and reserves

Retained earnings represent cumulative profit not yet distributed as dividends; in this course, they also act as a legal cap on dividends (the company cannot declare dividends in excess of retained earnings, except for liquidating dividends). Sometimes management transfers part of retained earnings to a separate reserve within equity (e.g. "capital expenditure reserve") to signal that those profits are earmarked for a specific purpose and not intended for ordinary dividends.

---

Flashcards for this section are as follows:

- retained earnings: practical meaning in dividend decisions ::@:: Cumulative profit not yet distributed; acts as an upper limit on ordinary dividends (company generally cannot declare dividends greater than retained earnings).
- reserves within equity: why transfer from retained earnings? ::@:: To earmark part of retained earnings for a specific purpose (e.g. future capital expenditure) and signal that it is not intended for ordinary dividends.
