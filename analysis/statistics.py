def compute_category_averages(data):
    result = {}
    for item in data:
        cat = item["category"]
        if cat not in result:
            result[cat] = []
        result[cat].append(item["price"])
    
    for cat in result:
        result[cat] = sum(result[cat]) / len(result[cat])
    return result

def get_most_expensive(data):
    sorted_data = sorted(data, key=lambda x: float(x["price"]), reverse=True)
    return sorted_data[0]
