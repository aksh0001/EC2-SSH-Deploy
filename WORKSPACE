load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# ***** START PYTHON *****
http_archive(
    name = "rules_python",
    sha256 = "934c9ceb552e84577b0faf1e5a2f0450314985b4d8712b2b70717dc679fdc01b",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.3.0/rules_python-0.3.0.tar.gz",
)

# NOTE: I had to use pip_parse rather than pip_install (pycharm not recognizing imports)
# https://github.com/bazelbuild/intellij/pull/2528
load("@rules_python//python:pip.bzl", "pip_parse")

# Create a central repo that knows about the dependencies needed from
# requirements.txt.
pip_parse(
    name = "deps",
    requirements_lock = "//:requirements.txt",
)

# Load the starlark macro which will define your dependencies.
load("@deps//:requirements.bzl", "install_deps")

# Call it to define repos for your requirements.
install_deps()
