import os

import sagemaker
from sagemaker.local import LocalSession
from sagemaker.pytorch import PyTorch

if __name__ == "__main__":
    # To execute SageMaker job from local PC, the role which is assumed
    # by SageMaker is needed. If you run this script from SageMaker
    # notebook, `sagemaker.get_execution_role()` gets the role ARN.
    try:
        _role = sagemaker.get_execution_role()
    except ValueError:
        _key = "SAGEMAKER_ROLE_ARN"
        _role = os.getenv(_key)
        if not _role:
            raise ValueError(
                f"Please specify value of `{_key}` as environmental variable."
            )

    # Specify if use local mode or not.
    # https://sagemaker.readthedocs.io/en/stable/overview.html?highlight=local%20mode#local-mode
    use_local = True
    print(f"use_local: {use_local}")

    if use_local:
        sagemaker_session = LocalSession()
        sagemaker_session.config = {"local": {"local_code": True}}

        input_uri = "file://./data/1_2_1/calc.txt"
    else:
        # uplaod data to S3 bucket
        # https://sagemaker.readthedocs.io/en/stable/api/utility/session.html#sagemaker.session.Session.upload_data
        input_uri = sagemaker.session.Session().upload_data(
            path="./data/1_2_1/calc.txt",
            bucket=sagemaker.session.Session().default_bucket(),
            key_prefix="training/1_2_1",
        )

    print(f"input_uri: {input_uri}")

    # https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#sagemaker.pytorch.estimator.PyTorch
    estimator = PyTorch(
        entry_point="calc.py",
        source_dir="./src/1_2_1",
        py_version="py38",
        # https://github.com/aws/deep-learning-containers/blob/master/available_images.md#prior-sagemaker-framework-container-versions
        framework_version="1.12.1",
        instance_count=1,
        # https://aws.amazon.com/jp/sagemaker/pricing/
        instance_type="local" if use_local else "ml.m5.xlarge",  # 0.298 USD/h
        role=_role,
    )
    estimator.fit(input_uri)
    print(estimator.latest_training_job.describe())
