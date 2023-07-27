# An Normalizer allows you to inline a value into the Pipeline file before the pipeline is initialized.
# Read More:
#   https://nodestream-proj.github.io/nodestream/docs/reference/normalizers/
#   https://nodestream-proj.github.io/nodestream/docs/guides/creating-your-own-normalizer/

from nodestream.pipeline.normalizers import Normalizer

class ApplicationNormalizer(Normalizer):
    # Base class for all normalizers in this project. 
    # This class is not required, but is useful for sharing common traits between normalizers.
    pass

