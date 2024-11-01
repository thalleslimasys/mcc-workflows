# MCC - Workflows

You can add the dashboard to an Arches project in just a few easy steps.

- Install if from this repo (or clone this repo and pip install it locally)
  
``` bash
pip install git+https://github.com/thalleslimasys/mcc-workflows
```

- Add `"workflows"` to the INSTALLED_APPS setting in the demo project's settings.py file below the demo project

``` python
INSTALLED_APPS = [
    ...
    "app",
    "workflows",
]
```

- Version your dependency on `"workflows"` in `pyproject.toml`:

``` python
dependencies = [
    "arches>=7.6.0,<7.7.0",
    "workflows==0.0.1",
]
```

- Update your urls.py file in your project

``` python
from django.urls import include, path
```

and then the following path:

```python
path("", include("workflows.urls")),
```

- Next be sure to rebuild your project's frontend to include the plugin

``` bash
yarn build_development
```

- When you're done you should see the Dashboard plugin added to your main navigation bar

![Workflow Summary](<assets/Workflow Summary.png>)
