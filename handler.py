try:
    import unzip_requirements  # NOQA
except ImportError:
    pass

import json
import requests
import os
from common.exceptions import InvalidResponseException

OAUTH_TOKEN = os.getenv('GITHUB_TOKEN', 'not_a_oauth_token'),


def _headers():
    return {
        'content-type': 'application/json',
        'Authorization': f'token {OAUTH_TOKEN[0]}'
    }


def _check_status(result):
    if result.status_code not in range(200, 299):
        raise InvalidResponseException(result.text['message'])


def _create_protection_issue_info(payload, issues_url, user):
    protection_data = {
        'enforce_admins': payload['enforce_admins']['enabled'],
        'required_linear_history': payload['required_linear_history']['enabled'],
        'allow_force_pushes': payload['required_linear_history']['enabled'],
        'allow_deletions': payload['required_linear_history']['enabled'],
        'required_pull_request_reviews': None,
        'restrictions': None,
        'required_status_checks': None
    }
    body = f'@{user} please see the following protection details: \n'
    body += f'```json \n{json.dumps(protection_data, indent=2)}\n```'

    issue_data = {
        'title': 'Protection Details',
        'body': body,
        'assignees': [],
        'labels': ['info']
    }

    result = requests.post(
        issues_url,
        data=json.dumps(issue_data),
        headers=_headers()
    )
    payload = json.loads(result.text)
    return payload


def _retrieve_protection_details(payload):
    result = requests.get(
        payload['protection_url'],
        headers=_headers()
    )
    payload = json.loads(result.text)
    return payload


def _check_branch_exists(payload):
    branch_url = payload['repository']['branches_url'].replace('{/branch}', '/master')
    result = requests.get(
        branch_url,
        headers=_headers()
    )
    _check_status(result)
    payload = json.loads(result.text)
    return payload


def _protect_master_branch(payload):
    data = {
        'required_linear_history': True,
        'allow_force_pushes': False,
        'allow_deletions': False,
        'required_status_checks': None,
        'enforce_admins': True,
        'required_pull_request_reviews': None,
        'restrictions': None
    }

    result = requests.put(
        payload['protection_url'],
        data=json.dumps(data),
        headers=_headers()
    )
    payload = json.loads(result.text)
    return payload


def github_webhook_protect_master(event, __):
    payload = json.loads(event['body']['payload'])

    if payload['action'] == 'created':
        try:
            branch_payload = _check_branch_exists(payload=payload)

            if not branch_payload['protected']:
                protection_payload = _protect_master_branch(payload=branch_payload)
            else:
                protection_payload = _retrieve_protection_details(payload=branch_payload)

            user = payload['sender']['login']
            issues_url = payload['repository']['issues_url'].replace('{/number}', '')

            _create_protection_issue_info(
                payload=protection_payload,
                issues_url=issues_url,
                user=user
            )
        except InvalidResponseException:
            return False

    return True
