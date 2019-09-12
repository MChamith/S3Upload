from argparse import ArgumentParser
from process_dataset import process_dataset
from upload_data import upload_file


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-p", "--path", dest="file_path",
                        help="define path to process data", metavar="PATH")
    parser.add_argument("-b", "--bucket", dest="bucket_name",
                        help="define bucket to upload data", metavar="BUCKET")
    parser.add_argument("-d", "--directory", dest="work_dir",
                        help="define working directory in bucket", metavar="DIR")

    args = parser.parse_args()
    process_dataset(args.file_path, args.bucket_name, args.work_dir)



