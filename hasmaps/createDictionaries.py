import re

def grade_by_keyword_density(answer_text, required_keywords, ideal_density_range=(1, 3)):
    # 1. Text Preprocessing: convert to lowercase and remove punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', answer_text).lower()
    words = cleaned_text.split()
    total_words = len(words)
    
    if total_words == 0:
        return 0, "Empty answer."

    # 2. Count occurrences of each required keyword
    # Use a set for efficient checking if a word is a keyword
    keyword_set = set(k.lower() for k in required_keywords)
    matched_counts = {}
    for word in words:
        if word in keyword_set:
            matched_counts[word] = matched_counts.get(word, 0) + 1

    # 3. Calculate total keyword occurrences and density
    total_keyword_occurrences = sum(matched_counts.values())
    # Formula: (Number of keyword occurrences / Total word count) * 100
    density = (total_keyword_occurrences / total_words) * 100

    # 4. Assign a score/grade based on density
    score = 0
    feedback = f"Total words: {total_words}. Keyword occurrences: {total_keyword_occurrences}. Density: {density:.2f}%."

    if ideal_density_range[0] <= density <= ideal_density_range[1]:
        score = 100
        feedback += " Ideal density achieved."
    elif density > ideal_density_range[1]:
        # Penalize for keyword stuffing
        score = max(0, 100 - (density - ideal_density_range[1]) * 10) 
        feedback += " Density too high (possible keyword stuffing)."
    else:
        # Lower score for insufficient density
        score = max(0, density * (100 / ideal_density_range[0])) # Scale score based on target
        feedback += " Density too low."

    return score, feedback

# Example Usage:
answer = "Machine learning is a field of study that uses statistical techniques to give computer systems the ability to 'learn' with data. It is a core component of AI."
keywords = ["machine learning", "statistical techniques", "AI", "computer systems"]

# This basic method works best with single word keywords.
# For multi-word keywords like "machine learning" you would need more advanced NLP techniques (see Method 2).
score, feedback = grade_by_keyword_density(answer, ["machine", "learning", "statistical", "techniques", "AI", "computer", "systems"])

print(f"Score: {score}")
print(f"Feedback: {feedback}")
