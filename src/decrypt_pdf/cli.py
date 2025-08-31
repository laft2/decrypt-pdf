import pypdf
import argparse
import os

def main():
    parser = argparse.ArgumentParser(
    description='decrypt a pdf file you know its password')
    parser.add_argument('source_path', help='source path')
    parser.add_argument('password', help='password of pdf')
    parser.add_argument('-o', '--dist-path',
                        help='distination path, this is source_path + _decrypted.pdf as default', default="undef")
    args = parser.parse_args()

    source_path: str = args.source_path
    src_pdf = pypdf.PdfReader(source_path)
    if not src_pdf.is_encrypted:
        print("Note: This file is not encrypted.")
        exit(0)

    code = src_pdf.decrypt(args.password)
    if code == pypdf.PasswordType.NOT_DECRYPTED:
        print("Error: Password is incorrect.")
        exit(1)

    dst_pdf = pypdf.PdfWriter()
    dst_pdf.clone_document_from_reader(src_pdf)
    d = {key: src_pdf.metadata[key] for key in src_pdf.metadata.keys()}
    dst_pdf.add_metadata(d)
    dist_path = args.dist_path
    if dist_path == "undef":
        dist_path = os.path.splitext(source_path)[0] + "_decrypted.pdf"
    with open(dist_path, 'wb') as f:
        dst_pdf.write(f)
    print(f"Success: {source_path} is decrypted and saved as {dist_path}")

if __name__ == "__main__":
    main()
