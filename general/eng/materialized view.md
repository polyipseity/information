---
aliases:
  - materialized view
  - materialized views
  - view materialization
  - view materializations
tags:
  - flashcard/active/general/eng/materialized_view
  - language/in/English
---

# materialized view

## algorithms

In a database, there are usually {@{many possible views to materialize}@}. But it is {@{not practical to materialize them all because of practical constraints}@}, such as {@{the number of views, the total size of views, the update cost, etc.}@} Selecting the best views that {@{reduces the cost of answering queries while staying within the constraints}@} is known as {@{the view materialization problem}@}. It is {@{[NP-complete](NP-completeness.md)}@}. A variety of [algorithms](materialized%20view.md#algorithms) have been explored, such as {@{[greedy algorithms](#greedy%20algorithm), randomized search, [genetic algorithms](genetic%20algorithm.md), and [A* search algorithm](A*%20search%20algorithm.md)}@}.

### terminology

Let $\top$ be {@{the top view, i.e. the unaggregated view containing all transactions}@}. Let $\bot$ be {@{the bottom view, i.e. the view containing one transaction aggregating all transactions}@}. Each view $v$ is {@{associated with a real number called the cost $v_c$, with $\top_c$ being the total number of transactions and $\bot_c = 1$}@}. The view cost $v_c$ can be considered as {@{the cost of answering an query using said view $v$}@}.

A view $v$ is the parent of another $v'$ if {@{every query that we care about that are answerable by $v'$ is also answerable by $v$}@}. For example, a table containing parts, suppliers, and costs {@{can answer queries answerable by a table containing parts and costs only or a table containing suppliers and cost only}@}. Note that the above parent—child relation is dependant on the queries that we care about. So the example above might only works for some queries. $\top$ is {@{the common ancestor of all views excluding itself}@}, and $\bot$ is {@{the common children of all views excluding itself}@}. The relations for a set of views can be {@{visualized as a graph, along with the view costs}@}.

> [!example] visualizing relations between a set of views
>
> Each alphabet represents {@{a transaction property}@}. "p" represents product, "s" represents supplier, and "c" represents cost. "psc" is the {@{top view $\top$}@}, while "none" is the {@{bottom view $\bot$}@}.
>
> An {@{graph of relations between a set of views}@} is as below:
>
> ![relations between a set of views, dense](attachments/materialized%20view%20-%20data%20cube%20-%20dense.png)
>
> Of course, each view in the graph {@{does not need to connect every possible subset}@}:
>
> ![relations between a set of views, sparse](attachments/materialized%20view%20-%20data%20cube%20-%20sparse.png)

The cost of answering a query depends on {@{the view (materialized or not) to be queried against and the views materialized}@}. First, identify the {@{least costly view (materialized or not) required to answer the query}@}, and then find the {@{least costly (direct or indirect) parent view that is materialized}@}, and its {@{associated cost is the cost of answering said query}@}.

### greedy algorithm

We assume that {@{each view is equally likely to be queried}@}. We also assume the top view $\top$ {@{is materialized}@}, and the bottom view $\bot$ {@{is ignored and assumed does not exist}@}.

Let $S$ be {@{the set of materialized views}@}. Define the total cost function {@{accepting a set of materialized views $C(S)$ as the total cost of accessing each possible views once, taking the materialized views into consideration}@}. Next, define the gain {@{$G(A, B)$ accepting 2 sets of materialized views, as $G(A, B) = C(B) - C(A)$, i.e. the total cost reduction of materializing $A$ over materializing $B$}@}. Finally, define the benefit {@{$B(v, S) = G(S \cup \set{v}, S)$, i.e. the total cost reduction of _additionally_ materializing $v$ over only materializing $S$}@}.

The objective is to {@{find the best $S$ that maximizes the gain $G(S, \set{\top})$ over the top view, while satisfying the given constraints}@}. The constraints we will consider here are {@{the maximum number of materialized views or the max total cost of materialized views}@}. The constraints are considered separately.

