# An Interpretation allows you to define operations to map data from your pipeline into a graph.
# Read More:
#   https://nodestream-proj.github.io/nodestream/docs/reference/interpretations/
#   https://nodestream-proj.github.io/nodestream/docs/guides/creating-your-own-interpretation/

from nodestream.interpreting import Interpretation

class ApplicationInterpretation(Interpretation):
    # Base class for all interpretation in this project. 
    # This class is not required, but is useful for sharing common traits between interpretations resolvers.
    pass
