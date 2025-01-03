import argparse
import sys
import os
from torch.utils.data import DataLoader
sys.path.append(os.getcwd())
from rerankai import datasets, models
from rerankai.utils import *

query = "query"
docs = ["doc1", "doc2", "doc3"]

def main(args):
    config = load_config(args.model_config_path)
    """ get net struction """
    net = models[config["model_type"]](**config["model"])
    net.load_pretrained(config["logging"]["save_dir"])

    """ rerank """
    scores = net.rerank(query, docs)
    print(scores)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_config_path",type=str,default = "config/rerank.yml")
    args = parser.parse_args()
    main(args)
