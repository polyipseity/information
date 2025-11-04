---
aliases:
  - FINA 3203 question
  - FINA 3203 questions
  - FINA3203 question
  - FINA3203 questions
  - HKUST FINA 3203 question
  - HKUST FINA 3203 questions
  - HKUST FINA3203 question
  - HKUST FINA3203 questions
tags:
  - flashcard/active/special/academia/HKUST/FINA_3203/questions
  - language/in/English
---

# questions

- HKUST FINA 3203

## derivative definition

1. Is a stock a derivative? ::@:: No by most people's account. <p> But philosophically, you could argue it is a derivative of itself... Whatever that means. <!--SR:!2025-12-12,64,310!2025-12-02,56,310-->
2. Is a combination of stocks \(e.g. mutual fund\) a derivative? ::@:: No by most people's account. You could argue if a stock is not a derivative, then why should a combination of stocks should be? <p> But you could also argue it in the opposite way: It is a derivative of the individual stocks in the combination. <!--SR:!2025-12-15,67,310!2025-12-01,55,310-->
3. Is a closed-end mutual fund a derivative? ::@:: No by most people's account. You could argue it the same way as above. <p> But you could also argue it in the opposite way: Compared to a mutual fund \(combination of stocks\), "closed-end" \(closed to new capital\) makes its value further removed from the underlying stocks, so it is a derivative. <!--SR:!2025-12-06,59,310!2026-03-10,123,290-->
4. Must the item underlying a derivative be delivered at maturity of the derivative? ::@:: No. For example, an event derivative cannot "deliver" an event, whatever that means... <!--SR:!2025-12-08,61,310!2025-12-11,63,310-->

## forward contracts

1. People sometimes commit theft, even taking securities such as shares or bonds. Could the same individuals also pilfer \(steal\) forward contracts? Provide an explanation. \(Assume no legal problems apart from potentially getting jailed.\) ::@:: Yes, if the value of the forward contract is positive. <!--SR:!2026-01-30,82,338!2026-01-30,82,338-->
2. Suppose a risk‑free asset trades at 100 today and the prevailing interest rate is positive. If you commit to sell that same asset one year later for 50, what amount would you consider an equitable present payment so that, on average, you neither profit nor suffer a loss? ::@::  - __Present‑value method__: The future cash inflow of \$50 in one year must be discounted at the prevailing risk‑free rate $r>0$. $$\text{Fair present payment today}=100 - 50\,e^{-rT} > 50$$ Because a positive interest rate means money today is worth more than its future value, you would accept more than \$50 now. <br/> - __No‑arbitrage argument__: Assume you could receive any amount $P$ today in exchange for selling the asset \(currently priced at \$100\) one year from now at \$50. Current payoff is $P$ and future payoff is $50 - S_T$. By investing using $P$, current payoff becomes $0$ and future payoff $50 - S_T + Pe^{rT}$. Also long a forward of the same asset, so current payoff remains $0$ and future payoff becomes $50 + Pe^{rT} - 100e^{rT}$. There is no risk involved \(assuming no counterparty risk\), as the interest rate is risk-free. By no arbitrage, $$50 + Pe^{rT} - 100e^{rT} = 0 \implies P = 100 - 50e^{-rT} > 50 \,.$$ Thus this is the only value of \(P\) that precludes arbitrage—and therefore is fair. <p> \(__this course__: It seems like the instructor prefers the no-arbitrage argument...\) <!--SR:!2025-11-18,15,218!2025-12-02,19,198-->
3. What does it mean to sell short? What does it mean to sell long?
    - What does it mean to sell short? ::@:: Sell short means selling a security that you do not currently own, with the intention of buying it back later at a lower price; your profit comes from a decline in its market value. <!--SR:!2025-12-28,54,318!2026-01-21,74,338-->
    - What does it mean to sell long? ::@:: Sell long \(or simply buy\) means purchasing a security and holding it, expecting its price to rise so you can sell later for a higher amount. <!--SR:!2026-01-30,82,338!2026-01-24,77,338-->
