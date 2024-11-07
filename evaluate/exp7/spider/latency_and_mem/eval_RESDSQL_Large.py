import time
import torch

def load_queries_from_sql(file_path):
    with open(file_path, 'r') as f:
        sql_content = f.read()
    queries = [query.strip() for query in sql_content.split(';') if query.strip()]
    return queries

def evaluate_method_from_file(sql_file_path):
    queries = load_queries_from_sql(sql_file_path)
    latencies = []
    gpu_memories = []
    ex_index_results = []
    
    for query in queries:
        torch.cuda.empty_cache()
        mem_before = torch.cuda.memory_allocated()
        start_time = time.time()
        generated_query = model.predict(query)  # Replace with actual C3SQL prediction function
        end_time = time.time()
        mem_after = torch.cuda.memory_allocated()
        latency = end_time - start_time
        memory_used = mem_after - mem_before
        latencies.append(latency)
        gpu_memories.append(memory_used)
        ex_index = calculate_ex_index(generated_query, query)  # Replace with actual EX index calculation
        ex_index_results.append(ex_index)
    
    avg_latency = sum(latencies) / len(latencies)
    avg_memory_usage = sum(gpu_memories) / len(gpu_memories) / (1024**2)
    avg_ex_index = sum(ex_index_results) / len(ex_index_results)
    
    print(f"Average Latency: {avg_latency:.4f} seconds")
    print(f"Average GPU Memory Usage: {avg_memory_usage:.2f} MB")
    print(f"Average EX Index: {avg_ex_index:.4f}")

sql_file_path = "/home/hung1832001nb/NL2SQL360/tests/predict_sqls/spider_dev/resdsql_text2sql_large.sql"
evaluate_method_from_file(sql_file_path)

