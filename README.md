# Learning-Anti-Patterns
data and scripts used for the experiment we executed in the Onto.Com 2021 paper 

## Quickstart Guide 
Install python 3.x.

Install the following libraries:

```bash
$ pip install networkx
$ pip install matplotlib.pyplot
$ pip install regex
$ pip install pandas
$ pip install pygraphviz
```
Install [RapidMiner](https://rapidminer.com/) free version.

Run the the [gufo2alloy](https://github.com/OntoUML/gufo2alloy) converter to generate [Alloy](https://alloytools.org/) `.als` specifications (see [related model](https://github.com/unibz-core/ConstraintLearning/tree/main/model) examples). 

Customize the simulations scope. Run simulations. Save the output simulations into `.DOT` files.

Copy any generated anti-pattern occurrence `.DOT` into a `.txt` file (see example file `car-binover-proc.txt`). Then execute the following steps:

1. Use the anti-pattern occurrence (`.txt` format) as input of `generalize-pattern.py` in [scritpts](https://github.com/unibz-core/Learning-Anti-Patterns/tree/main/scripts)

2. Use all the outputs of 1. to generate an example set like `examples.xlsx`.

3. Give `examples.xlsx` as input of `embedding+clustering.xml` in [scritpts](https://github.com/unibz-core/Learning-Anti-Patterns/tree/main/scripts) - this is necessary to embed, bootstrap, evaluate, cluster and extract the clusters prototypes as described in the paper.

4. To generate the generalized anti-pattern give the output of 1. to `generate-dot.py` and then to `visualize-graph.py`.
