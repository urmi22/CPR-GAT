
## Anonymous code repository for CPR-GAT

1. Clone the repository.
2. Download GloVe version glove.6B.300d.txt and put this file path in the glove_path variable in feature.py file.
3. Change directory to the CPR-GAT folder `cd CPR-GAT`.
4. To create feature vector for node and edges, navigate to the MOOC-DSA using `cd MOOC-DSA` and run `python3 feature.py` to create feature vector.
5. For training and inference, from the model folder, navigate to the MOOC-DSA using `cd ../model` and run `python3 feature.py` execute gat-model.py.
