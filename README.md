# EC2-SSH-Deploy

Example CI/CD configuration that builds on GitHub Actions and deploys to a remote server over SSH.

A sample Python application is built using Bazel and deployed to an EC2 instance over SSH (although any cloud VM can be
used).

To replicate, simply set the following environment secrets, as used in the [main.yml](.github/workflows/main.yml)
workflow file:

- `SERVER_SSH_KEY`
- `REMOTE_HOST`
- `REMOTE_USER`
- `REMOTE_TARGET_DIRECTORY`