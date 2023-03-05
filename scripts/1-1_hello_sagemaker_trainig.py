import sagemaker
from sagemaker.pytorch import PyTorch

if __name__ == "__main__":
    # https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/sagemaker.pytorch.html#sagemaker.pytorch.estimator.PyTorch
    estimator = PyTorch(
        entry_point="./src/1-1/hello_sagemaker_training.py",
        py_version="py38",
        # https://github.com/aws/deep-learning-containers/blob/master/available_images.md#prior-sagemaker-framework-container-versions
        framework_version="1.12.1",
        isinstance=1,
        # https://aws.amazon.com/jp/sagemaker/pricing/
        instance_type="ml.m5.xlarge",  # 0.298 USD/h
        role=sagemaker.get_execution_role(),
    )
    estimator.fit()
