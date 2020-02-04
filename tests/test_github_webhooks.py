from unittest import TestCase
from mock import patch, MagicMock
import handler


def _lambda_event_payload():
    return {
        'body': {
            "payload": "{\"action\":\"created\",\"repository\":{\"id\":238065325,\"node_id\":\"MDEwOlJlcG9zaXRvcnkyMzgwNjUzMjU=\",\"name\":\"test\",\"full_name\":\"XXXXXX/test\",\"private\":false,\"owner\":{\"login\":\"XXXXXX\",\"id\":60596407,\"node_id\":\"MDEyOk9yZ2FuaXphdGlvbjYwNTk2NDA3\",\"avatar_url\":\"https://avatars3.githubusercontent.com/u/60596407?v=4\",\"gravatar_id\":\"\",\"url\":\"https://api.github.com/users/XXXXXX\",\"html_url\":\"https://github.com/XXXXXX\",\"followers_url\":\"https://api.github.com/users/XXXXXX/followers\",\"following_url\":\"https://api.github.com/users/XXXXXX/following{/other_user}\",\"gists_url\":\"https://api.github.com/users/XXXXXX/gists{/gist_id}\",\"starred_url\":\"https://api.github.com/users/XXXXXX/starred{/owner}{/repo}\",\"subscriptions_url\":\"https://api.github.com/users/XXXXXX/subscriptions\",\"organizations_url\":\"https://api.github.com/users/XXXXXX/orgs\",\"repos_url\":\"https://api.github.com/users/XXXXXX/repos\",\"events_url\":\"https://api.github.com/users/XXXXXX/events{/privacy}\",\"received_events_url\":\"https://api.github.com/users/XXXXXX/received_events\",\"type\":\"Organization\",\"site_admin\":false},\"html_url\":\"https://github.com/XXXXXX/test\",\"description\":null,\"fork\":false,\"url\":\"https://api.github.com/repos/XXXXXX/test\",\"forks_url\":\"https://api.github.com/repos/XXXXXX/test/forks\",\"keys_url\":\"https://api.github.com/repos/XXXXXX/test/keys{/key_id}\",\"collaborators_url\":\"https://api.github.com/repos/XXXXXX/test/collaborators{/collaborator}\",\"teams_url\":\"https://api.github.com/repos/XXXXXX/test/teams\",\"hooks_url\":\"https://api.github.com/repos/XXXXXX/test/hooks\",\"issue_events_url\":\"https://api.github.com/repos/XXXXXX/test/issues/events{/number}\",\"events_url\":\"https://api.github.com/repos/XXXXXX/test/events\",\"assignees_url\":\"https://api.github.com/repos/XXXXXX/test/assignees{/user}\",\"branches_url\":\"https://api.github.com/repos/XXXXXX/test/branches{/branch}\",\"tags_url\":\"https://api.github.com/repos/XXXXXX/test/tags\",\"blobs_url\":\"https://api.github.com/repos/XXXXXX/test/git/blobs{/sha}\",\"git_tags_url\":\"https://api.github.com/repos/XXXXXX/test/git/tags{/sha}\",\"git_refs_url\":\"https://api.github.com/repos/XXXXXX/test/git/refs{/sha}\",\"trees_url\":\"https://api.github.com/repos/XXXXXX/test/git/trees{/sha}\",\"statuses_url\":\"https://api.github.com/repos/XXXXXX/test/statuses/{sha}\",\"languages_url\":\"https://api.github.com/repos/XXXXXX/test/languages\",\"stargazers_url\":\"https://api.github.com/repos/XXXXXX/test/stargazers\",\"contributors_url\":\"https://api.github.com/repos/XXXXXX/test/contributors\",\"subscribers_url\":\"https://api.github.com/repos/XXXXXX/test/subscribers\",\"subscription_url\":\"https://api.github.com/repos/XXXXXX/test/subscription\",\"commits_url\":\"https://api.github.com/repos/XXXXXX/test/commits{/sha}\",\"git_commits_url\":\"https://api.github.com/repos/XXXXXX/test/git/commits{/sha}\",\"comments_url\":\"https://api.github.com/repos/XXXXXX/test/comments{/number}\",\"issue_comment_url\":\"https://api.github.com/repos/XXXXXX/test/issues/comments{/number}\",\"contents_url\":\"https://api.github.com/repos/XXXXXX/test/contents/{+path}\",\"compare_url\":\"https://api.github.com/repos/XXXXXX/test/compare/{base}...{head}\",\"merges_url\":\"https://api.github.com/repos/XXXXXX/test/merges\",\"archive_url\":\"https://api.github.com/repos/XXXXXX/test/{archive_format}{/ref}\",\"downloads_url\":\"https://api.github.com/repos/XXXXXX/test/downloads\",\"issues_url\":\"https://api.github.com/repos/XXXXXX/test/issues{/number}\",\"pulls_url\":\"https://api.github.com/repos/XXXXXX/test/pulls{/number}\",\"milestones_url\":\"https://api.github.com/repos/XXXXXX/test/milestones{/number}\",\"notifications_url\":\"https://api.github.com/repos/XXXXXX/test/notifications{?since,all,participating}\",\"labels_url\":\"https://api.github.com/repos/XXXXXX/test/labels{/name}\",\"releases_url\":\"https://api.github.com/repos/XXXXXX/test/releases{/id}\",\"deployments_url\":\"https://api.github.com/repos/XXXXXX/test/deployments\",\"created_at\":\"2020-02-03T21:25:49Z\",\"updated_at\":\"2020-02-03T21:25:49Z\",\"pushed_at\":null,\"git_url\":\"git://github.com/XXXXXX/test.git\",\"ssh_url\":\"git@github.com:XXXXXX/test.git\",\"clone_url\":\"https://github.com/XXXXXX/test.git\",\"svn_url\":\"https://github.com/XXXXXX/test\",\"homepage\":null,\"size\":0,\"stargazers_count\":0,\"watchers_count\":0,\"language\":null,\"has_issues\":true,\"has_projects\":true,\"has_downloads\":true,\"has_wiki\":true,\"has_pages\":false,\"forks_count\":0,\"mirror_url\":null,\"archived\":false,\"disabled\":false,\"open_issues_count\":0,\"license\":null,\"forks\":0,\"open_issues\":0,\"watchers\":0,\"default_branch\":\"master\"},\"organization\":{\"login\":\"XXXXXX\",\"id\":60596407,\"node_id\":\"MDEyOk9yZ2FuaXphdGlvbjYwNTk2NDA3\",\"url\":\"https://api.github.com/orgs/XXXXXX\",\"repos_url\":\"https://api.github.com/orgs/XXXXXX/repos\",\"events_url\":\"https://api.github.com/orgs/XXXXXX/events\",\"hooks_url\":\"https://api.github.com/orgs/XXXXXX/hooks\",\"issues_url\":\"https://api.github.com/orgs/XXXXXX/issues\",\"members_url\":\"https://api.github.com/orgs/XXXXXX/members{/member}\",\"public_members_url\":\"https://api.github.com/orgs/XXXXXX/public_members{/member}\",\"avatar_url\":\"https://avatars3.githubusercontent.com/u/60596407?v=4\",\"description\":null},\"sender\":{\"login\":\"Adam-Randall\",\"id\":4488231,\"node_id\":\"MDQ6VXNlcjQ0ODgyMzE=\",\"avatar_url\":\"https://avatars1.githubusercontent.com/u/4488231?v=4\",\"gravatar_id\":\"\",\"url\":\"https://api.github.com/users/Adam-Randall\",\"html_url\":\"https://github.com/Adam-Randall\",\"followers_url\":\"https://api.github.com/users/Adam-Randall/followers\",\"following_url\":\"https://api.github.com/users/Adam-Randall/following{/other_user}\",\"gists_url\":\"https://api.github.com/users/Adam-Randall/gists{/gist_id}\",\"starred_url\":\"https://api.github.com/users/Adam-Randall/starred{/owner}{/repo}\",\"subscriptions_url\":\"https://api.github.com/users/Adam-Randall/subscriptions\",\"organizations_url\":\"https://api.github.com/users/Adam-Randall/orgs\",\"repos_url\":\"https://api.github.com/users/Adam-Randall/repos\",\"events_url\":\"https://api.github.com/users/Adam-Randall/events{/privacy}\",\"received_events_url\":\"https://api.github.com/users/Adam-Randall/received_events\",\"type\":\"User\",\"site_admin\":false}}"
        },
    }


