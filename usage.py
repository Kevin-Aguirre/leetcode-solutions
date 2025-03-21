mainUsageStr = """
usage

manage problems
    add-problem\t\tcreates folder with README, starter code, and updates metadata. Err if problem exists
    rm-problem\t\tremoves specified folder, updates metadata. Err if problem dne.

get stats
    sort-by-tag\t\treturns all problems organized by their tag. 
    top-topics\t\treturns top x topics based on y latest problems

manipulate metadata
    add-tags\t\tadds tags to list of accepted tags

"""

add_problem_usage = """
add-problem usage 

add-problem {leetcodelink} 
    {leetcodelink} - required
        A link that should be of the format https://leetcode.com/problems/{problem-slug}/

creates a folder in problems directory, throws error if folder already exists       
"""

rm_problem_usage = """
rm-problem usage 

rm-problem {leetcodelink}
    {leetcodelink} - required
        A link that should be of the format https://leetcode.com/problems/{problem-slug}, this is required 
    
removes problem in problems directory specified by link, throws error if folder doesn't exist
"""

sort_by_tag_usage = """
sort-by-tag usage

sort-by-tag {tag} {ofilename}
    {tag} - required
        must be a tag in list of seen tags in metadata 
    {ofilename} - optional 
        will be the name of the md file created displaying output. default name is sort-by-tag.md

    
sorts all problems specified by tag 
"""

top_topics_usage = """
top_topics usage:

top_topics {n} {p} {outfilename}
    {n} - optional
        returns information regarding the n most studied topics. default is all topics.  
    {p} - optional
        considers the p most recent problems to determine most studied topics. default is all problems.
    {outfilename} - optional 
        name of the md file created displaying output. default name is top_topics.md

returns information regarding most studied topics 
"""