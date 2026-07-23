---
aliases:
  - EPS
  - diluted earnings per share
  - dilutive securities and earnings per share
  - earnings per share
tags:
  - flashcard/active/special/academia/HKUST/ACCT_3020/dilutive_securities_and_earnings_per_share
  - language/in/English
---

# dilutive securities and earnings per share

This note covers the ACCT 3020 material on convertible debt, convertible preference shares, warrants, share-based compensation, share-appreciation rights, and the computation and presentation of basic and diluted earnings per share under IFRS. The topic has two linked ideas. First, many securities start as debt or equity but can later become ordinary shares. Second, because those securities can increase the number of ordinary shares, the company must show both the earnings currently available to ordinary shareholders and the earnings per share that would result if dilutive instruments were converted or exercised.

A useful high-level split is:

- __simple capital structure__: only ordinary shares are outstanding, so basic EPS and diluted EPS are the same.
- __complex capital structure__: the company also has convertible securities, options, warrants, or similar rights that may reduce EPS.

## convertible securities: debt and preference shares

Convertible securities combine current financing with a possible future move into ordinary equity.

---

Flashcards for this section are as follows:

- convertible securities: parent-level idea ::@:: These instruments begin as financing but may later become ordinary equity, so the accounting must explain both the current financing claim and the possible future share issuance. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible debt versus convertible preference shares ::@:: Convertible debt starts with a liability component plus an equity component, while convertible preference shares are treated as equity from the start in this course. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

### convertible debt

A __convertible bond__ is a compound instrument under IFRS because it contains both:

- a __liability component__: the contractual coupon and principal cash flows; and
- an __equity component__: the holder's option to convert into a fixed number of ordinary shares.

The course uses the __with-and-without__ logic at issuance:

1. Start with the issue proceeds of the convertible bond as a whole.
2. Compute the fair value of the liability component by discounting the contractual bond cash flows at the market rate for similar __non-convertible__ debt.
3. Put the residual into equity as _Share premium — conversion equity_.

This matters because later interest expense is based on the __liability carrying amount__ and the __market rate__, not on the stated coupon alone. The equity component stays in equity until maturity, conversion, or repurchase.

Two transcript details are easy to miss.

- If the bonds are converted __before maturity__, remove the liability at its __carrying amount__, not automatically at face value, because effective-interest amortization has already changed the debt component.
- If the issuer __repurchases__ the convertible debt for cash instead of waiting for conversion, the settlement gain or loss belongs to the __liability__ analysis. The conversion-equity component is still an equity item rather than an operating profit-or-loss item.

Representative examples:

