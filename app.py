from typing import Final

import aws_cdk
from lib.sagemaker_stack import SageMakerSdkStack

_arg_context: Final = "env"

app: Final = aws_cdk.App()
_project_name: Final = app.node.try_get_context("project_name")
_env_name: Final = app.node.try_get_context(_arg_context)
if not _env_name:
    raise ValueError(
        f"Please specify `env` with context option. ex) cdk synth -c {_arg_context}=dev"
    )

SageMakerSdkStack(app, "sagemaker-sdk", project_name=_project_name, env_name=_env_name)

app.synth()
