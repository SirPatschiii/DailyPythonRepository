def main():
    # Define the input and output file paths
    input_file = "input.txt"    # Windows-1252 encoded file
    output_file = "output.txt"   # UTF-8 encoded file

    try:
        with open(input_file, 'rb') as f_input:
            content = f_input.read().decode('windows-1252')

        with open(output_file, 'w', encoding='utf-8') as f_output:
            f_output.write(content)

        print("File conversion completed.")
    except IOError as e:
        print("An error occurred:", e)


if __name__ == '__main__':
    main()
