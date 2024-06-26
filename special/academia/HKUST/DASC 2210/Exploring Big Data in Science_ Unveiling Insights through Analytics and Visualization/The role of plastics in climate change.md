---
aliases:
  - The role of plastics in climate change
tags:
  - by/self
  - date/2023/11/22/from
  - date/2023/11/24/to
  - functional/text
  - language/in/English
---

<!-- markdownlint-disable-next-line MD041 -->
2023 November 24

# The role of plastics in climate change

William So

## Abstract

Plastic is a widely used versatile material. However, its overuse has raised concerns about its health effects, environment effects, and now, climate change. This report quantifies the contribution of plastic production to greenhouse gas (GHG) emission and emphasizes the urgent need to reduce plastic production to address climate change. Additionally, potential actions to reduce plastic production will be discussed.

## Introduction

Plastic is a commonly used material that has greatly benefited our lives. The global production of plastic has reached unprecedented levels, with 380 million tonnes produced in 2015 alone (Geyer, Jambeck & Law, 2017). Whilst there is extensive research into health (Wright & Kelly, 2017) and environment effects (MacLeod, Tekman & Jahnke, 2021) of plastic overuse, little attention has been given to climate change. Considering plastics are derived from petrochemicals and the significant production volume, examining their role in contributing to climate change is crucial (Shen et al., 2020).

This report aims to quantify relationships between plastic production and GHG emissions by analyzing existing datasets. By examining plastic production and GHG emissions in various scenarios, the link between plastics and climate change can be better understood, helping find better ways to tackle plastic overuse.

## Methodology

To conduct this analysis, four datasets from Our World in Data were utilized. Two datasets provided information on annual CO<sub>2</sub> emission to limit global temperature rise to 2 °C and 1.5 °C. The time range for said datasets was from 1850 to 2100, with 27 predictions for scenarios where CO<sub>2</sub> reduction starts in a certain year, where said year ranges from 2000 to 2026 (Ritchie, Roser & Rosado, 2020). The other two datasets focused on GHG emission from plastic and global plastics production. The time range for GHG emission from plastic was from 2015 to 2019. The time range for global plastics production covered the years from 1950 to 2019 (Ritchie, Samborska & Roser, 2023). By combining these datasets, the link between plastics and GHG emission can be shown, allowing predictions to be made.

All four datasets were loaded into a spreadsheet. The global plastics production dataset was missing 1974, so the value of the previous year was used. Otherwise, the data was completely clean.

Next, global plastics production and total GHG emission were extrapolated up to 2050 using exponential regression. The GHG emission to plastic production ratio was calculated from 2015 to 2019, and then extrapolated from 1950 to 2050 using exponential regression. This ratio was used to estimate plastic GHG emission from based on plastics production. The results were compared against the total GHG emission for three scenarios: business as usual, below 2 °C, and below 1.5 °C. Charts were created to visualize the findings (Figure 1-5). Time was spent on finding the correct spreadsheet formula to use, but otherwise there was little trouble analyzing the data.

Exponential regression was used to extrapolate global plastics production and total GHG emission because they closely match the historical trend. For GHG emission to plastic production ratio, while there is little historical data, it is reasonable to expect that efficiency gains will be increasingly hard to make, so exponential regression was also used.

## Results

The analysis revealed several concerning trends. First, plastic production has been increasing exponentially without any signs of slowing down. In 2019, 459.75 million tonnes of plastics were produced, and this is projected to quadruple to 1897 million tonnes by 2050. This shows that about every 15 years, plastic production doubles (Figure 1). This exponential growth highlights the severity of the plastic overuse problem.

> ![Figure 1. Extrapolated plastic production](The%20role%20of%20plastics%20in%20climate%20change/extrapolated%20plastic%20production.png)
>
> __Figure 1. Extrapolated plastic production__

Second, total GHG emission has also been increasing exponentially, reaching 42.3 billion tonnes in 2019. It is expected to nearly double to 70.5 billion tonnes by 2050. The figure also shows scenarios where the global temperature rise has a 66% chance of being limited to 2 °C and 1.5 °C if CO<sub>2</sub> reduction starts from 2019 (Figure 2). This underscores the significant gap between current emissions and the scenarios required to limit the global temperature rise.

> ![Figure 2. Extrapolated GHG emission](The%20role%20of%20plastics%20in%20climate%20change/extrapolated%20GHG%20emission.png)
>
> __Figure 2. Extrapolated GHG emission__

Third, in a turn of good news, we found that the GHG emission per kilogram of plastic produced decreased by 11.9% from 3.94 in 2015 to 3.47 in 2019 (Figure 3). This shows that improvements in industrial processes are made. We expect such gains to continue but increasingly slowly as room for improvement runs out.

