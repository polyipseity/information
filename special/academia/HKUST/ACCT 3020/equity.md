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

This note covers the equity topics in ACCT 3020: issuing shares (for cash and non-cash consideration), share issue costs, preference shares, treasury shares (cost method), and the main types of dividends (cash, property, liquidating, and share dividends). The worked journal-entry examples are integrated directly into the relevant sections below.

## issuing shares for non-cash consideration

When a company issues shares and receives non-cash assets or services (e.g. land, a patent, or professional services), the transaction is measured at fair value. The measurement hierarchy in this course is:

1. Use the __fair value of the goods or services received__ if it can be measured reliably.
2. If that is not available, use the __fair value of the shares issued__ (e.g. market price on the issue date).
3. If neither is observable, use a __discounted cash flow__ estimate: present value of expected future cash flows from the asset or service.

In all cases, the amount recorded for the asset or service equals the amount credited to equity (share capital at par plus share premium).

__Special case: Fair value below par.__ Occasionally, the fair value of the asset received is less than the par value of shares issued. Because _Share capital_ must be credited at par (the legal stated capital), any shortfall creates a debit balance on _Share premium — ordinary_. Under IFRS this is permissible for this specific scenario, though it is rare in practice.

Representative journal entry examples:

> _Astera case 1._ Astera Biotech plc issues {@{10 000 ordinary shares, par 10}@} in exchange for a patent portfolio. The fair value of the patent portfolio is not reliably known, but the shares trade at {@{140 000}@}.
>
> | {@{Issue ordinary shares for patent (measure at share fair value)}@} | Dr            | Cr            |
> | -------------------------------------------------------------------- | ------------- | ------------- |
> | {@{Patents}@}                                                        | {@{140 000}@} |               |
> | {@{Share capital — ordinary (10 000 × 10)}@}                         |               | {@{100 000}@} |
> | {@{Share premium — ordinary}@}                                       |               | {@{40 000}@}  | <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _Astera case 2._ The fair value of Astera's shares is not known, but the patent portfolio's fair value is {@{150 000}@}.
>
> | {@{Issue ordinary shares for patent (measure at patent fair value)}@} | Dr            | Cr            |
> | --------------------------------------------------------------------- | ------------- | ------------- |
> | {@{Patents}@}                                                         | {@{150 000}@} |               |
> | {@{Share capital — ordinary (10 000 × 10)}@}                          |               | {@{100 000}@} |
> | {@{Share premium — ordinary}@}                                        |               | {@{50 000}@}  | <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _Astera case 3._ Neither the share fair value nor the patent-portfolio fair value is observable; an independent consultant values the portfolio at {@{125 000}@} based on discounted expected cash flows.
>
> | {@{Issue ordinary shares for patent (measure at DCF value)}@} | Dr            | Cr            |
> | ------------------------------------------------------------- | ------------- | ------------- |
> | {@{Patents}@}                                                 | {@{125 000}@} |               |
> | {@{Share capital — ordinary (10 000 × 10)}@}                  |               | {@{100 000}@} |
> | {@{Share premium — ordinary}@}                                |               | {@{25 000}@}  |
>
> _Explanation._ In each case, the asset is recorded at its measured fair value and equity is credited for the same amount (par plus premium); only the measurement basis (shares, patent, or discounted cash flows) changes. <!--SR:!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _Astera case 4: fair value below par._ Astera Biotech plc issues {@{10 000 ordinary shares}@}, par {@{10 each, so total par value is 100 000}@}, for a patent portfolio whose fair value is only {@{85 000, leaving a 15 000 shortfall below par}@}.
>
> | {@{Issue shares for patent — fair value (85 000) below total par (100 000)}@} | Dr            | Cr            |
> | ----------------------------------------------------------------------------- | ------------- | ------------- |
> | {@{Patents}@}                                                                 | {@{85 000}@}  |               |
> | {@{Share premium — ordinary (shortfall/discount)}@}                           | {@{15 000}@}  |               |
> | {@{Share capital — ordinary (10 000 × 10)}@}                                  |               | {@{100 000}@} |
>
> _Explanation._ _Share capital_ is credited at the full par amount of {@{100 000 for the 10 000 ordinary shares issued}@}. The asset is recorded at its fair value of {@{85 000 for the patent received}@}. The balancing debit of {@{15 000 falls on Share premium — ordinary}@}, giving it a {@{debit (negative) balance instead of the usual credit premium balance}@}. Under IFRS this is permissible but unusual. <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288-->

<!-- markdownlint-disable-next-line MD028 -->
> _Follow-on share issue that partly cures the negative premium._ After the below-par Astera patent issue above, the company later issues {@{5 000 additional ordinary shares with par 10 for cash of 60 000}@}. The new issue creates a normal premium of {@{10 000}@}, which offsets part of the earlier {@{15 000 debit balance in Share premium — ordinary}@}.
>
> | {@{Issue additional ordinary shares and partly offset the earlier negative premium balance}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{60 000}@} | |
> | {@{Share capital — ordinary}@} | | {@{50 000}@} |
> | {@{Share premium — ordinary}@} | | {@{10 000}@} |
>
> _Explanation._ The new positive premium does {@{not erase the earlier debit balance automatically}@}; it simply reduces the running {@{debit balance in Share premium — ordinary from 15 000 to 5 000}@}. <!--SR:!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321-->

---

Flashcards for this section are as follows:

- non-cash share issue: primary measurement basis ::@:: Use the fair value of the goods or services received, if it can be measured reliably. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- non-cash share issue: when to use share fair value? ::@:: When the fair value of the asset/service is not reliably measurable but the fair value of the shares (e.g. market price) is known. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- non-cash share issue: last resort measurement ::@:: Use discounted cash flows (present value of expected future cash flows) when neither asset/service fair value nor share fair value is observable. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- non-cash share issue (patent): general entry structure ::@:: Dr _Patents_ (or other asset) at fair value; Cr _Share capital — ordinary_ at par; Cr _Share premium — ordinary_ for the excess over par. <!--SR:!2026-04-12,4,288!2026-04-12,4,299-->
- non-cash share issue: measurement hierarchy in examples ::@:: Use (1) fair value of goods/services received, (2) if unavailable, fair value of shares issued, and (3) if neither is observable, discounted cash flow value of the asset/service. <!--SR:!2026-04-12,4,299!2026-04-12,4,299-->
- non-cash share issue example (Astera case 1): patent portfolio for 10 000 shares, share FV 140 000, par 10—entry? ::@:: Dr _Patents_ 140 000; Cr _Share capital — ordinary_ 100 000; Cr _Share premium — ordinary_ 40 000. <!--SR:!2026-04-12,4,299!2026-04-12,4,299-->
- non-cash share issue example (Astera case 2): patent-portfolio FV 150 000 for 10 000 shares, par 10—entry? ::@:: Dr _Patents_ 150 000; Cr _Share capital — ordinary_ 100 000; Cr _Share premium — ordinary_ 50 000. <!--SR:!2026-04-12,4,299!2026-04-12,4,299-->
- non-cash share issue example (Astera case 3): patent-portfolio DCF value 125 000 for 10 000 shares, par 10—entry? ::@:: Dr _Patents_ 125 000; Cr _Share capital — ordinary_ 100 000; Cr _Share premium — ordinary_ 25 000. <!--SR:!2026-04-12,4,288!2026-04-12,4,299-->
- non-cash share issue: fair value below par—how to record? ::@:: General entry: Dr _Patents_ at fair value, Dr _Share premium — ordinary_ for the shortfall (debit balance), Cr _Share capital — ordinary_ at par. <br/> Example: patent FV 85 000, par total 100 000 → Dr _Patents_ 85 000, Dr _Share premium — ordinary_ 15 000, Cr _Share capital — ordinary_ 100 000. <br/> Permissible under IFRS. <!--SR:!2026-04-12,4,299!2026-04-12,4,299-->
- negative share premium after a below-par non-cash issue: can it later shrink? ::@:: Yes. A later ordinary share issue that creates a positive premium balance offsets part or all of the earlier debit balance in _Share premium — ordinary_, because it is a running cumulative account. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->

## share issue costs: direct versus indirect

Share issue costs are split into:

- __Direct (traceable)__ costs that can be specifically identified with a share issue (e.g. underwriting fees, legal fees for the prospectus, accounting fees for valuation, printing the prospectus).
- __Indirect (allocated)__ costs that relate to running the company more generally (e.g. salaries of the in-house investor relations department, allocated head-office overhead).

Direct share issue costs are deducted from equity: reduce share premium first (and share capital if premium is exhausted). Indirect costs are expensed as incurred (e.g. administrative expense).

When direct costs are small relative to the issue premium the reduction simply lowers share premium. When direct costs are very large — exceeding the premium generated — the excess comes off share capital instead. Share premium does __not__ carry a negative balance in this scenario: the rule is to reduce share capital rather than allow a debit balance on share premium.

---

Flashcards for this section are as follows:

- share issue costs: parent-level split ::@:: Separate direct, traceable share-issue costs from indirect overhead; direct costs reduce equity, while indirect costs are expensed. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- share issue costs: what is the overall waterfall? ::@:: Direct issue costs reduce the relevant share premium first and, if that premium is exhausted, reduce the related share capital instead of creating a negative premium balance. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->

### ordinary and preference share issue costs

Representative journal entry examples:

