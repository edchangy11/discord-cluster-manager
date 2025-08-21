# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/edchangy11/discord-cluster-manager/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                |    Stmts |     Miss |   Cover |   Missing |
|------------------------------------ | -------: | -------: | ------: | --------: |
| src/libkernelbot/\_\_init\_\_.py    |        0 |        0 |    100% |           |
| src/libkernelbot/consts.py          |       67 |        3 |     96% | 45, 54-55 |
| src/libkernelbot/db\_types.py       |       47 |        1 |     98% |         6 |
| src/libkernelbot/leaderboard\_db.py |      274 |       40 |     85% |72, 107, 639-641, 710-731, 888-912, 924-963, 970-991, 998-1005, 1021-1030 |
| src/libkernelbot/report.py          |      250 |       15 |     94% |305, 315, 336, 358-359, 362-367, 370-371, 374-375, 378 |
| src/libkernelbot/submission.py      |      109 |        1 |     99% |        17 |
| src/libkernelbot/task.py            |      106 |        5 |     95% |67, 117, 122-124 |
| src/libkernelbot/utils.py           |       87 |        5 |     94% |     39-48 |
|                           **TOTAL** |  **940** |   **70** | **93%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/edchangy11/discord-cluster-manager/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/edchangy11/discord-cluster-manager/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/edchangy11/discord-cluster-manager/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/edchangy11/discord-cluster-manager/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fedchangy11%2Fdiscord-cluster-manager%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/edchangy11/discord-cluster-manager/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.