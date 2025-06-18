import sys, os, time, random
import pandas as pd
import matplotlib.pyplot as plt
import tracemalloc

# 외부 경로 지정 및 import
src_dir = "src"
data_csv = "data/ndn_prefix_dataset_5K.csv"
if src_dir not in sys.path:
    sys.path.append(src_dir)

from nlapb import NLAPB  # NLAPB 클래스는 반드시 'trie' 속성 가져야 
from analysis_tools import (
    export_encoding_table,
    visualize_trie_nodes,
    save_hash_table_to_csv,
    save_hash_table_to_txt,
    export_cbf_to_csv
)



### 메인 함수
def main():
    # CSV 로딩 (prefix, face)
    df = pd.read_csv(data_csv)
    if "prefix" in df.columns and "face" in df.columns:
        prefix_face_pairs = list(zip(df["prefix"], df["face"]))
    else:
        # fallback: 단일 열일 경우 랜덤 face 부여
        prefix_face_pairs = [(p, f"face{random.randint(1,5)}") for p in df.iloc[:, 0].dropna().tolist()]

    # 엔진 초기화 및 삽입
    engine = NLAPB(t=3)
    start_insert = time.time()
    for prefix, face in prefix_face_pairs:
        engine.insert(prefix, face)
    insert_time = time.time() - start_insert
    print(f"Insertion time: {insert_time:.4f} seconds")

    ### 삽입 결과 시각화 ###
    export_encoding_table(engine.trie_nodes, path="encoding_table.csv")
    save_hash_table_to_csv(engine.hash_table, path="hash_table.csv")
    save_hash_table_to_txt(engine.hash_table, path="hash_table.txt")
    visualize_trie_nodes(engine.trie_nodes, path="trie_nodes.txt")
    export_cbf_to_csv(engine.cbf_dict, path_prefix="cbf_array")

# 실행 진입점
if __name__ == "__main__":
    main()
