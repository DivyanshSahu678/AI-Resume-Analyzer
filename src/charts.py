import matplotlib.pyplot as plt


def create_skill_pie_chart(matched, missing):

    labels = ["Matched Skills", "Missing Skills"]

    values = [len(matched), len(missing)]

    fig, ax = plt.subplots(figsize=(5,5))

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Skill Match Analysis")

    return fig

def create_bar_chart(matched, missing):

    labels = ["Matched", "Missing"]

    values = [len(matched), len(missing)]

    fig, ax = plt.subplots()

    ax.bar(labels, values)

    ax.set_ylabel("Skills")

    ax.set_title("Matched vs Missing Skills")

    return fig