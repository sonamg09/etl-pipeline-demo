from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def run_etl():
    raw = extract_data()
    processed = transform_data(raw)
    load_data(processed)

if __name__ == "_main":
    run_etl()