> _Harbor Glass case A._ Harbor Glass plc issues {@{300 000 ordinary shares at 3 per share}@}; par value is {@{1 per share}@}. Underwriting costs are {@{20 000}@}. Net cash received is {@{880 000}@}.
>
> | {@{Issue ordinary shares for cash (net of underwriting costs)}@} | Dr            | Cr            |
> | ---------------------------------------------------------------- | ------------- | ------------- |
> | {@{Cash}@}                                                       | {@{880 000}@} |               |
> | {@{Share capital — ordinary (300 000 × 1)}@}                     |               | {@{300 000}@} |
> | {@{Share premium — ordinary}@}                                   |               | {@{580 000}@} |
>
> _Explanation._ Gross proceeds are {@{900 000 (300 000 × 3)}@}; underwriting costs of {@{20 000}@} reduce the amount credited to equity, so only {@{880 000}@} is recorded in Cash and Share premium is {@{580 000}@} instead of {@{600 000}@}. <!--SR:!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _Harbor Glass case B: direct costs exceed premium._ Harbor Glass plc issues {@{200 000 ordinary shares at 1.50 per share}@}; par value is {@{1.00 per share}@}. Direct costs total {@{150 000}@}. Net cash received is {@{150 000}@}.
>
> | {@{Issue ordinary shares — direct costs (150 000) exceed premium (100 000)}@} | Dr            | Cr            |
> | ----------------------------------------------------------------------------- | ------------- | ------------- |
> | {@{Cash}@}                                                                    | {@{150 000}@} |               |
> | {@{Share capital — ordinary (net: 200 000 − 50 000 excess costs)}@}           |               | {@{150 000}@} |
>
> _Explanation._ Gross proceeds are {@{300 000 (200 000 × 1.50)}@}; premium before costs is {@{100 000}@}. Direct costs of {@{150 000}@} first exhaust the {@{100 000 premium, reducing Share premium to zero}@}, and the remaining {@{50 000 reduces Share capital from 200 000 to 150 000}@}. _Share premium_ ends at {@{zero rather than a negative balance}@}; the excess is borne by _Share capital_, not carried as a debit balance on _Share premium_. <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _Harbor Glass preference issue costs can exhaust preference premium too._ Harbor Glass plc issues {@{40 000 preference shares at 5.20 per share}@}; par value is {@{5.00 per share}@}. Direct issue costs are {@{12 000}@}, so the original {@{8 000 preference premium is not enough}@}.
>
> | {@{Issue preference shares when direct costs exceed the preference premium generated}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{196 000}@} | |
> | {@{Share capital — preference (net after excess direct costs)}@} | | {@{196 000}@} |
>
> _Explanation._ Gross proceeds are {@{208 000 (40 000 × 5.20)}@}. Preference premium before costs is only {@{8 000}@}. Direct costs of {@{12 000}@} first eliminate that {@{8 000 preference premium}@}, and the remaining {@{4 000}@} reduces {@{Share capital — preference from 200 000 to 196 000}@}. The same exhaustion logic applies class by class: ordinary issue costs use {@{ordinary premium first}@}, while preference issue costs use {@{preference premium first}@}. <!--SR:!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315-->

---

Flashcards for this section are as follows:

- ordinary or preference share issue costs: what is the class-specific rule? ::@:: Use the premium generated by that same class first, then reduce that class's share capital if the direct costs still exceed the available premium. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- direct issue costs exceeding premium: where does the excess go? ::@:: To the related share capital account, not to retained earnings and not to a negative share-premium balance. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->

### when share premium is used up

The exam trap is to assume that every exhausted premium account eventually pushes the difference into retained earnings. That is __not__ true.

- For __ordinary share issue costs__, exhaust __Share premium — ordinary__ first; any remaining direct issue cost reduces __Share capital — ordinary__.
- For __preference share issue costs__, exhaust __Share premium — preference__ first; any remaining direct issue cost reduces __Share capital — preference__.
- For __treasury-share reissuance below cost__, exhaust __Share premium — treasury__ first; only the remaining shortfall then reduces __Retained earnings__.

So retained earnings is the spillover account for __treasury-share shortfalls__, not the default spillover account for every equity-premium problem.

---

Flashcards for this section are as follows:

- direct share issue costs: examples and treatment ::@:: Underwriting, legal, accounting, and prospectus printing costs that relate specifically to a share issue; reduce _Share premium_ (and then _Share capital_ if needed), not expensed. <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->
- share issue costs: can share premium go negative? ::@:: No. Direct costs reduce _Share premium_ first; when premium is exhausted the excess reduces _Share capital_, not a negative balance on _Share premium_. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- share issue costs exceeding premium (Harbor Glass case B): Harbor Glass issues 200 000 ordinary shares at 1.50, par 1.00, and direct share issue costs are 150 000. Gross proceeds are 300 000, initial share premium is 100 000, and net cash received is therefore 150 000. What is the net entry? ::@:: Dr _Cash_ 150 000; Cr _Share capital — ordinary_ 150 000. Explanation: the 100 000 premium created by the issue is first reduced to zero, then the remaining 50 000 of direct costs reduces _Share capital_ from 200 000 to 150 000. _Share premium — ordinary_ ends at zero, not negative. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- preference share issue costs exceeding preference premium: what is the class-specific rule? ::@:: Reduce _Share premium — preference_ first; if that premium is exhausted, the remaining direct issue cost reduces _Share capital — preference_ rather than retained earnings. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- indirect/allocated share issue costs: examples and treatment ::@:: Ongoing salaries or allocated overhead (e.g. investor relations, head office); not traceable to a specific issue, so expensed as incurred (e.g. administrative expense) and do not reduce equity. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- share issue with underwriting costs: equity effect (net method) ::@:: Record _Cash_ net of direct share issue costs; Cr _Share capital_ at par and Cr _Share premium_ for the remaining net proceeds; do not expense underwriting costs. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- share issue with underwriting costs: numbers in example? ::@:: Gross proceeds 900 000 (300 000 × 3), underwriting costs 20 000, net cash 880 000, _Share premium — ordinary_ 580 000. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- share premium exhaustion: when does retained earnings get hit? ::@:: Not when ordinary or preference share issue costs exceed premium. Retained earnings is hit when a treasury-share reissue below cost exhausts _Share premium — treasury_ and still has a remaining shortfall. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->

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

The participating feature can be understood as downside protection combined with upside participation. Without it, preference shareholders are __capped__: no matter how high total dividends go, they collect only their fixed stated rate while ordinary shareholders receive all the surplus. With the participating feature, the preference share acts like a downside-protected ordinary share — the preference floor is guaranteed when profits are low, but if profits are high enough the preference shareholder also joins in the extra payout on an "as-if-ordinary" basis. The following table shows how payout behaves across different dividend-pool levels for a participating preference share:

| Dividend pool vs. preference rate | Preference payout | Ordinary payout |
| --------------------------------- | ----------------- | --------------- |
| Dividend < preference rate | All available funds | Zero |
| Dividend = preference rate | Full stated fixed rate | Zero |
| Dividend > stated rate but not yet large enough for both stated rates | Full stated fixed rate | Remaining small balance |
| Dividend large enough for both stated rates, with surplus remaining | Stated rate + pro-rata share of surplus | Stated rate + pro-rata share of surplus |

Intuitively:

- Cumulative preference shares behave like a "dividend debt": unpaid amounts build up and must be cleared before ordinary shareholders can receive anything.
- Participating preference shares behave like "enhanced" preference: after their fixed preference return, they also join the ordinary shareholders in any extra payout based on their relative capital at risk (par value).

However, even for cumulative preference shares, __dividends in arrears are not recorded as a liability__ until the board actually declares the dividend; instead, the arrears are usually disclosed in the notes to the financial statements.

---

Flashcards for this section are as follows:

- preference shares: parent-level economic idea ::@:: Preference shares give holders priority for dividends and often liquidation proceeds, but usually with less control than ordinary shareholders. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- cumulative versus participating preference shares ::@:: Cumulative protects the preference holder in low-dividend years through arrears, while participating lets the preference holder join in surplus dividends when the pool is large enough. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->

### liquidation preference and liquidation amount

Liquidation preference tells you __who gets paid first__ if the company is wound up. The corresponding __liquidation amount__ tells you __how much__ must be set aside for preference shareholders before ordinary shareholders can claim the residual net assets.

In this course, the safe habit is not to assume that the liquidation amount is just par value. Depending on the share terms, the preference claim on liquidation may equal:

- par value only;
- par value plus a stated liquidation premium; or
- par value plus cumulative dividends in arrears (if the terms make those arrears part of the liquidation claim).

So "liquidation preference" is the contractual priority feature, while "liquidation amount" is the actual dollar claim implied by the terms of the question. For participating preference shares, there can be a second layer: after receiving the basic liquidation amount, preference shareholders may also share additional residual assets with ordinary shareholders according to the participation formula.

> _Liquidation amount example._ Harbor Crest plc has {@{100 000 cumulative preference shares with par 1 and a 6% dividend rate}@}. The terms say preference shareholders receive {@{par plus any dividends in arrears on liquidation}@}. If {@{two annual preference dividends are in arrears}@}, the liquidation amount is {@{100 000 + (100 000 × 6% × 2) = 112 000}@}. <!--SR:!2026-04-12,4,328!2026-04-12,4,328!2026-04-12,4,328!2026-04-12,4,328-->

---

Flashcards for this section are as follows:

- liquidation preference (preference shares) ::@:: Liquidation preference is the contractual priority that gives preference shareholders a claim on net assets before ordinary shareholders on winding up. <!--SR:!2026-04-12,4,328!2026-04-12,4,328-->
- liquidation amount (preference shares) ::@:: The liquidation amount is the actual dollar claim preference shareholders receive ahead of ordinary shareholders on liquidation; it may be par only, par plus liquidation premium, or par plus dividends in arrears if the terms require that. <!--SR:!2026-04-12,4,328!2026-04-12,4,328-->
- liquidation preference versus liquidation amount ::@:: Liquidation preference is the priority feature; liquidation amount is the numeric claim implied by the terms. A question about book value or liquidation allocation needs the amount, not just the label. <!--SR:!2026-04-12,4,328!2026-04-12,4,328-->
- liquidation amount example: 100 000 cumulative preference shares, par 1, 6% rate, two years in arrears, claim = par plus arrears—result? ::@:: Liquidation amount = 100 000 + (100 000 × 6% × 2) = 112 000. <!--SR:!2026-04-12,4,328!2026-04-12,4,328-->
- why liquidation amount matters for ordinary shareholders ::@:: Because ordinary shareholders receive only the residual net assets left after the full preference liquidation claim has been satisfied. <!--SR:!2026-04-12,4,328!2026-04-12,4,328-->

### mixed preference classes and different par values

When a company has more than one preference class, do __not__ collapse everything into a single generic preference line too early. Keep each class separate until the accounting logic is finished, because each class may have a different:

- par value,
- stated dividend rate,
- cumulative status,
- participating status, and
- share-premium balance.

That means both issuance entries and dividend-allocation calculations are usually done __class by class first__, and only then summarized for presentation.

