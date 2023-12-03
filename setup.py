from setuptools import setup


def parse_version(fpath):
    """
    Statically parse the version number from a python file
    """
    value = static_parse("__version__", fpath)
    return value


def static_parse(varname, fpath):
    """
    Statically parse the a constant variable from a python file
    """
    import ast
    from os.path import exists

    if not exists(fpath):
        raise ValueError("fpath={!r} does not exist".format(fpath))
    with open(fpath, "r") as file_:
        sourcecode = file_.read()
    pt = ast.parse(sourcecode)

    class StaticVisitor(ast.NodeVisitor):
        def visit_Assign(self, node):
            for target in node.targets:
                if getattr(target, "id", None) == varname:
                    self.static_value = node.value.s

    visitor = StaticVisitor()
    visitor.visit(pt)
    try:
        value = visitor.static_value
    except AttributeError:
        import warnings

        value = "Unknown {}".format(varname)
        warnings.warn(value)
    return value

with open("README.md", "r") as fh:
    long_description = fh.read()


INIT_PATH = "jellyfin_apiclient_python/__init__.py"
VERSION = parse_version(INIT_PATH)

setup(
    name='jellyfin-apiclient-python',
    version=VERSION,
    author="Ian Walton",
    author_email="iwalton3@gmail.com",
    description="Python API client for Jellyfin",
    license='GPLv3',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iwalton3/jellyfin-apiclient-python",
    packages=['jellyfin_apiclient_python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests', 'urllib3', 'websocket_client', 'certifi']
)
