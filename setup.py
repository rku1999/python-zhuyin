import setuptools

with open("README.md", "r") as f:
    long_desc = f.read()

setuptools.setup(
    name="pyzhuyin",
    version="0.0.3",
    author="Raymond Ku",
    description="注音和拼音的轉換工具",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/rku1999/pyzhuyin",
    project_urls={
        "Source": "https://github.com/rku1999/pyzhuyin",
        "Bug Tracker": "https://github.com/rku1999/pyzhuyin/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Text Processing",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],
    keywords="pinyin, zhuyin, 拼音, 注音",
)