<!-- markdownlint-disable-next-line MD028 -->
> _Issuing two preference classes with different par values._ Crescent Utilities plc issues {@{10 000 Series A preference shares with €5 par at €6 each}@} and {@{4 000 Series B preference shares with €20 par at €22 each}@}.
>
> | {@{Issue multiple preference classes while keeping each class's capital and premium separate}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{148 000}@} | |
> | {@{Share capital — preference, Series A}@} | | {@{50 000}@} |
> | {@{Share premium — preference, Series A}@} | | {@{10 000}@} |
> | {@{Share capital — preference, Series B}@} | | {@{80 000}@} |
> | {@{Share premium — preference, Series B}@} | | {@{8 000}@} |
>
> _Explanation._ The company does {@{not lump the two classes into one preference-share-capital figure before computing par and premium}@}. Each class keeps its own par-value and premium logic. <!--SR:!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315-->

<!-- markdownlint-disable-next-line MD028 -->
> _Dividend allocation with different preference par values._ Suppose Series A above carries an {@{8% dividend rate while Series B carries 6%, so each class's fixed dividend must be computed separately}@}. If the board declares total dividends of {@{25 000 to allocate across both preference classes and ordinary shareholders}@} and both classes are {@{non-cumulative and non-participating}@}, the class-by-class priority calculation is:
>
> - {@{Series A preference dividend = 50 000 × 8% = 4 000}@}
> - {@{Series B preference dividend = 80 000 × 6% = 4 800}@}
> - {@{Ordinary shareholders receive the residual 16 200}@}
>
> | {@{Declare dividends after computing each preference class separately}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Retained earnings}@} | {@{25 000}@} | |
> | {@{Dividends payable — preference, Series A}@} | | {@{4 000}@} |
> | {@{Dividends payable — preference, Series B}@} | | {@{4 800}@} |
> | {@{Dividends payable — ordinary}@} | | {@{16 200}@} |
>
> _Explanation._ Different par values matter because the fixed preference dividend for each class is based on that class's own {@{par amount and stated rate}@}, not on a blended shortcut. <!--SR:!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315-->

Representative journal entry example at issuance:

> _Scenario._ Crescent Utilities plc issues {@{10 000 preference shares, par 10, for 12 cash per share}@}.
>
> | {@{Issue preference shares for cash}@}         | Dr            | Cr            |
> | ---------------------------------------------- | ------------- | ------------- |
> | {@{Cash}@}                                     | {@{120 000}@} |               |
> | {@{Share capital — preference (10 000 × 10)}@} |               | {@{100 000}@} |
> | {@{Share premium — preference}@}               |               | {@{20 000}@}  | <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

---

Flashcards for this section are as follows:

- mixed preference classes: why keep them separate at first? ::@:: Because each class can have its own par value, rate, cumulative status, participation rights, and premium balance, so the accounting must be computed class by class before summarizing. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- mixed preference classes and dividends: why is a blended shortcut dangerous? ::@:: Because each class's fixed dividend is based on that class's own par amount and stated rate rather than on one combined preference average. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- issuance of preference shares for cash: basic entry ::@:: Dr _Cash_ (issue price × number of shares), Cr _Share capital — preference_ at par, Cr _Share premium — preference_ for the excess over par. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- issuance of 10 000 preference shares, par 10, at 12—entry? ::@:: Dr _Cash_ 120 000; Cr _Share capital — preference_ 100 000; Cr _Share premium — preference_ 20 000. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->

## treasury shares (cost method)

Treasury shares are the company's own shares that it has repurchased. Under the cost method used in this course:

- On repurchase, debit _Treasury shares_ at __cost__ and credit _Cash_.
- _Treasury shares_ is a __contra-equity__ account (reduces total equity), not an asset and not an expense.
- On reissue above cost: credit _Treasury shares_ at cost and credit _Share premium — treasury_ for the excess.
- On reissue below cost: first use any existing _Share premium — treasury_ balance; any further shortfall is debited to _Retained earnings_ (not to _Share premium — ordinary_ and not treated as a loss in profit or loss).
- If _Retained earnings_ is already low or zero when the shortfall hits it, the debit may reduce _Retained earnings_ to a negative balance (accumulated deficit). A negative _Retained earnings_ balance is permissible but signals that the company has distributed or absorbed more than it has ever earned.

Management often repurchases shares when they believe the shares are undervalued or to adjust capital structure.

Representative journal entry examples:

> _SilverPeak case A: reissue above cost._ SilverPeak Retail plc previously repurchased 1 000 treasury shares at {@{50 per share (total cost 50 000)}@}. It reissues them for {@{60 per share}@} (proceeds {@{60 000}@}).
>
> | {@{Reissue treasury shares above cost}@}  | Dr           | Cr           |
> | ----------------------------------------- | ------------ | ------------ |
> | {@{Cash}@}                                | {@{60 000}@} |              |
> | {@{Treasury shares (at cost)}@}           |              | {@{50 000}@} |
> | {@{Share premium — treasury}@}            |              | {@{10 000}@} | <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _SilverPeak case B: reissue below cost — Share premium — treasury balance sufficient._ The same SilverPeak treasury shares (cost {@{50 000}@}) are reissued for {@{45 per share}@} (proceeds {@{45 000}@}). Existing _Share premium — treasury_ balance is {@{15 000}@}.
>
> | {@{Reissue treasury shares below cost (shortfall covered by premium)}@} | Dr           | Cr           |
> | ----------------------------------------------------------------------- | ------------ | ------------ |
> | {@{Cash}@}                                                              | {@{45 000}@} |              |
> | {@{Share premium — treasury (shortfall: 50 000 − 45 000)}@}             | {@{5 000}@}  |              |
> | {@{Treasury shares (at cost)}@}                                         |              | {@{50 000}@} | <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _SilverPeak case C: reissue below cost — shortfall exceeds premium, hits retained earnings._ The same SilverPeak treasury shares (cost {@{50 000}@}) are reissued for {@{30 per share}@} (proceeds {@{30 000}@}). Existing _Share premium — treasury_ balance is only {@{8 000}@}.
>
> | {@{Reissue treasury shares below cost (excess shortfall hits retained earnings)}@} | Dr           | Cr           |
> | ---------------------------------------------------------------------------------- | ------------ | ------------ |
> | {@{Cash}@}                                                                         | {@{30 000}@} |              |
> | {@{Share premium — treasury (all available)}@}                                     | {@{8 000}@}  |              |
> | {@{Retained earnings (remaining shortfall: 20 000 − 8 000)}@}                      | {@{12 000}@} |              |
> | {@{Treasury shares (at cost)}@}                                                    |              | {@{50 000}@} |
>
> _Explanation._ Shortfall = {@{50 000 − 30 000 = 20 000}@}. The first {@{8 000}@} comes from _Share premium — treasury_ (exhausting it). The remaining {@{12 000}@} is debited to _Retained earnings_. If _Retained earnings_ was, say, only {@{5 000}@} before this entry, it would fall to {@{−7 000}@} — an accumulated deficit. The loss is absorbed by equity, not reported in profit or loss. <!--SR:!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

---

Flashcards for this section are as follows:

- treasury shares (cost method): acquisition entry ::@:: Dr _Treasury shares_ at cost, Cr _Cash_; _Treasury shares_ is a contra-equity account, not an asset. <!--SR:!2026-04-12,4,299!2026-04-12,4,288-->
- treasury shares reissued above cost: equity effect ::@:: Dr _Cash_, Cr _Treasury shares_ at cost, Cr _Share premium — treasury_ for the excess; total equity increases. <!--SR:!2026-04-12,4,299!2026-04-12,4,299-->
- treasury shares reissued below cost: waterfall order ::@:: Shortfall (cost − proceeds) first absorbs any _Share premium — treasury_ balance; once that is exhausted, the remaining shortfall is debited to _Retained earnings_. The shortfall never goes to _Share premium — ordinary_ and is never expensed in profit or loss. <!--SR:!2026-04-12,4,299!2026-04-12,4,299-->
- treasury reissue below cost: what if retained earnings is insufficient? ::@:: _Retained earnings_ can go to a negative balance (accumulated deficit). The debit simply pushes _Retained earnings_ below zero; this is permissible but signals the company has distributed or absorbed more than it has ever earned. <!--SR:!2026-04-12,4,299!2026-04-12,4,299-->
- treasury reissue SilverPeak case C numbers: cost 50 000, proceeds 30 000, premium–treasury 8 000—entry? ::@:: Dr _Cash_ 30 000, Dr _Share premium — treasury_ 8 000 (all remaining), Dr _Retained earnings_ 12 000; Cr _Treasury shares_ 50 000. <!--SR:!2026-04-12,4,299!2026-04-12,4,299-->

## equity accounts: when do accounts have negative balances?

In a typical company with positive earnings and conservative dividend policies, most equity accounts have positive (credit) balances. However, specific equity accounts can have negative (debit) balances under certain circumstances. Understanding when and why this occurs is important for proper financial statement interpretation.

__Share premium — can be negative?__ Only in one specific scenario permitted by this course:

- When a company issues shares for non-cash consideration and the fair value of the asset received is __below par value__, _Share premium — ordinary_ is debited for the shortfall, producing a negative balance. This is permissible under IFRS for non-cash share issuance only.

For treasury share reissuance below cost, the shortfall does __not__ go to _Share premium — ordinary_. Instead, once _Share premium — treasury_ is exhausted the remaining shortfall is charged to _Retained earnings_. _Share premium — ordinary_ is untouched and stays at its prior (non-negative) balance.

For share issue costs that exceed premiums generated, the excess reduces _Share capital_ rather than creating a negative _Share premium_.

---

Flashcards for this section are as follows:

- negative equity balances: parent-level map ::@:: The common debit-balance concern is retained earnings, while share premium can be negative only in the specific below-par non-cash issue scenario taught here. <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->
- equity accounts and negative balances: what is the exam habit? ::@:: Identify which account is actually designed to absorb the shortfall, because different equity problems send the debit to different places. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- share capital: can it be negative? ::@:: No. Share capital is the legal par amount and is always a credit balance. Severe capital reduction reduces par downward but does not create a negative share capital. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- retained earnings: when is it negative (accumulated deficit)? ::@:: When cumulative losses exceed cumulative profits, or dividends exceed earned profits. A deficit signals the company has lost money over time or in recent years. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- treasury shares: is it ever negative? ::@:: No. Treasury shares is a contra-equity account with a debit balance; it cannot be "more" negative. It grows when shares are repurchased and shrinks when they are reissued or cancelled. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- reserves: can they be negative? ::@:: Typically no. Reserves are earmarked portions of retained earnings with debit balances. If no longer needed, they are eliminated or released back to retained earnings, not carried as negative balances. <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->

### when equity premium is exhausted and when retained earnings is affected

The correct waterfall depends on __which premium account__ is running out.

- If __Share premium — ordinary__ is exhausted by direct ordinary-share issue costs, the remaining amount reduces __Share capital — ordinary__.
- If __Share premium — preference__ is exhausted by direct preference-share issue costs, the remaining amount reduces __Share capital — preference__.
- If __Share premium — treasury__ is exhausted on a treasury-share reissue below cost, the remaining shortfall reduces __Retained earnings__.

So the words "premium used up" do __not__ automatically imply a hit to retained earnings. Retained earnings is the spillover account only for the __treasury-share reissue below cost__ logic, not for ordinary or preference share issuance costs.

__Share capital — can be negative?__ Effectively, no. Under company law and IFRS, _Share capital_ represents the par value of shares issued and is recorded at the legal par amount (a credit balance). It cannot go negative unless shares are cancelled or par values are adjusted. If a company experiences severe losses or capital reductions, the board might authorise a reduction of par value, which would decrease _Share capital_ but not make it negative in the accounting sense (it would reduce to a lower positive amount).

__Retained earnings — can be negative (deficit)?__ Yes, and this is more common. An __accumulated loss__ or __deficit__ occurs when cumulative losses exceed cumulative profits and dividends exceed retained earnings in a period. In financial statements, a negative _Retained earnings_ is often labelled "Accumulated deficit" on the balance sheet. This signals that:

- The company has lost money over its history or recent years.
- No earned profits are available to fund dividends (though companies may still declare dividends from other reserves or by reducing capital).
- The company is relying on shareholder capital and reinvested capital rather than earned profits.

A significant accumulated deficit may concern creditors and shareholders, but it is not unusual for young, growing companies or those in distressed situations.

__Treasury shares — can have a negative balance?__ Not directly. _Treasury shares_ is a contra-equity account with a __debit balance__ by definition (it reduces equity). It cannot be "more negative"; its magnitude grows as more shares are repurchased. If all treasury shares are reissued or cancelled, the balance reduces to zero.

__Reserves — can be negative?__ Reserves (such as capital redemption reserve, general reserve) typically have __positive balances__ because they represent earmarked retained earnings or statutory requirements. However, if losses occur or reserves are released:

- Some reserves may be written down (reduced) to zero or even reversed if the reason for the reserve no longer applies.
- A reserve will not have a debit (negative) balance in normal circumstances; it would simply be eliminated.

__Summary__: The most common equity account that can be negative is _Retained earnings_ (accumulated deficit), which signals historical losses. _Share premium — ordinary_ can be negative only in the non-cash share issuance below-par scenario; it is __not__ made negative by treasury reissue shortfalls (those hit _Retained earnings_) or by share issue costs (those reduce _Share capital_). _Share capital_ is never negative in normal circumstances; _Treasury shares_ and reserves are not carried as negative balances.

> _Negative share-premium example._ Astera Biotech plc issues {@{1&nbsp;000 ordinary shares with par €10}@} for a patent portfolio with fair value only {@{€8&nbsp;500}@}. Because share capital must still be credited at {@{€10&nbsp;000}@}, the shortfall creates a debit balance in {@{Share premium — ordinary}@}.
>
> | {@{Issue shares for non-cash asset below par}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Patents}@} | {@{8&nbsp;500}@} | |
> | {@{Share premium — ordinary}@} | {@{1&nbsp;500}@} | |
> | {@{Share capital — ordinary}@} | | {@{10&nbsp;000}@} |
>
> _Explanation._ This is the rare IFRS case in this course where {@{Share premium — ordinary carries a debit balance}@}. <!--SR:!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321-->

<!-- markdownlint-disable-next-line MD028 -->
> _Negative retained-earnings example._ Treasury shares carried at {@{€50&nbsp;000}@} are reissued for only {@{€30&nbsp;000}@}, and there is {@{no Share premium — treasury balance remaining}@}. The full shortfall therefore hits retained earnings.
>
> | {@{Reissue treasury shares below cost when no treasury premium remains}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{30&nbsp;000}@} | |
> | {@{Retained earnings}@} | {@{20&nbsp;000}@} | |
> | {@{Treasury shares}@} | | {@{50&nbsp;000}@} |
>
> _Explanation._ If retained earnings had only {@{€12&nbsp;000}@} before the entry, it would fall to {@{a negative balance of €8&nbsp;000}@}, creating an accumulated deficit. <!--SR:!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321-->

---

Flashcards for this section are as follows:

- exhausted equity premium: what decides the next account hit? ::@:: The answer depends on which premium account is exhausted: ordinary and preference issue-cost excesses hit share capital, while treasury-share reissue shortfalls hit retained earnings after treasury premium is used up. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- retained earnings after premium exhaustion: when is it the spillover account? ::@:: Only for treasury-share reissues below cost after _Share premium — treasury_ has already been exhausted. <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->
- share premium: when can it be negative? ::@:: Only when shares are issued for non-cash consideration whose fair value is below par — _Share premium — ordinary_ takes the debit shortfall. It does __not__ go negative from treasury reissue shortfalls (those go to _Retained earnings_) or from share issue costs exceeding premium (those reduce _Share capital_). <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- share premium: treasury reissue shortfall — where does excess go? ::@:: To _Retained earnings_, not to _Share premium — ordinary_. Once _Share premium — treasury_ is exhausted, the remaining shortfall debits _Retained earnings_ only. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- equity premium exhausted: which cases reduce share capital instead of retained earnings? ::@:: Direct ordinary-share issue costs reduce _Share capital — ordinary_ after exhausting _Share premium — ordinary_, and direct preference-share issue costs reduce _Share capital — preference_ after exhausting _Share premium — preference_. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- below-par non-cash share issue: which account absorbs the shortfall? ::@:: _Share premium — ordinary_ is debited for the shortfall because _Share capital_ must still be credited at par. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- treasury reissue shortfall with no treasury premium left: which account absorbs the loss? ::@:: _Retained earnings_, because the shortfall cannot be charged to _Share premium — ordinary_ or profit or loss. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->

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

__Share dividends.__ The company issues additional shares to existing shareholders instead of paying cash. Under __IFRS (IAS 32)__, which is the standard used in this course, __all__ share dividends — whether small or large — are recorded at the __par value__ of shares issued. The recording sequence is the same regardless of size:

1. __Declaration__: Dr _Retained earnings_ (par value × new shares), Cr _Ordinary share dividend distributable_ (par value × new shares).
2. __Distribution__: Dr _Ordinary share dividend distributable_, Cr _Share capital — ordinary_ (par value × new shares).

Total equity is unchanged by a share dividend under IFRS; the reclassification simply moves par-value amounts from _Retained earnings_ into _Share capital_.

__US GAAP comparison (ASC 505).__ Under US GAAP, size determines the measurement basis:

- __Small share dividends__ (≤ approximately 20–25%): same as IFRS — record at par value only.
- __Large share dividends__ (> approximately 25%): record at __fair value__ of the shares issued. Declaration: Dr _Retained earnings_ (fair value × new shares), Cr _Ordinary share dividend distributable_ (fair value × new shares). Distribution: Dr _Ordinary share dividend distributable_, Cr _Share capital — ordinary_ (par × new shares), Cr _Share premium — ordinary_ (fair value − par) × new shares. This reduces _Retained earnings_ by more (the full fair value) and increases _Share capital_ __and__ _Share premium_.

The economic result differs: under US GAAP the large-dividend entry transfers the fair-value premium into _Share premium_, whereas under IFRS no premium component is created — only par is shifted between equity line items.

This is the right way to separate the accounting intuition from the course convention. In __this course__, IFRS is the primary method, so a share dividend is always recorded by the __par-value method__. Economically, that makes an IFRS share dividend feel closer to a __reclassification within equity__: shares outstanding rise, retained earnings falls, and share capital rises, but no market-value premium is capitalized. By contrast, the __US GAAP__ fair-value treatment for a __large__ share dividend is useful as a comparison intuition: it treats the transaction more like a __material capitalization of retained earnings at current market significance__, so the entry creates both _Share capital_ and _Share premium_. A share split is still different from both, because it changes share count and par per share without any retained-earnings reclassification at all.

Representative journal entry examples:

> _Scenario._ On June 10, Harbor Freight Logistics Ltd. declares a cash dividend of {@{0.50 per share on 1.8 million ordinary shares}@}, payable July 16 to shareholders of record June 24. Total dividend is {@{900 000}@}.
>
> | {@{At date of declaration (June 10)}@}            | Dr            | Cr            |
> | ------------------------------------------------- | ------------- | ------------- |
> | {@{Retained earnings (Cash dividends declared)}@} | {@{900 000}@} |               |
> | {@{Dividends payable}@}                           |               | {@{900 000}@} |
>
> | {@{At date of record (June 24)}@} | Dr  | Cr  |
> | --------------------------------- | --- | --- |
> | {@{No entry}@}                    |     |     |
>
> | {@{At date of payment (July 16)}@} | Dr            | Cr            |
> | ---------------------------------- | ------------- | ------------- |
> | {@{Dividends payable}@}            | {@{900 000}@} |               |
> | {@{Cash}@}                         |               | {@{900 000}@} | <!--SR:!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _Scenario._ Lotus Capital Ltd. transfers to shareholders some of its investments in securities, with carrying amount {@{1 250 000}@}. On December 28, 2024, it declares a property dividend to shareholders of record January 15, 2025, to be distributed January 30, 2025. At the declaration date, the investments have fair value {@{2 000 000}@}.
>
> | {@{At date of declaration (remeasure and declare dividend)}@} | Dr              | Cr              |
> | ------------------------------------------------------------- | --------------- | --------------- |
> | {@{Equity investments}@}                                      | {@{750 000}@}   |                 |
> | {@{Unrealised holding gain or loss — income}@}                |                 | {@{750 000}@}   |
> | {@{Retained earnings (Property dividends declared)}@}         | {@{2 000 000}@} |                 |
> | {@{Property dividends payable}@}                              |                 | {@{2 000 000}@} |
>
> | {@{At date of distribution (January 30, 2025)}@} | Dr              | Cr              |
> | ------------------------------------------------ | --------------- | --------------- |
> | {@{Property dividends payable}@}                 | {@{2 000 000}@} |                 |
> | {@{Equity investments}@}                         |                 | {@{2 000 000}@} | <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _Corporate tax consequence of the appreciated property dividend._ If the jurisdiction taxes the {@{750 000 gain created when the investment is remeasured from carrying amount 1 250 000 to fair value 2 000 000}@}, and the tax rate is {@{25%}@}, the company must also recognize the tax effect of that gain.
>
> | {@{Recognise current tax payable on the gain created by the property dividend remeasurement}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Income tax expense}@} | {@{187 500}@} | |
> | {@{Income taxes payable}@} | | {@{187 500}@} |
>
> _Explanation._ The property dividend can therefore trigger both a {@{distribution of assets}@} and a {@{current tax charge on the remeasurement gain}@}. <!--SR:!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,315-->

<!-- markdownlint-disable-next-line MD028 -->
> _Scenario._ Granite Ridge Mines plc issues a dividend to ordinary shareholders of {@{1 200 000}@}. The announcement states that {@{900 000}@} is income and {@{300 000}@} is a return of capital.
>
> | {@{At date of declaration}@}   | Dr            | Cr              |
> | ------------------------------ | ------------- | --------------- |
> | {@{Retained earnings}@}        | {@{900 000}@} |                 |
> | {@{Share premium — ordinary}@} | {@{300 000}@} |                 |
> | {@{Dividends payable}@}        |               | {@{1 200 000}@} |
>
> | {@{At date of payment}@} | Dr              | Cr              |
> | ------------------------ | --------------- | --------------- |
> | {@{Dividends payable}@}  | {@{1 200 000}@} |                 |
> | {@{Cash}@}               |                 | {@{1 200 000}@} | <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,288!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _Scenario._ Willow Foods plc has {@{100 000 ordinary shares, par 1}@}, retained earnings {@{50 000}@}, and declares a {@{10% share dividend}@}. It issues {@{10 000 additional shares}@}. Fair value at the time is {@{8 per share}@}, but the entry uses par value.
>
> | {@{At date of declaration (10% share dividend)}@} | Dr           | Cr           |
> | ------------------------------------------------- | ------------ | ------------ |
> | {@{Retained earnings (Share dividend declared)}@} | {@{10 000}@} |              |
> | {@{Ordinary share dividend distributable}@}       |              | {@{10 000}@} |
>
> | {@{At date of distribution}@}               | Dr           | Cr           |
> | ------------------------------------------- | ------------ | ------------ |
> | {@{Ordinary share dividend distributable}@} | {@{10 000}@} |              |
> | {@{Share capital — ordinary}@}              |              | {@{10 000}@} | <!--SR:!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _Scenario (IFRS — large share dividend at par)._ Copperleaf Metals plc has {@{50 000 ordinary shares, par 2}@}, retained earnings {@{300 000}@}, and declares a {@{40% share dividend}@}. It issues {@{20 000 additional shares}@}. Fair value at the time is {@{18 per share}@}. Under IFRS the entry uses {@{par value}@}, not fair value.
>
> | {@{At date of declaration (40% share dividend — IFRS, at par)}@} | Dr           | Cr           |
> | ---------------------------------------------------------------- | ------------ | ------------ |
> | {@{Retained earnings (Share dividend declared)}@}                | {@{40 000}@} |              |
> | {@{Ordinary share dividend distributable (20 000 × 2)}@}         |              | {@{40 000}@} |
>
> | {@{At date of distribution}@}               | Dr           | Cr           |
> | ------------------------------------------- | ------------ | ------------ |
> | {@{Ordinary share dividend distributable}@} | {@{40 000}@} |              |
> | {@{Share capital — ordinary (20 000 × 2)}@} |              | {@{40 000}@} |
>
> _IFRS vs US GAAP comparison for the Copperleaf example._ Under __IFRS__ (this course), _Retained earnings_ decreases by only {@{40 000}@} (par 2 × 20 000 new shares) and _Share capital_ increases by the same {@{40 000}@}; _Share premium_ is unchanged. Under __US GAAP__ (large dividend, for comparison), _Retained earnings_ would decrease by {@{360 000}@} (fair value 18 × 20 000 shares), _Share capital_ would increase {@{40 000}@} (par), and _Share premium_ would increase {@{320 000}@} (excess). The IFRS par-value method results in a smaller reduction to _Retained earnings_ and no premium creation; the US GAAP fair-value method transfers more from _Retained earnings_ and recognises the economic significance of issuing a large block of new shares. <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

<!-- markdownlint-disable-next-line MD028 -->
> _Post-declaration market-price collapse does not reopen the entry._ Using the same {@{40% share dividend on 20 000 new shares}@}, suppose the market price falls from {@{18 at declaration}@} to {@{11 before distribution}@}. Under __IFRS__, the entry still stays at {@{par value 40 000}@}. Under the __US GAAP comparison__, the fair-value-based declaration amount would still stay at the {@{declaration-date fair value of 360 000 rather than being remeasured down to 220 000}@}.
>
> | {@{Distribution after a market-price drop — IFRS entry unchanged}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Ordinary share dividend distributable}@} | {@{40 000}@} | |
> | {@{Share capital — ordinary}@} | | {@{40 000}@} |
>
> _Explanation._ The exam trap is to think the later market price rewrites the dividend accounting. It does {@{not rewrite the already-fixed declaration-date measurement}@}. The relevant amount is already fixed when the dividend is {@{declared}@}; IFRS stays at {@{par value}@}, and even the US-GAAP comparison would keep the {@{declaration-date fair-value measurement}@} rather than remeasuring again before distribution. <!--SR:!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321-->

