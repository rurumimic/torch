from setuptools import setup, Extension
from torch.utils import cpp_extension

setup(
  name='custom_operator',
  ext_modules=[
    cpp_extension.CppExtension(
        "custom_operator",
        ["muladd.cpp"],
        extra_compile_args={"cxx": ["-DPy_LIMITED_API=0x03090000"]},
        py_limited_api=True
    )
  ],
  cmdclass={'build_ext': cpp_extension.BuildExtension},
  options={
    "bdist_wheel": {"py_limited_api": "cp39"}
  }
)