def _branch_payload_protected_true():
    return {
        'name':'master',
        'protected': True,
        'protection': {
            'enabled': True,
            'required_status_checks': {
                'enforcement_level':'off',
                'contexts':[]
            }
        },
        'protection_url':'https://api.github.com/repos/XXXXXX/test/branches/master/protection'
    }


def _branch_payload_protected_false():
    return {
        'name':'master',
        'protected': False,
        'protection': {
            'enabled': False,
            'required_status_checks': {
                'enforcement_level':'off',
                'contexts':[]
            }
        },
        'protection_url':'https://api.github.com/repos/XXXXXX/test/branches/master/protection'
    }


def _protection_payload():
   return {
        'enforce_admins': {
            'enabled': True
        },
        'required_linear_history': {
            'enabled': True
        },
        'allow_force_pushes': {
            'enabled': False
        },
        'allow_deletions': {
            'enabled': False
        }
    }

def _issue_payload():
    return {
        'url':'https://api.github.com/repos/XXXXXX/test/issues/1',
        'number':1,
        'title':'Protection Details',
        'user':{
            'login':'Adam-Randall',
        },
        'labels':[
            {
              'name':'info',
            }
        ],
        'state':'open',
        'locked':False,
        'assignee':None,
        'assignees':[],
        'milestone':None,
        'created_at':'2020-02-04T07:45:07Z',
        'updated_at':'2020-02-04T07:45:08Z',
        'author_association':'MEMBER',
        'body':'@Adam-Randall JSON DETAILS',
        'closed_by':None
    }


class TestGithubWebhook(TestCase):
    @patch('handler._check_branch_exists', MagicMock(return_value=_branch_payload_protected_true()))
    @patch('handler._retrieve_protection_details', MagicMock(return_value=_protection_payload()))
    @patch('handler._create_protection_issue_info', MagicMock(return_value=_issue_payload()))
    def test_github_webhook_with_master(self):
        event = _lambda_event_payload()
        outcome = handler.github_webhook_protect_master(event, None)
        self.assertEqual(outcome, True)


    @patch('handler._check_branch_exists', MagicMock(return_value=_branch_payload_protected_false()))
    @patch('handler._protect_master_branch', MagicMock(return_value=_protection_payload()))
    @patch('handler._create_protection_issue_info', MagicMock(return_value=_issue_payload()))
    def test_github_webhook_without_master(self):
        event = _lambda_event_payload()
        outcome = handler.github_webhook_protect_master(event, None)
        self.assertEqual(outcome, True)