<!-- markdownlint-disable-next-line MD028 -->
> _Scenario._ Out of a {@{50 000 total dividend pool}@}, ordinary shares have par {@{400 000}@}; preference shares have par {@{100 000}@} with dividend rate {@{6%}@}. Four allocation patterns are common.
>
> __Non-cumulative, non-participating:__ preference {@{6 000}@}; ordinary {@{44 000}@}.
>
> | {@{Declare dividend (non-cumulative, non-participating)}@} | Dr           | Cr           |
> | ---------------------------------------------------------- | ------------ | ------------ |
> | {@{Retained earnings}@}                                    | {@{50 000}@} |              |
> | {@{Dividends payable — preference}@}                       |              | {@{6 000}@}  |
> | {@{Dividends payable — ordinary}@}                         |              | {@{44 000}@} |
>
> __Cumulative, non-participating:__ arrears {@{12 000}@} plus current year {@{6 000}@}; preference {@{18 000}@}; ordinary {@{32 000}@}.
>
> | {@{Declare dividend (cumulative, non-participating)}@} | Dr           | Cr           |
> | ------------------------------------------------------ | ------------ | ------------ |
> | {@{Retained earnings}@}                                | {@{50 000}@} |              |
> | {@{Dividends payable — preference}@}                   |              | {@{18 000}@} |
> | {@{Dividends payable — ordinary}@}                     |              | {@{32 000}@} |
>
> _Note on dividends in arrears._ Even for cumulative preference shares, {@{no liability is recorded for dividends in arrears until the board declares a dividend}@}; the arrears are {@{disclosed in the notes to the financial statements, not recognised as Dividends payable}@} until declaration.
>
> __Non-cumulative, participating:__ step 1 preference {@{6 000}@}, ordinary {@{24 000}@}; remaining {@{20 000}@}; step 2 split by par gives preference {@{4 000}@}, ordinary {@{16 000}@}; totals preference {@{10 000}@}, ordinary {@{40 000}@}.
>
> | {@{Declare dividend (non-cumulative, participating)}@} | Dr           | Cr           |
> | ------------------------------------------------------ | ------------ | ------------ |
> | {@{Retained earnings}@}                                | {@{50 000}@} |              |
> | {@{Dividends payable — preference}@}                   |              | {@{10 000}@} |
> | {@{Dividends payable — ordinary}@}                     |              | {@{40 000}@} |
>
> __Cumulative, participating:__ arrears plus current preference {@{18 000}@}; ordinary current-rate share {@{24 000}@}; remaining {@{8 000}@}; split by par gives preference {@{1 600}@}, ordinary {@{6 400}@}; final totals preference {@{19 600}@}, ordinary {@{30 400}@}.
>
> | {@{Declare dividend (cumulative, participating)}@} | Dr           | Cr           |
> | -------------------------------------------------- | ------------ | ------------ |
> | {@{Retained earnings}@}                            | {@{50 000}@} |              |
> | {@{Dividends payable — preference}@}               |              | {@{19 600}@} |
> | {@{Dividends payable — ordinary}@}                 |              | {@{30 400}@} | <!--SR:!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,288!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299!2026-04-12,4,299-->

