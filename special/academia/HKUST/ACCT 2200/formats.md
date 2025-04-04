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
