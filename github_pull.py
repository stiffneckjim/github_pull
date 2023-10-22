"""Clone and pull github repos in bulk"""
import os
from getpass import getpass
from dotenv import load_dotenv

from github import Github
from github import Auth


def github_auth(pat):
    """Log into GitHub using a personal access token (PAT)"""
    return Auth.Token(pat)


if __name__ == "__main__":
    load_dotenv()

    gh_pat = os.getenv("GITHUB_PAT")
    if gh_pat is None:
        gh_pat = getpass("Enter GitHub PAT: ")

    gh_auth = github_auth(gh_pat)
    gh_sess = Github(auth=gh_auth)
    gh_user = gh_sess.get_user()
    print(gh_user.login)

    for org in gh_user.get_orgs():
        print(org.name)
        for repo in org.get_repos():
            print(repo.name)
