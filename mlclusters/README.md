# mlclusters

The mlclusters is a tool to visualize ddRAD(Double Digest Restriction Associated DNA) assemblies in geno format using clustering methods available in [Scikit Learn](http://scikit-learn.org/stable/index.html). 

This library is still under development. Currently, only KMeans clustering method is available, however other clustering methods will be available in the near future. For more information, please visit [Scikit Learn KMeans clustering method](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html). Input assembly files need to be in geno format, which can be obtained using [ipyrad] (http://ipyrad.readthedocs.io/outline.html).

Please refer the notebook: mlclusters_nb_simulated_data.ipynb for demonstration of the library usedj with a generated data. 


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