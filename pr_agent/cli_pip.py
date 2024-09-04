import os

from pr_agent import cli
from pr_agent.config_loader import get_settings


def main():
    # Setting the configurations
    get_settings().set("CONFIG.git_provider", 'gitlab')
    get_settings().set("gitlab.url", "https://jihulab.com")
    get_settings().set("openai.key", os.getenv('OPENAI_KEY'))
    get_settings().set("gitlab.personal_access_token", os.getenv('PAT'))

    cli.run_command(
        "https://jihulab.com/cbd-premium/code-review/-/merge_requests/1",
        "/describe"
    )


if __name__ == '__main__':
    main()
