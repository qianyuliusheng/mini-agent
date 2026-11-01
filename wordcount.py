import os

def count_words(filepath):
    if not os.path.exists(filepath):
        print(f"文件不存在: {filepath}")
        return

    word_counts = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                # 去掉标点符号
                word = word.strip(".,!?\"'()[]{}")
                if word:
                    word_counts[word] = word_counts.get(word, 0) + 1

    # 按照词频排序
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    print(f"--- 文件 {filepath} 词频统计前10 ---")
    for word, count in sorted_words[:10]:
        print(f"{word}: {count}次")

if __name__ == "__main__":
    # 创建一个测试文件并写入内容
    test_file = "test.txt"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("Hello world! This is a test. Hello agent, hello world.")
    
    # 运行统计
    count_words(test_file)