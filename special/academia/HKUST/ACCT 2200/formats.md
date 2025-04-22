---
aliases:
  - ACCT 2200 format
  - ACCT 2200 formats
  - ACCT2200 format
  - ACCT2200 formats
  - HKUST ACCT 2200 format
  - HKUST ACCT 2200 formats
  - HKUST ACCT2200 format
  - HKUST ACCT2200 formats
tags:
  - flashcard/active/special/academia/HKUST/ACCT_2200/formats
  - language/in/English
---

# formats

- HKUST ACCT 2200

Do you really need to remember these _exactly_? ::@:: Not really... The approximate format should suffice.

## materials requisition form

> __example__
>
> ---
>
> {@{__Materials Requisition Form__}@}
>
> - {@{Materials Requisition Number: MR 420}@}
> - {@{Date: 2025-02-14}@}
> - {@{Job Number: 42}@}
> - {@{Description: Home}@}
>
> | {@{<u>Material Description</u>}@} | {@{<u>Quantity</u>}@} | {@{<u>Unit Cost</u>}@} | {@{<u>Total Cost</u>}@}  |
> | --------------------------------- | ---------------------:| ----------------------:| ------------------------:|
> | {@{1 × 1 meter wooden planks}@}   | {@{100 sq. m}@}       | {@{&dollar;2.00}@}     | {@{&dollar;200}@}        |
> | {@{24 bags of sand}@}             | {@{100 kg}@}          | {@{&dollar;10.00}@}    | {@{1&nbsp;000}@}         |
> | {@{3 bags of coal}@}              | {@{20 kg}@}           | {@{&dollar;25.00}@}    | {@{<u>500</u>}@}         |
> | &emsp;{@{Total cost}@}            |                       |                        | {@{&dollar;1&nbsp;700}@} |
>
> {@{Authorized Signature \_\_\_\_\_\_\_\_\_\_}@}

- materials requisition form ::@:: information, table, authorized signature
  - materials requisition form / information ::@:: materials requisition number, date, job number, description
  - materials requisition form / table
    - materials requisition form / table / column headers ::@:: material description (including numbers or sizes if needed), quantity, unit cost, total cost
    - materials requisition form / table / row headers ::@:: material description, (materials...), total cost

## direct labor time ticket

> __example__
>
> ---
>
> {@{__Direct Labor Time Ticket__}@}
>
> - {@{Dates: 2025-02-10 \(Monday\)—2025-02-14 \(Friday\)}@}
> - {@{Ticket Number: TT 1337}@}
> - {@{Employee: Chris Wong}@}
>
> | {@{Date}@}       | {@{Time Started}@} | {@{Time Ended}@}   | {@{Total Hours}@} | {@{Hourly Rate}@} | {@{Total Amount}@}       | {@{Job Number}@} |
> | ---------------- | ------------------ | ------------------ | -----------------:| -----------------:| ------------------------:| ---------------- |
> | {@{2025-02-10}@} | {@{03:00}@}        | {@{23:00}@}        | {@{20 hours}@}    | {@{&dollar;100}@} | {@{2&nbsp;000}@}         | {@{42}@}         |
> | {@{2025-02-11}@} | {@{06:00}@}        | {@{22:00}@}        | {@{16 hours}@}    | {@{100}@}         | {@{1&nbsp;600}@}         | {@{42}@}         |
> | {@{2025-02-12}@} | {@{06:30}@}        | {@{22:30}@}        | {@{16 hours}@}    | {@{100}@}         | {@{1&nbsp;600}@}         | {@{42}@}         |
> | {@{2025-02-13}@} | {@{04:00}@}        | {@{21:00}@}        | {@{17 hours}@}    | {@{100}@}         | {@{1&nbsp;700}@}         | {@{42}@}         |
> | {@{2025-02-13}@} | {@{22:45}@}        | {@{23:45}@}        | {@{1 hour}@}      | {@{100}@}         | {@{100}@}                | {@{Training}@}   |
> | {@{2025-02-14}@} | {@{07:00}@}        | {@{15:00}@}        | {@{8 hours}@}     | {@{100}@}         | {@{800}@}                | {@{69}@}         |
> |                  |                    | {@{Weekly Total}@} | {@{78 hours}@}    |                   | {@{&dollar;7&nbsp;800}@} |                  |
>
> {@{Authorized Signature \_\_\_\_\_\_\_\_\_\_}@}

- direct labor time ticket ::@:: information, table, authorized signature
  - direct labor time ticket / information ::@:: dates, ticket number, employee
  - direct labor time ticket / table
    - direct labor time ticket / table / column headers ::@:: date, time started, time ended, total hours, hourly rate, total amount, job number
    - direct labor time ticket / table / row headers ::@:: date, (consecutive working periods...), (whatever, e.g. weekly) total

## job cost sheet

