---
aliases:
  - The role of plastics in climate change
tags:
  - by/self
  - date/2023/11/22/from
  - date/2023/11/24/to
  - functional/texts
---

# The role of plastics in climate change

William So

## Abstract

Plastics are ubiquitous material for its versatility. Global production of plastics has never been higher than before. However, its overuse has attracted attention due to its health effects, environment effects, etc. Fewer focuses on its impact on climate change. This report aims to quantify said impact by analyzing existing datasets on GHG emissions and plastic production. What we found is that reducing plastic production is imminent and essential to solving climate change. Further possible actions to reduce plastic production are discussed.

## Introduction

Plastic is a widely used material because it has added much value to our lives. Global production of plastic has reached a staggering 380 million tonnes in 2015 (Geyer, Jambeck & Law, 2017). Most discussions in the media and literature associate its overuse with health effects (Wright & Kelly, 2017), environment effects (MacLeod, Tekman & Jahnke, 2021), etc. Few focuses on its effect on climate change, contributing to a lack of research in this aspect. Considering the high production of plastics and their origins from petrochemicals, this impact should not be ignored (Shen et al., 2020).

This report aims to quantify the effect of plastic production on greenhouse gas (GHG) emissions and predict its future trend using existing datasets. This way, we can explore better ways to tackle plastic overuse while considering their climate impact.

## Methodology

In this report, four datasets from Our World in Data are used. Two datasets show the annual amount of CO<sub>2</sub> emitted over time to keep the global temperature rise below respectively 2 °C and 1.5 °C. The time range is from 1850 to 2100. Each dataset contains a prediction for each year from 2000 to 2026 if CO<sub>2</sub> reductions start in said year. (Ritchie, Roser & Rosado, 2020). The other two are respectively GHG emissions from plastic and global plastics production. The time range in the former is from 2015 to 2019, while the latter ranges from 1950 to 2019 (Ritchie, Samborska & Roser, 2023). By combining these datasets, the link between plastic and GHG emissions can be shown. Predictions about GHG emissions from plastics can also be made.

All four datasets are loaded into a spreadsheet. The global plastic production dataset is missing 1974, so value of the previous year is used. Otherwise, the data is completely clean.

Next, global plastic production and total GHG emission are extrapolated into 2050 using exponential regression. The extrapolation for GHG emission to limit the temperature increase are obtained from the dataset directly. To find the link between plastic and GHG emission, GHG emission to plastic produced ratio is calculated from 2015 to 2019. Then it is extrapolated to from 1950 to 2050 using exponential regression. After that, this ratio is used to extrapolate plastic GHG emission from produced plastic. Lastly, the plastic GHG emission is compared against the total GHG emission for three scenarios: business as usual, below 2 °C, and below 1.5 °C. Charts are created for all of above. Quite some time is spent on finding the correct spreadsheet formula to use, but otherwise there is little trouble analyzing the data.

Exponential regression is used to extrapolate global plastic production and total GHG emission because they closely match the historical trend. For the GHG emission to plastic produced ratio, while there is little historical data, it is reasonable to expect that efficiency gains become increasingly hard to make, so exponential regression is also used.

## Results

The findings indicate the current plastic trends are worrying. First, plastic production has been increasing since historical records start, and the increase rate is exponential without any sign of slowing down. About every 15 years, plastic production doubles. 459.75 million tonnes of plastics were produced in 2019, and it is expected to quadruple to 1897 million tonnes by 2050. (Figure 1). This shows that plastic overuse is a worsening problem.

> ![Figure 1. Extrapolated plastic production](The%20role%20of%20plastics%20in%20climate%20change/extrapolated%20plastic%20production.png)
>
> __Figure 1. Extrapolated plastic production__

Second, what is also increasing exponentially is the total GHG emission. Similarly to Figure 1, there is little sign of trailing off, increasing to 42.3 billion tonnes in 2019 and expected to almost double to 70.5 billion tonnes by 2050. The figure also shows scenarios where the global temperature rise has a 66% chance of being kept below 2 °C and 1.5 °C starting from 2019, emphasizing how far off we are from said scenarios (Figure 2). This is unsurprising and has been adequately described by other literature. This is placed here so that later figures can reference it, especially the below 2 °C and below 1.5 °C scenarios.

> ![Figure 2. Extrapolated GHG emission](The%20role%20of%20plastics%20in%20climate%20change/extrapolated%20GHG%20emission.png)
>
> __Figure 2. Extrapolated GHG emission__

Third, in a slight turn of good news, from the little data on plastic GHG emission from 2015 to 2019, we find that the kilogram of GHG emission generated per kilogram of plastic produced has decreased by 11.9% from 3.94 in 2015 to 3.47 in 2019 (Figure 3). This means the industrial processes for making plastics has been improving to reduce the amount of GHG generated. We expect such gains to continue but increasingly slowly as room for improvement runs out.

