
    # חשוב לזכור להחליף את pass ב- return

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
def normalized_array(input_array):
    data = np.array(input_array)
    
    # בדיקה האם כל האיברים במערך זהים כדי למנוע חילוק באפס
    if np.all(data == data[0]):
        return np.zeros(data.shape)
    else:
        # חישוב נורמליזציה (Min-Max Scaling)
        new_array = (data - np.min(data)) / (np.max(data) - np.min(data))
        
    return new_array
