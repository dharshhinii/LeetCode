import requests
import os
import json
import time

def get_solved_questions(session, csrf):
    url = 'https://leetcode.com/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'LEETCODE_SESSION={session}; csrftoken={csrf}',
        'x-csrftoken': csrf,
        'Referer': 'https://leetcode.com/'
    }
    
    query = """
    query problemsetQuestionList($limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
      problemsetQuestionList: questionList(
        categorySlug: ""
        limit: $limit
        skip: $skip
        filters: $filters
      ) {
        total: totalNum
        questions: data {
          questionId
          frontendQuestionId: questionFrontendId
          title
          titleSlug
          topicTags {
            name
          }
        }
      }
    }
    """
    
    # Filter by AC (Accepted)
    variables = {
        "limit": 100, # Max allowed by LeetCode is 100 per request
        "skip": 0,
        "filters": {"status": "AC"}
    }
    
    all_questions = []
    
    while True:
        response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching questions: {response.text}")
            break
            
        data = response.json()
        try:
            questions = data['data']['problemsetQuestionList']['questions']
            total = data['data']['problemsetQuestionList']['total']
            all_questions.extend(questions)
            
            if len(all_questions) >= total or len(questions) == 0:
                break
                
            variables['skip'] += 100
        except KeyError:
            print("Could not fetch data. Please check your session cookie.")
            break
            
    return all_questions

def get_latest_submission_id(slug, session, csrf):
    url = 'https://leetcode.com/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'LEETCODE_SESSION={session}; csrftoken={csrf}',
        'x-csrftoken': csrf,
        'Referer': 'https://leetcode.com/'
    }
    
    query = """
    query submissionList($offset: Int!, $limit: Int!, $questionSlug: String!) {
      submissionList(offset: $offset, limit: $limit, questionSlug: $questionSlug) {
        submissions {
          id
          statusDisplay
          lang
        }
      }
    }
    """
    
    variables = {
        "offset": 0,
        "limit": 20,
        "questionSlug": slug
    }
    
    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    try:
        submissions = response.json()['data']['submissionList']['submissions']
        # Find the first Python accepted submission
        for sub in submissions:
            if sub['statusDisplay'] == 'Accepted' and ('python' in sub['lang']):
                return sub['id'], sub['lang']
    except Exception:
        pass
    return None, None

def get_submission_code(sub_id, session, csrf):
    url = 'https://leetcode.com/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'LEETCODE_SESSION={session}; csrftoken={csrf}',
        'x-csrftoken': csrf,
        'Referer': 'https://leetcode.com/'
    }
    
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
      }
    }
    """
    response = requests.post(url, json={'query': query, 'variables': {'submissionId': int(sub_id)}}, headers=headers)
    try:
        return response.json()['data']['submissionDetails']['code']
    except Exception:
        return None
        
def get_question_content(slug, session, csrf):
    url = 'https://leetcode.com/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'LEETCODE_SESSION={session}; csrftoken={csrf}',
        'x-csrftoken': csrf,
        'Referer': 'https://leetcode.com/'
    }
    
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        content
      }
    }
    """
    response = requests.post(url, json={'query': query, 'variables': {'titleSlug': slug}}, headers=headers)
    try:
        return response.json()['data']['question']['content']
    except Exception:
        return ""

def main():
    print("=== LeetCode Problem Fetcher (All Solved) ===")
    session = input("Enter your LEETCODE_SESSION cookie: ").strip()
    csrf = input("Enter your csrftoken cookie: ").strip()
    
    if not session or not csrf:
        print("Both cookies are required!")
        return

    print("\nFetching all accepted questions (this might take a few seconds)...")
    questions = get_solved_questions(session, csrf)
    
    if not questions:
        print("No solved questions found or cookies are invalid.")
        return
        
    print(f"Found {len(questions)} accepted questions total.")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(script_dir, ".pending")
    os.makedirs(base_dir, exist_ok=True)
    
    # Pre-scan the Python directory for existing problems to avoid topic name mismatches 
    # (e.g. 'Array' vs 'Arrays')
    existing_problems = set()
    python_dir = os.path.join(script_dir, "Python")
    
    if os.path.exists(python_dir):
        for topic_folder in os.listdir(python_dir):
            topic_path = os.path.join(python_dir, topic_folder)
            if os.path.isdir(topic_path):
                for prob_folder in os.listdir(topic_path):
                    existing_problems.add(prob_folder)
                    
    # Also scan .pending just in case
    for topic_folder in os.listdir(base_dir):
        topic_path = os.path.join(base_dir, topic_folder)
        if os.path.isdir(topic_path):
            for prob_folder in os.listdir(topic_path):
                existing_problems.add(prob_folder)

    
    for q in questions:
        slug = q['titleSlug']
        frontend_id = q['frontendQuestionId']
        title = q['title']
        
        topic = q['topicTags'][0]['name'] if q['topicTags'] else "Uncategorized"
        topic = topic.replace(" ", "_").replace("-", "_")
        
        prob_dir_name = f"{frontend_id}-{slug}"
        
        # Check if the problem is already anywhere in the repo
        if prob_dir_name in existing_problems:
            continue # Already in repo or already pending
            
        prob_dir = os.path.join(base_dir, topic, prob_dir_name)
            
        print(f"Fetching code for {frontend_id}. {title}...")
        sub_id, lang = get_latest_submission_id(slug, session, csrf)
        
        if not sub_id:
            print(f"  Skipping {title} (No Python accepted submission found)")
            continue
            
        code = get_submission_code(sub_id, session, csrf)
        content = get_question_content(slug, session, csrf)
        
        os.makedirs(prob_dir, exist_ok=True)
        
        with open(os.path.join(prob_dir, "README.md"), "w", encoding="utf-8") as f:
            f.write(f"<h2>{frontend_id}. {title}</h2>\n")
            f.write(content or "")
            
        with open(os.path.join(prob_dir, "solution.py"), "w", encoding="utf-8") as f:
            f.write(code or "")
            
        print(f"  Successfully staged {title} under {topic}!")
        time.sleep(1) # Be gentle with the API
        
    print("\nDone! All new problems have been staged in the '.pending' directory.")

if __name__ == "__main__":
    main()