> ![Figure 3. GHG/plastic ratio](The%20role%20of%20plastics%20in%20climate%20change/GHG_plastic%20ratio.png)
>
> __Figure 3. GHG/plastic ratio__

Fourth, combining results from Figure 1 and Figure 3, gains in industrial processes are insufficient to stop the growth of plastic GHG emission. It has slowed down the growth to linear, however. 1.60 billion tonnes of GHG were released in 2019, expecting to increase by 56.3% to 2.50 billion tonnes in 2050 (Figure 4). This shows that reducing plastic production is the only way to reduce plastic GHG emission and efficiency gains can only do so much.

> ![Figure 4. Extrapolated plastic GHG emission](The%20role%20of%20plastics%20in%20climate%20change/extrapolated%20plastic%20GHG%20emission.png)
>
> __Figure 4. Extrapolated plastic GHG emission__

Last, to find out the effect of plastic GHG emission relative to the total GHG emission, data from Figure 2 and Figure 4 are combined together. Historically, plastic GHG emission is only 3.5% of the total GHG emission and this percentage has stayed constant over time. If current policies continue, the percentage will still remain unchanged. However, if GHG emission starts decreasing from 2019 to limit the global temperature rise, then the contribution of plastic to GHG emission increases. For the below 2 °C scenario, the percentage rises from 3.8% in 2019 to 7.1% in 2035. For the below 1.5 °C, the increase is much more drastic and rises to 52.7% in 2035 (Figure 5). This indicates that any method to limit the global temperature rise must also involve reducing plastic production.

> ![Figure 5. Plastic GHG emission proportion](./The%20role%20of%20plastics%20in%20climate%20change/plastic%20GHG%20emission%20proportion.png)
>
> __Figure 5. Plastic GHG emission proportion__

## Discussion

Our results show that plastic overuse is worsening as plastic production continues to increase. Despite improvements in industrial processes, plastic GHG emission continues to increase, contributing to climate change. They also show that to limit the global temperature rise, especially to 1.5 °C, plastic reduction is essential.

The results paint a worryingly picture for our planet. Similar to climate change, the scale of the problem is large enough that reduction of plastic production is imminent. Moreover, both of them have accumulative effects, so the earlier reduction occurs, the better. However, production is also highly tied to economic activities, so a dilemma exists between reduction and economic growth. Another proposed solution is recycling plastics so that there is less need to produce plastics, but large-scale plastic recycling itself is limited by current technology (Payne & Jones, 2021).

The only thing is clear is that tremendous effort is needed on reducing plastic production, whether it be on improving processes, increasing recycling rates, or reducing demand for plastics, then we might have a chance at averting this plastic and climate catastrophe.

## Conclusion

The report analyzed four datasets on plastics and GHG emission and found that plastics and climate change are intricately linked. Policymakers should not overlook plastic reduction when considering climate policies. At the same time, the report also outlined the seriousness of the plastic overuse problem and difficulties in solving it. Moving forward, extra effort in all aspects, like research, policies, etc., is required to avoid the catastrophic consequences from plastic overuse and climate change.

## Acknowledgements

The authors declare no competing interests. Generative AI is used for paraphrasing the text only and its outputs are human checked. All data and supplementary materials are available on Google Drive (https://drive.google.com/file/d/1zUfvTzmn7bZjU4F_masS_pfS1n0YQ6jm/view?usp=sharing).

## References

- Geyer, R., Jambeck, J. R., & Law, K. L. (2017). Production, use, and fate of all plastics ever made. _Science advances_, _3_(7), e1700782. https://doi.org/10.1126/sciadv.1700782
- MacLeod, M., Arp, H. P. H., Tekman, M. B., & Jahnke, A. (2021). The global threat from plastic pollution. _Science_, _373_(6550), 61-65. https://doi.org/10.1126/science.abg5433
- Ritchie, H., Roser, M., & Rosado, P. (2020). CO₂ and Greenhouse Gas Emissions. _Our World in Data_. https://ourworldindata.org/co2-and-greenhouse-gas-emissions [Online Resource]
- Ritchie, H., Samborska, V., & Roser, M. (2023). Plastic Pollution. _Our World in Data_. 'https://ourworldindata.org/plastic-pollution [Online Resource]
- Payne, J., & Jones, M. D. (2021). The chemical recycling of polyesters for a circular plastics economy: challenges and emerging opportunities. _ChemSusChem_, _14_(19), 4041-4070. https://doi.org/10.1002/cssc.202100400
- Shen, M., Huang, W., Chen, M., Song, B., Zeng, G., & Zhang, Y. (2020). (Micro) plastic crisis: un-ignorable contribution to global greenhouse gas emissions and climate change. _Journal of Cleaner Production_, _254_, 120138. https://doi.org/10.1016/j.jclepro.2020.120138
- Wright, S. L., & Kelly, F. J. (2017). Plastic and human health: a micro issue?. _Environmental science & technology_, _51_(12), 6634-6647. https://doi.org/10.1021/acs.est.7b00423
