import json
import os

json_files_dir = os.path.join(
	os.path.dirname(__file__), 'json_files', ''
)

# https://www.whatismybrowser.com/guides/the-latest-user-agent/
user_agents = open(os.path.join(json_files_dir, 'user_agents.json')).read()
user_agents = json.loads(user_agents)

# https://github.com/soimort/translate-shell/wiki/Languages
languages = open(os.path.join(json_files_dir, 'language_codes.json')).read()
languages = json.loads(languages)

dns_cache = {
	'meuvivo.vivo.com.br': '177.79.246.171'
}
