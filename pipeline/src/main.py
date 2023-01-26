from collect_csv import prepare_dataset
from collect_rdap import collect_domain_rdap_data
from ingestion import ingestion_data
from normalize import normalize_data

if __name__ == "__main__":
    df = prepare_dataset()
    teste_df = df.head()
    df = collect_domain_rdap_data(teste_df)
    df = normalize_data(df)  # type: ignore
    ingestion_data(df)
