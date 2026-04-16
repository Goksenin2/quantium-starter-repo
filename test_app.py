import ssl
# Tell Mac to relax its security rules just for this download
ssl._create_default_https_context = ssl._create_unverified_context

from app import app
import chromedriver_autoinstaller

# Automatically get the Chrome keys
chromedriver_autoinstaller.install()

# Test 1: Is the header there?
def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)

# Test 2: Is the visualization there?
def test_visualization_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)

# Test 3: Is the region picker there?
def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-picker", timeout=10)