---

Flashcards for this section are as follows:

- cash dividend: journal entries on declaration and payment ::@:: Date of declaration: Dr _Retained earnings_, Cr _Dividends payable_. <br/> Date of payment: Dr _Dividends payable_, Cr _Cash_. <br/> No entry on date of record. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- property dividend: two-step accounting ::@:: Step 1: remeasure the asset to fair value and recognize the unrealised gain or loss. <br/> Step 2 — declaration entry: Dr _Retained earnings_, Cr _Property dividend payable_ at fair value. <br/> Step 3 — distribution entry: Dr _Property dividend payable_, Cr asset on distribution. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- liquidating dividend: how to split? ::@:: Amount up to _Retained earnings_ is treated as a normal dividend; any excess is treated as a return of capital (reduce _Share premium_ first, then _Share capital_). <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->
- share dividend (small): effect on equity ::@:: Total equity unchanged; _Retained earnings_ decreases and _Share capital_ increases by the par value of new shares via _Ordinary share dividend distributable_. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- dividend types in this course ::@:: _Cash_ dividends reduce total equity and working capital; property and liquidating dividends also reduce total equity; small share dividends do not change total equity but reclassify amounts within equity (_Retained earnings_ to _Share capital_). <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- dividend calculations (overview) ::@:: _Cash_ dividend = dividend per share × number of shares; property dividend measured at fair value of asset; liquidating dividend is split between _Retained earnings_ (income portion) and _Share premium_/_Share capital_ (return of capital); small share dividend amount = par value × number of new shares issued (e.g. % × existing shares × par). <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- cash dividend on ordinary shares: key dates and entries ::@:: Date of declaration: Dr _Retained earnings_, Cr _Dividends payable_; date of record: no entry; date of payment: Dr _Dividends payable_, Cr _Cash_. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- Harbor Freight cash dividend example: 0.50 on 1.8 million shares—amount and declaration entry? ::@:: Amount 900 000; Dr _Retained earnings_ (Cash dividends declared) 900 000, Cr _Dividends payable_ 900 000. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- property dividend: two journal steps ::@:: First remeasure asset to fair value and recognise unrealised gain or loss; then Dr _Retained earnings_ and Cr _Property dividends payable_ at fair value, followed by Dr _Property dividends payable_ and Cr asset on distribution. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- Lotus Capital property dividend example: FV 2 000 000, CV 1 250 000—remeasurement entry? ::@:: Dr _Equity investments_ 750 000, Cr _Unrealised holding gain or loss — income_ 750 000. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- property dividend of an appreciated asset: what extra entry may appear if the jurisdiction taxes the gain? ::@:: Recognize current tax on the gain created by remeasuring the asset to fair value before distribution, for example Dr _Income tax expense_, Cr _Income taxes payable_. <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->
- liquidating dividend: how to split between income and capital? ::@:: Dr _Retained earnings_ for the income portion and Dr _Share premium_ (then _Share capital_ if needed) for the capital portion; Cr _Dividends payable_ for the total. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- Granite Ridge liquidating dividend example: 1 200 000 total (900 000 income, 300 000 capital)—declaration entry? ::@:: Dr _Retained earnings_ 900 000, Dr _Share premium — ordinary_ 300 000, Cr _Dividends payable_ 1 200 000. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- share dividend (small): declaration and distribution entries ::@:: Declaration: Dr _Retained earnings_, Cr _Ordinary share dividend distributable_ (at par). <br/> Distribution: Dr _Ordinary share dividend distributable_, Cr _Share capital — ordinary_. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- Willow Foods share dividend example: 10% on 100 000 shares, par 1—declaration entry? ::@:: Dr _Retained earnings_ 10 000, Cr _Ordinary share dividend distributable_ 10 000. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- small vs large share dividend: measurement basis under IFRS vs US GAAP ::@:: __IFRS__ (this course): all share dividends — both small and large — are measured at __par value__. __US GAAP__: small dividends (≤ ~20–25%) at par value; large dividends (> ~25%) at __fair value__ of shares issued. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- small share dividend (par value method): total equity effect ::@:: Total equity unchanged; _Retained earnings_ decreases and _Share capital_ increases by the same par value amount; the company simply reclassifies within equity. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- large share dividend under IFRS: measurement basis and entry ::@:: Measured at __par value__, same as small dividend. _Retained earnings_ debited at par × new shares; _Ordinary share dividend distributable_ credited at par × new shares; on distribution, Dr _Distributable_, Cr _Share capital — ordinary_ (par × new shares). No _Share premium_ credit. Under US GAAP instead _Retained earnings_ would be debited at fair value, with the excess over par crediting _Share premium — ordinary_. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- large share dividend (40% Copperleaf example — IFRS): declaration entry? ::@:: IFRS declaration: Dr _Retained earnings_ 40 000 (par 2 × 20 000 new shares), Cr _Ordinary share dividend distributable_ 40 000. <br/> IFRS distribution: Dr _Ordinary share dividend distributable_ 40 000, Cr _Share capital — ordinary_ 40 000. <br/> Under US GAAP instead, declaration would be Dr _Retained earnings_ 360 000 (FV 18 × 20 000), Cr _Distributable_ 360 000; then distribution would be Dr _Distributable_ 360 000, Cr _Share capital_ 40 000, Cr _Share premium_ 320 000. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- share dividend after declaration: does a later share-price change alter the recorded amount? ::@:: No. Once the dividend is declared, the accounting amount is already fixed. Under IFRS it stays at par; under the US-GAAP comparison a large dividend stays at the declaration-date fair value rather than being remeasured again before distribution. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- when to use par vs fair value for share dividends ::@:: __IFRS__ (this course): always par value regardless of size. __US GAAP__: up to ~20–25% of shares outstanding → par value; over that threshold → fair value (material dilution recognised at economic cost). <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- share dividend vs share split: economic intuition (course IFRS first, but include US GAAP comparison) ::@:: Under __IFRS__ (the method used in this course), a share dividend is mainly a __par-value reclassification within equity__: retained earnings moves into share capital, share count rises, but no fair-value premium is created. So economically it feels closer to a bookkeeping capitalization than to a true new financing event. A __share split__ is even more mechanical: it increases share count and reduces par per share, but does __not__ reclassify retained earnings and usually needs no journal entry. For comparison, __US GAAP__ gives a different intuition for a __large__ share dividend because it uses fair value, so the entry capitalizes retained earnings at market significance and creates _Share premium_; that makes a large US-GAAP share dividend feel more like a material mini-issuance to existing shareholders than an IFRS par-only reclassification. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- non-cumulative, non-participating preference shares: allocation in example ::@:: Out of a 50 000 dividend, preference receives 6 000 (6% × 100 000) and ordinary receives 44 000. <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->
- cumulative, non-participating preference shares: allocation in example ::@:: With two years of arrears, preference receives 18 000 in total (12 000 arrears + 6 000 current) and ordinary receives 32 000 out of a 50 000 dividend. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- preference dividends: four patterns overview ::@:: Non-cumulative/non-participating (NC/NP), cumulative/non-participating (C/NP), non-cumulative/participating (NC/P), cumulative/participating (C/P). <br/> Each adds one feature: cumulative protects preference shareholders when dividends are low by accumulating arrears; participating protects them when dividends are high by letting them share the surplus. <br/> Intuitive tank model: think of the total dividend pool as water being poured into tanks — preference tank fills first (to its stated rate), then ordinary tank fills; the "participating" feature means any overflow after both tanks are at their stated level is shared proportionally, while the "cumulative" feature means the preference tank carries unpaid debt forward from prior years and must be filled first retroactively. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- non-cumulative, non-participating (NC/NP): protection and behaviour ::@:: preference gets stated rate first; ordinary gets remainder. Skipped dividends are lost (no arrears carry forward). <br/> Low dividend: ordinary gets nothing. <br/> High dividend: no share in surplus. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- cumulative, non-participating (C/NP): motivation and low-dividend behaviour ::@:: __Improvement over NC/NP__: unpaid preference dividends from prior years (arrears) must be paid in full before any ordinary dividend can be declared. <br/> Motivation: protects preference shareholders against boards strategically skipping dividends — arrears accumulate and must eventually be paid, making preference shares more like debt in a distress scenario. <br/> If dividend is __low__ (enough to cover some but not all arrears): arrears are paid in priority order (oldest first or pro-rata depending on convention), but ordinary still receives nothing until all arrears plus current year are satisfied. <br/> Tank model: preference tank has a "debt meter" that records unfilled amounts from previous periods; the current pour must first pay off the debt meter, then fill the current period, before any water reaches the ordinary tank. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- non-cumulative, participating (NC/P): motivation and low-dividend behaviour ::@:: __Improvement over NC/NP__: after both classes receive their stated dividend rate, any remaining surplus is shared pro-rata by par value. <br/> Motivation: prevents preference shareholders from being "capped" — if profits are very high, the participating feature means they share in the upside just like ordinary shareholders; preference acts as downside-protected ordinary (guaranteed floor + "as-if-ordinary" parity when surplus is large). <br/> If dividend is __low__ (total ≤ preference stated rate): only preference is paid (up to available amount); no participation kicks in because there is nothing left after the priority fill; ordinary gets nothing. <br/> Tank model: preference fills first (its 6% mark), then ordinary fills to its matching 6% mark, then any overflow is split proportionally; if the pour barely reaches the preference mark, no overflow ever happens. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- cumulative, participating (C/P): motivation and low-dividend behaviour ::@:: __Combines both features__: cumulative arrears are paid first (priority + time-protection), then current stated dividends, then surplus is shared. <br/> Motivation: maximum protection for preference shareholders — low years are "banked" (cumulative) and high years provide upside participation; this is the most creditor-like preference share from the shareholder perspective. <br/> If dividend is __low__ (not enough to cover all arrears plus current): ordinary gets nothing; preference receives as much as available, with remaining arrears carrying forward again. <br/> Tank model: preference tank has both a debt meter (arrears) and a standard-level mark; pay off debt meter first, then fill to the standard level, then match ordinary to its standard level, then split overflow. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- cumulative preference shares: what are dividends in arrears? ::@:: Unpaid preference dividends from prior years that must be paid before any ordinary dividend when dividends resume. <br/> Note: no liability is recorded until the board declares a dividend; arrears are only disclosed in the notes to the financial statements. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- participating preference shares: how are extra dividends shared? ::@:: After preference and ordinary each receive their stated rate (and preference arrears for cumulative), any remaining dividend is shared pro-rata by par value. <br/> Example: preference par 100 000, ordinary par 400 000, total par 500 000; remaining 20 000 is split 20% (4 000) to preference and 80% (16 000) to ordinary. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- preference dividend allocation example (non-cumulative, participating): totals? ::@:: Step 1 — each class gets stated 6%: preference 6 000; ordinary 24 000. <br/> Step 2 — remaining 20 000 split by par (20% / 80%): preference 4 000; ordinary 16 000. <br/> Step 3 — totals: preference 10 000; ordinary 40 000 out of 50 000 total. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- preference dividend allocation example (cumulative, participating): totals? ::@:: Step 1 — _Dividends payable — preference_ arrears (2 yrs × 6 000) + current 6 000 = 18 000; _Dividends payable — ordinary_ current 6% = 24 000; remaining 50 000 − 42 000 = 8 000. <br/> Step 2 — remaining 8 000 split by par (20%/80%): _Dividends payable — preference_ 1 600; _Dividends payable — ordinary_ 6 400. <br/> Final: _Dividends payable — preference_ 19 600; _Dividends payable — ordinary_ 30 400. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- dividend on treasury shares: accounting treatment ::@:: _Treasury shares_ held by the company do not usually receive a dividend. If _Treasury shares_ are sold/cancelled between declaration and record dates, new holders receive the dividend only if they held the shares on the record date (the "date of record" determines entitlement). <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->

