# PAISS18
NLE practical session for [PAISS 2018](https://project.inria.fr/paiss/)

## Installation

This code requires Python 3 and Pytorch 0.4. Follow the instructions below to install all the necessary dependencies.

### Linux / MacOS

First, download and install the appropriate version of miniconda following the instructions for [MacOS](https://conda.io/docs/user-guide/install/macos.html) or [Linux](https://conda.io/docs/user-guide/install/linux.html).

Then run the following commands:

```
source $HOME/miniconda3/bin/activate #Activates your conda environment
conda install numpy matplotlib ipython scikit-learn jupyter
conda install pytorch torchvision 
```

### Windows

Install anaconda on windows (launch .exe file downloaded from the [conda website](https://conda.io/docs/user-guide/install/windows.html)). It has to be python 3 (pytorch doesn’t support 2.7 on windows)

In the anaconda prompt, run:

```
conda create -n pytorch
activate pytorch
conda install pytorch-cpu -c pytorch
pip install torchvision --no-deps
conda install pillow
conda install jupyter
```

## Downloading the code, dataset, and models

First, clone this repository:

```
cd $HOME/my_projects
git clone https://github.com/rafarez/paiss.git
```

Then, you will need to download 3 files:

- oxbuild_images.tgz (1.8GB)
- gt\_files\_170407.tgz (280KB)
- features.tgz (311MB)

and store them in the appropriate paths.

_Note:_ All paths in this section are relative to the root directory of this repository.

**Oxford dataset**

On Linux/MacOS, execute the following:

```
cd $HOME/my_projects/paiss
wget www.robots.ox.ac.uk/~vgg/data/oxbuildings/oxbuild_images.tgz -O images.tgz
mkdir -p data/oxford5k/jpg && tar -xzf images.tgz -C data/oxford5k/jpg
wget www.robots.ox.ac.uk/~vgg/data/oxbuildings/gt_files_170407.tgz -O gt_files.tgz
mkdir -p data/oxford5k/lab && tar -xzf gt_files.tgz -C data/oxford5k/lab
```

On Windows, perform the following:

- Download www.robots.ox.ac.uk/~vgg/data/oxbuildings/oxbuild_images.tgz
- create directory `data/oxford5k/jpg/`
- uncompress oxbuild_images.tgz and store in `data/oxford5k/jpg/`
- Download www.robots.ox.ac.uk/~vgg/data/oxbuildings/gt_files_170407.tgz
- create directory `data/oxford5k/lab/`
- uncompress gt\_files\_170407.tgz and store in `data/oxford5k/lab/`

**Features**

On Linux/MacOS, execute the following:

```
cd $HOME/my_projects/paiss
wget https://www.dropbox.com/s/ilnow86hdvxle1k/features.tgz?dl=0 -O features.tgz
tar -xzf features.tgz -C data
```

On Windows, perform the following:

- Download https://www.dropbox.com/s/ilnow86hdvxle1k/features.tgz?dl=0
- Uncompress features.tgz and store in `data/`


## Notebook
Execute:
```
source $HOME/miniconda3/bin/activate
cd $HOME/my_projects/paiss
jupyter notebook --ip='localhost' --port=8080 --NotebookApp.token=''
```
On a browser, open localhost:8080/ and click Tutorial.ibnpy to open a new tab with the notebook.
