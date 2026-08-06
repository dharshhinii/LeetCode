import requests
import os
import json
import time

def get_recent_submissions(session, csrf):
    url = 'https://leetcode.com/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'LEETCODE_SESSION={session}; csrftoken={csrf}',
        'x-csrftoken': csrf,
        'Referer': 'https://leetcode.com/'
    }
    
    # We will fetch up to 200 recent submissions to get the missing ones
    query = """
    query recentAcSubmissions($limit: Int!) {
      recentAcSubmissionList(limit: $limit) {
        id
        title
        titleSlug
        timestamp
      }
    }
    """
    
    response = requests.post(url, json={'query': query, 'variables': {'limit': 200}}, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching submissions: {response.text}")
        return []
        
    data = response.json()
    if 'data' not in data or 'recentAcSubmissionList' not in data['data']:
        print("Could not fetch data. Please check your session cookie.")
        return []
        
    return data['data']['recentAcSubmissionList']

def get_submission_details(slug, sub_id, session, csrf):
    url = 'https://leetcode.com/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'LEETCODE_SESSION={session}; csrftoken={csrf}',
        'x-csrftoken': csrf,
        'Referer': 'https://leetcode.com/'
    }
    
    # Get submission code
    code_query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        lang {
          name
        }
      }
    }
    """
    
    # Get problem details (tags and description)
    prob_query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        content
        topicTags {
          name
        }
      }
    }
    """
    
    code_res = requests.post(url, json={'query': code_query, 'variables': {'submissionId': int(sub_id)}}, headers=headers)
    prob_res = requests.post(url, json={'query': prob_query, 'variables': {'titleSlug': slug}}, headers=headers)
    
    try:
        code_data = code_res.json()['data']['submissionDetails']
        prob_data = prob_res.json()['data']['question']
        
        # Pick the first topic as the main folder
        topic = prob_data['topicTags'][0]['name'] if prob_data['topicTags'] else "Uncategorized"
        # Sanitize topic name
        topic = topic.replace(" ", "_").replace("-", "_")
        
        return {
            'code': code_data['code'],
            'lang': code_data['lang']['name'],
            'title': prob_data['title'],
            'questionId': prob_data['questionId'],
            'content': prob_data['content'],
            'topic': topic,
            'slug': slug
        }
    except Exception as e:
        print(f"Error fetching details for {slug}: {e}")
        return None

def main():
    print("=== LeetCode Problem Fetcher & Streak Automator ===")
    print("This script will download your solved problems and stage them for the daily GitHub Action.")
    session = input("Enter your LEETCODE_SESSION cookie: ").strip()
    csrf = input("Enter your csrftoken cookie: ").strip()
    
    if not session or not csrf:
        print("Both cookies are required!")
        return

    print("\nFetching recent accepted submissions...")
    submissions = get_recent_submissions(session, csrf)
    
    if not submissions:
        print("No submissions found.")
        return
        
    print(f"Found {len(submissions)} accepted submissions.")
    
    base_dir = ".pending"
    os.makedirs(base_dir, exist_ok=True)
    
    processed = set()
    
    for sub in submissions:
        slug = sub['titleSlug']
        if slug in processed:
            continue
            
        print(f"Processing: {sub['title']}...")
        details = get_submission_details(slug, sub['id'], session, csrf)
        
        if details:
            # We only want Python submissions as per your repo structure
            if details['lang'] != 'python' and details['lang'] != 'python3':
                print(f"  Skipping {slug} (Not Python)")
                continue
                
            topic_dir = os.path.join(base_dir, details['topic'])
            prob_dir_name = f"{details['questionId']}-{slug}"
            prob_dir = os.path.join(topic_dir, prob_dir_name)
            
            # Check if this problem is already in the main repo to avoid duplicates
            main_repo_prob_path = os.path.join("Python", details['topic'], prob_dir_name)
            if os.path.exists(main_repo_prob_path) or os.path.exists(prob_dir):
                print(f"  Skipping {slug} (Already exists in repo or pending)")
                processed.add(slug)
                continue
                
            os.makedirs(prob_dir, exist_ok=True)
            
            # Write README.md
            with open(os.path.join(prob_dir, "README.md"), "w", encoding="utf-8") as f:
                f.write(f"<h2>{details['questionId']}. {details['title']}</h2>\n")
                f.write(details['content'] or "")
                
            # Write solution file
            ext = ".py"
            with open(os.path.join(prob_dir, f"solution{ext}"), "w", encoding="utf-8") as f:
                f.write(details['code'])
                
            print(f"  Successfully staged {slug} under {details['topic']}!")
            processed.add(slug)
            
        time.sleep(1) # Be gentle with the API
        
    print("\nDone! All new problems have been staged in the '.pending' directory.")
    print("The GitHub Action will now automatically commit 1 problem per day from this folder.")

if __name__ == "__main__":
    main()
