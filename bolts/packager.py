import argparse
import os
import re

import git


version_tag_rx = re.compile('v\d+\.\d+(?:\.\d+)?')


def build(repos_dir, archive_dir):

    for directory in os.listdir(repos_dir):
        directory = os.path.join(repos_dir, directory)

        try:
            repo = git.Repo(directory)
            print directory

            for tag in repo.tags:
                if version_tag_rx.match(tag.name):

                    directory_name = os.path.basename(directory)
                    package_name = re.sub('\.git$', '', directory_name)
                    version = tag.name[1:]
                    archive_name = '{}-{}.tar'.format(package_name, version)
                    archive_path = os.path.join(archive_dir, archive_name)

                    with open(archive_path, 'w') as fh:
                        repo.archive(fh, tag.name)

            print

        except git.exc.InvalidGitRepositoryError:
            if os.path.isdir(directory):
                build(directory, archive_dir)


parser = argparse.ArgumentParser()
parser.add_argument('repos')
parser.add_argument('packages')

if __name__ == '__main__':
    args = parser.parse_args()
    build(args.repos, args.packages)
