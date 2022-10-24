import os
import streamlit.components.v1 as components
import json

_RELEASE = False

title = "Component Template"

if _RELEASE:
    _component_func = components.declare_component(
        "my_component",
        path="./my_component/frontend/"
    )
else:
    _component_func = components.declare_component(
        "my_component",
        path="./scripts/custom_components/my_component/frontend/"
    )

def my_component(data = {"init"}):
    spec = json.dumps(data)
    print("received: "+spec)
    component_value = _component_func(spec = data, default = None)
    return component_value