---

## edge cases and special situations in equity

Beyond the standard cash dividend or textbook small share dividend, equity transactions involve a range of edge cases that require careful analysis.

One recurring complication arises with __fractional shares__. When a share dividend creates fractional entitlements (e.g. 1.5 shares per share held), the company must choose whether to pay cash for the fractions, round up or down per shareholder, or consolidate fractional entitlements through a holding agent. Whichever approach is chosen, the full dividend declaration is recorded in the usual way; any cash paid in lieu of fractional shares is settled through the liability.

A related timing issue concerns __when equity is reduced__. Equity declines on the __declaration date__ (not the record date or payment date). The record date only identifies who receives the dividend; the payment date merely extinguishes the liability. If a dividend is declared but not paid before a period end, _Dividends payable_ appears as a current liability on the balance sheet.

Should the board need to reverse or correct a dividend declared in error, the safest approach is to ask __which stage has already happened__. If the error is caught __after declaration but before payment__, the bookkeeping reversal usually mirrors the declaration entry: for a cash dividend, Dr _Dividends payable_, Cr _Retained earnings_. If the amount is merely being corrected rather than cancelled, adjust the same accounts by the amount of the overstatement or understatement. If the issue is discovered only __after distribution__, then it is no longer a simple dividend-reversal problem; the dividend entry has already been completed, so any recovery or correction is accounted for as a new transaction rather than by pretending the payment never happened.

