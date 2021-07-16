#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "631330a4-7ced-478b-a2c4-b759d51f000e")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "87ed8d33-accc-4d7b-b11a-f6fce69a840e")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://bubi-faq.azurewebsites.net/qnamaker")
