import os
import streamlit.components.v1 as components

_RELEASE = False

_component_func = components.declare_component(
    "my_component",
    path="./my_component/frontend/"
)

def my_component(data):
    # spec = json.dumps(fig, cls=PlotlyJSONEncoder)
    spec = data.to_json()
    component_value = _component_func(spec = spec, default = None)
    return component_value

if not _RELEASE:
    import streamlit as st

    st.subheader("Component with constant args")

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    num_clicks = my_component("World")
    st.markdown("You've clicked %s times!" % int(num_clicks))

    st.markdown("---")
    st.subheader("Component with variable args")

    # Create a second instance of our component whose `name` arg will vary
    # based on a text_input widget.
    #
    # We use the special "key" argument to assign a fixed identity to this
    # component instance. By default, when a component's arguments change,
    # it is considered a new instance and will be re-mounted on the frontend
    # and lose its current state. In this case, we want to vary the component's
    # "name" argument without having it get recreated.
    name_input = st.text_input("Enter a name", value="Streamlit")
    num_clicks = my_component(name_input, key="foo")
    st.markdown("You've clicked %s times!" % int(num_clicks))
