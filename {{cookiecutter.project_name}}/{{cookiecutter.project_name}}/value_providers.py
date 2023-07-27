# Value Providers are used to provide values to the pipeline by extracting data from the data record.

from nodestream.pipeline.value_providers import ValueProvider


class ApplicationValueProvider(ValueProvider):
    # Base class for all value providers in this project. 
    # This class is not required, but is useful for sharing common traits between value providers.
    pass

