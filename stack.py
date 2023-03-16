from typing import Any, Dict, Final

from aws_cdk import Stack, aws_iam
from constructs import Construct


class SageMakerSdkStack(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        project_name: str,
        env_name: str,
        **kwargs: Dict[str, Any],
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html
        sagemaker_sdk_role: Final = aws_iam.Role(
            self,
            id=f"{project_name}-{env_name}-sagemaker-sdk-role",
            assumed_by=aws_iam.ServicePrincipal("sagemaker.amazonaws.com"),
        )
        # https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol.html
        sagemaker_sdk_role.add_managed_policy(
            aws_iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSageMakerFullAccess"
            )
        )
