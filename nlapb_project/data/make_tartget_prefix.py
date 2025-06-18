# import pandas as pd
# import os

# # 데이터 로드
# input_path = "ndn_prefix_dataset.csv"
# df = pd.read_csv(input_path)

# # 출력 디렉토리 설정
# output_dir = "ndn_prefix_subsets"
# os.makedirs(output_dir, exist_ok=True)

# # 1M ~ 10M 행 기준으로 나눠서 저장
# subset_paths = []
# for i in range(1, 11):
#     subset = df.iloc[:i * 1_000_000]
#     output_path = os.path.join(output_dir, f"ndn_prefix_{i}M.txt")
#     subset.to_csv(output_path, index=False)
#     subset_paths.append(output_path)

# import ace_tools as tools; tools.display_dataframe_to_user(name="Subset Files (1M~10M)", dataframe=pd.DataFrame({"Subset Path": subset_paths}))

###########################################################################################################################################################33
# import os
# import pandas as pd

# # ndn_prefix_subsets 경로에서 1M~10M csv 파일의 prefix 열만 추출하는 작업
# subset_dir = "ndn_prefix_subsets"
# output_dir = "ndn_prefix_subset_txts"
# os.makedirs(output_dir, exist_ok=True)

# # 파일 생성 루프
# for i in range(1, 11):
#     csv_path = os.path.join(subset_dir, f"ndn_prefix_dataset_{i}M.csv")
#     txt_path = os.path.join(output_dir, f"lookup_targets_{i}M.txt")
    
#     if os.path.exists(csv_path):
#         df = pd.read_csv(csv_path)
#         if 'prefix' in df.columns:
#             prefixes = df['prefix'].dropna().unique()
#             with open(txt_path, "w", encoding="utf-8") as f:
#                 for p in prefixes:
#                     f.write(p + "\n")
###########################################################################################################################################################33
import random
import os

# 저장 설정
OUTPUT_DIR = "data/ndn_prefix_datasets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 컴포넌트 풀 정의
domain_pool = ["com", "org", "net", "jp", "io", "ae", "be", "store", "club", "lv"]
subdomain_pool = [
    "google", "facebook", "yoshizawa-gama", "ahnlab", "easynews", "neapay",
    "go-tou", "taxadmin", "dr-procedures", "ganaencasa20", "bungeesleeves", "limitededt"
]
component_pool = [
    "page", "img", "news", "data", "photo", "doc", "id", "section", "blog",
    "main", "2025", "x", "1", "2", "3", "a", "b", "top", "idx"
]

# prefix 생성 함수
def generate_realistic_prefix():
    depth = random.randint(4, 6)  # 도메인 포함 전체 depth
    components = [
        random.choice(domain_pool),
        random.choice(subdomain_pool)
    ]
    for _ in range(depth - 2):
        base = random.choice(component_pool)
        suffix = random.choice(["", "1", "2", "3", "a", "b", "x", "2025", "main"])
        components.append(base + suffix)
    return "/" + "/".join(components)

# 몇 M개를 생성할지 리스트로 지정
target_sizes = [2_000_000, 3_000_000, 4_000_000]

for count in target_sizes:
    filename = os.path.join(OUTPUT_DIR, f"ndn_prefix_dataset_{count//1_000_000}M.txt")
    print(f"🔄 {count:,}개 prefix 생성 중 → {filename}")
    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(count):
            f.write(generate_realistic_prefix() + "\n")
    print(f"✅ 저장 완료: {filename}")

