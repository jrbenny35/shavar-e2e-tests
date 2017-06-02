import pytest

from foxpuppet import FoxPuppet
from requests.exceptions import ConnectionError


@pytest.fixture
def foxpuppet(selenium):
    return FoxPuppet(selenium)


@pytest.fixture
def capabilities(capabilities):
    capabilities['marionette'] = True
    capabilities['acceptInsecureCerts'] = True
    return capabilities


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.set_preference(
        'extensions.install.requireBuiltInCerts', False)
    firefox_options.set_preference('xpinstall.signatures.required', False)
    firefox_options.set_preference('extensions.webapi.testing', True)
    firefox_options.set_preference('browser.startup.homepage', 'http://itisatrap.org/firefox/its-a-tracker.html')  # noqa
    return firefox_options


@pytest.fixture(scope="session")
def firefox_download():

    from mozdownload import FactoryScraper

    ch_type = 'daily'
    ch_version = ''
    ch_branch = 'mozilla-central'
    download_path = '.cache'
    ch_platform = ''

    try:
        scraper = FactoryScraper(
                      ch_type,
                      version=ch_version,
                      branch=ch_branch,
                      destination=download_path,
                      platform=ch_platform
        )
        scraper.download()

    except ConnectionError:
        print("ERROR: unable to download Firefox.  Aborting!")
