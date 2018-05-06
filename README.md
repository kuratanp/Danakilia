# mlclusters

The mlclusters is a tool to visualize ddRAD (Double Digest Restriction Associated DNA) assemblies in geno format using clustering methods available in [scikit-learn](http://scikit-learn.org/stable/index.html). 

This library is still under development. Currently, only [KMeans clustering method](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) is available, however other clustering methods will be available in the near future. Input assembly files need to be in geno format, which can be obtained using [ipyrad](http://ipyrad.readthedocs.io/outline.html).

Please refer the notebook: mlclusters_nb_simulated_data.ipynb to see a demonstration of the library used with a generated data. 

#### _In Development_

One of the problems with clustering methods is how to handle missing data. In the case in PCA clustering methods, missing data are often treated as 0 (homozygous) which may skew results. However, using scikit-learn we can cluster data with "missing data" instead of assigning 0. I am currently working on comparing those two methods. You can visit my notebook (Missing_data.ipynb) to see my progress.


### Installation

```
## clone the repo 
git clone [...]  

## cd into repo dir 
cd intro-ml  

## local development install with pip 
pip install -e . 
```

### Usage

See notebooks/ directory.