Examples help fix the idea. If a 100 000 cash dividend was declared but then cancelled before payment, reverse it by Dr _Dividends payable_ 100 000 and Cr _Retained earnings_ 100 000. If instead only 10 000 of the declared amount was an error, reverse just that overstatement by Dr _Dividends payable_ 10 000 and Cr _Retained earnings_ 10 000. For share or property dividends, use the same logic: reverse the declaration-stage distributable/payable balance and restore the equity amount that had been reclassified, provided distribution has not yet occurred.

Conditional dividends inject an additional layer of uncertainty. If a board declares a dividend subject to a future condition (e.g. "only if Q4 profit exceeds 50 000"), a liability is recorded __only if the condition is probable and measurable__. If not, the contingency is disclosed in the notes; the entry follows once the condition is met.

For __cumulative preference shares__, partial-year arrears require proration. A dividend declared in June on a January–December fiscal year typically gives cumulative preference shareholders only six months' arrears rather than a full year, unless the preference terms specify otherwise. Multiple dividend declarations within a single year are each allocated separately, with arrears re-assessed at each declaration date.

Finally, some transactions interact with share dividends before the distribution date. If new shares are issued or treasury shares are repurchased between declaration and distribution, the share dividend may need to be recalculated based on the updated outstanding share count. Similarly, when both ordinary and preference shares receive share dividends, each class's declaration and distribution entries are maintained independently — preference shareholders receive preference shares (or ordinary shares only if the articles permit), and entries are not blended across classes. For dividends declared in a foreign currency, the _Dividends payable_ liability is translated at the spot rate on the declaration date; any subsequent exchange gain or loss before payment flows through income or OCI.

> _Partial reversal of dividend declared in error._ Harbor Freight Logistics Ltd. declares a cash dividend of {@{€100&nbsp;000}@}, but before payment discovers that {@{€10&nbsp;000}@} of the declaration was an error. The correction is made before any cash is paid.
>
> | {@{Reverse overstated portion of declared cash dividend}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Dividends payable}@} | {@{10&nbsp;000}@} | |
> | {@{Retained earnings}@} | | {@{10&nbsp;000}@} |
>
> _Explanation._ Because the error is found {@{after declaration but before payment}@}, the correction simply reverses part of the original declaration entry. <!--SR:!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,315!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321-->

<!-- markdownlint-disable-next-line MD028 -->
> _Treasury shares do not receive dividends._ SilverPeak Retail plc has {@{100&nbsp;000 issued ordinary shares}@}, of which {@{5&nbsp;000 are held as treasury shares}@}. It declares a cash dividend of {@{€0.50 per share}@}. The dividend is paid only on the {@{95&nbsp;000 shares outstanding in outside hands}@}, so the total dividend is {@{€47&nbsp;500}@}, not {@{€50&nbsp;000}@}.
>
> | {@{Declare cash dividend excluding treasury shares}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Retained earnings}@} | {@{47&nbsp;500}@} | |
> | {@{Dividends payable — ordinary}@} | | {@{47&nbsp;500}@} |
>
> _Explanation._ Treasury shares are {@{not treated as outstanding for dividend entitlement}@}, so they are excluded from the dividend calculation. <!--SR:!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321-->

---

Flashcards for this section are as follows:

- fractional shares in a share dividend: handling methods ::@:: (a) Pay cash for the fractional entitlement; (b) round down or up per shareholder; (c) consolidate fractional shares in a holding agent and distribute periodically. The declared dividend is recorded in full; any cash for fractional shares is recorded separately as Dr _Dividends payable_, Cr _Cash_. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- conditional/contingent dividend: when to record a liability? ::@:: If the condition is __probable__ and __measurable__, record a _Dividends payable_ liability and Dr _Retained earnings_ on declaration. If not probable or measurable, disclose contingently in the notes and record the entry only when the condition is satisfied. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- dividend declared but not yet distributed (payment date after period end): timing? ::@:: _Dividends payable_ is a liability at the declaration date (statement date); it is not an adjustment to retained earnings after the statement date (post-balance-sheet event). _Retained earnings_ is reduced as of the declaration date; the liability is settled on the payment date. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- dividend reversal after declaration but before payment: how recorded for a cash dividend? ::@:: Reverse the declaration entry: Dr _Dividends payable_, Cr _Retained earnings_. Example: if a 100 000 declared cash dividend is cancelled before payment, record Dr _Dividends payable_ 100 000 and Cr _Retained earnings_ 100 000. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- dividend correction after declaration: how recorded if only part of the declared amount was wrong? ::@:: Adjust the same declaration-stage accounts by the error amount. Example: if a declared cash dividend was overstated by 10 000, record Dr _Dividends payable_ 10 000 and Cr _Retained earnings_ 10 000 to reverse only the overstatement. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- dividend reversal or correction after declaration: what is the stage-based decision rule? ::@:: Ask which stage has already happened. If the dividend has been declared but not yet paid, reverse or adjust the declaration-stage payable/distributable and restore the related equity amount. If the dividend has already been distributed, it is no longer a simple reversal of the original declaration entry; any recovery or correction is treated as a new transaction. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- multiple dividend declarations in same year to same preference class: allocation rule ::@:: Each new dividend declaration triggers a fresh allocation. Arrears accumulated up to the prior declaration are satisfied before the new allocation; any new arrears from a skipped prior period are reset. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- cumulative preference: partial-year arrears on a mid-period declaration ::@:: If a dividend is declared in (say) June on a January–December year, arrears are usually prorated (e.g. 6 months ÷ 12 months × annual rate) unless the preference terms state otherwise. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- share dividends on both ordinary and preference shares: separate accounting? ::@:: Yes, each class is handled separately. Ordinary shareholders receive _Share dividends — ordinary_; preference shareholders receive _Share dividends — preference_ (or ordinary shares if terms permit). Each class has its own declaration and distribution entries. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- large share dividend followed by share split (before distribution): how to account? ::@:: Record the share dividend at the declaration. If the share split occurs before distribution, usual practice is to re-measure the _Ordinary share dividend distributable_ based on the post-split share count and fair value, or to apply the split to the dividend amount pro-rata; exact treatment depends on the course's guidance or standard. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- foreign-currency dividend: exchange gain/loss at payment? ::@:: _Dividends payable_ is recorded in local currency at spot rate on declaration date. If the exchange rate moves before payment, the gain or loss on settlement is recorded as a _Foreign exchange gain/(loss)_ in income or OCI, depending on the nature of the transaction. <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->
- dividend after acquisition/change of control: which shareholders receive? ::@:: Only shareholders on the record date receive the dividend. If control changes after declaration but before record date, new owners must receive the dividend if they held shares on the record date. <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->
- treasury shares and dividends: how are they treated at declaration? ::@:: Treasury shares are excluded from the dividend entitlement calculation, so the company declares dividends only on shares outstanding in the hands of outside shareholders. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->

## return on ordinary shareholders' equity (ROE)

Return on ordinary shareholders' equity measures how efficiently a company generates profit for ordinary shareholders based on the equity they have invested and retained. In this course, ROE focuses on the return available to ordinary shareholders __after__ preference dividends.

The basic formula is:

- __ROE__ = (Profit for the year − Preference dividends) ÷ Average ordinary shareholders' equity. <!--SR:!2026-04-11,4,270-->

Where:

- Profit for the year is profit after tax.
- Preference dividends (on cumulative preference shares) include both current-year dividends and any dividends in arrears that relate to the year.
- Average ordinary shareholders' equity is typically the average of ordinary share capital plus reserves and retained earnings attributable to ordinary shareholders (beginning and ending balances).

Intuitively:

- ROE answers "for each dollar of ordinary shareholders' equity, how many dollars of profit (after preference claims) did the company generate this year?"
- Higher ROE suggests more efficient use of ordinary shareholders' capital, but differences in leverage, business risk, and accounting policies must be considered when comparing firms.

---

Flashcards for this section are as follows:

- ROE: formula in this course ::@:: (Profit for the year − Preference dividends) ÷ Average ordinary shareholders' equity. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- ROE: why subtract preference dividends? ::@:: Because ROE is meant to measure the return available to ordinary shareholders after satisfying the fixed claims of preference shareholders. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- ROE: what goes into ordinary shareholders' equity? ::@:: Ordinary _Share capital_ plus reserves and _Retained earnings_ attributable to ordinary shareholders, usually averaged over the period (beginning and ending). <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- ROE: intuitive interpretation ::@:: For each dollar of ordinary shareholders' equity invested in the company, ROE shows how many dollars of profit (after preference dividends) were generated during the year. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->

## share dividends versus share splits

Both share dividends and share splits increase the number of shares outstanding, but their accounting effects differ:

- A __share dividend__ transfers an amount from retained earnings to share capital (and possibly share premium); total equity is unchanged, but the mix between retained earnings and share capital changes. Par value per share stays the same; number of shares increases.
- A __share split__ (e.g. 2-for-1) changes par value and the number of shares (par per share halves and share count doubles in a 2-for-1 split) but does not change total share capital or retained earnings; no journal entry is recorded in this course.

The numerical contrast matters. If a company with 100 000 shares at par 2 declares a 20% share dividend, it issues 20 000 new shares and reclassifies 40 000 within equity under IFRS. If the same company instead declares a 2-for-1 share split, shares increase to 200 000 and par per share falls to 1, but __no amount is transferred out of retained earnings__. So a share dividend changes the composition of equity, while a share split changes only the share count and par structure.

---

Flashcards for this section are as follows:

- share dividend vs share split: key accounting difference ::@:: Share dividend transfers retained earnings to share capital (par unchanged; shares ↑); share split changes par per share and number of shares but leaves share capital and retained earnings unchanged (no journal entry). <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- 2-for-1 share split: effect on par and shares ::@:: Par value per share halves and the number of shares doubles; total share capital remains the same. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- share dividend versus share split: why is a share dividend not just a small share split? ::@:: Because a share dividend reclassifies an amount from retained earnings into share capital, while a share split changes share count and par per share without reclassifying equity balances. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- share dividend versus share split: numerical contrast in the example ::@:: Starting from 100 000 shares at par 2, a 20% share dividend issues 20 000 new shares and reclassifies 40 000 within equity, whereas a 2-for-1 share split raises shares to 200 000 and cuts par per share to 1 without moving any amount out of retained earnings. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->

## retained earnings and reserves