> __example__
>
> ---
>
> {@{__Job Cost Sheet__}@}
>
> - {@{Job Number: 42}@}
> - {@{Date Started: 2025-02-01}@}
> - {@{Date Completed:}@}
> - {@{Description: Home, Job \#42}@}
>
> | {@{__Actual Direct Materials__}@} |                          | {@{__Actual Direct Labor__}@} |                 |                          | {@{__Applied Manufacturing Overhead__}@} |                   |
> | --------------------------------- | ------------------------:| ----------------------------- | ---------------:| ------------------------:| ----------------------------------------:| -----------------:|
> | {@{__Req. No__}@}                 | {@{__Amount__}@}         | {@{__Ticket__}@}              | {@{__Hours__}@} | {@{__Amount__}@}         | {@{__Hours__}@}                          | {@{__Amount__}@}  |
> | {@{MR 420}@}                      | {@{&dollar;1&nbsp;700}@} | {@{TT 1337}@}                 | {@{69}@}        | {@{&dollar;6&nbsp;900}@} | {@{69}@}                                 | {@{&dollar;690}@} |
>
> ---
>
> {@{__Cost Summary__}@}
>
> |                                      |                                       |
> | ------------------------------------ | -------------------------------------:|
> | {@{Direct Materials Cost}@}          | {@{&dollar;&nbsp;1&nbsp;700}@}        |
> | {@{Direct Labor Cost}@}              | {@{6&nbsp;900}@}                      |
> | {@{Applied Manufacturing Overhead}@} | {@{<u>690</u>}@}                      |
> | &emsp;{@{Total Cost}@}               | {@{<u>&dollar;&nbsp;9&nbsp;290</u>}@} |

- job cost sheet ::@:: information, tables, cost summary
  - job cost sheet / information ::@:: job number, date started, date completed, description
  - job cost sheet / tables ::@:: actual direct materials, actual direct labor, applied manufacturing overhead
    - job cost sheet / tables / actual direct materials ::@:: req. no, amount
    - job cost sheet / tables / actual direct labor ::@:: ticket, hours, amount
    - job cost sheet / tables / applied manufacturing overhead ::@:: (primary cost driver unit), amount
  - job cost sheet / cost summary ::@:: direct materials cost + direct labor cost + applied manufacturing overhead = total cost

## cost of goods manufacturing report

> __example__
>
> ---
>
> |                                                       |                                     |
> | ----------------------------------------------------- | -----------------------------------:|
> | {@{Beginning raw materials inventory}@}               | {@{&dollar;400}@}                   |
> | &emsp;{@{Plus: Raw materials purchase}@}              | {@{500}@}                           |
> | &emsp;{@{Less: Indirect materials}@}                  | {@{\(100\)}@}                       |
> | &emsp;{@{Less: Ending raw materials inventory}@}      | {@{\(200\)}@}                       |
> | {@{Direct materials used}@}                           | {@{&dollar;600}@}                   |
> | {@{Direct labor}@}                                    | {@{900}@}                           |
> | {@{Manufacturing overhead applied}@}                  | {@{250}@}                           |
> | {@{Total current manufacturing costs}@}               | {@{&dollar;1&nbsp;750}@}            |
> | &emsp;{@{Plus: Beginning work in process inventory}@} | {@{2&nbsp;000}@}                    |
> | &emsp;{@{Less: Ending work in process inventory}@}    | {@{\(1&nbsp;000\)}@}                |
> | {@{Cost of goods manufactured}@}                      | {@{__&dollar;<u>2&nbsp;750</u>__}@} |

- cost of goods manufacturing report ::@:: total current manufacturing costs + \(plus:\) beginning work in process inventory − \(less:\) ending work in process inventory = cost of goods manufactured
  - cost of goods manufacturing report / total current manufacturing costs ::@:: direct materials used + direct labor + manufacturing overhead _applied_ \(not _actual_\)
  - cost of goods manufactured report / direct materials used ::@:: beginning raw materials inventory + \(plus:\) raw material purchases − \(less:\) indirect materials \(_important_\) − \(less:\) ending raw materials inventory

## income statement (cost of goods sold)

> __example__
>
> ---
>
> |                                                      |                      |                         |
> | ---------------------------------------------------- | --------------------:| -----------------------:|
> | {@{Less: Cost of goods sold}@}                       |                      |                         |
> | &emsp;{@{Beginning finished goods inventory}@}       | {@{600}@}            |                         |
> | &emsp;{@{Plus: Cost of goods manufactured}@}         | {@{2&nbsp;750}@}     |                         |
> | &emsp;{@{Less: Ending finished goods inventory}@}    | {@{<u>(200)</u>}@}   |                         |
> | {@{Unadjusted cost of goods sold}@}                  | {@{3&nbsp;150}@}     |                         |
> | &emsp;{@{Less: Overapplied manufacturing overhead}@} | {@{<u>\(150\)</u>}@} | {@{<u>3&nbsp;000</u>}@} |

- income statement \(cost of goods sold\) ::@:: _unadjusted_ cost of goods sold +/− \(plus:\) underapplied manufacturing overhead/\(less:\) overapplied manufacturing overhead = \(adjusted\) cost of goods sold
  - income statement \(cost of goods sold\) / unadjusted cost of goods sold ::@:: beginning finished goods inventory + \(plus:\) cost of goods manufactured − \(less:\) ending finished goods inventory
- income statement ::@:: sales revenue − \(less:\) cost of goods sold = gross profit <br/> gross profit − \(less:\) selling and administrative expenses = net operating income

## T account

> __example__
>
> ---
>
> |                         |                         |                                                    |                 |
> | -----------------------:| -----------------------:|:-------------------------------------------------- |:--------------- |
> |                         | {@{Increase}@}          | {@{Decrease}@}                                     |                 |
> |                         | {@{__Cash \(A\)__}@}    | {@{\(the left text should be centered instead\)}@} |                 |
> |                         | ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯              | ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯                                         |                 |
> |                         | {@{__Debits \(Dr\)__}@} | {@{__Credits \(Cr\)__}@}                           |                 |
> | {@{Beginning balance}@} | {@{100}@}               |                                                    |                 |
> | {@{Income}@}            | {@{100}@}               |                                                    |                 |
> |                         |                         | {@{50}@}                                           | {@{Transport}@} |
> |                         | ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯              | ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯                                         |                 |
> | {@{Ending balance}@}    | {@{__150__}@}           |                                                    |                 |

- T account ::@:: Draw a (big) "T". Write the account name (and optionally its type) on above the "T". Add a header for each of the two spaces below the horizontal line of the "T": "Debits (Dr)" on the left, "Credits (Cr)" on the right. Optionally, write "Increase" and "Decrease" above the account name, labeling which side is the _normal_ balance.
  - T account / recording ::@:: For each change to the account, write a number on either the left or the right side, depending on if it is a debit or credit. Optionally, label the number with a brief description. <p> To calculate the final account balance, draw a horizontal line below all the numbers. Calculate the remaining balance is on which side and write the number on the corresponding side below the new horizontal line.

## process costing (weighted average)

> __example__: {@{find physical units}@} <!-- flashcard ID: a557a424-95ef-40c6-9877-9ca8f66e3d9f -->
>
> ---
>
> | {@{Units to be Accounted For}@} | {@{Physical Units}@} |
> | ------------------------------- | --------------------:|
> | {@{Beginning Inventory}@}       | {@{420}@}            |
> | {@{Started This Period}@}       | {@{690}@}            |
> | {@{Total}@}                     | {@{1&nbsp;110}@}     |

<!-- markdownlint MD028 -->

> __example__: {@{convert physical units into equivalent units}@}
>
> ---
>
> | {@{Units Accounted For}@}   | {@{Physical Units}@} | {@{Direct Materials}@} | {@{Conversion}@} |
> | --------------------------- | --------------------:| ----------------------:| ----------------:|
> | {@{Completed/Transferred}@} | {@{500}@}            | {@{500}@}              | {@{500}@}        |
> | {@{Ending Inventory}@}      | {@{610}@}            | {@{600}@}              | {@{590}@}        |
> | {@{Total}@}                 | {@{1&nbsp;110}@}     | {@{1&nbsp;100}@}       | {@{1&nbsp;090}@} |

<!-- markdownlint MD028 -->

> __example__: {@{calculate cost per equivalent unit}@}
>
> ---
>
> | {@{Cost to be Accounted For}@}  | {@{Direct Materials}@}  | {@{Conversion}@}        | {@{Total}@}                    |
> | ------------------------------- | -----------------------:| -----------------------:| ------------------------------:|
> | {@{Beginning Inventory}@}       | {@{&dollar;&emsp;700}@} | {@{&dollar;&emsp;600}@} | {@{&dollar;&emsp;1&nbsp;300}@} |
> | {@{Cost Added in This Period}@} | {@{400}@}               | {@{490}@}               | {@{890}@}                      |
> | {@{Total Cost}@}                | {@{1&nbsp;100}@}        | {@{1&nbsp;090}@}        | {@{&dollar;&emsp;2&nbsp;190}@} |
> | {@{Equivalent Units}@}          | {@{÷&emsp;1&nbsp;100}@} | {@{÷&emsp;1&nbsp;090}@} |                                |
> | {@{Cost Per Equivalent Unit}@}  | {@{&dollar;&emsp;1}@}   | {@{&dollar;&emsp;1}@}   | {@{&dollar;&emsp;2}@}          |

<!-- markdownlint MD028 -->

> __example__: {@{reconcile costs}@}
>
> ---
>
> | {@{Cost Accounted For}@}      | {@{Direct Materials}@}         | {@{Conversion}@}               | {@{Total}@}                    |
> | ----------------------------- | ------------------------------:| ------------------------------:| ------------------------------:|
> | {@{Cost of Units Completed}@} | {@{&dollar;&emsp;500}@}        | {@{&dollar;&emsp;500}@}        | {@{&dollar;&emsp;1&nbsp;000}@} |
> | {@{Ending Inventory}@}        | {@{600}@}                      | {@{590}@}                      | {@{1&nbsp;190}@}               |
> | {@{Total}@}                   | {@{&dollar;&emsp;1&nbsp;100}@} | {@{&dollar;&emsp;1&nbsp;090}@} | {@{&dollar;&emsp;2&nbsp;190}@} |

- process costing \(weighted average\) ::@:: find physical units, convert physical units into equivalent units, calculate cost per equivalent unit, reconcile costs
  - process costing \(weighted average\) / column headers ::@:: diagonal header: units to be accounted for, units accounted for, cost to be accounted for, cost accounted for
    - process costing \(weighted average\) / column headers / units ::@:: physical units, direct materials, conversion
    - process costing \(weighted average\) / column headers / cost ::@:: direct materials, conversion, total
  - process costing \(weighted average\) / find physical units ::@:: _row headers_: beginning period, started this period, total
  - process costing \(weighted average\) / convert physical units into equivalent units ::@:: _row headers_: completed/transferred, ending inventory, total
  - process costing \(weighted average\) / calculate cost per equivalent unit ::@:: _row headers_: beginning inventory, cost added in this period, total cost, equivalent units, cost per equivalent unit
  - process costing \(weighted average\) / reconcile costs ::@:: _row headers_: cost of units completed, ending inventory, total
- production report \(weighted average\) ::@:: section 1: step 1, step 2 <br/> section 2: step 3 <br/> section 3: step 4
  - production report \(weighted average\) / headers ::@:: Section \(\#\) of Production Report <br/> \(company name\) <br/> Process Costing Production Report \(Weighted Average Method\) <br/> \(process name\) Process <br/> For \(time, e.g. the Quarter Ended March 31, 2025\)
  - production report \(weighted average\) / formatting ::@:: Add dollar signs if needed to the first and last currency number in the same column. Underline total costs in section 3.

## process costing (first-in, first-out)

> __example__: {@{find physical units}@} <!-- flashcard ID: a2b2f0b3-4333-405b-8760-d42c786993d6 -->
>
> ---
>
> | {@{Units to be Accounted For}@} | {@{Physical Units}@} |
> | ------------------------------- | --------------------:|
> | {@{Beginning Inventory}@}       | {@{420}@}            |
> | {@{Started This Period}@}       | {@{690}@}            |
> | {@{Total}@}                     | {@{1&nbsp;110}@}     |

<!-- markdownlint MD028 -->

> __example__: {@{convert physical units into equivalent units}@}
>
> ---
>
> | {@{Units Accounted For}@}       | {@{Physical Units}@} | {@{Direct Materials}@} | {@{Conversion}@} |
> | ------------------------------- | --------------------:| ----------------------:| ----------------:|
> | {@{Beginning Work In Process}@} | {@{420}@}            | {@{10}@}               | {@{30}@}         |
> | {@{Completed/Transferred}@}     | {@{80}@}             | {@{80}@}               | {@{80}@}         |
> | {@{Ending Inventory}@}          | {@{610}@}            | {@{600}@}              | {@{590}@}        |
> | {@{Total}@}                     | {@{1&nbsp;110}@}     | {@{690}@}              | {@{700}@}        |

<!-- markdownlint MD028 -->

> __example__: {@{calculate cost per equivalent unit}@}
>
> ---
>
> | {@{Cost to be Accounted For}@}  | {@{Direct Materials}@}  | {@{Conversion}@}        | {@{Total}@}                    |
> | ------------------------------- | -----------------------:| -----------------------:| ------------------------------:|
> | {@{Cost Added in This Period}@} | {@{&dollar;&emsp;690}@} | {@{&dollar;&emsp;700}@} | {@{&dollar;&emsp;1&nbsp;390}@} |
> | {@{Equivalent Units}@}          | {@{÷&emsp;690}@}        | {@{÷&emsp;700}@}        |                                |
> | {@{Cost Per Equivalent Unit}@}  | {@{&dollar;&emsp;1}@}   | {@{&dollar;&emsp;1}@}   | {@{&dollar;&emsp;2}@}          |

<!-- markdownlint MD028 -->

> __example__: {@{reconcile costs}@}
>
> ---
>
> | {@{Cost Accounted For}@}                            | {@{Direct Materials}@}         | {@{Conversion}@}               | {@{Total}@}                    |
> | --------------------------------------------------- | ------------------------------:| ------------------------------:| ------------------------------:|
> | {@{Cost Added to Beginning Inventory Last Period}@} | {@{&dollar;&emsp;410}@}        | {@{&dollar;&emsp;390}@}        | {@{&dollar;&emsp;800}@}        |
> | {@{Cost to Complete Beginning Inventory}@}          | {@{10}@}                       | {@{30}@}                       | {@{40}@}                       |
> | {@{Started and Completed}@}                         | {@{80}@}                       | {@{80}@}                       | {@{160}@}                      |
> | {@{Ending Inventory}@}                              | {@{600}@}                      | {@{590}@}                      | {@{1&nbsp;190}@}               |
> | {@{Total}@}                                         | {@{&dollar;&emsp;1&nbsp;100}@} | {@{&dollar;&emsp;1&nbsp;090}@} | {@{&dollar;&emsp;2&nbsp;190}@} |

- process costing \(first-in, first-out\) ::@:: find physical units, convert physical units into equivalent units, calculate cost per equivalent unit, reconcile costs
  - process costing \(first-in, first-out\) / column headers ::@:: diagonal header: units to be accounted for, units accounted for, cost to be accounted for, cost accounted for
    - process costing \(first-in, first-out\) / column headers / units ::@:: physical units, direct materials, conversion
    - process costing \(first-in, first-out\) / column headers / cost ::@:: direct materials, conversion, total
  - process costing \(first-in, first-out\) / find physical units ::@:: _row headers_: beginning period, started this period, total
  - process costing \(first-in, first-out\) / convert physical units into equivalent units ::@:: _row headers_: beginning work in process, completed/transferred, ending inventory, total
  - process costing \(first-in, first-out\) / calculate cost per equivalent unit ::@:: _row headers_: cost added in this period, equivalent units, cost per equivalent unit
  - process costing \(first-in, first-out\) / reconcile costs ::@:: _row headers_: cost added to beginning inventory last period, cost to complete beginning inventory, started and completed, ending inventory, total
- production report \(first-in, first-out\) ::@:: section 1: step 1, step 2 <br/> section 2: step 3 <br/> section 3: step 4
  - production report \(first-in, first-out\) / headers ::@:: Section \(\#\) of Production Report <br/> \(company name\) <br/> Process Costing Production Report \(FIFO Method\) <br/> \(process name\) Process <br/> For \(time, e.g. the Quarter Ended March 31, 2025\)
  - production report \(first-in, first-out\) / formatting ::@:: Add dollar signs if needed to the first and last currency number in the same column. Underline total costs in section 3.

## activity cost pool

> __example__
>
> ---
>
> | {@{Activity Cost Pool}@} | {@{Total Activity Cost}@}      | {@{Process A}@} | {@{Process B}@} | {@{Total}@} |
> | ------------------------ | ------------------------------:| ---------------:| ---------------:| -----------:|
> | {@{Machining}@}          | {@{&dollar;&emsp;4&nbsp;200}@} | {@{200}@}       | {@{220}@}       | {@{420}@}   |

- activity cost pool ::@:: _column headers_: activity cost pool, total activity cost, \(processes...\), total

## activity cost allocation

> __example__
>
> ---
>
> | {@{Activity Cost Pool}@} | {@{Process A}@}                | {@{Process B}@}                | {@{Total}@}                    |
> | ------------------------ | ------------------------------:| ------------------------------:| ------------------------------:|
> | {@{Machine Hours}@}      | {@{200}@}                      | {@{220}@}                      | {@{420}@}                      |
> | {@{Activity Rate}@}      | {@{×&nbsp;&dollar;&emsp;10}@}  | {@{×&nbsp;&dollar;&emsp;10}@}  |                                |
> |                          | {@{&dollar;&emsp;2&nbsp;000}@} | {@{&dollar;&emsp;2&nbsp;200}@} | {@{&dollar;&emsp;4&nbsp;200}@} |

- activity cost allocation
  - activity cost allocation / column headers ::@:: activity cost pool, \(processes...\), total
  - activity cost allocation / row headers ::@:: activity cost pool, \(activity driver unit\), activity rate, \(empty\)

## activity cost driver - setups

> __example__
>
> ---
>
> | {@{Activity Cost Pool}@}       | {@{Process A}@}   | {@{Process B}@}  | {@{Total}@} |
> | ------------------------------ | -----------------:| ----------------:| -----------:|
> | {@{Number of Units Produced}@} | {@{300}@}         | {@{100}@}        | {@{400}@}   |
> | {@{Average Units Per Batch}@}  | {@{20}@}          | {@{5}@}          |             |
> | {@{Number of Setups}@}         | {@{300/20 = 15}@} | {@{100/5 = 20}@} | {@{35}@}    |

- activity cost driver - setups
  - activity cost driver - setups / column headers ::@:: activity cost pool, \(processes...\), total
  - activity cost driver - setups / row headers ::@:: activity cost pool, number of units produced, average units per batch, number of setups

## total manufacturing overhead

> __example__
>
> ---
>
> | {@{Activity Cost Pool}@}                | {@{Process A}@}                | {@{Process B}@}                | {@{Total}@}                    |
> | --------------------------------------- | ------------------------------:| ------------------------------:| ------------------------------:|
> | {@{Machining}@}                         | {@{&dollar;&emsp;2&nbsp;000}@} | {@{&dollar;&emsp;2&nbsp;200}@} | {@{&dollar;&emsp;4&nbsp;200}@} |
> | {@{Setup}@}                             | {@{1&nbsp;500}@}               | {@{2&nbsp;000}@}               | {@{3&nbsp;500}@}               |
> | {@{Total Manufacturing Overhead Cost}@} | {@{&dollar;&emsp;3&nbsp;500}@} | {@{&dollar;&emsp;4&nbsp;200}@} | {@{&dollar;&emsp;7&nbsp;700}@} |

- total manufacturing overhead
  - total manufacturing overhead / column headers ::@:: activity cost pool, (activity pools...), total manufacturing overhead cost
  - total manufacturing overhead / row headers ::@:: activity cost pool, (processes...), total

## contribution margin income statement

> __example__
>
> ---
>
> {@{Comparing Apples With Oranges Company}@} <br/>
> {@{__Contribution Margin Income Statement__}@} <br/>
> {@{Based on Target Profit of &dollar;300}@}
>
>
> |                                  |                    |                        |                                    |                    |                         |                                 |                          |                                    |
> | -------------------------------- | ------------------:| ----------------------:| ----------------------------------:| ------------------:| -----------------------:| -------------------------------:| ------------------------:| ----------------------------------:|
> |                                  |                    | {@{__<u>apple</u>__}@} |                                    |                    | {@{__<u>orange</u>__}@} |                                 | {@{__<u>overall</u>__}@} |                                    |
> |                                  | {@{per unit}@}     | {@{total}@}            | {@{percent}@}                      | {@{per unit}@}     | {@{total}@}             | {@{percent}@}                   | {@{total}@}              | {@{percent}@}                      |
> | {@{sales revenue}@}              | {@{&dollar;3}@}    | {@{&dollar;420}@}      | {@{100%}@}                         | {@{&dollar;4}@}    | {@{&dollar;720}@}       | {@{100%}@}                      | {@{&dollar;1&nbsp;140}@} | {@{100%}@}                         |
> | {@{less: variable costs}@}       | {@{<u>\(2\)</u>}@} | {@{<u>\(280\)</u>}@}   | {@{<u>\(66.67\)&nbsp;&nbsp;</u>}@} | {@{<u>\(2\)</u>}@} | {@{<u>\(360\)</u>}@}    | {@{<u>\(50\)&nbsp;&nbsp;</u>}@} | {@{<u>\(640\)</u>}@}     | {@{<u>\(56.14\)&nbsp;&nbsp;</u>}@} |
> | &emsp;{@{contribution margin}@}  | {@{&dollar;1}@}    | {@{&dollar;140}@}      | {@{33.33%}@}                       | {@{&dollar;2}@}    | {@{&dollar;360}@}       | {@{50%}@}                       | {@{&dollar;500}@}        | {@{43.86%}@}                       |
> | {@{less: fixed costs}@}          |                    |                        |                                    |                    |                         |                                 | {@{<u>\(200\)</u>}@}     |                                    |
> | &emsp;{@{net operating income}@} |                    |                        |                                    |                    |                         |                                 | {@{&dollar;300}@}        |                                    |

- contribution margin income statement ::@:: headers, products & overall, row headers
  - contribution margin income statement / headers ::@:: \(company name\), contribution margin income statement, based on breakeven/target profit of &dollar;\(target profit\)
  - contribution margin income statement / products & overall ::@:: per unit, total, percent; per unit is for products, and choose per unit, percent, or both
  - contribution margin income statement / row headers ::@:: sales revenue, less: variable costs, contribution margin, less: fixed costs, net operating income
  - contribution margin income statement / sub-formats ::@:: Only using overall gives the income statement under variable costing.

## incremental analysis (unit)

> __example__
>
> ---
>
> {@{__Incremental Analysis of the Special Order for 20 Special Units__}@}
>
> |                                            | {@{per unit}@}  | {@{total}@}       |
> | ------------------------------------------ | ---------------:| -----------------:|
> | {@{incremental revenue}@}                  | {@{&dollar;5}@} | {@{&dollar;100}@} |
> | {@{less: incremental costs}@}              |                 |                   |
> | &emsp;{@{direct materials}@}               | {@{\(1\)}@}     | {@{\(20\)}@}      |
> | &emsp;{@{direct labor}@}                   | {@{\(1\)}@}     | {@{\(20\)}@}      |
> | &emsp;{@{variable overhead}@}              | {@{\(1\)}@}     | {@{\(20\)}@}      |
> | &emsp;{@{fixed overhead}@}                 | {@{-}@}         | {@{-}@}           |
> | &emsp;{@{opportunity cost of lost sales}@} | {@{\(1\)}@}     | {@{\(20\)}@}      |
> | {@{total incremental costs}@}              | {@{\(4\)}@}     | {@{\(80\)}@}      |
> | {@{incremental profit \(loss\)}@}          | {@{&dollar;1}@} | {@{&dollar;20}@}  |

- incremental analysis \(unit\) ::@:: "incremental analysis of \(decision\)", column headers, row headers
  - incremental analysis \(unit\) / column headers ::@:: \(empty\), per unit, total
  - incremental analysis \(unit\) / row headers ::@:: incremental revenue, less: incremental costs \(subitems\), _total_ incremental costs, \(other costs and benefits\), incremental profit \(loss\)

## incremental analysis (comparative)

> __example__
>
> ---
>
> |                                | {@{option 1: keep in-house}@} | {@{option 2: outsourcing}@} | {@{difference: \(cost\) or benefit of outsourcing}@} |
> | ------------------------------ | -----------------------------:| ---------------------------:| ----------------------------------------------------:|
> | {@{revenue}@}                  | {@{&dollar;10}@}              | {@{&dollar;5}@}             | {@{&dollar;\(5\)}@}                                  |
> | {@{less:}@}                    |                               |                             |                                                      |
> | &emsp;{@{direct materials}@}   | {@{\(1\)}@}                   | {@{-}@}                     | {@{1}@}                                              |
> | &emsp;{@{direct labor}@}       | {@{\(1\)}@}                   | {@{-}@}                     | {@{1}@}                                              |
> | &emsp;{@{variable overhead}@}  | {@{\(1\)}@}                   | {@{-}@}                     | {@{1}@}                                              |
> | &emsp;{@{fixed overhead}@}     | {@{\(2\)}@}                   | {@{\(1\)}@}                 | {@{1}@}                                              |
> | {@{revenue from new service}@} | {@{-}@}                       | {@{2}@}                     | {@{2}@}                                              |
> | {@{net operating profit}@}     | {@{&dollar;5}@}               | {@{&dollar;6}@}             | {@{&dollar;1}@}                                      |

- incremental analysis \(comparative\) ::@:: column headers, row headers
  - incremental analysis \(comparative\) / column headers ::@:: \(empty\), option 1: \(description\), option 2: \(description\), difference: \(cost\) or benefit of \(option 2 description\)
  - incremental analysis \(comparative\) / row headers ::@:: incremental revenue, less: + subitems, \(other costs and benefits\), incremental profit \(loss\)

## incremental analysis (incremental)

> __example__
>
> ---
>
> |                                                |                          |
> | ---------------------------------------------- | ------------------------:|
> | {@{elimination of product A}@}                 |                          |
> | &emsp;{@{loss sales revenue}@}                 | {@{&dollar;\(100\)}@}    |
> | &emsp;{@{less: avoidable variable costs}@}     | {@{20}@}                 |
> | &emsp;{@{less: avoidable direct fixed costs}@} | {@{20}@}                 |
> | &emsp;{@{__lost segment margin__}@}            | {@{__&dollar;\(60\)__}@} |
> | {@{effect on product B}@}                      |                          |
> | &emsp;{@{increased sales}@}                    | {@{&dollar;100}@}        |
> | &emsp;{@{less: increased variable costs}@}     | {@{\(50\)}@}             |
> | &emsp;{@{__increased contribution margin__}@}  | {@{__&dollar;50__}@}     |
> | {@{__net effect eliminating product A__}@}     | {@{__&dollar;\(10\)__}@} |

- incremental analysis \(incremental\) ::@:: column headers, row headers
  - incremental analysis \(incremental\) / column headers ::@:: \(empty\), \(empty\)
  - incremental analysis \(incremental\) / row headers ::@:: main effect + subitems, \(side effects + subitems\), net effect

## constrained optimization using contribution margin

> __example__
>
> ---
>
> | {@{priority}@}                        | {@{1 large}@}    | {@{2 small}@}    | {@{3 medium}@}             |
> | ------------------------------------- | ----------------:| ----------------:| --------------------------:|
> | {@{contribution margin per kg}@}      | {@{&dollar;3}@}  | {@{&dollar;2}@}  | {@{&dollar;1}@}            |
> | {@{units produced}@}                  | {@{10}@}         | {@{20}@}         | {@{5}@}                    |
> | {@{raw materials required per unit}@} | {@{3&nbsp;kg}@}  | {@{1&nbsp;kg}@}  | {@{2&nbsp;kg}@}            |
> | {@{total required raw material}@}     | {@{30&nbsp;kg}@} | {@{20&nbsp;kg}@} | {@{10&nbsp;kg remaining}@} |
> | {@{total contribution margin}@}       | {@{&dollar;90}@} | {@{&dollar;40}@} | {@{&dollar;10}@}           |

- constrained optimization using contribution margin ::@:: column headers, row headers
  - constrained optimization using contribution margin / column headers ::@:: priority, \(items in decreasing priorities\)
  - constrained optimization using contribution margin / row headers ::@:: contribution margin per capacity or resource, units produced, capacity or resource required per unit, total required capacity or resource, total contribution margin
  - constrained optimization using contribution margin / note ::@:: Do not multiply contribution margin per capacity or resource by units produced to get total contribution margin! Multiply it by total required capacity or resouce instead.

## budget

> __example__
>
> ---
>
> {@{__Aether Company__}@} <br/>
> {@{__Budgeted Cash Payments__}@} <br/>
> {@{__For the Year Ended December 31, 2025__}@}
>
> |                                                           | {@{quarter 1 <br/> Jan–Mar}@} | {@{quarter 2 <br/> Apr–Jun}@} | {@{quarter 3 <br/> Jul–Sep}@} | {@{quarter 4 <br/> Oct–Dec}@} | {@{yearly <br/> total}@} |
> | --------------------------------------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- | ------------------------ |
> | {@{budgeted cost of direct materials purchases}@}         | {@{<u>&dollar;0</u>}@}        | {@{<u>&dollar;100</u>}@}      | {@{<u>&dollar;200</u>}@}      | {@{<u>&dollar;300</u>}@}      | {@{<u>&dollar;600</u>}@} |
> |                                                           |                               |                               |                               |                               |                          |
> | {@{cash paid during the quarter of purchase \(25%\)}@}    | {@{&dollar;0}@}               | {@{&dollar;25}@}              | {@{&dollar;50}@}              | {@{&dollar;75}@}              | {@{&dollar;150}@}        |
> | {@{cash paid in the quarter following purchase \(75%\)}@} | {@{<u>75</u>}@}               | {@{<u>0</u>}@}                | {@{<u>75</u>}@}               | {@{<u>150</u>}@}              | {@{<u>300</u>}@}         |
> | {@{cash paid for direct materials}@}                      | {@{&dollar;75}@}              | {@{&dollar;25}@}              | {@{&dollar;125}@}             | {@{&dollar;225}@}             | {@{&dollar;450}@}        |
> | {@{cash paid for direct labor}@}                          | {@{25}@}                      | {@{75}@}                      | {@{75}@}                      | {@{75}@}                      | {@{250}@}                |
> | {@{manufacturing overhead}@}                              | {@{10}@}                      | {@{20}@}                      | {@{30}@}                      | {@{40}@}                      | {@{100}@}                |
> | {@{less: depreciation \(non-cash expense\)}@}             | {@{\(100\)}@}                 | {@{\(100\)}@}                 | {@{\(100\)}@}                 | {@{\(100\)}@}                 | {@{\(400\)}@}            |
> | {@{cash paid for selling and administrative expenses}@}   | {@{40}@}                      | {@{30}@}                      | {@{20}@}                      | {@{10}@}                      | {@{100}@}                |
> | {@{cash paid for equipment \(capex\)}@}                   | {@{<u>100</u>}@}              | {@{<u>0</u>}@}                | {@{<u>100</u>}@}              | {@{<u>100</u>}@}              | {@{<u>300</u>}@}         |
> | {@{budgeted cash payments}@}                              | {@{<u>&dollar;150</u>}@}      | {@{<u>&dollar;50</u>}@}       | {@{<u>&dollar;250</u>}@}      | {@{<u>&dollar;350</u>}@}      | {@{<u>&dollar;800</u>}@} |

- budget ::@:: headers, column headers, row headers, format
  - budget / headers ::@:: \(company name\), \(budget name\), \(duration, e.g. "For the Year Ended December 31, 2025"\)
  - budget / columns headers ::@:: \(duration segments, e.g. "Quarter 1 \(newline\) Jan–Mar"\), \(duration, e.g. "Yearly \(newline\) Total"\)
  - budget / row headers ::@:: Many items. A total at the end. Indent as needed.
  - budget / format ::@:: Dollar signs \(&dollar;\) for the first rows, subtotals, and the total. For subtotals and the total, add a line above them. For the total, double underline it.
  - budget / no information ::@:: If there are no information for some numbers, just indicate them as blank. Derive as much numbers as possible, up until derived numbers that depend on missing numbers. <p> The yearly total is likely not applicable with missing data, e.g. halfway through a year.

## delayed cash receipts or payments

> __example__
>
> ---
>
> |                              | {@{cash collected in Mar}@}                          | {@{cash collected in Apr}@}                          |
> | ---------------------------- | ----------------------------------------------------:| ----------------------------------------------------:|
> | {@{sales in Jan}@}           | {@{&dollar;200<br/>\(&dollar;1&nbsp;000×80%×25%\)}@} |                                                      |
> | {@{sales in Feb}@}           | {@{&dollar;300<br/>\(&dollar;500×80%×75%\)}@}        | {@{&dollar;100<br/>\(&dollar;500×80%×25%\)}@}        |
> | {@{sales in Mar}@}           | {@{&dollar;200<br/>\(&dollar;1&nbsp;000×20%\)}@}     | {@{&dollar;600<br/>\(&dollar;1&nbsp;000×80%×75%\)}@} |
> | {@{sales in Apr}@}           |                                                      | {@{&dollar;500<br/>\(&dollar;2&nbsp;500×20%\)}@}     |
> | {@{total cash collections}@} | {@{&dollar;700}@}                                    | {@{&dollar;1&nbsp;200}@}                             |

- delayed cash receipts or payments ::@:: column headers, row headers
  - delayed cash receipts or payments / column headers ::@:: \(empty\), cash collected/paid in \(time\)...
  - delayed cash receipts or payments / row headers ::@:: sales/purhcases in \(time\)..., total cash collections/payments

## standard cost card

> __example__
>
> ---
>
> | {@{manufacturing costs}@}                            | {@{standard quantity}@} | {@{standard price/rate}@} | {@{standard unit cost}@}    |
> | ---------------------------------------------------- | -----------------------:| -------------------------:| ---------------------------:|
> | {@{direct materials \(steel\)}@}                     | {@{0.1 tons per unit}@} | {@{&dollar;999 per ton}@} | {@{&dollar;99.90}@}         |
> | {@{direct labor}@}                                   | {@{24 hrs per unit}@}   | {@{&dollar;25 per hr}@}   | {@{600.00}@}                |
> | {@{variable overhead \(60% of direct labor cost\)}@} | {@{24 hrs per unit}@}   | {@{&dollar;15 per hr}@}   | {@{360.00}@}                |
> | {@{fixed overhead \(&dollar;100/2 units\)}@}         |                         |                           | {@{50.00}@}                 |
> | {@{standard manufacturing cost per unit}@}           |                         |                           | {@{&dollar;1&nbsp;109.90}@} |

- standard cost card ::@:: column headers, row headers
  - standard cost card / column headers ::@:: manufacturing costs, standard quantity, standard price/rate, standard unit cost
  - standard cost card / row headers ::@:: direct materials, direct labor, variable overhead, fixed overhead, standard manufacturing cost per unit
