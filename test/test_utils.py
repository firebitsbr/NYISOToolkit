import datetime
import pytest

import utils


def test_fetch_months_to_download_general():
    cur_date = datetime.datetime(2020, 8, 2)
    year_to_collect = 2019

    expected = [
        '20181201', '20190101', '20190201', '20190301', '20190401', '20190501',
        '20190601', '20190701', '20190801', '20190901', '20191001', '20191101',
        '20191201', '20200101'
    ]

    actual = utils.fetch_months_to_download(cur_date=cur_date, year_to_collect=year_to_collect)

    # sort for testing ease
    expected = sorted(expected)
    actual = sorted(actual)

    assert actual == expected


def test_fetch_months_to_download_bad_input():
    cur_date = datetime.datetime(2020, 8, 2)

    with pytest.raises(AssertionError):
        utils.fetch_months_to_download(cur_date=cur_date, year_to_collect=2021)


def test_test_fetch_months_to_download_same_year():
    cur_date = datetime.datetime(2020, 8, 2)

    expected = [
        '20191201', '20200101', '20200201', '20200301', '20200401', '20200501',
        '20200601', '20200701', '20200801'
    ]

    actual = utils.fetch_months_to_download(cur_date=cur_date, year_to_collect=2020)

    # sort for testing ease
    expected = sorted(expected)
    actual = sorted(actual)

    assert actual == expected


def test_fetch_dataset_url_map_general():
    dataset = "lbmp_rt_5m"
    expected = utils.dataset_details(
        dataset,
        'lbmp',
        utils.BASE_URL + "realtime" + "/{}" + "realtime_zone_csv.zip",
        "5T",
        "Name",
        None
    )
    assert utils.fetch_dataset_url_map(dataset) == expected


def test_fetch_dataset_url_map_failure():
    with pytest.raises(KeyError):
        utils.fetch_dataset_url_map('bad_key')
