import pandas as pd
import numpy as np
from bs4 import BeautifulSoup, element
# Load AR-ASAG DataSet XML-Moodle Version.
pathXML = "MoodleXML- Questions - Student  Answers - Average Gold.xml"


soup: BeautifulSoup
with open(pathXML, "r") as xml:
    soup = BeautifulSoup(xml, features="xml")

questionTag = soup.find_all("Question")
questionTextDic = {}
questionTextList = []
answers = []
for q in questionTag:
    questionTextDic[q.questiontext.text] = []
    questionTextList.append(q.questiontext.text)
    answerTag = q.find_all("answer")
    answers.append(answerTag)

# To Dictionary :
for index, q in enumerate(questionTextList):
    for answer in answers[index]:
        questionTextDic[q].append([answer.text, answer.attrs["fraction"]])

# To CSV:
all = []
for index, q in enumerate(questionTextList):
    for answer in answers[index]:
        all.append(
            [
                index + 1,
                q.replace("\n", ""),
                answer.text.replace("\n", ""),
                float(answer.attrs["fraction"]),
            ]
        )
df = pd.DataFrame(all, columns=["NumQuestion", "Question", "Answer", "Degree"])
print(df.head())
df.to_excel("data.xlsx", index=False)
