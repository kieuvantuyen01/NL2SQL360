from engine.engine import Engine
from dataset.dataset_builder import SpiderDataset, BirdDataset
import os

if __name__ == "__main__":
    db_url = "sqlite:///data/storage/hypersql_new.sqlite"
    engine = Engine(db_url)
    
    spider_dataset = SpiderDataset("data/dataset")
    # engine.create_dataset_table(spider_dataset, "dev")
    # raw_data = spider_dataset.get_raw_data("dev")
    # engine.insert_dataset_table(spider_dataset, "dev", raw_data)
    
    # engine.create_dataset_table(spider_dataset, "train")
    # raw_data = spider_dataset.get_raw_data("train")
    # engine.insert_dataset_table(spider_dataset, "train", raw_data)
    
    # pred_files = os.listdir("data/predict/spider")
    
    # for pred_file in pred_files:
    #     with open(os.path.join("data/predict/spider", pred_file), "r") as f:
    #         preds = [line.strip().split("\t")[0] for line in f.readlines()]
    #     eval_name = pred_file.split(".")[0]
    #     engine.insert_evaluation_table(spider_dataset, "dev", eval_name, preds)
    
    # bird_dataset = BirdDataset("data/dataset")
    # engine.create_dataset_table(bird_dataset, "dev")
    # raw_data = bird_dataset.get_raw_data("dev")
    # engine.insert_dataset_table(bird_dataset, "dev", raw_data)
    
    # engine.create_dataset_table(bird_dataset, "train")
    # raw_data = bird_dataset.get_raw_data("train")
    # engine.insert_dataset_table(bird_dataset, "train", raw_data)
    
    # pred_files = os.listdir("data/predict/bird")
    
    pred_files = ["pretrained_codellama_7b.txt", "pretrained_llama2_7b.txt", "pretrained_starcoder_7b.txt", "pretrained_deepseek_coder_7b.txt"]
    
    for pred_file in pred_files:
        with open(os.path.join("data/predict/spider_dev", pred_file), "r", encoding="utf-8") as f:
            preds = [line.strip().split("\t")[0] for line in f.readlines()]
        eval_name = pred_file.split(".")[0]
        engine.insert_evaluation_table(spider_dataset, "dev", eval_name, preds)