> ![Figure 3. GHG/plastic ratio](The%20role%20of%20plastics%20in%20climate%20change/GHG_plastic%20ratio.png)
>
> __Figure 3. GHG/plastic ratio__

Fourth, combining the findings from Figure 1 and Figure 3, it is evident that gains in industrial processes are insufficient to stop the growth of plastic GHG emission. Without reducing plastic production, 1.60 billion tonnes of GHG were released in 2019, projected to increase by 56.3% to 2.50 billion tonnes in 2050 (Figure 4). This highlights the crucialness of reducing plastic production in reducing plastic GHG emission.

> ![Figure 4. Extrapolated plastic GHG emission](The%20role%20of%20plastics%20in%20climate%20change/extrapolated%20plastic%20GHG%20emission.png)
>
> __Figure 4. Extrapolated plastic GHG emission__

Last, data from Figure 2 and Figure 4 are combined. Considering the proportion of plastic GHG emission relative to total GHG emission, historically, plastic GHG emission accounted for only 3.5% of the total GHG emission. If current policies continue, the proportion will remain unchanged. However, under the below 2 °C scenario and below 1.5 °C scenario, this proportion increases significantly, rising from 3.8% in 2019 to 7.1% in 2035 under the first scenario and to 52.7% in 2035 under the second scenario (Figure 5). This outlines the importance of reducing plastic production in limiting the global temperature rise due to GHG emission.

> ![Figure 5. Plastic GHG emission proportion](./The%20role%20of%20plastics%20in%20climate%20change/plastic%20GHG%20emission%20proportion.png)
>
> __Figure 5. Plastic GHG emission proportion__

## Discussion

The results of this analysis highlight the worsening problem of plastic overuse and its contribution to climate change. The exponential growth in plastics production and GHG emission demonstrates the urgent need to address this issue. While improvements in industrial processes have slowed down the growth of plastic GHG emission, they are insufficient to limit the global temperature rise to 1.5 °C or even 2 °C. Plastic reduction is essential for limiting the rise.

The findings also emphasize the scale of the problem and the need for action. Accumulative effects from plastics and GHG emission make it even more urgent. Reducing plastic production is a complex challenge, as it is closely tied to economic activities. However, it is crucial to find a balance between economic growth and environmental sustainability. Recycling plastics is another potential solution, but current technology limitations hinder large-scale plastic recycling (Payne & Jones, 2021).

## Conclusion

To conclude, the report analyzed four datasets on plastics and GHG emission and found that plastics and climate change are intricately linked. Policymakers should not overlook plastic reduction when considering climate policies. At the same time, the report also outlined the seriousness of the plastic overuse problem and difficulties in solving it. Moving forward, a comprehensive approach, such as reducing production, improving processes, reducing demands, and increasing recycling rates, is required to mitigate the catastrophic consequences of plastic overuse and climate change.

## Acknowledgements

The authors declare no competing interests. Generative AI is used for paraphrasing the text only and its outputs are human checked. All data and supplementary materials are available on Google Drive (<https://drive.google.com/file/d/1zUfvTzmn7bZjU4F_masS_pfS1n0YQ6jm/view?usp=sharing>).

## References

- Geyer, R., Jambeck, J. R., & Law, K. L. (2017). Production, use, and fate of all plastics ever made. _Science advances_, _3_(7), e1700782. <https://doi.org/10.1126/sciadv.1700782>
- MacLeod, M., Arp, H. P. H., Tekman, M. B., & Jahnke, A. (2021). The global threat from plastic pollution. _Science_, _373_(6550), 61-65. <https://doi.org/10.1126/science.abg5433>
- Ritchie, H., Roser, M., & Rosado, P. (2020). CO<sub>2</sub> and Greenhouse Gas Emissions. _Our World in Data_. <https://ourworldindata.org/co2-and-greenhouse-gas-emissions> [Online Resource]
- Ritchie, H., Samborska, V., & Roser, M. (2023). Plastic Pollution. _Our World in Data_. <https://ourworldindata.org/plastic-pollution> [Online Resource]
- Payne, J., & Jones, M. D. (2021). The chemical recycling of polyesters for a circular plastics economy: challenges and emerging opportunities. _ChemSusChem_, _14_(19), 4041-4070. <https://doi.org/10.1002/cssc.202100400>
- Shen, M., Huang, W., Chen, M., Song, B., Zeng, G., & Zhang, Y. (2020). (Micro) plastic crisis: un-ignorable contribution to global greenhouse gas emissions and climate change. _Journal of Cleaner Production_, _254_, 120138. <https://doi.org/10.1016/j.jclepro.2020.120138>
- Wright, S. L., & Kelly, F. J. (2017). Plastic and human health: a micro issue?. _Environmental science & technology_, _51_(12), 6634-6647. <https://doi.org/10.1021/acs.est.7b00423>