The pseudocode is as follows:

1. initialization ::@:: Initialize $S$ to consist of the top view $\top$ only.
2. looping condition ::@:: The looping condition depends on the constraint. For example, loop while the number of materialized views has not exceeded the limit. Another example is, loop while there exists an view not in $S$ such that materializing the view does not make the total cost of materialized views exceed the limit. Go to step 5 if the loop stops.
3. selection with heuristic ::@:: Select an view not in $S$ such that the constraint is respected while maximizing a specific heuristic function. The heuristic function also depends on the constraint. For example, the heuristic function can be the benefit $B(v, S)$ of materializing the view if the number of materialized views is limited. Another example is, the benefit per view cost $B(v, S) / c_v$ of materializing the view if the total cost of materialized views is constrained.
4. update ::@:: Add the view to $S$. Go to step 2.
5. results ::@:: $S$ is the resulting view selection.

To run the above algorithm manually, we can use {@{a benefit table with row headers being the possible views to materialize and column headers being the _n_-th choice}@}. Fill in the benefit table from {@{left to right, with advancing one column representing choosing one more view}@}. When a view is selected, there is {@{no need to further calculate its benefit (or an alternative heuristic function) in subsequent columns}@}. Calculate the benefit {@{with reference to the graph of relations between a set of views earlier}@}. On completing an column, {@{the view with the most benefit is selected}@}.

In details, when calculating the benefit for a view to be materialized, only consider {@{the (direct and indirect) children of the view}@}. For each considered child, find {@{the least costly (direct or indirect) parent view that is already materialized}@}. Then, compare {@{it to the new view to be materialized}@}. If {@{the new view is more costly}@}, then {@{the benefit for that child is 0}@}. Otherwise, {@{the benefit for that child is the difference in cost}@}. Finally, the benefit of materializing that view is {@{the sum of all benefits for each individual child}@}.

> [!examples] benefit table example
>
> A {@{benefit table}@} example as below, using the 1st graph of relations between a set of views earlier:
>
> |    | 1st choice (M)     | 2nd choice (M)    |
> | -- | ------------------ | ----------------- |
> | pc | 0 × 3 = 0          | 0 × 2 = 0         |
> | ps | 5.2 × 3 = __15.6__ | N/A               |
> | sc | 0 × 3 = 0          | 0 × 2 = 0         |
> | p  | 5.8 × 1 = 5.8      | 0.6 × 1 = 0.6     |
> | s  | 5.99 × 1 = 5.99    | 0.79 × 1 = 0.79   |
> | c  | 5.9 × 1 = 5.9      | 5.9 × 1 = __5.9__ |
>
> The above benefit table shows that the resulting greedy selection is {@{"ps" and _then_ "c"}@}.

The resulting selection is {@{greedy and may not be the optimal solution}@}. When {@{the heuristic function is simply the benefit}@}, the above problem is {@{a [submodular set function maximization](submodular%20set%20function.md#submodular%20set%20function%20maximization) problem}@}. In this case, it has been proven that the greedy selection {@{has a benefit that is at least $1 - 1 / e \approx 0.632$ times of that of the optimal selection}@}.<sup>[\[1\]](#^ref-Nemhauser-1978)</sup>

## references

This text incorporates [content](https://en.wikipedia.org/wiki/materialized_view) from [Wikipedia](Wikipedia.md) available under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

1. Nemhauser, G.L., Wolsey, L.A., & Fisher, M.L. (1978). ["An analysis of approximations for maximizing submodular set functions—I"](https://researchgate.net/publication/242914003). _Mathematical Programming_. __14__ (1): 265-294. [doi](doi%20(identifier).md):[10.1007/BF01588971](https://doi.org/10.1007%2FBF01588971). [S2CID](S2CID%20(identifier).md) [206800425](https://api.semanticscholar.org/CorpusID:206800425). <a id="^ref-Nemhauser-1978"> ^ref-Nemhauser-1978
