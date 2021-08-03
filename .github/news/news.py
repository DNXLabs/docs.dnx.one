import os
import github3
import json
import calendar
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


MAIN_BRANCH          = 'master'
GITHUB_TOKEN         = os.environ['GITHUB_TOKEN']


# Jinja setup
root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('news.md')


with open('news-repo.json') as f:
    news_json = json.load(f)

# Connect to GitHub API and push the changes.
github = github3.login(token=GITHUB_TOKEN)

docs_repository = github.repository('DNXLabs', 'docs.dnx.one')
github_docs_contents = docs_repository.directory_contents('/docs/news/', return_as=dict)

news = []
all_releases = []


for repository in news_json['repositories']:
    gh_repository = github.repository('DNXLabs', repository)
    all_repo_releases = gh_repository.releases()
    repo_releases = [r for r in all_repo_releases]
    for release in repo_releases:
        release_dict = release.as_dict()
        release_dict['repository'] = repository
        all_releases.append(release_dict)

all_releases.sort(key=lambda item:item['created_at'], reverse=False)

current_month = 1
current_year = 2019
index = 1

for release in all_releases:
    datetime_object = datetime.strptime(release['created_at'], "%Y-%m-%dT%H:%M:%SZ")

    if datetime_object.month != current_month or datetime_object.year != current_year:

        filename = os.path.join(root, '../../docs/news/news-%s-%s.md' % (current_year, current_month))
        if len(news) >= 1:
            news.sort(key=lambda item:item['created_at'], reverse=True)
            with open(filename, 'w') as fh:
                fh.write(template.render(
                    news   = news,
                    month = calendar.month_name[current_month],
                    year = current_year,
                    index = index
                ))
            with open(filename) as f:
                news_file = f.read()
                file_name = 'news-%s-%s.md' % (current_year, current_month)
                if file_name in github_docs_contents:
                    github_docs_index = docs_repository.file_contents('/docs/news/' + file_name, ref=MAIN_BRANCH)
                    if github_docs_index.decoded != news_file.encode('utf-8'):
                        pushed_docs_changes = github_docs_index.update(
                            'Update %s news document' % file_name,
                            news_file.encode('utf-8'),
                            branch=MAIN_BRANCH
                        )
                        print("Pushed commit {} to {} branch:\n    {}".format(
                            pushed_docs_changes['commit'].sha,
                            MAIN_BRANCH,
                            pushed_docs_changes['commit'].message,
                        ))
                    else:
                        print('Document %s already up-to-date' % file_name)
                else:
                    docs_repository.create_file('docs/news/' + file_name,
                        'Update %s news document' % file_name, news_file.encode('utf-8'), branch=MAIN_BRANCH)
                    print('Created %s document' % file_name)

        index = index + 1
        news = []
        current_month = datetime_object.month
        current_year = datetime_object.year

    new = {
        'repository': release['repository'],
        'release': release['tag_name'],
        'body': release['body'],
        'created_at': release['created_at'].split('T')[0]
    }

    news.append(new)