# Run GitLab as a Dokku app

## Quick start

1. Clone/fork this project.
2. Update settings in `dokku.env` (please refer to <https://github.com/sameersbn/docker-gitlab#available-configuration-parameters>).
3. Run:

```bash
DOKKU_HOST=dokku.me dokku apps:create gitlab
dokku postgres:create gitlab
dokku postgres:link gitlab gitlab
echo "CREATE EXTENSION pg_trgm;" | dokku postgres:connect gitlab
# pg_dump --no-owner --no-acl old_gitlab > gitlab.backup.sql
# dokku postgres:connect gitlab < gitlab.backup.sql
dokku redis:create gitlab
dokku redis:link gitlab gitlab
dokku config:set \
	GITLAB_SECRETS_OTP_KEY_BASE="$(pwgen -s -n 64 -c 1)" \
	GITLAB_SECRETS_DB_KEY_BASE="$(pwgen -s -n 64 -c 1)" \
	GITLAB_SECRETS_SECRET_KEY_BASE="$(pwgen -s -n 64 -c 1)"
dokku config:set $(cat dokku.env)
dokku storage:mount /srv/gitlab/data:/home/git/data
dokku storage:mount /srv/gitlab/log:/var/log/gitlab
git push dokku master
```

Your new GitLab instance is now running at <https://git.dokku.me>.

## Enable SSH access

Please note that GitLab SSH server runs *inside* the Docker container. You will need to setup port forwarding on the host to connect to it from the outside network. This guide doesn't cover that scenario.

Alternatively, it is possible to setup a SSH proxy at the Dokku host, which will allow to access GitLab like this:

```bash
git clone git@git.dokku.me:group/project.git
```

To achieve that, please follow the guide from <https://github.com/sameersbn/docker-gitlab/pull/737>.

After walking through the guide, replace the docker container name in the proxy script with `gitlab.web.1`:

```bash
docker exec -i -u git gitlab.web.1 sh ...
```
