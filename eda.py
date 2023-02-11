from extract import Extract

def main():
    source_dir = 'sources/testdata'
    target_csv_file = Extract.select_target(source_dir)
    Extract.read(target_csv_file)

if __name__ == '__main__':
    main()