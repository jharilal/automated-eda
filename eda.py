from extract import Extract
from analyze import Analyze

def main():
    source_dir = 'sources/testdata'

    # Extract
    target_df = Extract.extractor(source_dir)

    # Analyze
    Analyze.analyzer(target_df)


if __name__ == '__main__':
    main()