Retained earnings represent cumulative profit not yet distributed as dividends; in this course, they also act as a legal cap on dividends (the company cannot declare dividends in excess of retained earnings, except for liquidating dividends). Sometimes management transfers part of retained earnings to a separate reserve within equity (e.g. "capital expenditure reserve") to signal that those profits are earmarked for a specific purpose and not intended for ordinary dividends.

---

Flashcards for this section are as follows:

- retained earnings: practical meaning in dividend decisions ::@:: Cumulative profit not yet distributed; acts as an upper limit on ordinary dividends (company generally cannot declare dividends greater than _Retained earnings_). <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->
- reserves within equity: why transfer from retained earnings? ::@:: To earmark part of _Retained earnings_ for a specific purpose (e.g. future capital expenditure) and signal that it is not intended for ordinary dividends. <!--SR:!2026-04-11,4,270!2026-04-11,4,270-->

## statement of changes in equity and overall equity presentation

The statement of financial position normally groups equity into the major balances that explain __where the shareholders' claim comes from__. In this course, the main line items are:

- __share capital__;
- __share premium__;
- __retained earnings__;
- __reserves__ and accumulated other comprehensive income, if relevant; and
- __treasury shares__ as a deduction from total equity.

The detailed movement schedule is the __statement of changes in equity__. It reconciles beginning and ending balances for each equity component and shows why equity changed during the period.

Typical causes of change are:

- profit or loss for the year;
- other comprehensive income;
- share issues and treasury-share transactions;
- dividends; and
- transfers between retained earnings and reserves.

This statement is especially useful because the income statement alone cannot explain equity changes caused by owner transactions. For example, a company may have high profit but still show lower retained earnings if it declared large dividends or transferred amounts into reserves.

---

Flashcards for this section are as follows:

- statement of changes in equity: why is it needed? ::@:: Because profit alone cannot explain owner transactions, dividends, reserve transfers, share issues, treasury-share movements, and OCI changes that also move equity. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->
- equity presentation: what big line items should the reader expect? ::@:: Share capital, share premium, retained earnings, reserves / accumulated OCI when relevant, and treasury shares as a deduction. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->

### how to present equity cleanly in journal entries and in the equity section

When one transaction touches several equity accounts, present each class and each premium account __on its own line__. Do not collapse everything into one generic _Share capital_ or one generic _Share premium_ if the question distinguishes:

- ordinary versus preference shares,
- different preference series,
- treasury-share balances, or
- reserves and retained earnings.

The journal entry should show the __movement by account__. The statement of financial position or statement of changes in equity should show the __ending balances by account__. Those are related but not identical views.

<!-- markdownlint-disable-next-line MD028 -->
> _Comprehensive equity-presentation example._ A company raises cash by issuing {@{20 000 ordinary shares with €2 par at €6 each}@} and {@{5 000 preference shares with €10 par at €12 each}@}. The transaction should be presented class by class in the journal entry.
>
> | {@{Present a combined equity-raising transaction by separate equity lines instead of lumping everything together}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{180 000}@} | |
> | {@{Share capital — ordinary}@} | | {@{40 000}@} |
> | {@{Share premium — ordinary}@} | | {@{80 000}@} |
> | {@{Share capital — preference}@} | | {@{50 000}@} |
> | {@{Share premium — preference}@} | | {@{10 000}@} |
>
> _Presentation logic._ The journal entry shows the {@{movement in each equity account}@}. If the statement of financial position were prepared immediately afterward, the equity section would present those same balances as separate line items such as {@{Share capital — ordinary, Share premium — ordinary, Share capital — preference, Share premium — preference, Retained earnings, reserves, and Treasury shares (deduction)}@}. That is the clean way to present an equity-heavy transaction on an exam. <!--SR:!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321-->

<!-- markdownlint-disable-next-line MD028 -->
> _Simple statement-of-changes logic._ Beginning retained earnings are {@{300 000}@}. Profit for the year is {@{120 000}@}. Cash dividends are {@{40 000}@}, and the company transfers {@{20 000}@} from retained earnings to a capital-expenditure reserve.
>
> | Equity component | Beginning | Change | Ending |
> | --- | ---: | ---: | ---: |
> | {@{Retained earnings}@} | {@{300 000}@} | {@{+120 000 − 40 000 − 20 000}@} | {@{360 000}@} |
> | {@{Capital expenditure reserve}@} | {@{0}@} | {@{+20 000}@} | {@{20 000}@} |
>
> _Interpretation._ Total equity rises because profit exceeds the dividend, but the statement of changes in equity also shows that not all of the increase stays in retained earnings. <!--SR:!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,315!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,315-->

---

Flashcards for this section are as follows:

- equity presentation cleanliness: what should not be lumped together? ::@:: Do not collapse ordinary and preference capital, different series, treasury-share balances, reserves, or retained earnings into one generic equity line when the problem distinguishes them. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- journal-entry view versus statement-of-changes view ::@:: The journal entry shows account-by-account movement from the transaction, while the statement of changes in equity shows the ending balances after all those movements are reconciled. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
- comprehensive equity presentation: how should a journal entry show multiple equity classes? ::@:: Put each equity account on its own line—such as _Share capital — ordinary_, _Share premium — ordinary_, _Share capital — preference_, and _Share premium — preference_—instead of netting unlike equity components together. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- equity section presentation: which balances should usually stay visibly separate? ::@:: Ordinary share capital, ordinary share premium, preference share capital, preference share premium, retained earnings, reserves or accumulated OCI, and treasury shares as a deduction. <!--SR:!2026-04-12,4,315!2026-04-12,4,321-->

## book value per ordinary share

__Book value per ordinary share__ asks how much ordinary equity is attributable to each ordinary share based on accounting carrying amounts, not market price.

The usual formula is:

- `Book value per ordinary share = ordinary shareholders' equity / ordinary shares outstanding`

If the company has preference shares with a prior claim on net assets, the preference amount is removed first. The exact amount deducted depends on the terms:

- if the preference shares are __non-participating__, subtract the amount payable to preference shareholders on liquidation, often par plus any dividend arrears or liquidation premium if relevant;
- if the preference shares are __participating__, the allocation must reflect the extra participation rights as well.

So the safe calculation order is:

1. compute the preference shareholders' liquidation amount from the share terms;
2. subtract that preference claim from total equity to obtain the amount attributable to ordinary shareholders; and
3. divide by ordinary shares outstanding.

Book value per share is not the same as market price per share. Market price reflects investors' expectations about future profitability and risk. Book value per share reflects the accounting net assets currently attributable to ordinary shareholders.

> _Book value per ordinary share example._ Total equity is {@{900 000}@}. Included within that total are {@{100 000 preference shares with par 1, but their liquidation amount is 120 000}@}. Ordinary shares outstanding are {@{260 000}@}. The correct deduction is therefore the {@{full preference liquidation amount of 120 000, not merely the par amount of 100 000}@}. So ordinary equity is {@{900 000 − 120 000 = 780 000}@}, and book value per ordinary share is {@{780 000 / 260 000 = 3.00}@}. If one incorrectly subtracted only par, one would overstate book value per ordinary share. <!--SR:!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,328-->

---

Flashcards for this section are as follows:

- book value per ordinary share: formula ::@:: Ordinary shareholders' equity divided by ordinary shares outstanding. <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->
- book value per ordinary share: why subtract preference claims first? ::@:: Because book value per ordinary share should measure only the net assets attributable to ordinary shareholders after satisfying prior preference claims. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- book value per ordinary share: what is the safe step-by-step method when preference shares exist? ::@:: First compute the preference liquidation amount from the share terms, then subtract that amount from total equity to get ordinary equity, then divide by ordinary shares outstanding. <!--SR:!2026-04-12,4,328!2026-04-12,4,328-->
- book value per share versus market price ::@:: Book value per share uses accounting net assets, while market price reflects investors' expectations about future profitability, growth, and risk. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- book value per ordinary share example: total equity 900 000, preference liquidation amount 120 000, ordinary shares 260 000—result? ::@:: Ordinary equity is 780 000, so book value per ordinary share is 3.00. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- book value per ordinary share: why is subtracting only preference par sometimes wrong? ::@:: Because the preference claim on liquidation may exceed par once liquidation premiums or cumulative dividends in arrears are included; book value per ordinary share must deduct the full liquidation amount, not just stated capital. <!--SR:!2026-04-12,4,328!2026-04-12,4,328-->

## restrictions on retained earnings

Not all retained earnings are always freely available for dividends. A company may face __restrictions on retained earnings__ even when the balance is positive.

Common restrictions in the course material are:

- __legal restrictions__, such as statutory capital-maintenance rules;
- __contractual restrictions__, such as loan covenants that limit dividends until specified ratios are maintained;
- __board-designated restrictions__, where management transfers part of retained earnings into a reserve for a planned purpose; and
- __practical restrictions__, where retained earnings exists on paper but liquidity is tied up in operations.

The accounting effect depends on the type of restriction.

- A __formal appropriation__ within equity is shown by transferring an amount from retained earnings into a named reserve.
- A __covenant or legal restriction__ may require disclosure even if no separate journal entry is made.

The main exam idea is that a positive retained-earnings balance does __not__ automatically mean the whole amount can be distributed immediately.

> _Restriction by appropriation._ A company with retained earnings of {@{500 000}@} decides to earmark {@{150 000}@} for future plant expansion.
>
> | {@{Transfer retained earnings into plant-expansion reserve}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Retained earnings}@} | {@{150 000}@} | |
> | {@{Plant expansion reserve}@} | | {@{150 000}@} |
>
> _Interpretation._ Total equity is unchanged, but only the unappropriated portion of retained earnings remains clearly available for ordinary dividends. <!--SR:!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321!2026-04-12,4,315!2026-04-12,4,321-->

---

Flashcards for this section are as follows:

- restrictions on retained earnings: common sources ::@:: Legal restrictions, contractual restrictions such as loan covenants, board-designated appropriations, and practical liquidity constraints. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- can a company have positive retained earnings but still face dividend limits? ::@:: Yes; legal, contractual, or internal restrictions may limit how much of retained earnings is actually available for distribution. <!--SR:!2026-04-12,4,321!2026-04-12,4,315-->
- retained earnings appropriation: journal-entry effect ::@:: Debit retained earnings and credit a reserve within equity; total equity does not change. <!--SR:!2026-04-12,4,315!2026-04-12,4,315-->
- restrictions on retained earnings: why is disclosure important? ::@:: Because users may otherwise assume the full retained-earnings balance is freely available for dividends when part of it is legally or contractually restricted. <!--SR:!2026-04-12,4,321!2026-04-12,4,321-->
