from pathlib import Path
from bs4 import BeautifulSoup
import datetime
import re
import requests
import usage

lc_pattern = r"^https://leetcode\.com/problems/.+/"
pe_pattern = r"^https://projecteuler\.net/problem=\d+"

# TODO: write to metadata, maybe write topics somewhere in read me or make readme more reobust with info about date and time 
def handle_add_problem(link: str):
    # make sure we have a valid link 
    if (re.match(lc_pattern, link) is None) and (re.match(pe_pattern, link) is None):
        print(f"Link not in proper format\n{usage.add_problem_usage}")
        return

    if (re.match(lc_pattern, link)):
        # fetch problem info 
        problem_slug = link.split('/')[-2]
        data = {"operationName":"questionData","variables":{"titleSlug":f"{problem_slug}"},"query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}
        r = requests.post('https://leetcode.com/graphql', json = data).json()

        # check if question is paywalled 
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
        problems_dir = Path.cwd() / "leetcode"
        newFolder = problems_dir / f"{qID}-{qSlug}"
        if newFolder.exists() and newFolder.is_dir():
            print(f"A directory for this problem already exists.")
            return
        newFolder.mkdir(parents=True, exist_ok=True)
        readme = newFolder / "README.md"
        solution = newFolder / "main.py"
        htmlfile = newFolder / "problem.html"

        # write to html 
        htmlfile.write_text(f"<!DOCTYPE html><html><body><h1>{qID}. {qTitle}</h1><p>{qDifficulty}</p>\n{qProblemHTML}</body></html> ")

        # write to readme 
        readme.write_text(f"# {qID}. {qTitle}\n\n## Solution 1\n")

        # write to solution     
        for code_snip_dict in r['data']['question']['codeSnippets']:
            if code_snip_dict['lang'] == 'Python':
                solution.write_text(f"# {qID}. {qTitle}\n# {qDifficulty}\n# {datetime.date.today().strftime('%m-%d-%Y')}\n\"\"\"{qProblemText}\"\"\"\n{code_snip_dict['code']}")
                break
        return
    elif (re.match(pe_pattern, link)):
        problem_number = int(link.split('=')[-1])
        problem_html = requests.get(f'https://projecteuler.net/minimal={problem_number}').text
        problems_dir = Path.cwd() / "project-euler"
        newFolder = problems_dir / f"problem-{problem_number}"
        if newFolder.exists() and newFolder.is_dir():
            print(f"A directory for this problem already exists.")
            return
    
        newFolder.mkdir(parents=True, exist_ok=True)
        readme = newFolder / "README.md"
        solution = newFolder / "main.py"
        htmlfile = newFolder / "problem.html"

        formatted_prob_html = re.sub(r'\$(\d+)\$', r'\\(\1\\)', problem_html)
        htmlfile.write_text(f"<!DOCTYPE html><html><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Fibonacci Sequence</title><script type=\"text/javascript\" async src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML\"></script><body><h1>Problem {problem_number}</h1>{formatted_prob_html}</body></html> ")

        readme.write_text(f"# Problem {problem_number}\n\n## Solution\n")
        solution.write_text('# Answer Here')
    else:
        print('you shouldn\'t be here')

def handle_rm_problem(args):
    pass

def handle_sort_by_tag(args):
    pass

def handle_top_topics(args):
    pass

def handle_add_tags(args):
    pass
