def generate_suggestions(missing_skills):

    suggestions = []

    skill_suggestions = {
        "react": "Learn React and build at least one frontend project.",
        "machine learning": "Study Machine Learning fundamentals and create one ML project.",
        "tensorflow": "Learn TensorFlow for Deep Learning applications.",
        "pytorch": "Learn PyTorch and implement neural networks.",
        "sql": "Improve SQL by practicing joins, subqueries, and indexing.",
        "git": "Learn Git branching, merging, and GitHub collaboration.",
        "github": "Upload your projects to GitHub with proper README files.",
        "html": "Strengthen HTML semantic tags and forms.",
        "css": "Practice responsive design using Flexbox and Grid.",
        "javascript": "Improve JavaScript ES6 concepts and DOM manipulation.",
        "python": "Practice Python with real-world automation and data analysis projects."
    }

    for skill in missing_skills:
        skill = skill.lower()

        if skill in skill_suggestions:
            suggestions.append(skill_suggestions[skill])

    if len(suggestions) == 0:
        suggestions.append("Excellent! Your resume matches the required skills.")

    return suggestions