from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from PySide6 import QtCore, QtWidgets
import datetime
import sys
import os
import shutil
import re
import json
import requests
import usage

pattern = r"^https://leetcode\.com/problems/.+/"

# https://leetcode.com/problems/add-two-numbers/

"""
args[2] = link
"""
def handle_add_problem(lcLink: str):
    if (re.match(pattern, lcLink) is None):
        print(f"Leetcode Link not in proper format\n{usage.add_problem_usage}")
        return

    problem_slug = lcLink.split('/')[-2]
    data = {"operationName":"questionData","variables":{"titleSlug":f"{problem_slug}"},"query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}
    r = requests.post('https://leetcode.com/graphql', json = data).json()
    if (r['data']['question']['isPaidOnly']):
        print("This question is premium only")
        return
    

    # define vars
    qID = r['data']['question']['questionFrontendId']
    qTitle = r['data']['question']['title']
    qSlug = r['data']['question']['titleSlug']
    qDifficulty = r['data']['question']['difficulty']
    qProblemText = BeautifulSoup(r['data']['question']['content'], 'lxml').get_text()
    qProblemHTML = r['data']['question']['content']

    # create directory and files 
    problems_dir = Path.cwd() / "problems"
    newFolder = problems_dir / f"{qID}-{qSlug}"
    newFolder.mkdir(parents=True, exist_ok=True)
    readme = newFolder / "README.md"
    solution = newFolder / "main.py"
    htmlfile = newFolder / "test.html"

    # write to html 
    htmlfile.write_text(f"<!DOCTYPE html><html><body>{qProblemHTML}</body></html> ")

    # write to readme 
    readme.write_text(f"# {qID}. {qTitle}\n my solution here")

    # write to solution     
    for code_snip_dict in r['data']['question']['codeSnippets']:
        if code_snip_dict['lang'] == 'Python':
            solution.write_text(f"# {qID}. {qTitle}\n# {qDifficulty}\n# {datetime.date.today().strftime('%m-%d-%Y')}\n\"\"\"{qProblemText}\"\"\"\n{code_snip_dict['code']}")
            break
    return

def handle_rm_problem(args):
    pass

def handle_sort_by_tag(args):
    pass

def handle_top_topics(args):
    pass

def handle_add_tags(args):
    pass
