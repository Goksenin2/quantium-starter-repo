from app import app

# Test 1: Is the header there?
def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    # The robot looks for the 'h1' title tag
    dash_duo.wait_for_element("h1", timeout=10)

# Test 2: Is the visualization there?
def test_visualization_is_present(dash_duo):
    dash_duo.start_server(app)
    # The robot looks for the specific ID of our chart
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)

# Test 3: Is the region picker there?
def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    # The robot looks for the specific ID of our radio buttons
    dash_duo.wait_for_element("#region-picker", timeout=10)
