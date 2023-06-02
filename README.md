
## Anonymous code repository for CPR-GAT

1. Clone the repository.
2. Create the environment from the `environment.yml` file using `conda env create -f environment.yml` command.
2. Download GloVe using `wget http://nlp.stanford.edu/data/glove.6B.zip` command.
3. Unzip the glove6B.zip using `unzip glove*.zip` command.
3. Use this file (glove.6B.300d.txt) or file path in the glove_path variable in feature.py file.
3. Change your current directory to the CPR-GAT folder using `cd CPR-GAT` command and all the code from this folder.
4. To create feature vector for node and edges, run `python3 MOOC-DSA/feature/extreme-value-feature/feature.py` file.
5. For training and inference, run `python3 MOOC-DSA/model/gat-model.py` file.
