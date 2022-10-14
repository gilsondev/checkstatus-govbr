from collect_csv import prepare_sheet_export_url
from normalize import normalize_data

if __name__ == "__main__":
    url = prepare_sheet_export_url()
    normalize_data(url)