> _Convertible bond issued at par but with a lower coupon than market debt._ Roche issues {@{2&nbsp;000 convertible bonds with face value €1&nbsp;000 each}@}. Total proceeds are {@{€2&nbsp;000&nbsp;000}@}. The bonds pay {@{6% annual interest over 4 years}@}, and each bond converts into {@{250 ordinary shares with €1 par}@}. Similar non-convertible debt yields {@{9%, so the liability component is only €1&nbsp;805&nbsp;606 and the residual equity component is about €194&nbsp;394 by logic}@}; the course illustration uses {@{€194&nbsp;374 after rounding}@}.
>
> | {@{Issue convertible debt}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{2&nbsp;000&nbsp;000}@} | |
> | {@{Bonds payable}@} | | {@{1&nbsp;805&nbsp;606}@} |
> | {@{Share premium — conversion equity}@} | | {@{194&nbsp;394}@} |
>
> _Course note._ Use the course's rounded equity figure if you are matching the slide deck exactly; the accounting idea is unchanged. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Conversion at maturity._ For the {@{Roche convertible bonds issued above — 2&nbsp;000 bonds with total face value €2&nbsp;000&nbsp;000, convertible into 500&nbsp;000 ordinary shares with €1 par}@}, assume conversion occurs at maturity instead of cash repayment. The liability is removed and the equity component is transferred within equity.
>
> | {@{Convert bonds into ordinary shares at maturity}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Share premium — conversion equity}@} | {@{194&nbsp;374}@} | |
> | {@{Bonds payable}@} | {@{2&nbsp;000&nbsp;000}@} | |
> | {@{Share capital — ordinary}@} | | {@{500&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{1&nbsp;694&nbsp;374}@} |
>
> _Explanation._ There is {@{no gain or loss on conversion}@}. The transaction is treated as a capital reclassification, not a settlement gain. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Induced conversion._ If the issuer offers an extra cash sweetener to persuade bondholders to convert early, that extra payment is a {@{current-period conversion expense}@}, not part of ordinary share premium. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Repurchase of convertible debt before maturity._ A company repurchases convertible bonds for {@{€990&nbsp;000 cash}@}. At the repurchase date, the {@{liability carrying amount is €950&nbsp;000}@}, the {@{fair value of the liability component is €970&nbsp;000}@}, and the remaining {@{€20&nbsp;000 of the repurchase price is attributed to the equity component}@}.
>
> | {@{Repurchase convertible debt before maturity}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Bonds payable}@} | {@{950&nbsp;000}@} | |
> | {@{Loss on extinguishment of debt}@} | {@{20&nbsp;000}@} | |
> | {@{Share premium — conversion equity}@} | {@{20&nbsp;000}@} | |
> | {@{Cash}@} | | {@{990&nbsp;000}@} |
>
> _Explanation._ The liability piece is settled as debt, so the company compares {@{liability fair value €970&nbsp;000}@} with {@{liability carrying amount €950&nbsp;000}@} and recognizes a {@{€20&nbsp;000 loss because the liability fair value exceeds its carrying amount}@}. The residual {@{€20&nbsp;000 repurchase amount attributable to the equity component}@} reduces the equity component directly. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Same instrument converted instead of repurchased._ Assume the same convertible debt above is {@{converted into ordinary shares immediately instead of being repurchased for cash}@}. At the conversion date, the {@{liability carrying amount is still €950&nbsp;000}@} and the remaining {@{Share premium — conversion equity is €20&nbsp;000}@}. The conversion produces ordinary shares with total {@{€100&nbsp;000 par}@}.
>
> | {@{Convert the same convertible debt instead of repurchasing it}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Bonds payable}@} | {@{950&nbsp;000}@} | |
> | {@{Share premium — conversion equity}@} | {@{20&nbsp;000}@} | |
> | {@{Share capital — ordinary}@} | | {@{100&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{870&nbsp;000}@} |
>
> _Explanation._ This is the contrast the exam likes: a {@{cash repurchase can create a gain or loss because debt is being extinguished for consideration}@}, but a {@{conversion is only a reclassification within equity and therefore creates no gain or loss}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Induced conversion with a cash sweetener._ A company has {@{€500&nbsp;000 par convertible bonds}@} outstanding, convertible into {@{40&nbsp;000 ordinary shares with €1 par}@}. The original balance in {@{Share premium — conversion equity is €12&nbsp;000}@}. To induce immediate conversion, the company pays a {@{€30&nbsp;000 cash sweetener}@}.
>
> | {@{Record induced conversion of convertible debt}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Conversion expense}@} | {@{30&nbsp;000}@} | |
> | {@{Share premium — conversion equity}@} | {@{12&nbsp;000}@} | |
> | {@{Bonds payable}@} | {@{500&nbsp;000}@} | |
> | {@{Cash}@} | | {@{30&nbsp;000}@} |
> | {@{Share capital — ordinary}@} | | {@{40&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{472&nbsp;000}@} |
>
> _Explanation._ The {@{sweetener is an expense of the current period}@}. The rest of the entry still follows ordinary conversion accounting, with {@{no gain or loss on conversion itself}@}. <!--SR:!fsrs,2026-08-08T14:57:26.510Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:26.510Z!fsrs,2026-08-08T14:57:15.759Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:15.759Z!fsrs,2026-08-08T14:57:28.632Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:28.632Z!fsrs,2026-08-08T14:57:49.677Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:49.677Z!fsrs,2026-08-08T14:58:08.181Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:58:08.181Z!fsrs,2026-08-08T14:57:25.554Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:25.554Z!fsrs,2026-08-27T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-17T00:00:00.000Z!fsrs,2026-08-08T14:57:23.834Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:23.834Z!fsrs,2026-08-08T14:57:27.383Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:27.383Z!fsrs,2026-08-08T14:57:18.018Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:18.018Z!fsrs,2026-08-08T14:57:28.077Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:28.077Z!fsrs,2026-08-08T14:57:23.128Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:23.128Z!fsrs,2026-08-08T14:57:54.763Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:54.763Z!fsrs,2026-08-08T14:58:05.738Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:58:05.738Z!fsrs,2026-11-22T00:00:00.000Z,130,129.8425842,3.96783414,2,3,0,0,2026-07-15T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- convertible debt: what is the with-and-without split doing? ::@:: It values the debt as if it were non-convertible and treats the residual as the equity value of the conversion option. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible debt: why can repurchase create a gain or loss while conversion does not? ::@:: A repurchase is a debt extinguishment for consideration, but a conversion is only a reclassification within equity. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible bond: why is it a compound instrument? ::@:: Because it contains both a liability component (coupon and principal cash flows) and an equity component (the conversion option into a fixed number of ordinary shares). <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- with-and-without method: steps ::@:: Start with total issue proceeds, value the liability component using the market rate for similar non-convertible debt, and treat the residual as equity. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible debt: why is the coupon rate not enough for later interest expense? ::@:: Because interest expense follows the effective-interest method on the liability component, so it is based on the carrying amount and the market rate for similar debt. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible debt: what happens to the equity component at maturity if the bonds are repaid in cash? ::@:: It remains in equity or is transferred within equity; it is not reclassified back into a liability. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible debt: conversion at maturity—profit or loss effect? ::@:: No gain or loss is recognized; the liability is removed and the conversion-equity balance is transferred into ordinary equity accounts. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible debt: if conversion happens before maturity, what liability amount is removed? ::@:: The bond's carrying amount at the conversion date, not automatically the face value. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- induced conversion: how is the sweetener treated? ::@:: As a current-period conversion expense, not as part of ordinary share premium. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible debt repurchase: where does any gain or loss belong? ::@:: To the liability settlement analysis, while the equity component remains an equity reclassification rather than an operating gain or loss. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible debt repurchase before maturity: how is the repurchase price split? ::@:: First allocate consideration to the liability component at its fair value to determine the gain or loss on debt settlement; the residual consideration is treated as a reduction of the conversion-equity component. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- Roche: 2 000 bonds × €1 000 = €2 000 000, 6% coupon, 4 years, non-convertible rate 9% → equity component = ? ::@:: Liability component = PV of cash flows at 9% = €1 805 606; equity = €2 000 000 − €1 805 606 = €194 394 credited to _Share premium — conversion equity_. <!--SR:!fsrs,2026-08-02T00:00:00.000Z,42,41.57871783,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

### convertible preference shares

Under __IAS 32__, whether a preference share is a liability or equity depends on whether the issuer has a __contractual obligation to deliver cash__. If the preference share is __mandatorily redeemable__ (the issuer must redeem it for cash at a specified date), it is classified as a __financial liability__; the same with-and-without split used for convertible bonds would then apply. In the typical course case, the convertible preference shares carry no such mandatory redemption obligation, so they are classified as __equity__ from the outset.

A __convertible preference share__ in this course is therefore treated as equity from the start. When the preference shares are converted or repurchased, the change remains within equity and there is generally __no gain or loss__ in profit or loss.

> _Convertible preference share issuance._ A company issues {@{1&nbsp;000 convertible preference shares}@} with {@{€1 par}@} at {@{€200 per share}@}.
>
> | {@{Issue convertible preference shares}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{200&nbsp;000}@} | |
> | {@{Share capital — preference}@} | | {@{1&nbsp;000}@} |
> | {@{Share premium — conversion equity}@} | | {@{199&nbsp;000}@} | <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Convertible preference shares converted into ordinary shares._ Assume {@{2&nbsp;000 preference shares with €2 par}@} were issued at {@{€60 each}@}, so total book value is {@{€120&nbsp;000}@}. Each preference share converts into {@{4 ordinary shares with €5 par}@}.
>
> | {@{Convert preference shares into ordinary shares}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Share capital — preference}@} | {@{4&nbsp;000}@} | |
> | {@{Share premium — conversion equity}@} | {@{116&nbsp;000}@} | |
> | {@{Share capital — ordinary}@} | | {@{40&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{80&nbsp;000}@} |
>
> _Explanation._ The total {@{book value of the preference shares stays inside equity}@}. The conversion only reallocates that book value between _ordinary share capital_ and _ordinary share premium_. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Repurchase of convertible preference shares._ Using the same preference shares above, assume the company repurchases them for {@{€150&nbsp;000 cash}@} instead of converting them.
>
> | {@{Repurchase convertible preference shares above book value}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Share capital — preference}@} | {@{4&nbsp;000}@} | |
> | {@{Share premium — conversion equity}@} | {@{116&nbsp;000}@} | |
> | {@{Retained earnings}@} | {@{30&nbsp;000}@} | |
> | {@{Cash}@} | | {@{150&nbsp;000}@} |
>
> _Explanation._ Because the shares are already {@{equity instruments rather than liabilities}@}, the excess of repurchase price over book value is charged to {@{retained earnings rather than profit or loss}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- convertible preference shares: what is the main accounting contrast with convertible debt? ::@:: They are treated as equity from the beginning, so later conversion or repurchase stays inside equity rather than creating debt-settlement gain or loss. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-02T00:00:00.000Z,42,41.57871783,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible preference share repurchase above book value: where does the excess go? ::@:: To _Retained earnings_, because the transaction is an equity transaction rather than a profit-or-loss event. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible preference shares: main accounting difference from convertible debt ::@:: Convertible preference shares are treated as equity from the start, so conversion or repurchase generally stays within equity and does not create profit-or-loss gains or losses. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible preference shares: when would IAS 32 require liability classification? ::@:: When the preference share is mandatorily redeemable — the issuer is contractually obligated to deliver cash at a future date. In that case the liability component is valued first and the residual is equity, just as for convertible bonds. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

## warrants and share-based compensation

A __share warrant__ gives the holder the right to buy ordinary shares at a stated price within a stated period. In this course, warrants matter in two common situations:

- they are attached to another security, often to make debt easier to sell; and
- they are granted as part of employee compensation.

When warrants are issued together with bonds or similar financing, the company allocates the proceeds between the debt and the warrant equity component. The course again uses a __with-and-without__ idea: value the debt component as if no warrant existed, then treat the residual as _Share premium — share warrants_.

---

Flashcards for this section are as follows:

- warrants and share-based compensation: parent-level split ::@:: Warrants can appear either as financing sweeteners attached to securities or as compensation tools granted to employees. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- warrants issued with debt: what is the allocation logic? ::@:: Value the debt as if no warrant existed and place the residual proceeds in warrant equity. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

### detachable warrants and warrant equity

The lecture also distinguishes __warrants__ from the shorter-term __options__ used in derivative examples. Warrants are usually longer-dated issuer-related rights and, when exercised, normally create __new ordinary shares__. Options are often shorter-term market contracts discussed from the holder's trading perspective.

> _Bonds with detachable warrants._ Siemens issues debt with detachable warrants. Total proceeds are {@{€10&nbsp;200&nbsp;000}@}. The present value of the bond cash flows without the warrants is {@{€9&nbsp;707&nbsp;852}@}. The residual amount allocated to the warrants is {@{€492&nbsp;148}@}.
>
> | {@{Issue bonds with detachable warrants}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{10&nbsp;200&nbsp;000}@} | |
> | {@{Bonds payable}@} | | {@{9&nbsp;707&nbsp;852}@} |
> | {@{Share premium — share warrants}@} | | {@{492&nbsp;148}@} | <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-02T00:00:00.000Z,42,41.57871783,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Exercise of all warrants._ Assume the detachable warrants above carry a remaining balance of {@{€492&nbsp;148}@} and let investors buy {@{10&nbsp;000 ordinary shares with €5 par}@} at {@{€25 each}@}.
>
> | {@{Exercise detachable warrants}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{250&nbsp;000}@} | |
> | {@{Share premium — share warrants}@} | {@{492&nbsp;148}@} | |
> | {@{Share capital — ordinary}@} | | {@{50&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{692&nbsp;148}@} | <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Partial warrant exercise followed by lapse of the rest._ Suppose instead that only {@{8&nbsp;000 of the 10&nbsp;000 detachable warrants are exercised}@} at {@{€25 each}@}, while the remaining {@{2&nbsp;000 warrants expire unexercised}@}. The warrant-equity balance is therefore split proportionally.
>
> | {@{Exercise only part of the detachable warrants}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{200&nbsp;000}@} | |
> | {@{Share premium — share warrants}@} | {@{393&nbsp;718}@} | |
> | {@{Share capital — ordinary}@} | | {@{40&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{553&nbsp;718}@} |
>
> | {@{Reclassify the lapsed portion of detachable warrants within equity}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Share premium — share warrants}@} | {@{98&nbsp;430}@} | |
> | {@{Share premium — expired share warrants}@} | | {@{98&nbsp;430}@} |
>
> _Explanation._ The original warrant balance does {@{not all move into ordinary share premium just because some warrants were exercised}@}. The exercised and expired portions are {@{tracked separately and proportionally}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2027-04-18T00:00:00.000Z,264,264.31905225,1,2,4,0,0,2026-07-28T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- detachable warrants: what happens to the previously recorded warrant equity on exercise? ::@:: It is transferred out of _Share premium — share warrants_ and combined with cash proceeds to form _ordinary share capital_ and _ordinary share premium_. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- detachable warrants versus options in this course ::@:: Warrants are issuer-side equity-linked rights that commonly create new shares, while options in other examples are usually shorter-term market contracts. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- warrant: definition ::@:: A share warrant gives the holder the right to buy ordinary shares at a stated price within a stated period. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- warrants issued with debt: why is part of the proceeds allocated to equity? ::@:: Because the warrants are a separate equity-type benefit given to investors, so the total proceeds must be split between the debt and the warrant component. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- warrants with debt: allocation logic ::@:: Value the debt as if it had no warrant attached, then treat the residual as _Share premium — share warrants_. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- warrant exercise: general entry structure ::@:: Dr _Cash_ for the exercise proceeds, Dr _Share premium — share warrants_ for the previously allocated warrant balance, then Cr _Share capital — ordinary_ at par and Cr _Share premium — ordinary_ for the remainder. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- detachable warrants: what happens if only part of the warrants are exercised and the rest lapse? ::@:: Reclassify the exercised portion of _Share premium — share warrants_ into ordinary equity in proportion to the warrants exercised, and reclassify the lapsed portion to an expired-warrants equity account rather than to income. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- Siemens: total proceeds €10&nbsp;200&nbsp;000, bond PV (no warrants) = €9&nbsp;707&nbsp;852 → warrant equity = ? ::@:: Residual = €10&nbsp;200&nbsp;000 − €9&nbsp;707&nbsp;852 = €492&nbsp;148 credited to _Share premium — share warrants_. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

### employee share-based compensation

Share-based compensation goes beyond financing. It is meant to align employees' incentives with shareholder value. Under IFRS, the course uses the __fair-value method__.

For a __share option plan__:

- measure total compensation at the __grant date__ using an acceptable option-pricing model such as Black-Scholes;
- recognize compensation expense over the __service period__ (vesting period); and
- move the accumulated amount from _Share premium — share options_ into ordinary equity when the option is exercised.

> _Share options granted to executives._ Chen grants {@{10&nbsp;000 options}@} with total fair-value-based compensation of {@{¥22&nbsp;000&nbsp;000}@}. The vesting period is {@{2 years}@}, so annual compensation expense is {@{¥11&nbsp;000&nbsp;000}@}.
>
> | {@{Recognize annual compensation expense for share options}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Compensation expense}@} | {@{11&nbsp;000&nbsp;000}@} | |
> | {@{Share premium — share options}@} | | {@{11&nbsp;000&nbsp;000}@} | <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Acceleration of vesting after one year._ Using the same grant above, assume a change in control causes the company to {@{accelerate vesting at the end of year 1}@}. The remaining unrecognized compensation of {@{¥11&nbsp;000&nbsp;000}@} must be recognized immediately.
>
> | {@{Recognize the remaining share-option compensation when vesting is accelerated}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Compensation expense}@} | {@{11&nbsp;000&nbsp;000}@} | |
> | {@{Share premium — share options}@} | | {@{11&nbsp;000&nbsp;000}@} |
>
> _Explanation._ The total grant-date fair value does {@{not change}@}; what changes is the {@{timing of expense recognition}@}. Acceleration creates a nasty one-period hit because the remaining compensation can no longer be spread over future service years. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Modification (repricing) of share options._ A company originally granted {@{10&nbsp;000 share options}@} with {@{exercise price €50}@} and total grant-date fair value {@{€80&nbsp;000}@} (€8 per option) over a {@{4-year vesting period}@}. After {@{2 years}@}, the share price has fallen below the exercise price, so the company reduces the exercise price to {@{€35}@}. At the modification date, the fair value of the unmodified options is {@{€3 per option}@} and the fair value of the modified options is {@{€7 per option}@}. The {@{incremental fair value is €4 per option (€7 − €3)}@}, giving total incremental compensation of {@{10&nbsp;000 × €4 = €40&nbsp;000}@} recognized over the remaining {@{2 years}@}.
>
> | {@{Recognize annual compensation expense in each of the 2 remaining years after repricing}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Compensation expense}@} | {@{40&nbsp;000}@} | |
> | {@{Share premium — share options}@} | | {@{40&nbsp;000}@} |
>
> _Explanation._ The charge each year combines the {@{original annual amount (€80&nbsp;000 ÷ 4 = €20&nbsp;000)}@} and the {@{incremental annual amount (€40&nbsp;000 ÷ 2 = €20&nbsp;000)}@} for a total of {@{€40&nbsp;000 per year}@}. Under {@{IFRS 2}@}, {@{any modification that increases the fair value of an equity-settled award}@} must be {@{recognized in addition to the original grant-date fair value}@}; {@{a modification that reduces fair value}@} is {@{ignored and the original grant-date compensation continues unchanged}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Partial exercise of vested share options._ Assume the company originally granted {@{6&nbsp;000 options}@} with total grant-date fair value {@{€12&nbsp;000&nbsp;000}@}. After vesting, executives exercise {@{1&nbsp;500 options}@} at {@{€4&nbsp;000 per share}@}. Each ordinary share has {@{€100 par}@}.
>
> | {@{Record partial exercise of vested share options}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{6&nbsp;000&nbsp;000}@} | |
> | {@{Share premium — share options}@} | {@{3&nbsp;000&nbsp;000}@} | |
> | {@{Share capital — ordinary}@} | | {@{150&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{8&nbsp;850&nbsp;000}@} |
>
> _Explanation._ Only the portion of {@{Share premium — share options related to the exercised 1&nbsp;500 options}@} is transferred on exercise. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Expiration of unexercised options._ If the remaining {@{4&nbsp;500 options}@} (grant-date fair value €2&nbsp;000 each) later expire unexercised, the unexercised balance is reclassified within equity.
>
> | {@{Record expiration of unexercised share options}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Share premium — share options}@} | {@{9&nbsp;000&nbsp;000}@} | |
> | {@{Share premium — expired share options}@} | | {@{9&nbsp;000&nbsp;000}@} |
>
> _Explanation._ The expired-option balance does {@{not stay indefinitely in Share premium — share options}@}; it is reclassified to a separate equity account for expired awards. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- employee share-based compensation: what is the IFRS measurement anchor here? ::@:: Grant-date fair value, recognized over the service or vesting period. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- employee share-based compensation: what happens to the accumulated equity amount on exercise? ::@:: The relevant portion of _Share premium — share options_ is transferred into _ordinary share capital_ and _ordinary share premium_. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- share options: measurement basis under IFRS in this course ::@:: Use the fair-value method at the grant date, usually with an option-pricing model such as Black-Scholes. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- share options: over what period is compensation expense recognized? ::@:: Over the service period or vesting period, because that is the period in which the employees earn the award. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- accelerated vesting of share options: what happens to the unrecognized grant-date fair value? ::@:: Recognize the remaining compensation expense immediately, because the service condition has effectively been satisfied at once. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- share options: what happens to the unexercised balance at expiration? ::@:: Reclassify the remaining balance in _Share premium — share options_ to an equity account such as _Share premium — expired share options_. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- share option modification (repricing): what incremental amount is recognized? ::@:: The difference between the fair value of the modified options and the fair value of the original unmodified options at the modification date, multiplied by the number of options, recognized over the remaining vesting period in addition to the original grant-date compensation. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-02T00:00:00.000Z,42,41.57871783,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- share option repricing: what if the modification reduces the fair value? ::@:: Ignore the reduction — the original grant-date compensation continues unchanged and no negative adjustment is made. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

#### restricted share plans

For a __restricted share plan__:

- shares are issued at grant, but the employee cannot freely sell or transfer them until vesting;
- the company records _Unearned compensation_ as a __contra-equity__ balance at grant; and
- compensation expense is then recognized over the service period.

> _Restricted shares granted to the CEO._ Ogden grants {@{1&nbsp;000 restricted shares}@} with fair value {@{&#36;20 each}@} and par {@{&#36;1}@}. The service period is {@{5 years}@}.
>
> | {@{Grant restricted shares}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Unearned compensation}@} | {@{20&nbsp;000}@} | |
> | {@{Share capital — ordinary}@} | | {@{1&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{19&nbsp;000}@} |
>
> | {@{Recognize one year's compensation expense}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Compensation expense}@} | {@{4&nbsp;000}@} | |
> | {@{Unearned compensation}@} | | {@{4&nbsp;000}@} | <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Restricted-share forfeiture before vesting._ Assume a company granted {@{500 restricted shares with €2 par and €30 fair value per share}@}. Total unearned compensation at grant was {@{€15&nbsp;000}@}. After {@{2 years of a 5-year service period}@}, the executive leaves before vesting, so previously recognized compensation of {@{€6&nbsp;000}@} must be reversed.
>
> | {@{Record forfeiture of restricted shares before vesting}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Share capital — ordinary}@} | {@{1&nbsp;000}@} | |
> | {@{Share premium — ordinary}@} | {@{14&nbsp;000}@} | |
> | {@{Compensation expense}@} | | {@{6&nbsp;000}@} |
> | {@{Unearned compensation}@} | | {@{9&nbsp;000}@} |
>
> _Explanation._ The company reverses both the {@{equity initially issued at grant}@} and the {@{compensation amounts recognized so far}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-02T00:00:00.000Z,42,41.57871783,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- restricted share plans: why is unearned compensation recorded at grant? ::@:: Because the shares are issued immediately, but the employee still owes service before the award is fully earned. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- restricted share forfeiture before vesting: what is reversed? ::@:: Reverse the issued equity balances and the compensation recognized so far, while clearing the remaining unearned compensation. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- restricted shares forfeited before vesting: what is reversed? ::@:: Reverse the share-capital and share-premium balances issued at grant, credit back previously recognized compensation expense, and clear the remaining unearned compensation. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

#### employee share-purchase plans

An __employee share-purchase plan__ is also compensatory when employees buy shares at a discount. The compensation expense is the discount from market price.

> _Employee share-purchase plan._ A company allows employees to buy {@{30&nbsp;000 ordinary shares with €1 par}@} at {@{€32 per share}@} when market price is {@{€40 per share}@}. The total discount-based compensation is therefore {@{€240&nbsp;000}@}.
>
> | {@{Issue shares under an employee share-purchase plan}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Cash}@} | {@{960&nbsp;000}@} | |
> | {@{Compensation expense}@} | {@{240&nbsp;000}@} | |
> | {@{Share capital — ordinary}@} | | {@{30&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{1&nbsp;170&nbsp;000}@} |
>
> _Explanation._ Compensation expense equals {@{(€40 − €32) × 30&nbsp;000 = €240&nbsp;000}@}. The discount is treated as compensation, not ignored as a mere pricing choice. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- employee share-purchase plan: what creates compensation expense? ::@:: The discount between the market price and the employee purchase price. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- employee share-purchase plan: why is the discount not ignored as pricing? ::@:: Because the reduced price is compensation given to employees for services, not just a normal financing discount. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- employee share-purchase plan: compensation expense equals what? ::@:: The difference between market price and employee purchase price, multiplied by the number of shares purchased. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

## share-appreciation rights

A __share-appreciation right__ (SAR) gives an executive compensation equal to the increase in the share price above a pre-established base price. The company may settle the SAR in cash, in shares, or in a combination of both.

The accounting depends on whether the SAR is classified as an __equity award__ or a __liability award__.

If the holder will receive __shares__, the award is treated more like an equity-settled share-based payment:

- determine a fair value at grant; and
- recognize compensation expense over the service period.

If the holder will receive __cash__, the SAR is a liability award:

- measure fair value at grant;
- accrue compensation over the service period; and
- __remeasure__ the fair value at each reporting date until settlement.

That remeasurement point is the key distinction. Equity awards lock in grant-date fair value; liability awards keep moving with market conditions until the company actually settles the obligation.

---

Flashcards for this section are as follows:

- share-appreciation rights: parent-level split ::@:: SAR accounting depends on settlement form: cash-settled awards are liability awards, while share-settled awards are equity awards. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- SARs: what is the key distinction after grant? ::@:: Liability awards are remeasured each reporting date, while equity awards stay anchored to grant-date fair value apart from vesting estimates. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2027-04-18T00:00:00.000Z,264,264.31905225,1,2,4,0,0,2026-07-28T00:00:00.000Z-->
- share-appreciation right: definition ::@:: A share-appreciation right gives the holder compensation equal to the increase in share price above a pre-established base price. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- SARs: what determines whether they are equity awards or liability awards? ::@:: The settlement form: if the holder receives shares, the award is treated as equity-settled; if the holder receives cash, it is treated as a liability award. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- SARs: why do liability awards create more volatility than equity awards? ::@:: Because the liability is remeasured each reporting period, so changes in share price keep changing compensation expense. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

### liability award SARs

> _Cash-settled SAR example._ Brazil Hotels grants {@{10&nbsp;000 SARs}@} with base price {@{R&#36;10}@}. At the end of 2025, each SAR has fair value {@{R&#36;3}@}, and the service period is {@{2 years}@}. The company records one half of the grant-date-equivalent obligation in year 1.
>
> | {@{Recognize first-year SAR compensation expense}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Compensation expense}@} | {@{15&nbsp;000}@} | |
> | {@{Liability under share-appreciation plan}@} | | {@{15&nbsp;000}@} |
>
> _Explanation._ The liability keeps changing afterward because the eventual settlement is in cash, not in shares. <!--SR:!fsrs,2026-08-08T14:58:00.702Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:58:00.702Z!fsrs,2026-08-08T14:57:29.375Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:29.375Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-08T14:58:06.632Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:58:06.632Z!fsrs,2026-08-08T14:57:24.738Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:57:24.738Z!fsrs,2026-08-08T14:58:01.566Z,56,56.31566409,3.98153807,2,2,0,0,2026-06-13T14:58:01.566Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Remeasurement of a cash-settled SAR liability._ Assume that at the end of the next year the required liability under the same SAR plan is reassessed downward to only {@{R&#36;10&nbsp;000}@}. Because the company already carries a liability of {@{R&#36;15&nbsp;000}@}, it recognizes {@{negative compensation expense of R&#36;5&nbsp;000}@}.
>
> | {@{Record downward remeasurement of SAR liability}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Liability under share-appreciation plan}@} | {@{5&nbsp;000}@} | |
> | {@{Compensation expense}@} | | {@{5&nbsp;000}@} |
>
> _Explanation._ Liability-settled SARs are {@{remeasured each reporting period}@}, so compensation expense can move {@{up or down}@} before settlement. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Cash settlement of SARs._ If the company later settles the SARs for {@{R&#36;28&nbsp;000 cash}@} when the liability on the books is still {@{R&#36;10&nbsp;000}@}, it first records the final increase and then pays cash.
>
> | {@{Record final increase in SAR liability before settlement}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Compensation expense}@} | {@{18&nbsp;000}@} | |
> | {@{Liability under share-appreciation plan}@} | | {@{18&nbsp;000}@} |
>
> | {@{Settle SAR liability in cash}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Liability under share-appreciation plan}@} | {@{28&nbsp;000}@} | |
> | {@{Cash}@} | | {@{28&nbsp;000}@} | <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Partial cash settlement while some vested SARs remain outstanding._ Assume a liability-award SAR plan has {@{20&nbsp;000 vested SARs and a carrying liability of R&#36;60&nbsp;000 immediately before settlement}@}. The company settles only {@{8&nbsp;000 SARs for R&#36;26&nbsp;000 cash}@}; the carrying amount of the settled portion is therefore {@{R&#36;24&nbsp;000 = R&#36;60&nbsp;000 × 8&nbsp;000 / 20&nbsp;000}@}.
>
> | {@{Record partial settlement of vested cash-settled SARs when cash paid exceeds the carrying amount of the portion settled}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Liability under share-appreciation plan}@} | {@{24&nbsp;000}@} | |
> | {@{Compensation expense}@} | {@{2&nbsp;000}@} | |
> | {@{Cash}@} | | {@{26&nbsp;000}@} |
>
> _Explanation._ Cash-settled SARs are settled against the {@{carrying amount of the rights actually extinguished}@}. If cash paid is higher than that carrying amount, the excess is {@{current-period compensation expense rather than an equity reclassification}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Forfeiture of unvested cash-settled SARs before the service period ends._ Suppose a company had already recognized a {@{R&#36;18&nbsp;000 liability}@} for a liability-award SAR plan, but employee departures mean that {@{one-third of the unvested rights are now expected to be forfeited}@}. The revised required liability is only {@{R&#36;12&nbsp;000}@}.
>
> | {@{Reduce the SAR liability when expected forfeitures lower the amount that is now expected to vest}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Liability under share-appreciation plan}@} | {@{6&nbsp;000}@} | |
> | {@{Compensation expense}@} | | {@{6&nbsp;000}@} |
>
> _Explanation._ For a liability award, expected forfeitures change the {@{required liability balance immediately}@}. The company therefore records a {@{catch-up reduction of both the liability and cumulative compensation cost}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- liability-award SARs: what is the defining measurement feature? ::@:: The liability is remeasured to current fair value at each reporting date until settlement. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- liability-award SARs: can compensation expense move down as well as up? ::@:: Yes. A downward remeasurement or lower expected vesting reduces both the liability and cumulative compensation cost. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- SAR liability award: what is the crucial accounting feature after grant? ::@:: The award is remeasured to fair value at each reporting date until settlement. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- SAR liability remeasurement: can compensation expense be negative? ::@:: Yes. If the required liability decreases from one reporting date to the next, the reduction is recognized as negative compensation expense. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- liability-award SAR partial settlement: what amount is removed from the liability? ::@:: Remove the carrying amount of the portion of vested SARs actually settled. If cash paid exceeds that carrying amount, the excess is additional compensation expense. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- liability-award SAR forfeiture before vesting: what is the catch-up entry? ::@:: Debit the _SAR liability_ and credit _compensation expense_ for the amount by which the revised required liability falls when fewer rights are now expected to vest. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- Brazil Hotels: 10&nbsp;000 SARs, year-end FV R&#36;3, 2-year service period → Year 1 SAR liability = ? ::@:: 10&nbsp;000 × R&#36;3 × 1/2 = R&#36;15&nbsp;000 (half of the total estimated payout accrued for the first year of service). <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

### equity award SARs

<!-- markdownlint MD028 -->

> _Share-settled SAR instead of cash-settled SAR._ Assume a separate plan grants {@{5&nbsp;000 share-settled SARs}@} with total grant-date fair value {@{€50&nbsp;000}@} and a {@{2-year service period}@}. Because settlement will be in shares rather than cash, the company does {@{not remeasure a liability every reporting date}@}.
>
> | {@{Recognize first-year compensation for a share-settled SAR plan}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Compensation expense}@} | {@{25&nbsp;000}@} | |
> | {@{Share premium — share-settled SARs}@} | | {@{25&nbsp;000}@} |
>
> | {@{Settle fully vested share-settled SARs by issuing ordinary shares}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Share premium — share-settled SARs}@} | {@{50&nbsp;000}@} | |
> | {@{Share capital — ordinary}@} | | {@{10&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{40&nbsp;000}@} |
>
> _Explanation._ This is the key fork from the cash-settled SAR example: once the award is clearly {@{equity-settled}@}, the company keeps the amount in {@{equity rather than a remeasured liability}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Second-year expense for the same equity-award SAR plan even after the share price changes._ Keep the same {@{5&nbsp;000 share-settled SARs with total grant-date fair value €50&nbsp;000 and a 2-year service period}@}. By the end of year 2, the market price has risen sharply, but the company still records only the remaining {@{€25&nbsp;000 grant-date-based compensation}@}.
>
> | {@{Recognize the second-year compensation expense for the equity-award SAR plan without remeasuring for the later share-price increase}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Compensation expense}@} | {@{25&nbsp;000}@} | |
> | {@{Share premium — share-settled SARs}@} | | {@{25&nbsp;000}@} |
>
> _Explanation._ The tricky point is that an equity award is {@{locked to grant-date fair value for expense measurement}@}. Later share-price changes may affect intuition, but they do {@{not create a new remeasurement entry}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Partial settlement of vested equity-award SARs._ Assume the accumulated balance in {@{Share premium — share-settled SARs is €50&nbsp;000 for 5&nbsp;000 fully vested SARs}@}. Only {@{2&nbsp;000 SARs are settled now by issuing ordinary shares with €1 par}@}. The equity balance transferred is therefore {@{€20&nbsp;000 = €50&nbsp;000 × 2&nbsp;000 / 5&nbsp;000}@}.
>
> | {@{Transfer only the proportionate equity balance for the SARs that are actually settled in shares}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Share premium — share-settled SARs}@} | {@{20&nbsp;000}@} | |
> | {@{Share capital — ordinary}@} | | {@{2&nbsp;000}@} |
> | {@{Share premium — ordinary}@} | | {@{18&nbsp;000}@} |
>
> _Explanation._ Equity-award SAR settlement uses a {@{pure equity reclassification for only the portion actually settled}@}. The unsatisfied SAR balance {@{stays in Share premium — share-settled SARs until those rights settle or lapse}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Forfeiture of unvested equity-award SARs before vesting._ Suppose a company granted {@{10&nbsp;000 share-settled SARs with total grant-date fair value €80&nbsp;000 over 4 years}@}. After 2 years it has already recognized {@{€40&nbsp;000}@}, but revised expectations show that {@{25% of the rights will forfeit before vesting}@}. The cumulative amount that should now be recognized is only {@{€30&nbsp;000}@}.
>
> | {@{Reverse previously recognized equity-award SAR compensation for the portion now expected to forfeit}@} | Dr | Cr |
> | --- | ---: | ---: |
> | {@{Share premium — share-settled SARs}@} | {@{10&nbsp;000}@} | |
> | {@{Compensation expense}@} | | {@{10&nbsp;000}@} |
>
> _Explanation._ Even though equity awards are {@{not remeasured for later share-price changes}@}, they are still adjusted for {@{changes in the number of rights expected to vest}@}. That is why a forfeiture estimate creates a {@{catch-up reversal of cumulative expense and equity}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- equity-award SARs: what stays fixed after grant? ::@:: Grant-date fair value remains the basis for expense measurement rather than being remeasured for later market-price changes. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- equity-award SARs: what still can change even without market-price remeasurement? ::@:: The cumulative expense can still be adjusted when the number of rights expected to vest changes. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- SAR equity award: what is the crucial accounting feature after grant? ::@:: The grant-date fair value is recognized over the service period without repeated liability remeasurement. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- share-settled SAR: what happens at settlement? ::@:: Reclassify the accumulated equity balance for the SAR plan into _ordinary share capital_ and _ordinary share premium_; there is no final liability remeasurement because the award is equity-settled. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- equity-award SAR after grant: do later share-price changes create a remeasurement entry? ::@:: No. Equity-award SARs stay on grant-date fair value for expense measurement; later price changes do not create a liability-style remeasurement. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- equity-award SAR partial settlement: how much equity is transferred? ::@:: Transfer only the proportionate balance in _Share premium — share-settled SARs_ for the SARs actually settled, then split that transfer between _Share capital — ordinary_ at par and _Share premium — ordinary_. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- equity-award SAR forfeiture before vesting: what is adjusted even though there is no remeasurement for market-price changes? ::@:: The number of rights expected to vest. A downward revision in expected vesting causes a catch-up reversal of cumulative compensation expense and the related equity balance. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

## basic earnings per share

__Basic EPS__ measures the income earned by each ordinary share actually outstanding during the period.

The general formula is:

- `Basic EPS = (net income - current-year preference dividends) / weighted-average ordinary shares outstanding`

The numerator focuses on the income available to __ordinary__ shareholders. The denominator focuses on the ordinary shares that were actually outstanding during the year.

Two adjustments are easy to miss.

First, if the company has preference shares, the current-year preference dividend is removed from net income before computing income available to ordinary shareholders.

Second, the number of ordinary shares must be __weighted by time__. If shares are issued halfway through the year, they are only counted for half the year. If a share dividend or share split occurs, earlier share numbers are __restated__ so that the whole year is presented on a comparable post-split basis.

A useful rule is:

- __time weighting__ applies to actual share issuances and repurchases; but
- __restatement__, not time weighting, applies to share dividends and share splits.

Two practical EPS traps deserve explicit emphasis.

- When discontinued operations are presented, the gain or loss used in EPS is the __net-of-tax__ discontinued-operations amount, not a pretax figure.
- When a share dividend or share split does __not__ affect every share pool equally, restate only the ordinary shares actually affected. Treasury shares do not receive a dividend from the company itself, and preference shares are not mechanically restated just because ordinary shares were.

> _Weighted-average shares example._ Sabrina begins the year with {@{600&nbsp;000 ordinary shares}@}, issues {@{200&nbsp;000 shares on April 1}@}, has a {@{2-for-1 split on July 1}@}, and issues {@{150&nbsp;000 more shares on October 1}@}. The split requires the earlier share counts to be restated before the weighting is finalized.
>
> _Calculation._ Restate everything to the {@{post-split share basis}@}. {@{January to March: 600&nbsp;000 × 2 × 3/12 = 300&nbsp;000}@}. {@{April to June: 800&nbsp;000 × 2 × 3/12 = 400&nbsp;000}@}. {@{July to September: 1&nbsp;600&nbsp;000 × 3/12 = 400&nbsp;000}@}. {@{October to December: 1&nbsp;750&nbsp;000 × 3/12 = 437&nbsp;500}@}. Weighted-average ordinary shares = {@{1&nbsp;537&nbsp;500}@}.
>
> _Interpretation._ The whole point is to express the year's EPS using a consistent share unit rather than mixing pre-split and post-split numbers in one denominator. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Share dividend applies only to outstanding ordinary shares, not treasury shares._ A company begins the year with {@{500&nbsp;000 issued ordinary shares, of which 50&nbsp;000 are treasury shares, so only 450&nbsp;000 are outstanding}@}. On {@{July 1 it declares a 10% share dividend on the outstanding ordinary shares only}@}. On {@{October 1 it issues 40&nbsp;000 new ordinary shares for cash}@}. The treasury shares do {@{not receive the share dividend}@}.
>
> _Calculation._ Restate the pre-dividend period using the dividend factor only for the {@{450&nbsp;000 outstanding ordinary shares that actually receive the 10% dividend}@}. {@{January to June: 450&nbsp;000 × 1.10 × 6/12 = 247&nbsp;500}@}. {@{July to September: 495&nbsp;000 × 3/12 = 123&nbsp;750}@}. {@{October to December: 535&nbsp;000 × 3/12 = 133&nbsp;750}@}. Weighted-average ordinary shares = {@{505&nbsp;000}@}.
>
> _Explanation._ The tricky point is that EPS restatement follows the {@{ordinary shares actually affected by the share dividend}@}, not every issued share figure sitting somewhere in equity. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Chained share dividend and share split in one year._ A company begins the year with {@{300&nbsp;000 ordinary shares}@} and issues {@{60&nbsp;000 more on March 1}@}. It then declares a {@{20% share dividend on July 1}@} and later executes a {@{3-for-2 share split on November 1}@}. Because both events restate earlier share counts, the denominator must carry the __combined__ factor for earlier periods.
>
> _Calculation._ Pre-July share counts must be multiplied by {@{1.20 × 1.50 = 1.80}@}. {@{January to February: 300&nbsp;000 × 1.80 × 2/12 = 90&nbsp;000}@}. {@{March to June: 360&nbsp;000 × 1.80 × 4/12 = 216&nbsp;000}@}. {@{July to October: 432&nbsp;000 × 1.50 × 4/12 = 216&nbsp;000}@}. {@{November to December: 648&nbsp;000 × 2/12 = 108&nbsp;000}@}. Weighted-average ordinary shares = {@{630&nbsp;000}@}.
>
> _Explanation._ The restatement is __chained__: each earlier block is multiplied by {@{every later share-restatement event that affects it}@}, not by only the next event in isolation. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2027-04-18T00:00:00.000Z,264,264.31905225,1,2,4,0,0,2026-07-28T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Comprehensive basic EPS example._ Diaz has income from continuing operations of {@{R&#36;580&nbsp;000}@}, gain on discontinued operations __net of tax__ of {@{R&#36;240&nbsp;000}@}, declared preference dividends of {@{R&#36;100&nbsp;000}@}, and {@{1&nbsp;537&nbsp;500 weighted-average ordinary shares outstanding}@}. The preference dividends reduce the income available to ordinary shareholders for EPS purposes.
>
> _Calculation._ Income available to ordinary shareholders from continuing operations = {@{R&#36;580&nbsp;000 − R&#36;100&nbsp;000 = R&#36;480&nbsp;000}@}. Income available to ordinary shareholders for total net income = {@{R&#36;580&nbsp;000 + R&#36;240&nbsp;000 − R&#36;100&nbsp;000 = R&#36;720&nbsp;000}@}. Continuing-operations EPS = {@{R&#36;480&nbsp;000 ÷ 1&nbsp;537&nbsp;500 ≈ R&#36;0.31 per share}@}. Net-income EPS = {@{R&#36;720&nbsp;000 ÷ 1&nbsp;537&nbsp;500 ≈ R&#36;0.47 per share}@}. If the discontinued-operations amount is shown separately, it is {@{R&#36;240&nbsp;000 ÷ 1&nbsp;537&nbsp;500 ≈ R&#36;0.16 per share using the net-of-tax discontinued-operations amount, not a pretax amount}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Discontinued-operations loss must also be used net of tax._ A company reports {@{R&#36;900&nbsp;000 income from continuing operations}@}. It also reports a {@{discontinued-operations loss before tax of R&#36;200&nbsp;000 with a tax benefit of R&#36;50&nbsp;000}@}, so the discontinued-operations amount entering EPS is {@{a net-of-tax loss of R&#36;150&nbsp;000}@}. Current-year preference dividends are {@{R&#36;100&nbsp;000}@}, and weighted-average ordinary shares are {@{250&nbsp;000}@}.
>
> _Calculation._ Continuing-operations EPS = {@{(R&#36;900&nbsp;000 − R&#36;100&nbsp;000) ÷ 250&nbsp;000 = R&#36;3.20 per share}@}. Net-income EPS = {@{(R&#36;900&nbsp;000 − R&#36;150&nbsp;000 − R&#36;100&nbsp;000) ÷ 250&nbsp;000 = R&#36;2.60 per share}@}. If the discontinued-operations amount is shown separately, it is {@{−R&#36;150&nbsp;000 ÷ 250&nbsp;000 = −R&#36;0.60 per share}@}.
>
> _Explanation._ The EPS numerator uses the {@{net-of-tax discontinued-operations gain or loss}@}. The pretax discontinued amount and its tax effect are useful analysis, but they are {@{not the numerator actually used in EPS}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

When discontinued operations exist, the company must disclose EPS for:

- __continuing operations__; and
- __net income__.

The discontinued-operations amount may be shown on the face of the income statement or in the notes, but the user must still be able to see how the total EPS was built up.

---

Flashcards for this section are as follows:

- basic EPS: formula ::@:: Basic EPS equals `(net income - current-year preference dividends) / weighted-average ordinary shares outstanding`. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- basic EPS: why subtract preference dividends from net income? ::@:: Because basic EPS is meant to measure the earnings available to ordinary shareholders after satisfying the preference shareholders' current-year claim. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- weighted-average shares: why not just use year-end shares? ::@:: Because different share counts may have been outstanding for different portions of the year, so the denominator must reflect time outstanding rather than just the final balance. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- share split or share dividend in basic EPS: what adjustment is made? ::@:: Earlier share counts are restated to the new share basis so the whole year is presented using a comparable unit. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- basic EPS with discontinued operations: what must be shown? ::@:: EPS for continuing operations and EPS for net income, with the discontinued-operations effect disclosed separately on the face of the income statement or in the notes. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- discontinued operations in EPS: what numerator is used? ::@:: Use the discontinued-operations gain or loss __net of tax__ for the EPS numerator, not the pretax discontinued-operations amount. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- share dividend and treasury shares in basic EPS: what is the tricky restatement rule? ::@:: Restate only the outstanding ordinary shares actually affected by the share dividend. Treasury shares do not receive the dividend, so they are not mechanically restated as if they had. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- chained share dividends and share splits: how is the restatement factor applied? ::@:: Each earlier time block is multiplied by every later restatement event that affects it, so the factors are chained rather than applied one at a time in isolation. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2027-04-18T00:00:00.000Z,264,264.31905225,1,2,4,0,0,2026-07-28T00:00:00.000Z-->
- basic EPS with a discontinued-operations loss: what is the common tax mistake? ::@:: Students often plug in the pretax discontinued loss, but EPS must use the discontinued-operations amount after tax. <!--SR:!fsrs,2027-04-18T00:00:00.000Z,264,264.31905225,1,2,4,0,0,2026-07-28T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- Sabrina: 600&nbsp;000 shares Jan 1, +200&nbsp;000 Apr 1, 2-for-1 split Jul 1, +150&nbsp;000 Oct 1 → WACS = ? ::@:: Post-split basis: Jan–Mar 600&nbsp;000 × 2 × 3/12 = 300&nbsp;000; Apr–Jun 800&nbsp;000 × 2 × 3/12 = 400&nbsp;000; Jul–Sep 1&nbsp;600&nbsp;000 × 3/12 = 400&nbsp;000; Oct–Dec 1&nbsp;750&nbsp;000 × 3/12 = 437&nbsp;500; WACS = 1&nbsp;537&nbsp;500. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-09-30T00:00:00.000Z,96,96.09448938,1,2,3,0,0,2026-06-26T00:00:00.000Z-->

## diluted earnings per share

__Diluted EPS__ asks a tougher question than basic EPS: what would earnings per ordinary share look like if all __dilutive__ potential ordinary shares were assumed to be converted or exercised?

Only securities that __reduce__ EPS are included. If a security would increase EPS or leave it unchanged, it is __antidilutive__ and must be excluded.

The course uses two main methods.

---

Flashcards for this section are as follows:

- diluted EPS: parent-level idea ::@:: Ask what EPS would look like if all dilutive potential ordinary shares were converted or exercised, but exclude instruments that are antidilutive. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-09-30T00:00:00.000Z,96,96.09448938,1,2,3,0,0,2026-06-26T00:00:00.000Z-->
- diluted EPS: what are the two main methods? ::@:: Use the if-converted method for convertibles and the treasury-share method for options and warrants. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- diluted EPS: basic idea ::@:: Diluted EPS shows what earnings per ordinary share would be if all dilutive potential ordinary shares were converted or exercised. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- antidilutive security: definition ::@:: A security is antidilutive if including it would increase EPS or leave EPS unchanged, so it must be excluded from diluted EPS. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

### if-converted method

Use the __if-converted method__ for convertible bonds and convertible preference shares.

Assume conversion happened:

- at the __beginning of the period__; or
- at the __issuance date__ if the security was issued during the year.

Then:

- increase the denominator by the ordinary shares that would have been issued on conversion; and
- adjust the numerator for any financing cost that would have disappeared.

For convertible debt, add back:

- the related __interest expense__; and
- use the __after-tax__ amount because interest would also have changed the tax effect.

For convertible preference shares, do __not__ subtract the preference dividend in the numerator, because conversion would mean those preference dividends would not exist.

---

Flashcards for this section are as follows:

- if-converted method: what changes in numerator and denominator? ::@:: Add the conversion shares to the denominator and restore financing costs that would disappear from the numerator. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- if-converted method: what is commonly forgotten for convertible debt? ::@:: Use the liability-component interest and add it back after tax, not before tax. <!--SR:!fsrs,2026-08-02T00:00:00.000Z,42,41.57871783,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- if-converted method: when is it used? ::@:: For convertible bonds and convertible preference shares. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- if-converted method: core assumption ::@:: Assume the conversion happened at the beginning of the period, or at the issuance date if the security was issued during the year. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- if-converted method for convertible debt: numerator adjustment ::@:: Add back the related interest expense net of tax, because that interest would not exist if the debt had been converted. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- if-converted method for convertible preference shares: numerator adjustment ::@:: Do not subtract the preference dividend, because conversion would eliminate the preference-share claim. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- if-converted method for convertible debt: what two things are commonly forgotten? ::@:: Use the liability-component interest rather than simply stated coupon cash, and add it back after tax rather than before tax. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- convertible preference shares in diluted EPS: why is the preference dividend restored? ::@:: Because diluted EPS assumes the preference shares were converted into ordinary shares, so those preference dividends would not exist. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

> _Convertible bonds in diluted EPS._ Mayfield has net income of {@{£210&nbsp;000}@} and {@{100&nbsp;000 weighted-average ordinary shares}@}. Basic EPS is {@{£2.10}@}. It also has two convertible bond issues. The if-converted method adds back the {@{after-tax interest expense that would disappear if the bonds were converted}@} and adds the {@{ordinary shares issuable on conversion}@} to the denominator, using a {@{time-weighted fraction for both shares and after-tax interest if one bond issue was outstanding for only part of the year}@}. Diluted EPS is then recomputed after each issue is added, excluding any issue that turns out to be {@{antidilutive}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Detailed if-converted calculation for convertible debt._ Assume bond issue A has {@{£62&nbsp;000 of liability-component interest expense}@} and converts into {@{20&nbsp;000 ordinary shares}@}. Bond issue B has {@{£80&nbsp;000 annual liability-component interest expense}@}, was outstanding for only {@{9/12 of the year}@}, and converts into {@{32&nbsp;000 shares}@}. The tax rate is {@{40%}@}.
>
> _Calculation._ After-tax add-back for issue A = {@{£62&nbsp;000 × (1 − 0.40) = £37&nbsp;200}@}. Per-share effect of issue A = {@{£37&nbsp;200 ÷ 20&nbsp;000 = £1.86 per share}@}. After-tax add-back for issue B = {@{£80&nbsp;000 × 9/12 × (1 − 0.40) = £36&nbsp;000}@}. Incremental shares from issue B = {@{32&nbsp;000 × 9/12 = 24&nbsp;000 shares}@}. Per-share effect of issue B = {@{£36&nbsp;000 ÷ 24&nbsp;000 = £1.50 per share}@}. Because {@{£1.50 is more dilutive than £1.86}@}, issue B is tested before issue A. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Convertible preference shares in diluted EPS._ A company reports {@{€240&nbsp;000 net income}@}, has {@{100&nbsp;000 ordinary shares outstanding}@}, and also has {@{€1&nbsp;000&nbsp;000 of 6% convertible preference shares}@}. Each {@{€100 preference share converts into 5 ordinary shares}@}, so full conversion would create {@{50&nbsp;000 ordinary shares}@}. Current-year preference dividends are {@{€60&nbsp;000}@}.
>
> _Calculation._ Basic EPS = {@{(€240&nbsp;000 − €60&nbsp;000) ÷ 100&nbsp;000 = €1.80}@}. Diluted EPS under the if-converted method = {@{€240&nbsp;000 ÷ (100&nbsp;000 + 50&nbsp;000) = €1.60}@}. The preference dividend is {@{not subtracted in diluted EPS}@} because the calculation assumes the preference shares were converted into ordinary shares. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

### treasury-share method

Use the __treasury-share method__ for options and warrants.

Assume:

1. the options or warrants are exercised at the beginning of the period (or issuance date if later); and
2. the company uses the exercise proceeds to buy back ordinary shares at the __average market price__.

Only the __net incremental shares__ remain in the diluted denominator.

This is why the treasury-share method never changes the numerator. It only changes the denominator.

Two guardrails from the transcript matter a lot in exam questions:

- if the __average market price__ is less than or equal to the exercise price, the options or warrants are __antidilutive__ because the assumed proceeds could buy back all of the issued shares or more; and
- if conversion terms change over time, use the __most dilutive__ currently relevant conversion rate rather than averaging conversion rates mechanically.

---

Flashcards for this section are as follows:

- treasury-share method: why does the numerator stay unchanged? ::@:: Because assumed option or warrant exercise changes only the number of shares, not the period's net income. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- treasury-share method: when are options or warrants antidilutive? ::@:: When the average market price is less than or equal to the exercise price, so the assumed proceeds could buy back all issued shares or more. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- treasury-share method: when is it used? ::@:: For options and warrants. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- treasury-share method: core assumption ::@:: Assume exercise at the beginning of the period and assume the company uses the exercise proceeds to buy back shares at the average market price. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- changing conversion terms: what rate is used in diluted EPS? ::@:: Use the most dilutive conversion rate rather than averaging the available rates. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- Kubitz: 5 000 options, exercise ₴20, avg market ₴28 → net incremental shares = ? ::@:: Proceeds = 5 000 × ₴20 = ₴100 000; repurchase = ₴100 000 ÷ ₴28 ≈ 3 571 shares; net incremental = 5 000 − 3 571 = 1 429 shares; diluted EPS = ₴220 000 ÷ 101 429 ≈ ₴2.17. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

> _Options example._ Kubitz has net income of {@{₴220&nbsp;000}@}, {@{100&nbsp;000 weighted-average shares}@}, {@{5&nbsp;000 options}@} with exercise price {@{₴20}@}, and average market price {@{₴28}@}. The assumed exercise produces {@{₴100&nbsp;000}@} of proceeds, which repurchases only part of the shares at the average market price, so the net incremental shares are added to the diluted denominator.
>
> _Treasury-share calculation._ Assumed proceeds = {@{5&nbsp;000 × ₴20 = ₴100&nbsp;000}@}. Shares repurchased at average market price = {@{₴100&nbsp;000 ÷ ₴28 ≈ 3&nbsp;571 shares}@}. Net incremental shares added to the diluted denominator = {@{5&nbsp;000 − 3&nbsp;571 ≈ 1&nbsp;429 shares}@}. The {@{numerator stays unchanged}@} because the treasury-share method affects only the denominator.
>
> _Diluted EPS from the treasury-share method._ Diluted EPS = {@{₴220&nbsp;000 ÷ (100&nbsp;000 + 1&nbsp;429) ≈ ₴2.17}@}. The drop from {@{basic EPS of ₴2.20}@} shows why the options are {@{dilutive rather than antidilutive}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2027-04-18T00:00:00.000Z,264,264.31905225,1,2,4,0,0,2026-07-28T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

## ranking dilutive effects, contingently issuable shares, and presentation

When a company has __multiple__ potentially dilutive securities, it cannot simply throw everything into diluted EPS at once. The course uses an ordered process.

1. Start from __basic EPS__.
2. Compute the __per-share effect__ of each potentially dilutive security.
3. Rank the securities from __most dilutive__ (smallest earnings effect per share) to __least dilutive__.
4. Add them one at a time, recalculating EPS after each step.
5. Stop as soon as the next security would stop reducing EPS.

This ranking rule matters because a security that is dilutive on its own may become antidilutive after more strongly dilutive securities have already been included.

For a company with positive EPS from continuing operations, the test is exactly the one students often suspect but should say more carefully: a candidate security is dilutive only if its __incremental EPS effect is less than the current EPS being tested__. If the candidate's effect is equal to or greater than the current EPS, adding it would not reduce EPS, so it is __antidilutive__. The comparison is made __step by step__ as the diluted-EPS calculation is built.

The most exam-relevant caveat is that the antidilution test is anchored to __continuing operations__. If continuing operations show a loss, potential ordinary shares are usually antidilutive because they make the continuing-operations loss per share less negative, even if total net income is still positive because of a discontinued-operations gain.

__Contingently issuable shares__ are another special case. These are ordinary shares issuable for little or no cash once specified conditions are met, such as in some business-combination earn-out arrangements. They enter diluted EPS only when the relevant conditions are already satisfied for the reporting period and the effect is dilutive.

Presentation rules are straightforward once the computation is done:

- a company with a __simple__ capital structure reports only basic EPS; and
- a company with a __complex__ capital structure reports both __basic EPS__ and __diluted EPS__.

If continuing operations and discontinued operations are both present, the EPS presentation must still let the reader see the per-share amount for continuing operations and for total net income. In practice, that means a company with a __complex capital structure__ and __discontinued operations__ will normally have at least four required face figures: basic EPS for continuing operations, diluted EPS for continuing operations, basic EPS for total net income, and diluted EPS for total net income. If the entity also shows the discontinued-operations component explicitly, that usually adds two more figures: basic and diluted EPS for the discontinued-operations amount.

> _Ranking dilutive effects one security at a time._ Suppose a company starts with {@{basic EPS of €3.00}@}. The per-share effect of its options is the {@{smallest among the candidate securities, so the options are added first}@}, and diluted EPS falls to {@{€2.82}@}. Next, convertible bond issue A reduces EPS further to {@{€2.67}@}. Convertible bond issue B then reduces EPS again to {@{€2.55}@}. However, adding convertible preference shares would increase the recomputed EPS to {@{€2.58}@}, so those preference shares are {@{antidilutive and excluded}@}.
>
> _Interpretation._ A security can be {@{tested after other securities and then excluded}@}. The ranking process is therefore {@{iterative rather than all-at-once}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Antidilution test for a convertible bond._ A company has {@{€210&nbsp;000 net income}@}, {@{100&nbsp;000 weighted-average ordinary shares}@}, and a convertible bond whose after-tax interest add-back is {@{€36&nbsp;000}@}. The bond would create {@{10&nbsp;000 additional ordinary shares}@} if converted.
>
> _Calculation._ Basic EPS = {@{€210&nbsp;000 ÷ 100&nbsp;000 = €2.10}@}. Per-share effect of the bond = {@{€36&nbsp;000 ÷ 10&nbsp;000 = €3.60 per share}@}. Because {@{€3.60 is greater than the current EPS of €2.10}@}, the bond is {@{antidilutive and excluded}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Continuing-operations loss but positive total net income._ Suppose a company reports a {@{continuing-operations loss of €150&nbsp;000}@} but also a {@{discontinued-operations gain net of tax of €220&nbsp;000}@}, so total net income is still {@{€70&nbsp;000}@}. Weighted-average ordinary shares are {@{100&nbsp;000}@}, and employee options would add {@{20&nbsp;000 incremental shares}@} under the treasury-share method.
>
> _Calculation._ Basic continuing-operations EPS = {@{−€150&nbsp;000 ÷ 100&nbsp;000 = −€1.50 per share}@}. If the options were included, diluted continuing-operations EPS would become {@{−€150&nbsp;000 ÷ 120&nbsp;000 = −€1.25 per share}@}. That is {@{less negative than −€1.50 and therefore antidilutive}@}. Even though total net-income EPS would fall from {@{€70&nbsp;000 ÷ 100&nbsp;000 = €0.70}@} to {@{€70&nbsp;000 ÷ 120&nbsp;000 ≈ €0.58}@}, the options are still {@{excluded because antidilution is tested using continuing operations}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _How many EPS figures appear when both diluted EPS and discontinued operations exist?_ Assume a company has a __complex capital structure__ and reports {@{income from continuing operations of €360&nbsp;000}@}, a {@{discontinued-operations gain net of tax of €120&nbsp;000}@}, current-year preference dividends of {@{€60&nbsp;000}@}, basic weighted-average ordinary shares of {@{120&nbsp;000}@}, and a dilutive convertible preference issue that would add back {@{€60&nbsp;000 of preference dividends}@} and create {@{30&nbsp;000 extra ordinary shares}@}.
>
> _Calculation._ Basic continuing-operations EPS = {@{(€360&nbsp;000 − €60&nbsp;000) ÷ 120&nbsp;000 = €2.50}@}. Basic net-income EPS = {@{(€360&nbsp;000 + €120&nbsp;000 − €60&nbsp;000) ÷ 120&nbsp;000 = €3.50}@}. If the discontinued-operations amount is shown separately, basic discontinued-operations EPS = {@{€120&nbsp;000 ÷ 120&nbsp;000 = €1.00}@}. Diluted continuing-operations EPS = {@{€360&nbsp;000 ÷ 150&nbsp;000 = €2.40}@}. Diluted net-income EPS = {@{€480&nbsp;000 ÷ 150&nbsp;000 = €3.20}@}. If shown separately, diluted discontinued-operations EPS = {@{€120&nbsp;000 ÷ 150&nbsp;000 = €0.80}@}.
>
> _Explanation._ The minimum face presentation is the {@{four figures for continuing operations and total net income under both basic and diluted EPS}@}. When the discontinued-operations component is also shown explicitly, the set expands to {@{six figures in total}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> _Contingently issuable shares._ In a business combination, the acquirer promises to issue {@{40&nbsp;000 additional ordinary shares}@} if the acquired business reaches a stated revenue target. If the target has already been {@{met by the reporting date}@}, those shares enter diluted EPS {@{only if their inclusion reduces EPS}@}. If the target has {@{not yet been met}@}, they are not included. <!--SR:!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z!fsrs,2026-10-02T00:00:00.000Z,80,79.80449519,1,2,2,0,0,2026-07-14T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- multiple dilutive securities: why must they be ranked? ::@:: Because diluted EPS is built by adding securities from most dilutive to least dilutive, stopping when a further security would no longer reduce EPS. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- per-share ranking test: what is being ranked? ::@:: The incremental earnings effect per share for each potentially dilutive security. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- can a security be dilutive alone but antidilutive after others are added? ::@:: Yes; that is why the diluted-EPS computation is iterative rather than all-at-once. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- contingently issuable shares: definition ::@:: Ordinary shares issuable for little or no cash once specified conditions are satisfied, such as in some contingent share agreements. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- contingently issuable shares: when are they included in diluted EPS? ::@:: When the relevant conditions are satisfied for the reporting period and including them is dilutive. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- EPS presentation: when must both basic and diluted EPS be shown? ::@:: When the company has a complex capital structure with potentially dilutive securities such as convertibles, options, or warrants. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- complex capital structure: definition ::@:: A capital structure that includes securities which could become ordinary shares and therefore reduce earnings per ordinary share. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- antidilution test: what comparison determines exclusion? ::@:: If the security's per-share effect is greater than or equal to the current EPS being tested, the security is antidilutive and must be excluded. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- antidilution test: which EPS is the benchmark during the step-by-step ranking process? ::@:: Use the __current EPS from continuing operations__ at that step of the diluted-EPS calculation, not a stale starting number and not merely total net-income EPS. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- continuing-operations loss and antidilution: why are potential ordinary shares usually excluded? ::@:: Because adding shares makes the continuing-operations loss per share less negative, which is antidilutive even if total net income stays positive because of discontinued operations. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- complex capital structure with discontinued operations: how many EPS figures are normally presented? ::@:: At least four on the face of the statements—basic and diluted EPS for continuing operations, and basic and diluted EPS for total net income. If the discontinued-operations component is also shown explicitly, that usually adds two more figures. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- discontinued-operations EPS in a complex capital structure: how is it computed if shown separately? ::@:: Use the discontinued-operations gain or loss __net of tax__ as the numerator, and compute both a basic and a diluted per-share amount using the basic and diluted denominators respectively. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

## comprehensive exercise: diluted EPS with share split, convertible bonds, and warrants

> _Norden SA — comprehensive diluted EPS exercise._ Norden SA reports net income of €3&nbsp;300&nbsp;000 for the year ended 31 December 2026. The tax rate is 30%. Preference dividends declared in 2026 are €300&nbsp;000. The following share activity occurred during 2026:
>
> - 1 January: 600&nbsp;000 ordinary shares outstanding.
> - 1 July: Norden issues 300&nbsp;000 new ordinary shares for cash.
> - 1 October: 2-for-1 ordinary share split.
>
> Additional information:
>
> - Convertible bonds outstanding all year: face value €6&nbsp;000&nbsp;000, 6% stated coupon. Under IAS 32, the bonds are split into a liability component and an equity component. The liability-component interest expense recognized in 2026 using the effective-interest method is €420&nbsp;000. Full conversion would produce 280&nbsp;000 ordinary shares on a post-split basis.
> - Share warrants outstanding all year (adjusted for the split): 120&nbsp;000 warrants with exercise price €25 per share. Average market price of the ordinary shares during 2026 was €40.
>
> _Required._ Compute (a) basic EPS for 2026 and (b) diluted EPS for 2026. Show all workings, including the treasury-share method for warrants and the if-converted method for the bonds. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-09-22T00:00:00.000Z,65,64.75639033,6.0091915,2,3,0,0,2026-07-19T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Compute the weighted-average ordinary shares for Norden SA given:
>
> - 1 January: 600&nbsp;000 ordinary shares outstanding
> - 1 July: issue 300&nbsp;000 new ordinary shares for cash
> - 1 October: 2-for-1 ordinary share split
>
> (Restate all shares to a post-split basis before time-weighting.)
>
> - 1 January to 30 June: {@{600&nbsp;000 × 2 × 6/12 = 600&nbsp;000 weighted shares}@}.
> - 1 July to 30 September: {@{(600&nbsp;000 + 300&nbsp;000) × 2 × 3/12 = 450&nbsp;000 weighted shares}@}.
> - 1 October to 31 December: {@{(600&nbsp;000 + 300&nbsp;000) × 2 × 3/12 = 450&nbsp;000 weighted shares}@}. [Note: post-split total is {@{1&nbsp;800&nbsp;000}@}]
> - Weighted-average ordinary shares (WACS): {@{600&nbsp;000 + 450&nbsp;000 + 450&nbsp;000 = 1&nbsp;500&nbsp;000 shares}@}. <!--SR:!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Using the WACS from above (1&nbsp;500&nbsp;000 shares), compute basic EPS given net income of €3&nbsp;300&nbsp;000 and preference dividends declared of €300&nbsp;000.
>
> | | |
> | --- | ---: |
> | Net income | {@{€3&nbsp;300&nbsp;000}@} |
> | Less: preference dividends | {@{(€300&nbsp;000)}@} |
> | Income available to ordinary shareholders | {@{€3&nbsp;000&nbsp;000}@} |
> | Weighted-average ordinary shares | {@{1&nbsp;500&nbsp;000}@} |
> | Basic EPS | {@{€2.00}@} | <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Step 1 — compute per-share effects.
>
> __Treasury-share method (warrants).__ Givens: 120&nbsp;000 warrants (post-split), exercise price €25, average market price €40.
>
> - Proceeds from assumed exercise: {@{120&nbsp;000 × €25 = €3&nbsp;000&nbsp;000}@}.
> - Shares repurchased at average market price: {@{€3&nbsp;000&nbsp;000 ÷ €40 = 75&nbsp;000 shares}@}.
> - Net incremental shares: {@{120&nbsp;000 − 75&nbsp;000 = 45&nbsp;000 shares}@}.
> - Numerator effect: {@{€0}@} (treasury-share method {@{never changes the numerator}@}).
> - Per-share effect: {@{€0 ÷ 45&nbsp;000 = €0.00}@}.
>
> __If-converted method (convertible bonds).__ Givens: liability-component interest expense €420&nbsp;000, tax rate 30%, full conversion produces 280&nbsp;000 ordinary shares (post-split).
>
> - After-tax interest add-back: {@{€420&nbsp;000 × (1 − 0.30) = €294&nbsp;000}@}.
> - Incremental shares: {@{280&nbsp;000 ordinary shares}@}.
> - Per-share effect: {@{€294&nbsp;000 ÷ 280&nbsp;000 = €1.05}@}. <!--SR:!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Step 2 — rank {@{from most dilutive to least dilutive (lowest per-share effect first)}@}.
>
> From Step 1: warrants have a €0 numerator effect, 45&nbsp;000 incremental shares, and a €0.00 per-share effect. Bonds have a €294&nbsp;000 numerator effect, 280&nbsp;000 incremental shares, and a €1.05 per-share effect.
>
> | Security | Numerator effect | Incremental shares | Per-share effect |
> | --- | ---: | ---: | ---: |
> | {@{Warrants (treasury-share method)}@} | {@{€0}@} | {@{45&nbsp;000}@} | {@{€0.00}@} |
> | {@{Convertible bonds (if-converted method)}@} | {@{€294&nbsp;000}@} | {@{280&nbsp;000}@} | {@{€1.05}@} | <!--SR:!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z!fsrs,2026-07-31T00:00:00.000Z,8,8.2956,1,2,1,0,0,2026-07-23T00:00:00.000Z-->

<!-- markdownlint MD028 -->

> Step 3 — add securities one at a time, most dilutive first. Start from basic EPS: numerator €3&nbsp;000&nbsp;000, denominator 1&nbsp;500&nbsp;000, EPS = €2.00.
>
> _Add warrants (per-share effect €0.00)._ Per-share effect {@{€0.00 < €2.00 → dilutive}@}. Numerator = {@{€3&nbsp;000&nbsp;000}@}; Denominator = {@{1&nbsp;500&nbsp;000 + 45&nbsp;000 = 1&nbsp;545&nbsp;000}@}; Recomputed EPS = {@{€3&nbsp;000&nbsp;000 ÷ 1&nbsp;545&nbsp;000 ≈ €1.942}@}.
>
> _Add convertible bonds (per-share effect €1.05)._ Per-share effect {@{€1.05 < €1.942 → dilutive}@}. Numerator = {@{€3&nbsp;000&nbsp;000 + €294&nbsp;000 = €3&nbsp;294&nbsp;000}@}; Denominator = {@{1&nbsp;545&nbsp;000 + 280&nbsp;000 = 1&nbsp;825&nbsp;000}@}; Diluted EPS = {@{€3&nbsp;294&nbsp;000 ÷ 1&nbsp;825&nbsp;000 ≈ €1.81}@}.
>
> _Conclusion._ Diluted EPS = {@{≈ €1.81}@}, basic EPS = {@{€2.00}@}. Both securities are {@{dilutive}@}. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->

---

Flashcards for this section are as follows:

- comprehensive EPS: why must the 2-for-1 split be applied before time-weighting? ::@:: Because a share split is treated as if it were always in effect for the whole period, so all earlier share counts must be restated to a post-split basis before any fraction-of-year weighting is applied. <!--SR:!fsrs,2027-04-18T00:00:00.000Z,264,264.31905225,1,2,4,0,0,2026-07-28T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- comprehensive EPS: treasury-share method — why does the numerator not change? ::@:: The assumed exercise of warrants only adds shares; it does not change the net income earned during the period. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- comprehensive EPS: if-converted method — what two items change? ::@:: The numerator increases by the after-tax interest that would disappear if the bonds converted, and the denominator increases by the ordinary shares issuable on conversion. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
- comprehensive EPS: why are warrants ranked ahead of the convertible bonds as most dilutive? ::@:: Because the treasury-share method assigns a €0 per-share effect to the warrants (no numerator change), while the convertible bonds carry a positive per-share effect of €1.05, making the warrants more dilutive. <!--SR:!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z!fsrs,2026-08-31T00:00:00.000Z,71,70.63155138,1,2,2,0,0,2026-06-21T00:00:00.000Z-->
