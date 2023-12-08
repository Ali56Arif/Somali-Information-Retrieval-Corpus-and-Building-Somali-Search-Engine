#Calculating the performance of the Somali IR evaluation system.
def calculate_metrics(retrieved_relevant, total_retrieved, total_relevant):
    precision = retrieved_relevant / total_retrieved
    recall = retrieved_relevant / total_relevant if total_relevant > 0 else 0
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return precision, recall, f1_score
#our Som-IR main function
def main():
    retrieved_relevant = 0
    total_retrieved = 0
    total_relevant = 0

    # Read the lists of retrieved and relevant files
    with open('TF-IDF-Evaluation', 'r') as retrieved_file:
        retrieved_files = set(retrieved_file.read().splitlines())

    with open('Judgements', 'r') as relevant_file:
        relevant_files = set(relevant_file.read().splitlines())

    # Calculate retrieved relevant, total retrieved, and total relevant files
    retrieved_relevant = len(retrieved_files.intersection(relevant_files))
    total_retrieved = len(retrieved_files)
    total_relevant = len(relevant_files)

    # Calculate precision, recall, and F1-score
    precision, recall, f1_score = calculate_metrics(retrieved_relevant, total_retrieved, total_relevant)

    if total_relevant == 0:
        print("No relevant files.")
    elif retrieved_relevant == 0:
        print("No match between the files.")
    else:
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1-Score:", f1_score)

if __name__ == "__main__":
    main()
