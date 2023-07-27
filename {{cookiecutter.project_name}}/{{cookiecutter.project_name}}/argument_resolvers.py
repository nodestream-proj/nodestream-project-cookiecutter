# An ArgumentResolver allows you to inline a value into the Pipeline file before the pipeline is initialized.
# Read More:
#   https://nodestream-proj.github.io/nodestream/docs/reference/argument-resovlers/
#   https://nodestream-proj.github.io/nodestream/docs/guides/creating-your-own-argument-resolver/

from nodestream.pipeline.argument_resolvers import ArgumentResolver

class ApplicationArgumentResolver(ArgumentResolver):
    # Base class for all argument resolvers in this project. 
    # This class is not required, but is useful for sharing common traits between argument resolvers.
    pass