4. Given an S&P&nbsp;500 spot level of 1100, a continuously compounded risk‑free rate of 5%, and no dividend yield, consider the following scenarios: <p> - If the quoted price for a six‑month forward is 1135, what action would you take? <br/> - If the quoted price for a six‑month forward is 1115, how would you respond? ::@:: Theoretical forward price is $$1100 \cdot e^{0.05 \times \frac 6 {12} }\approx 1127.9 \,.$$ <p> If the market quote is higher \(e.g. 1135\), you would _short_ the forward \(for being _overpriced_\). To do so, _long_ the stock \(buy the stock\) and _short_ a bond \(borrow money\). Reverse these trades at maturity. <p> If the quote lies below the fair price \(e.g. 1115\), so you would _go long_ the forward \(for being _underpriced_\). To do so, _short_ the stock \(borrow the stock\) and _long_ a bond \(lend money\). Reverse these trades at maturity. <!--SR:!2025-12-21,48,318!2025-12-06,34,298-->
    - arbitrage on forward contracts ::@:: Thinking in terms of _positions_ and _payoffs_ help to figure out the correct actions. <p> We take _opposite_ positions on the forward and the stock, which removes the \(uncertain\) future spot price $S_T$ from the future payoff. The current payoff is however nonzero. <p> Then, we take _opposite_ positions on the stock and the bond, which resets the current payoff to zero, but the future payoff remains positive. Now we have a risk-free positive future payoff, i.e. arbitrage. <!--SR:!2025-12-26,52,318!2026-01-30,82,338-->

## futures contracts

1. Assume there is no limit on how many futures contracts can be traded for any commodity, even though the actual physical supply may be much smaller. Suppose you're a long holder of a futures contract that _may_ require you to take delivery at expiry, and you have huge financial resources \(or access to large bank funding\) roughly equal in value to all the deliverable commodity available. If the exchange imposes no volume caps on your positions, how would you guarantee a profit? ::@:: An open-ended question. This is trying to demonstrate _cornering the market_. <!--SR:!2026-01-22,75,338!2026-01-30,82,338-->
    - [cornering the market](../../../../general/cornering%20the%20market.md) ::@:: You would _buy_ all the deliverable commodity, and _long_ all the futures contracts. <p> At expiry, you deliver the commodity to satisfy your futures contracts. The price difference between the spot price when you bought the commodity and the futures price when you entered into the futures contract is your profit. Since you bought all the deliverable commodity, no one else can enter into futures contracts to compete with you, so you are guaranteed a profit. <!--SR:!2025-12-09,36,298!2026-01-30,82,338-->
      - cornering the market / risks ::@:: The risk is that the commodity price may fall significantly after you bought it, so your profit from the futures contracts may not cover your loss from the commodity purchase. <p> Another risk is that the exchange may impose position limits or other regulations to prevent market manipulation, which could limit your ability to corner the market. <p> This shows that after cornering the market, "_cleaning up the corpse_" is difficult and not guaranteed. <!--SR:!2026-01-25,78,338!2026-01-30,82,338-->

## currency forwards and futures

1. If market participants expect the underlying asset's price to rise in the next month, how will that expectation affect the one‑month forward price? ::@:: Assuming the market is efficient, the spot price already reflects all information, including future expectation. Even if you assume this future expectation is newly formed, the spot price will soon reflect this new expectation by increasing. <p> So the one-month forward price is not affected _directly_, and is still based on the spot price. <p> This shows markets are _forward-looking_. <!--SR:!2026-01-30,82,338!2025-11-20,21,278-->
2. Imagine you are the sole trader worldwide who knows that the U.S. dollar will strengthen against a foreign currency later on. The rate is quoted as U.S. dollars per unit of the foreign currency \(e.g., 1.429&nbsp;GBP/USD\). How can you exploit a forward contract to earn profit? ::@:: GBP is the underlying \(_base_ currency\). USD is the price \(_quote_ currency\). USD appreciating means GBP is depreciating. So short the currency forward. <!--SR:!2026-01-30,82,338!2026-01-20,73,338-->
3. Would your strategy in Scenario&nbsp;2 \(short the currency forward\) change if the quotation format were reversed, showing units of foreign currency per one U.S. dollar \(for example, 0.7&nbsp;USD/GBP\)? ::@:: Now USD is the underlying \(_base_ currency\). GBP is the price \(_quote_ currency\). Long the currency forward instead. <!--SR:!2026-01-22,75,338!2025-12-16,44,318-->
